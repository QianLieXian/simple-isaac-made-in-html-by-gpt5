# 地窖速通实验室 · Basement Speedrun Lab

[![Progress](https://img.shields.io/badge/Progress-99%25-blue)](#) [![HTML5 Canvas](https://img.shields.io/badge/Engine-HTML5%20Canvas-orange)](#) [![Single-file](https://img.shields.io/badge/Build-Single--file-green)](#) [![Zero Deps](https://img.shields.io/badge/Deps-0-lightgrey)](#)

> 纯前端、**单文件** 的地牢速通实验室：顶视角射击、覆盖式引导、道具图鉴与进度可视化，开箱即玩。  
> A **single-file** HTML5 Canvas prototype: snappy top-down combat, contextual overlays, and a live item codex—zero dependencies.

---

## 目录 · Table of Contents
- [概览 · Overview](#概览--overview)
- [快速上手 · Quick Start](#快速上手--quick-start)
- [核心特性 · Core Features](#核心特性--core-features)
- [地下城生成 · Procedural Basement](#地下城生成--procedural-basement)
- [战斗循环 · Combat Loop](#战斗循环--combat-loop)
- [资源与掉落 · Resources & Drops](#资源与掉落--resources--drops)
- [进度呈现 · Progress Visibility](#进度呈现--progress-visibility)
- [道具图鉴 · Item Codex](#道具图鉴--item-codex)
- [卡牌一览 · Card Deck](#卡牌一览--card-deck)
- [怪物图鉴 · Monster Bestiary](#怪物图鉴--monster-bestiary)
- [Boss 图鉴 · Boss Gallery](#boss-图鉴--boss-gallery)
- [无障碍与技术注记 · A11y & Tech Notes](#无障碍与技术注记--a11y--tech-notes)
- [运行与部署 · Run & Deploy](#运行与部署--run--deploy)
- [版权 · License](#版权--license)

---

## 概览 · Overview

**当前进度 Progress:** 96%（作者自述）
This is a single-file HTML5 Canvas **Basement Speedrun Lab**. It ships a top-down shooter, contextual overlays, and a live item codex—**no external assets** needed.

---

## 快速上手 · Quick Start

- **移动/射击**: WASD / 方向键 · *Use WASD/arrow keys for movement & shooting*  
- **放置炸弹**: `E` · *Drop bombs*  
- **购物**: `F` · *Shop*  
- **释放卡牌**: `Q` · *Play cards*  
- **开始/菜单**: `Enter` · *Start / Menu*  
- **暂停**: `P` · *Pause*  
- **重开**: `R` · *Restart*

开局、暂停与阵亡会弹出覆盖提示；点击 **“我要出发！”** 即刻回到战斗。  
Contextual overlays at start, pause, and game over; hit **“我要出发！”** to dive back in.

---

## 核心特性 · Core Features

- **自适应界面 · Adaptive Interface**  
  响应式 HUD 展示生命、资源、主被动充能与核心数值，适配桌面与移动端。  
  *Responsive HUD across form factors.*

- **辅助工具 · Utilities**  
  可折叠**作弊面板**（生命/伤害/移动/资源修改，支持道具编号召唤）、带 **ARIA** 的屏幕键盘、随解锁进度生成缩略图的**道具图鉴**。  
  *Collapsible cheat console, ARIA-aware on-screen keyboard, auto-rendered item codex.*

- **战斗可读性 · Combat Readability**
  所有 Boss 攻击新增独立前摇/后摇与配色提示；HUD 道具栏同步展示持有数量（名称 ×N）。

  *Boss telegraphs now glow per action and the HUD item list tallies every stack.*

- **动态阴影 · Dynamic Shadows**
  玩家与怪物依据飞行 / 贴地状态渲染不同阴影轮廓，悬浮高度与压迫感一眼可辨。

  *Dynamic contact shadows differentiate grounded vs. flying units at a glance.*

- **小地图与事件可视化 · Readable Flow**
  小地图颜色区分：当前房间 / Boss / 道具房 / 商店；另有 **Boss 血条、开场介绍与拾取横幅**。  
  *Minimap color-codes key rooms; boss bars and pickup banners spotlight beats.*

---

## 地下城生成 · Procedural Basement

基于 **9×9 潜在网格的随机游走**：自动铺设主线、Boss、道具房与商店；保证房门连通、障碍簇分布与隐藏房间掉落的合理性，新增生命上限献祭台，每层有25%的概率会在初始房间的左上角生成，有硫黄火，权重只有15。  
*9×9 lattice random walk places paths, bosses, treasure, and shops with door connectivity and secret-room rewards.*

---

## 战斗循环 · Combat Loop

- **移动**：带加速/减速惯性，上限速度可被道具突破。
- **射击**：独立冷却；实时重算伤害、半径、穿透、追踪。
- **炸弹**：击退、连锁与震屏；可摧毁障碍或引出隐藏掉落。
- **阴影反馈**：飞行单位的阴影更小更淡，跃起 Boss 的阴影会随高度收缩。
*Movement uses acceleration/drift; tears recalc stats; bombs shove/chain/shake and reveal secrets. Shadow feedback shrinks airborne foes and scales boss leaps.*
- **冲刺与时停 · Dash & Time Control**：`冲击巧克力` 解锁双击方向键的无敌冲刺与冲击光带，`怀表` 可冻结时间 4 秒，`肾上腺素` 则在当前房间内大幅提升攻速与射程但牺牲 1 点生命。
*Impact Chocolate adds invulnerable impact dashes, the Pocket Watch freezes enemies for four seconds, and Adrenaline trades 1 HP for a brutal room-long power surge.*

---

## 资源与掉落 · Resources & Drops

房间结算、障碍破坏与宝箱会产出 **心/钥匙/炸弹/金币**，并有概率掉落**单次卡牌**。拾取道具会触发横幅与卡牌判定，金币/生命系道具会**重算伤害收益**。  
*Rooms, rubble, and chests spawn core resources; pickups broadcast banners and may spill cards; gold/HP-scaling perks recalc damage.*

---

## 进度呈现 · Progress Visibility

小地图颜色区分房型；**Boss 血条**、**开场介绍**与**拾取横幅**让关键事件清晰可见。  
*Minimap color-codes rooms; boss bars, intro slates, and banners highlight moments.*

---

## 道具图鉴 · Item Codex

> 说明：中文为主，斜体为英文补充。效果以游戏内实现为准。

### 主池 · Core Drops

| ID | 道具 · Item | 类型 | 效果 · Effect |
|---:|:--|:--|:--|
| 01 | 洋葱 *Onion* | 被动 | 射速 **+0.75 次/秒** · *+0.75 shots/sec* |
| 02 | 焦油抹布 *Tar Rag* | 被动 | 伤害 **+0.5**，泪滴更厚 · *+0.5 dmg, thicker tears* |
| 03 | 小短跑鞋 *Sprinter Shoes* | 被动 | 移动速度 **+35** · *+35 move speed* |
| 04 | 胡椒牛排 *Pepper Steak* | 被动 | 伤害 **+1**，射速 **+1**，射程 **×1.5**，上限 **+1** 并治疗 · *+1 dmg, +1 rps, ×1.5 range, +1 max HP with heal* |
| 05 | 绳子 *Rope* | 被动 | 获得飞行，叠层小幅提升移速/弹速 · *Flight; stacks add slight move & tear speed* |
| 06 | 酒枣 *Spirit Date* | 被动 | 射程 **×1.5**，泪滴穿透障碍 · *×1.5 range, pierces terrain* |
| 07 | 伙伴倒戈犬 *Betrayal Hound* | 被动 | 伤害 **×2 +1.5**，射速 **−0.25 次/秒** · *Damage ×2+1.5, fire rate −0.25* |
| 08 | 绝望呐喊 *Cry of Despair* | 被动 | 泪滴寿命 **×5** · *×5 tear range* |
| 09 | 坏东西 *Bad Thing* | 被动 | 子弹速度 **×1.1** · *Tear speed ×1.1* |
| 10 | 好东西 *Good Thing* | 被动 | 子弹速度 **×0.75**，射速 **+0.75**，射程 **×1.25** · *×0.75 tear speed, +0.75 rps, ×1.25 range* |
| 11 | 冲击巧克力 *Impact Chocolate* | 被动 | 双击方向冲刺并留高伤光带，叠层延长距离/降冷却，4 层可碎障 · *Double-tap dash with damaging trail; stacks extend dash, reduce cooldown, break rocks at 4 stacks* |
| 12 | 热巧克力 *Hot Chocolate* | 被动 | 泪滴可蓄力，长按依序获得高伤→追踪→穿透，额外杯数强化成长 · *Charge shots for scaling damage; long charges add homing then piercing; stacks boost scaling* |
| 13 | 豆浆 *Soy Milk* | 被动 | 射速 **×4**，伤害 **×0.25**，射程 **×2.5**，移速 **×1.25** · *×4 fire rate, ×0.25 dmg, ×2.5 range, ×1.25 speed* |
| 14 | 透视雷达 *Seer Map* | 被动 | 当前与未来楼层地图全显，叠层提供折扣与卡牌掉率加成 · *Reveal full maps now & next floors; stacks add shop discount and card drop bonus* |
| 15 | 户外腰包 *Outdoor Pouch* | 主动（5 充能） | 使用时翻出钥匙×1、炸弹×1、金币×3 · *5-charge active: +1 key, +1 bomb, +3 coins* |
| 16 | 怀表 *Pocket Watch* | 主动（4 充能） | 冻结时间 4 秒，仅玩家可行动 · *4-charge active: freeze time for 4 s* |
| 17 | 肾上腺素 *Adrenaline* | 主动（3 充能） | 本房间伤害/射速 **+2**、射程 **×5**、子弹速度 **×2**，消耗 1 滴红心 · *3-charge active: +2 dmg/+2 rps/×5 range/×2 tear speed; costs 1 heart* |
| 18 | 炸弹表舅 *Bomb Cousin* | 被动 | 炸弹 **+5**，爆炸范围 **×2**，伤害 **×2** · *+5 bombs, ×2 radius & damage* |
| 19 | 炸弹舅爷 *Bomb Uncle* | 被动 | 炸弹 **+99**，爆炸范围 **×5**，伤害 **×5**，附带强震屏 · *+99 bombs, ×5 radius & damage with strong shake* |
| 20 | 炸弹爷爷 *Bomb Grandpa* | 被动 | 免疫炸弹伤害，被爆炸改为治疗 · *Bomb immunity; explosions heal* |
| 21 | 魔术子弹 *Magic Bullet* | 被动 | 射程 **×3**，泪滴强力追踪 · *×3 range with strong homing tears* |
| 22 | 表弟 *Younger Cousin* | 跟班 | 跟班以 **3 次/秒** 射出 **4 点伤害** 泪滴，射程/速度为玩家 **1.5×** · *Familiar: 3 rps, 4 dmg, 1.5× range & speed* |
| 23 | 大姨妈 *Aunt Brimstone* | 跟班 | 蓄力 2 秒喷射 1.5 秒硫磺火，每 8 帧造成 0.75 伤害 · *Familiar: 2s charge, 1.5s brimstone beam (0.75 dmg per 8 frames)* |
| 24 | 黑屁股 *Black Buddy* | 跟班 | 自动拾取红心，累积 3 枚奖励随机资源 · *Collects red hearts; every three grants a random resource* |
| 25 | 神圣之心 *Holy Heart* | 被动 | 上限 +2、魂心 +3，伤害 ×2.5 +2、射程 ×9，附带飞行/穿透/追踪；满血时额外再乘 ×2.5，受伤后当房失效。 · *+2 max HP, +3 soul hearts; damage ×2.5 +2, range ×9, grants flight/penetration/homing; when at full HP, damage ×2.5 again until hit (room-based).* |
| 26 | 双瞳 *Double Eyes* | 被动 | 攻击变为双发，伤害 ×0.9；与多瞳/宝宝套装等兼容；道具房道具池；· *Fires two shots, damage ×0.9; compatible with other eye items/sets; in item room pool. * |
| 27 | 三瞳 *Triple Eyes* | 被动 | 攻击变为三发，射速 ×0.75；与双瞳/四瞳/宝宝套装等兼容；道具房道具池 · *Fires three shots, fire rate ×0.75; compatible with other eye items/sets; in item room pool.* |
| 28 | 四瞳 *Quad Eyes* | 被动 | 攻击变为四发，伤害 ×0.9，射速 ×0.75；与双瞳/三瞳/宝宝套装等兼容；道具房道具池 · *Fires four shots, damage ×0.9, fire rate ×0.75; compatible with other eye items/sets; in item room pool.* |

### 商店精选 · Shop Specials

| 编号 | 道具 · Item | 类型 | 效果 · Effect |
|:---:|:--|:--|:--|
| S1 | 血之力 *Blood Power* | 被动 | 生命越充沛，伤害越高 · *Damage scales with remaining red hearts* |
| S2 | 钱之力 *Money Power* | 被动 | 金币越多，火力越猛 · *Damage scales with held coins* |
| S3 | 绝望之力 *Despair Power* | 被动 | 红心越少越愤怒 · *Damage rises as health drops* |
| S4 | 炸弹表舅 *Bomb Cousin* | 被动 | 炸弹 **+5**，爆炸范围/伤害 **×2** · *+5 bombs; ×2 blast radius & damage* |
| S5 | 炸弹舅爷 *Bomb Uncle* | 被动 | 炸弹 **+99**，爆炸范围/伤害 **×5** 并额外震屏 · *+99 bombs; ×5 blast with heavy shake* |
| S6 | 炸弹爷爷 *Bomb Grandpa* | 被动 | 免疫爆炸伤害并改为治疗 · *Bomb damage heals you instead* |
| SR | 神圣之心 *Holy Heart* | 稀有被动 | 上限 **+2**、魂心 **+3**、伤害 **×2.5 +2**，附带飞行/穿透/追踪与神圣光环 · *+2 max HP, +3 soul hearts, ×2.5 dmg +2, grants flight/pierce/homing & holy aura* |

> 商店还会售卖“炸弹亲戚”等主池道具的额外拷贝。

### Boss 奖励 · Boss Rewards

| 编号 | 道具 · Item | 类型 | 效果 · Effect |
|:---:|:--|:--|:--|
| B1 | 狗粮 *Dog Food* | 被动 | 上限 **+1** 并立即回满 · *+1 max HP with heal* |
| B2 | 结束纸条 *Ending Note* | 被动 | 射速 **+0.75**，射程 **×1.1** · *+0.75 rps, ×1.1 range* |
| B3 | 热水壶 *Kettle* | 被动 | 伤害 **+1** · *+1 damage* |

> 其他 Boss 奖励可能掉落主池或主动类道具，便于补齐构筑。

### 献祭道具 · Life Trade Relics

| 编号 | 道具 · Item | 类型 | 效果 · Effect |
|:---:|:--|:--|:--|
| L1 | 硫磺火 *Brimstone* | 被动 | 攻击改为蓄力血色激光并强制上限 1，叠层加粗束宽 · *Charge a piercing brimstone beam; sets max HP to 1, stacks widen the beam* |
| L2 | 兄弟 *Brother* | 跟班 | 复制玩家射击与特效的跟班 · *Familiar mirrors your tears and modifiers* |
| L3 | 姐妹 *Sisters* | 跟班 | 左右双胞胎以 **0.75×** 伤害同步射击 · *Twin familiars fire at 0.75× your damage* |
| L4 | 表哥 *Cousin* | 跟班 | 发射追踪弹（伤害 5，射速 2 次/秒），射程/速度 **×2** · *Familiar: 2 rps homing tears, 5 dmg, 2× range & speed* |
| L5 | 亚巴顿 *Abaddon* | 被动 | 获得 3 点蓝心，伤害 **×2**，射程 **×3**，敌人移速下降 · *+3 soul hearts, damage ×2, range ×3, slows enemies* |
| L6 | 逃生工具 *Escape Tool* | 被动 | 移速 **×5**、子弹速度 **×5**、无敌帧 **×3**，并减少敌人生成量 · *×5 move & tear speed, ×3 i-frame duration, fewer enemies spawn* |
| L7 | 炸弹老祖 *Bomb Elder* | 被动 | 射击改为喷射定时炸弹（约 **320%** 伤害），同时强化炸弹半径与震动 · *Fires timed mega-bombs (~320% dmg) and buffs bomb radius/shake* |
| L8 | 炸弹鼻祖 *Bomb Progenitor* | 被动 | 长按布置导引准星，2 秒后连环轰炸（约 **2000%** 伤害，最多 16 枚） · *Hold to aim chained 2000% guided strikes (up to 16 bombs)* |

> 默认献祭 **1 点生命上限**；若有特殊代价会在道具面板上标注。

---

## 卡牌一览 · Card Deck

- **通透牌 · Seer Card**：当前楼层**地图全显** · *Reveal whole floor*  
- **伤害牌 · Rage Card**：本房间 **伤害 +2** · *+2 dmg this room*  
- **追踪牌 · Homing Card**：本房间 **泪滴追踪** · *Homing tears this room*  
- **杂耍牌 · Juggle Card**：**钥匙/炸弹/生命 各 1**  
- **无敌牌 · Invincible Card**：**3 秒无敌**  
- **血牌 · Blood Card**：**生命回满**  
- **穿透牌 · Pierce Card**：本房间**子弹穿透障碍**  
- **玩家牌 · Player Card**：**随机被动道具**

---

## 怪物图鉴 · Monster Bestiary

| 敌人 · Enemy | 类型 · Type | 行为 · Behavior（简述） |
|:--|:--:|:--|
| 追击者 · *Chaser* | 地面 · Ground | 直线猛冲；受击短暂后退。*Charges straight; recoils on hit.* |
| 轨道蛆 · *Orbiter* | 飞行 · Flying | 绕行锚点缓慢逼近。*Orbits a drifting anchor.* |
| 气囊怪 · *Gasbag* | 地面 · Ground | 近身点燃自爆，弹出小飞虫。*Explodes into Tiny Flies.* |
| 分裂体 · *Splitter* | 地面 · Ground | 死亡分裂再集结。*Splits into smaller clones.* |
| 易爆蛞蝓 · *Volatile* | 地面 · Ground | 触发引线，蓄满即爆。*Fuse → wide blast.* |
| 小飞虫 · *Tiny Fly* | 飞行 · Flying | 贴脸骚扰，弹飞再冲刺。*Buzz, bounce, re-engage.* |
| 老飞虫 · *Elder Fly* | 飞行 · Flying | 保持距离绕行并读条射击。*Circles, telegraphed volleys.* |
| 哨卫 · *Sentry* | 地面 · Ground | 原地锁定，三向弹幕。*Locks on, triple burst.* |
| 冲刺鬼 · *Dashling* | 地面 · Ground | 预兆→高速冲刺→疲劳循环。*Telegraph → lunge → recover.* |
| 潜伏者 · *Burrower* | 地面 · Ground | 潜地追踪，出土直刺。*Burrow and erupt lunge.* |
| 火花灵 · *Spark* | 飞行 · Flying | 小半径轨道，环形电弧弹。*Radial spark bursts.* |
| 育母虫 · *Brood* | 地面 · Ground | 中距离孵化小飞虫。*Spawns minions in radius.* |
| 蜘蛛跃者 · *Spider Leaper* | 地面 · Ground | 读条弹跳落地冲击，狂暴加速。*Telegraphed acrobatics.* |
| 炸弹客 · *Bomber* | 漫游并周期性丢下长导火索炸弹，逼迫你换位。*Roams and plants long-fuse bombs to flush you out.* |
| 暗影回声 · *Shadow Echo* | 悬浮援军，瞬移到主宰或玩家身侧纠缠。*Teleports around its master and lunges at the player.* |
| 悖论碎片 · *Paradox Shard* | 围绕终焉织主旋转并射出强力碎光；Boss 狂暴时攻势同步升级。*Orbits the Paradox heart and fires empowered shards when enraged.* |
---

## Boss 图鉴 · Boss Gallery

- **新增总览**：所有 Boss 的攻击现在拥有独立的前摇/后摇与视觉提示，便于读招与反击。

  *New:* every boss telegraphs each move with dedicated wind-ups, recoveries, and color cues.

- **哭泣塑像 · Idol**
  随机使用喷射弹幕 / 召唤援兵 / 冲刺；低血狂暴。
  *Sprays, summons, and charges; enrages at low HP.*

- **余烬教官 · Master**  
  跳斩、地震冲击波、扇形弹幕；狂暴后频率更高并召唤蜘蛛。  
  *Leaps, flame waves, spider calls—shorter cooldowns when enraged.*

- **炽耀九头蛇 · Hydra**  
  椭圆轨道盘旋；扇面/螺旋/灵魂球三套远程压场；可切换旋向与延迟爆裂。  
  *Orbiting arena control with fans, spirals, orbs; flips spin; timed bursts.*

- **占兆之眼 · Seer**  
  隐身跃迁至预设节点；释放光矛、镜像符阵或流星雨；符阵逐个爆裂成追踪针弹。  
  *Blinks to nodes, channels lances/sigils/meteors; runes detonate to tracking bolts.*

- **地窖泰坦 · Titan**
  缓步压境、连跳、地裂与碎片风暴；怒火提升后叠加延迟事件与更密弹幕。
  *Stalks, chains leaps, shockwaves, shard storms; stacks timed events when enraged.*

- **黯影穿梭者 · Umbra**
  瞬移追踪、暗影扇形与追踪刃雨交替施压，并可召唤暗影回声协同围攻，隐身与再现阶段短暂无敌。
  *Blinks around the arena, fans shadow needles, hurls homing blades, and calls Shadow Echo minions; vanish/reappear windows grant brief invulnerability.*

- **终焉织主 · Paradox**
  扭曲时间、分阶段改造场景，施放螺旋/风暴/追踪弧光并召唤悖论碎片与暗影仆从；二阶段开启虚空场景与时间减速。
  *Warps space-time, rewrites the arena, fires spirals and meteor storms, and summons paradox shards plus shadow minions; phase two drags you into the void with time dilation.*

---

## 无障碍与技术注记 · A11y & Tech Notes

- **单文件架构**：`index.html` 内联 CSS/JS，**零依赖**，可直接部署任意静态托管。  
- **屏幕键盘/作弊台**：使用 `aria-hidden`、`aria-expanded` 等可访问属性；支持**指针捕获**，触屏/手柄友好。  
- **高分屏绘制**：自动按设备像素比（DPR）重采样，逻辑坐标为 **800×600**，在高 DPI 下保持清晰。  
- **图鉴渲染**：拾取即登记集合；刷新时按 **ID** 排序并**异步绘制**像素缩略图，实现轻量图鉴。

---

## 运行与部署 · Run & Deploy

1. 克隆或下载仓库后，直接双击 `index.html` 用现代浏览器打开即可。  
   *Open `index.html` directly in a modern browser.*
2. 推荐环境：Chromium/Firefox 最新版，启用硬件加速。  
3. 可选：使用任意静态托管（GitHub Pages、Vercel、Netlify、本地 `python -m http.server`）一键上线。  
4. 移动端建议横屏游玩；若触控设备 DPI 过高，可在设置中开启“像素适配”选项（若已实现）。

---

## 版权 · License

© Authors. 保留所有权利 / All rights reserved.  
（如需开源协议，请在此替换为 MIT/Apache-2.0 等声明。）
