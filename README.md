项目概览 · Project Overview

这是一个受 《以撒的结合》 启发的 HTML5 Canvas 单页游戏。
涵盖自适应界面、键位提示与集成控制面板，支持浏览器直接游玩，呈现 “地窖速通实验室” 的俯视角射击体验。

It is a single-file HTML5 Canvas experiment inspired by The Binding of Isaac, bundling adaptive layout, on-screen guidance, and integrated control panels to deliver a “Basement Speedrun Lab” top-down shooter entirely in the browser.

快速上手 · Quick Start

控制 / Controls

WASD：移动 (move)

方向键：射击 (shoot)

E：放置炸弹 (drop bombs)

F：购买 (purchase)

Enter：开始或回主菜单 (start/menu)

P：暂停 (pause)

R：重开 (restart)

开局提示、暂停信息和死亡提示通过覆盖层呈现，点击 “我要出发！” 即可立即开跑。
Overlays brief you at start, pause, and game over; click “我要出发！” to dive in.

界面与可访问性 · UI & Accessibility

自适应深色界面：HUD 与面板适配桌面与移动端

虚拟按键：支持长按/点按，映射物理键码

作弊面板：可直接修改生命、伤害、移速、资源与道具，字段同步玩家状态并具备 ARIA 属性

道具图鉴：实时累计已获得道具，绘制像素化小图并统计进度，鼓励继续探索

核心系统 · Core Systems
地下城生成 · Dungeon Generation

9×9 网格随机游走生成主线房间

自动追加 Boss 房、道具房与商店

确保房门连通与可达性

房间逻辑

不同类型决定敌人、障碍、掉落与锁门

Boss 房注入特定首领

安全房直接标记清理完成

障碍系统

包含隐藏/镂空结构

炸毁后有概率掉落物

密室宝箱可能刷新隐藏道具

玩家与战斗 · Player & Combat

移动/射击方向分离，含冲刺与射击惯性

泪滴：射速、寿命影响 DPS

伤害：基础值 + 乘区 + 特效实时重算

炸弹：导火、击退、爆炸半径，能炸障碍、推掉落、波及敌我

资源与掉落 · Resources & Drops

配置表定义掉落几率（心、钥匙、金币等）

拾取物具备惯性、边界约束与爆炸连锁

道具与商店 · Items & Shops

三大道具池：基础 / 商店 / Boss（加权抽取，唯一编号）

商店：15/5 金币定价，购买后刷新

拾取道具触发提示、登记图鉴、即时应用

道具图鉴 · Item Codex
ID	中文名	English Name	效果 Effect
01	洋葱	Onion	射速 +0.75 次/秒 · Fire rate +0.75 shots/sec
02	焦油抹布	Tar Rag	伤害 +0.5，泪滴更厚重 · +0.5 dmg, heavier tears
03	小短跑鞋	Sprinter Shoes	移速 +35 · Move speed +35
04	胡椒牛排	Pepper Steak	伤害 +1，射速 +1，射程 ×1.5，血上限 +1
05	绳子	Rope	赋予飞行 · Grants flight
06	酒枣	Spirit Date	射程 ×1.5，泪滴穿透障碍
07	伙伴倒戈犬	Betrayal Hound	伤害 ×2+1.5，射速 -0.25
08	绝望呐喊	Cry of Despair	射程 ×5
09	坏东西	Bad Thing	子弹速度 ×1.1
10	好东西	Good Thing	子弹速度 ×0.75，射速 +0.75，射程 ×1.25
11	血之力	Blood Power	血越厚，伤害越高
12	钱之力	Money Power	金币转化为伤害
13	绝望之力	Despair Power	血越少，伤害越高
14	狗粮	Dog Food	血量上限 +1，拾取即治疗
15	结束纸条	Ending Note	射速 +0.75，射程 ×1.1
16	热水壶	Kettle	伤害 +1
敌人图鉴 · Enemy Bestiary

追击者 · Chaser：冲向玩家，被击中短暂击退

轨道蛆 · Orbiter：围绕基点旋转缓慢逼近，贴身伤害

气囊怪 · Gasbag：靠近时自爆，召唤小飞虫

小飞虫 · Tiny Fly：高速贴脸，受击弹开

老飞虫 · Elder Fly：维持距离后发射泪弹

蜘蛛跃者 · Spider Leaper：读条后跃向玩家，落地伤害

Boss 图鉴 · Boss Gallery

哭泣塑像 · 社畜蛹 (Idol)

冲刺、激光雨、狂暴阶段

血量下降后攻速/弹幕密度上升

余烬教官 · Master

徘徊、读条、跳斩、震地与火焰波

半血后进入愤怒形态，频率提升
