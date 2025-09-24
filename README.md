# 地窖速通实验室 · Basement Speedrun Lab

[![Progress](https://img.shields.io/badge/Progress-96%25-blue)](#) [![HTML5 Canvas](https://img.shields.io/badge/Engine-HTML5%20Canvas-orange)](#) [![Single-file](https://img.shields.io/badge/Build-Single--file-green)](#) [![Zero Deps](https://img.shields.io/badge/Deps-0-lightgrey)](#)

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
*Movement uses acceleration/drift; tears recalc stats; bombs shove/chain/shake and reveal secrets.*

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

| ID | 道具 · Item | 效果 · Effect |
|---:|:--|:--|
| 01 | 洋葱 *Onion* | 射速 **+0.75 次/秒** · *+0.75 shots/sec* |
| 02 | 焦油抹布 *Tar Rag* | 伤害 **+0.5**，泪滴更厚重 · *+0.5 dmg, heavier tears* |
| 03 | 小短跑鞋 *Sprinter Shoes* | 移动速度 **+35** · *+35 move speed* |
| 04 | 胡椒牛排 *Pepper Steak* | 伤害 **+1**，射速 **+1**，射程 **×1.5**，上限 **+1** 并治疗 · *+1 dmg, +1 rps, ×1.5 range, +1 max HP w/ heal* |
| 05 | 绳子 *Rope* | 获得**飞行** · *Grants flight* |
| 06 | 酒枣 *Spirit Date* | 射程 **×1.5**，泪滴**穿透障碍** · *×1.5 range, piercing* |
| 07 | 伙伴倒戈犬 *Betrayal Hound* | 伤害 **×2 +1.5**，射速 **−0.25** 次/秒 |
| 08 | 绝望呐喊 *Cry of Despair* | 射程/寿命 **×5** |
| 09 | 坏东西 *Bad Thing* | 子弹速度 **×1.1** |
| 10 | 好东西 *Good Thing* | 子弹速度 **×0.75**，射速 **+0.75**，射程 **×1.25** |
| 11 | 透视雷达 *Seer Map* | 当前与未来楼层**地图全显** |
| 12 | 户外腰包 *Outdoor Pouch* | **主动·5 充能**：钥匙×1、炸弹×1、金币×3 |
| 13 | 肾上腺素 *Adrenaline* | **主动·3 充能**：本房间 **伤害+2/射速+2/射程×5/弹速×2**，生命 **−1** |
| 14 | 炸弹表舅 *Bomb Cousin* | 炸弹 **+5**，爆炸范围 **×2**，伤害 **×2** |
| 15 | 炸弹舅爷 *Bomb Uncle* | 炸弹 **+99**，范围 **×5**，伤害 **×5**，触发**震动** |
| 16 | 炸弹爷爷 *Bomb Grandpa* | **免疫炸弹伤害**，爆炸**治疗** |
| 17 | 魔术子弹 *Magic Bullet* | 射程 **×3**，泪滴**追踪最近敌人** |
| 18 | 血之力 *Blood Power* | **生命越多伤害越高** |
| 19 | 钱之力 *Money Power* | **金币转化为伤害** |
| 20 | 绝望之力 *Despair Power* | **血越少越凶猛** |
| 21 | 狗粮 *Dog Food* | **上限 +1 并立即恢复** |
| 22 | 结束纸条 *Ending Note* | **射速 +0.75**，**射程 ×1.1** |
| 23 | 热水壶 *Kettle* | **伤害 +1** |
| 24 | 硫磺火 *idkeng* | **更改攻击方式** |

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

| 敌人 · Enemy | 行为 · Behavior（简述） |
|:--|:--|
| 追击者 · *Chaser* | 直线猛冲；受击短暂后退。*Charges straight; recoils on hit.* |
| 轨道蛆 · *Orbiter* | 绕行锚点缓慢逼近。*Orbits a drifting anchor.* |
| 气囊怪 · *Gasbag* | 近身点燃自爆，弹出小飞虫。*Explodes into Tiny Flies.* |
| 分裂体 · *Splitter* | 死亡分裂再集结。*Splits into smaller clones.* |
| 易爆蛞蝓 · *Volatile* | 触发引线，蓄满即爆。*Fuse → wide blast.* |
| 小飞虫 · *Tiny Fly* | 贴脸骚扰，弹飞再冲刺。*Buzz, bounce, re-engage.* |
| 老飞虫 · *Elder Fly* | 保持距离绕行并读条射击。*Circles, telegraphed volleys.* |
| 哨卫 · *Sentry* | 原地锁定，三向弹幕。*Locks on, triple burst.* |
| 冲刺鬼 · *Dashling* | 预兆→高速冲刺→疲劳循环。*Telegraph → lunge → recover.* |
| 潜伏者 · *Burrower* | 潜地追踪，出土直刺。*Burrow and erupt lunge.* |
| 火花灵 · *Spark* | 小半径轨道，环形电弧弹。*Radial spark bursts.* |
| 育母虫 · *Brood* | 中距离孵化小飞虫。*Spawns minions in radius.* |
| 蜘蛛跃者 · *Spider Leaper* | 读条弹跳落地冲击，狂暴加速。*Telegraphed acrobatics.* |

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
