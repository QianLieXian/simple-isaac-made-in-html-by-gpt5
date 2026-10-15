"""Browser regressions: python3 tests/browser_regression.py (requires Playwright + Chromium).

Test-only hooks are injected by this local server; production HTML exposes no internals.
Deterministic frame tests use the actual loop with a synthetic rAF clock, not monitor FPS.
"""
import os
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading
import unittest
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
HOOK = r"""
  window.testGame = {
    get player(){return player}, get dungeon(){return dungeon}, runtime,
    get state(){return state}, STATE, keys, keyOrder, audio,
    items: CODEX_ALL_ITEMS, startGame, handleSpikeContact, makeBloodSpikeObstacle,
    registerItemDiscovery, readNumberInput, advanceToNextFloor, startLoopRun,
    triggerRunEnding, showMenu, renderHUD,
    frames(fps, seconds){
      let now = lastTime;
      for(let i=0; i<Math.round(fps*seconds); i++) { now += 1000/fps; loop(now); }
    }
  };
  window.testStarts = 0;
  const originalStartGame = startGame;
  startGame = (...args)=>{window.testStarts++; return originalStartGame(...args)};
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ('/', '/index.html'):
            self.send_error(404)
            return
        source = (ROOT / 'index.html').read_text()
        marker = '\n})();\n</script>'
        assert source.count(marker) == 1
        payload = source.replace(marker, HOOK + marker).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_):
        pass

class GameRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(
            executable_path=os.environ.get('CHROMIUM_PATH', '/usr/bin/chromium'),
            headless=True, args=['--no-sandbox'])
        cls.url = f'http://127.0.0.1:{cls.server.server_port}/'

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.errors = []
        self.page.on('pageerror', lambda error: self.errors.append(str(error)))

    def tearDown(self):
        self.context.close()
        self.assertEqual(self.errors, [])

    def load(self, manual=False):
        if manual:
            self.page.add_init_script('window.requestAnimationFrame = ()=>0')
        self.page.goto(self.url)
        self.page.wait_for_function('!!window.testGame')

    def test_menu_one_minute_without_errors(self):
        self.load()
        self.page.wait_for_timeout(60000)
        expect(self.page.locator('#menu')).to_be_visible()
        self.assertEqual(self.page.evaluate('testStarts'), 0)

    def test_focused_start_single_activation_and_pause(self):
        self.load()
        self.page.locator('#startBtn').focus()
        self.page.keyboard.press('Enter')
        self.assertEqual(self.page.evaluate('testStarts'), 1)
        self.page.keyboard.press('p')
        expect(self.page.locator('#paused')).to_be_visible()
        before = self.page.evaluate('testGame.runtime.runTimer.getElapsed()')
        self.page.wait_for_timeout(200)
        self.assertEqual(before, self.page.evaluate('testGame.runtime.runTimer.getElapsed()'))
        self.page.keyboard.press('p')
        expect(self.page.locator('#paused')).not_to_be_visible()
        self.page.keyboard.down('d')
        self.page.evaluate("window.dispatchEvent(new Event('blur'))")
        self.assertEqual(self.page.evaluate('[testGame.keys.size,testGame.keyOrder.size]'), [0,0])
        expect(self.page.locator('#paused')).to_be_visible()
        self.page.keyboard.up('d')
        self.page.keyboard.press('p')
        self.page.wait_for_timeout(250)
        self.assertEqual(self.page.evaluate('testGame.keys.size'), 0)
        self.page.keyboard.down('ArrowUp')
        self.page.evaluate("Object.defineProperty(document,'hidden',{configurable:true,value:true});document.dispatchEvent(new Event('visibilitychange'))")
        self.assertEqual(self.page.evaluate('[testGame.keys.size,testGame.keyOrder.size]'),[0,0])
        expect(self.page.locator('#paused')).to_be_visible()

    def test_zero_empty_invalid_cheat_values(self):
        self.load()
        self.page.keyboard.press('Enter')
        self.page.locator('#cheat-toggle').click()
        for name in ('bombs','keys','coins'):
            self.page.locator('#cheat-'+name).fill('0')
        self.page.locator('#cheat-apply-resources').click()
        self.assertEqual(self.page.evaluate('[testGame.player.bombs,testGame.player.keys,testGame.player.coins]'), [0,0,0])
        self.assertEqual(self.page.evaluate("['', 'bad', 'Infinity', '0'].map(value=>testGame.readNumberInput({value}, 5))"), [5,5,5,0])
        self.page.locator('#cheat-hp').fill('0')
        self.page.locator('#cheat-apply-stats').click()
        expect(self.page.locator('#gameover')).to_be_visible()
        self.page.keyboard.press('r')
        self.assertEqual(self.page.evaluate('testGame.player.hp'),6)

    def test_speed_items_and_stacking(self):
        self.load(manual=True)
        values = self.page.evaluate("""()=>{
          testGame.startGame(); const p=testGame.player;
          const before=[p.accelTime,p.decelTime];
          const medal=testGame.items.find(i=>i.slug==='wind-sprint-medal'); medal.apply(p);
          const after=[p.accelTime,p.decelTime];
          testGame.items.find(i=>i.slug==='guardian-core').apply(p);
          const guardian=p.decelTime;
          for(let i=0;i<50;i++)medal.apply(p);
          return {before,after,guardian,stacked:[p.accelTime,p.decelTime]};
        }""")
        for old,new in zip(values['before'], values['after']):
            self.assertAlmostEqual(new, old*.88)
        self.assertLess(values['guardian'],values['after'][1])
        self.assertEqual(values['stacked'],[.03,.03])

    def test_spike_damage_across_frame_rates_and_contacts(self):
        self.load(manual=True)
        damage = self.page.evaluate("""()=>{
          testGame.startGame();
          return [15,30,60,144,240].map(fps=>{
            let damage=0;
            const e={x:10,y:10,r:5,damage(d){damage+=d;return false}};
            const flying={...e,flying:true,damage(){throw Error('flying enemy hit')}};
            const obs=testGame.makeBloodSpikeObstacle(0,0,20,20,{playerDamage:0});
            const room={enemies:[e,flying]};
            for(let i=0;i<fps*2;i++)testGame.handleSpikeContact(room,obs,1/fps,{bleeding:true});
            e.x=100;testGame.handleSpikeContact(room,obs,1,{bleeding:true});
            e.x=10;testGame.handleSpikeContact(room,obs,0,{bleeding:true});
            return damage;
          });
        }""")
        self.assertEqual(damage,[120]*5)

    def test_low_fps_clock_and_simulation(self):
        self.load(manual=True)
        values=self.page.evaluate("""()=>[15,30,60,144,240].map(fps=>{
          testGame.startGame(); testGame.player.bombCooldown=20; testGame.frames(fps,10);
          return [testGame.runtime.runTimer.getElapsed(),testGame.player.bombCooldown];
        })""")
        for elapsed,cooldown in values:
            self.assertAlmostEqual(elapsed,10,places=6)
            self.assertAlmostEqual(cooldown,10,places=6)
        stopped=self.page.evaluate("""()=>{
          testGame.startGame();testGame.runtime.timeStopTimer=1;
          testGame.frames(15,2); return testGame.runtime.runTimer.getElapsed();
        }""")
        self.assertAlmostEqual(stopped,1,places=6)
        stalled=self.page.evaluate("""()=>{
          testGame.startGame();testGame.player.bombCooldown=20;testGame.frames(1,1);
          return [testGame.runtime.runTimer.getElapsed(),testGame.player.bombCooldown];
        }""")
        self.assertAlmostEqual(stalled[0],1,places=6)
        self.assertAlmostEqual(stalled[1],19.75,places=6)

    def test_codex_storage_filter_and_corrupt_save(self):
        self.load()
        self.page.evaluate('testGame.registerItemDiscovery(testGame.items[0])')
        self.page.reload()
        expect(self.page.locator('#codex-count')).to_have_text('1')
        self.page.locator('#item-codex summary').click()
        self.page.locator('#codex-filter').select_option('unlocked')
        expect(self.page.locator('.codex-entry')).to_have_count(1)
        self.page.evaluate("localStorage.setItem('isaac.codex.v1',JSON.stringify(['unknown',testGame.items[0].slug]))")
        self.page.reload();expect(self.page.locator('#codex-count')).to_have_text('1')
        self.page.evaluate("localStorage.setItem('isaac.codex.v1','broken')")
        self.page.reload();expect(self.page.locator('#codex-count')).to_have_text('0')

    def test_blocked_storage_does_not_prevent_play(self):
        self.page.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('blocked')}})")
        self.load()
        self.page.keyboard.press('Enter')
        self.page.evaluate('testGame.registerItemDiscovery(testGame.items[0])')
        expect(self.page.locator('#codex-count')).to_have_text('1')
        expect(self.page.locator('#menu')).not_to_be_visible()

    def test_hud_preserves_nodes_and_audio_settings(self):
        self.load(manual=True)
        self.assertTrue(self.page.evaluate("""()=>{
          testGame.startGame();testGame.renderHUD();
          const heart=document.querySelector('#hud-left span');
          const stat=document.querySelector('#hud-stats span');
          const right=document.querySelector('#hud-right span');
          testGame.frames(60,1);
          return heart===document.querySelector('#hud-left span') && stat===document.querySelector('#hud-stats span') && right===document.querySelector('#hud-right span');
        }"""))
        self.page.locator('.audio-settings summary').click()
        self.page.locator('#audio-muted').check()
        self.page.locator('#audio-volume').fill('25')
        self.page.reload()
        self.assertEqual(self.page.evaluate('testGame.audio.getSettings()'),{'volume':.25,'muted':True})

    def test_mobile_actions_and_layout(self):
        self.context.close()
        self.context=self.browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True)
        self.page=self.context.new_page()
        self.page.on('pageerror',lambda error:self.errors.append(str(error)))
        self.load()
        self.page.locator('#startBtn').tap()
        self.page.locator('#vk-toggle').tap()
        codes=self.page.locator('#virtual-kb button').evaluate_all('(nodes)=>nodes.map(n=>n.dataset.code)')
        for code in ['KeyW','KeyA','KeyS','KeyD','ArrowUp','ArrowDown','ArrowLeft','ArrowRight','KeyQ','Space','KeyE','KeyF','KeyP','KeyR','Enter']:
            self.assertIn(code,codes)
        self.page.evaluate("testGame.player.singleUseItem={name:'test',use(){window.cardUsed=true;return true}};testGame.player.activeItem={name:'test',use(){window.activeUsed=true;return true}};testGame.player.activeMaxCharge=1;testGame.player.activeCharge=1")
        self.page.locator('[data-code="KeyQ"]').tap()
        self.page.locator('[data-code="Space"]').tap()
        self.assertTrue(self.page.evaluate('window.cardUsed && window.activeUsed'))
        self.assertTrue(self.page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
        self.page.set_viewport_size({'width':844,'height':390})
        self.assertTrue(self.page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
        canvas=self.page.locator('#game').bounding_box()
        controls=self.page.locator('#virtual-kb').bounding_box()
        self.assertLessEqual(canvas['y']+canvas['height'],390)
        self.assertLessEqual(canvas['x']+canvas['width'],controls['x'])
        self.assertNotIn('user-scalable=no',self.page.locator('meta[name="viewport"]').get_attribute('content'))

    def test_floor_loop_and_restart_state_smoke(self):
        self.load(manual=True)
        result=self.page.evaluate("""()=>{
          testGame.startGame();const floors=[];
          for(let i=1;i<=7;i++){
            if(i>1)testGame.advanceToNextFloor();
            testGame.frames(60,.5);floors.push(testGame.runtime.floor);
          }
          testGame.triggerRunEnding();
          const ended=testGame.state===testGame.STATE.OVER;
          testGame.startLoopRun({fromEnding:true});testGame.frames(60,.5);
          const loop=[testGame.runtime.floor,testGame.runtime.loopCount,testGame.state];
          testGame.showMenu();testGame.startGame();
          return {floors,ended,loop,restarted:[testGame.runtime.floor,testGame.runtime.loopCount,testGame.player.items.length]};
        }""")
        self.assertEqual(result['floors'],list(range(1,8)))
        self.assertTrue(result['ended'])
        self.assertEqual(result['loop'],[1,1,1])
        self.assertEqual(result['restarted'],[1,0,0])

if __name__=='__main__':
    unittest.main(verbosity=2)
