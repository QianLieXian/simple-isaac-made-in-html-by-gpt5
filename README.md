项目概览 Project Overview
这是一个受《以撒的结合》启发的 HTML5 Canvas 单页游戏，涵盖自适应界面、键位提示与集成控制面板，支持浏览器直接游玩并展示“地窖速通实验室”主题的俯视角射击体验。

It is a single-file HTML5 Canvas experiment inspired by The Binding of Isaac, bundling adaptive layout, on-screen guidance, and integrated control panels to deliver a “Basement Speedrun Lab” top-down shooter entirely in the browser.

快速上手 Quick Start
控制 / Controls: WASD 移动 (move), 方向键射击 (shoot), E 放置炸弹 (drop bombs), F 购买 (purchase), Enter 开始或回主菜单 (start/menu), P 暂停 (pause), R 重开 (restart).

通过覆盖层可以查看开局提示、暂停信息以及死亡后提示，点击“我要出发！”即可立即开跑。 Overlays brief you at start, pause, and game over; click “我要出发！” to dive in.

界面与可访问性 UI & Accessibility
自适应深色界面、面板化 HUD 与响应式虚拟按键设计适配桌面与移动端，屏幕键盘支持长按/点按映射物理键码。Responsive dark-theme panels, HUD, and virtual keyboard cater to desktop/mobile players with hold/tap mapping to keycodes.

作弊台以弹出面板呈现，可直接修改生命、伤害、移速、资源与道具；所有字段同步玩家状态并具备无障碍 ARIA 属性。The cheat console pops out to edit HP, damage, speed, resources, and grant items while mirroring player stats and exposing ARIA metadata.

“道具图鉴”面板实时累计已获得道具，绘制像素化小图并统计进度，空白状态会鼓励继续探索。The “Codex” records discovered items with dynamically rendered icons and progress counters, motivating further runs.

核心系统 Core Systems
地下城生成 Dungeon Generation
以 9×9 网格随机游走生成主线房间，并自动追加 Boss 房、道具房与商店；房门彼此连通，确保可达性。A 9×9 random walk carves core rooms, then attaches boss, item, and shop rooms with guaranteed connectivity.

房间按类型决定敌人、障碍、掉落与锁门，Boss 房会注入特定首领，安全房则直接标记已清理。Room archetypes drive enemy spawns, obstacle clusters, drop tables, and locks; boss rooms spawn dedicated leaders while safe rooms start cleared.

障碍生成考虑隐藏/镂空结构与被炸毁后的掉落概率，密室宝箱也可能刷新隐藏道具。Obstacle clusters manage hidden/hollow variants and drop chances when destroyed, occasionally revealing secret items.

玩家与战斗 Player & Combat
玩家拥有冲刺、射击惯性、炸弹投放与资源上限，移动/射击方向分离，火力受攻速与泪滴寿命影响。The player sports momentum-aware tears, bombs, and capped resources; movement and firing are decoupled, and DPS scales with rate and tear lifetime.

伤害通过基础值、乘区与特效加成动态重算，血量、金币等资源也会反馈到火力。Damage recalculates from base values, multipliers, and active effects, with health and coin-based traits feeding back into DPS.

炸弹具有导火、击退与爆炸半径，可炸毁障碍、推走掉落物或波及敌我双方。Bombs track fuse timers, knockback, and blast radius, affecting obstacles, loot, enemies, and the player alike.

资源与掉落 Resources & Drops
配置表定义心、炸弹、钥匙、金币等掉落几率与起始库存，房间结算时自动处理拾取。Config blocks set drop odds for hearts and consumables, plus starting stocks, with room cleanup driving pickup logic.

掉落物具备惯性、边界约束与碰撞分离，炸弹爆炸还能推远拾取物或点燃连锁反应。Pickups carry inertia, boundary limits, and obstacle resolution, while blasts can shove them or trigger chain reactions.

道具与商店 Items & Shops
三大道具池（基础/商店/Boss）采用加权抽取并分配唯一编号，便于图鉴追踪与作弊召唤。Three weighted pools—base, shop, and boss—assign sequential IDs for codex tracking and cheat-based retrieval.

商店按概率提供道具或资源货架，价格分别为 15/5 金币，购买成功会更新库存。Shops roll items versus consumables, price them at 15/5 coins, and refresh inventories post-purchase.

拾取道具时会触发弹幕提示、图鉴登记，并立刻套用对应能力。Item pickups trigger pop-up cues, codex registration, and instant stat changes.

道具图鉴 Item Codex
ID	中文名 · English name	效果 Effect
01	洋葱 · Onion	CN: 泪腺更发达，射速 +0.75 次/秒。EN: Boosts tear glands, raising fire rate by 0.75 shots/sec.
02	焦油抹布 · Tar Rag	CN: 伤害 +0.5，泪滴更厚重。EN: Adds 0.5 damage, making tears heavier.
03	小短跑鞋 · Sprinter Shoes	CN: 移动速度 +35，轻盈不少。EN: Increases move speed by 35 for snappier dodges.
04	胡椒牛排 · Pepper Steak	CN: 伤害 +1，攻速 +1，射程 ×1.5，血上限 +1。EN: Supercharges stats—damage +1, fire rate +1 shot/sec, range ×1.5, +1 max HP.
05	绳子 · Rope	CN: 轻盈漂浮，飞行不再畏惧地形。EN: Grants flight to ignore ground hazards.
06	酒枣 · Spirit Date	CN: 射程 ×1.5，泪滴可穿透障碍。EN: Extends range ×1.5 and lets tears pierce obstacles.
07	伙伴倒戈犬 · Betrayal Hound	CN: 伤害 ×2 +1.5，射速 -0.25 次/秒。EN: Doubles damage with +1.5 bonus but slows fire rate by 0.25 shots/sec.
08	绝望呐喊 · Cry of Despair	CN: 射程 ×5。EN: Multiplies tear range by five for map-spanning shots.
09	坏东西 · Bad Thing	CN: 子弹速度 ×1.1。EN: Speeds up tears by 10%, trading safety for velocity.
10	好东西 · Good Thing	CN: 子弹速度 ×0.75，射速 +0.75，射程 ×1.25。EN: Slows tears but adds 0.75 fire rate and 1.25× range.
11	血之力 · Blood Power	CN: 血越厚，伤害越高。EN: Damage scales with remaining HP.
12	钱之力 · Money Power	CN: 财源滚滚，伤害随金币提升。EN: Converts coins into bonus damage.
13	绝望之力 · Despair Power	CN: 血越少，越要反击。EN: Raises damage the lower your HP gets.
14	狗粮 · Dog Food	CN: 血量上限 +1。EN: Adds one max heart, healing on pickup.
15	结束纸条 · Ending Note	CN: 射速 +0.75 次/秒，射程 ×1.1。EN: Adds 0.75 fire rate and 1.1× range.
16	热水壶 · Kettle	CN: 伤害 +1。EN: Grants a flat +1 damage boost.
敌人图鉴 Enemy Bestiary
类型 Type	行为特征 Behavior
追击者 · Chaser	CN: 直接冲向玩家，被击中短暂击退。EN: Rushes straight at the player and recoils briefly on hit.
轨道蛆 · Orbiter	CN: 围绕基点旋转并缓慢逼近，贴身伤害。EN: Orbits a drifting anchor toward the player, dealing contact damage.
气囊怪 · Gasbag	CN: 保持安全距离，接近即点燃并爆炸召唤小飞虫。EN: Maintains distance, ignites near targets, and explodes into Tiny Flies.
小飞虫 · Tiny Fly	CN: 高速贴脸，受击向外弹开。EN: Fast chaser that bounces away briefly when hit.
老飞虫 · Elder Fly	CN: 在距离区间内盘旋，读条后发射泪弹。EN: Strafes to maintain min/max range and telegraphs tear shots.
蜘蛛跃者 · Spider Leaper	CN: 读条闪烁后跃向玩家，落地判定伤害。EN: Telegraphs with glow before leaping at the player and damaging on landing.
Boss 图鉴 Boss Gallery
Boss	行为特征 Behavior
哭泣塑像 · 社畜蛹 (Idol)	CN: 拥有冲刺、激光雨与陷入狂暴的阶段，血量下降后加速并生成多段弹幕。EN: Executes charges, radial volleys, and enrages at low HP for faster, denser attacks.
余烬教官 · Master	CN: 在闲置、读条、跳斩、震地与火焰波之间切换，半血后进入愤怒形态提升频率。EN: Cycles through idle drift, telegraphed jump slams, and flame waves, ramping cadence once enraged below half HP.
