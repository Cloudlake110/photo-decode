# Photo Decode · 解图

<p align="center">
  <strong>一张图，解出另一种视觉。</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skill-v1.0.0-2B2B2B" alt="Skill v1.0.0">
  <img src="https://img.shields.io/badge/status-stable-4C7A67" alt="Stable">
  <img src="https://img.shields.io/badge/license-non--commercial-B8844F" alt="Non-commercial license">
  <img src="https://img.shields.io/badge/examples-5-D76A5A" alt="5 examples">
</p>

「解图 Photo Decode」是一个面向 Codex / Agent 的视觉 Skill。上传任意图片，它会制作成固定的五区块编辑分析板：

1. **ORIGINAL SOURCE** — 原图
2. **REINTERPRETED VISUAL (FLAT)** — 去背景、压缩、扁平化后的新主视觉
3. **IMAGE ESSENCE** — 标题 + 图片解读
4. **COLOR PALETTE** — 从右侧新主视觉提取色卡，并为每个色块标注 HEX 色号
5. **KEY ELEMENTS** — 从右侧新主视觉继续拆出的关键元素

核心链路：

> **复杂信息 → 提取 → 选择 → 压缩 → 去背景 → 扁平化 → 形成新的平面视觉对象**

## 两条最重要的联动规则

**色卡不是从原图提取。** 它必须等 `REINTERPRETED VISUAL (FLAT)` 完成后，再从右侧新图提取。

**关键元素也不是从原图直接拆。** 它必须来自右侧新图；如果右侧已经删除某个背景信息，右下角就不能再把它作为元素放回来。

```text
ORIGINAL SOURCE
      ↓
REINTERPRETED VISUAL (FLAT)
      ↓
COLOR PALETTE + KEY ELEMENTS
```

## 五个精选稳定案例

| 人物肖像 | 高饱和风景 |
|---|---|
| ![Portrait](examples/gallery/06-portrait.png) | ![Landscape](examples/gallery/04-saturated-landscape.png) |

| 复杂新闻现场 | 多人群像 |
|---|---|
| ![Complex news](examples/gallery/05-complex-news-scene.png) | ![Group portrait](examples/gallery/07-group-portrait.png) |

### 产品 / 商业陈列

![Retail display](examples/gallery/08-retail-display.png)

## 已测试类型

- 世界名画 / 绘画
- 新闻照片 / 复杂现场
- 人物肖像
- 多人 / 群像
- 高饱和风景
- 建筑 / 空间
- 产品 / 商业陈列
- 广告 / 强图形图片

## 安装到 Codex

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Cloudlake110/photo-decode.git ~/.codex/skills/photo-decode
```

然后重新开启 Codex 会话。

## 使用

```text
调用“解图 / Photo Decode”处理这张图片。
```

或者：

```text
Use photo-decode on this image.
```

## 固定五区块

每次输出必须包含：

```text
1. ORIGINAL SOURCE
2. REINTERPRETED VISUAL (FLAT)
3. IMAGE ESSENCE
4. COLOR PALETTE
5. KEY ELEMENTS
```

其中色卡下方 **每个色块都必须有 HEX 色号**。

## 质量门控

Skill 会检查：五区块完整性、右侧是否真正扁平化、背景是否删除、色卡是否来自右图、HEX 是否缺失、右下元素是否来自右图、群像主次、新闻图事实边界，以及是否出现无来源圆形/波浪/拱形等模板化装饰。

详见 [`references/quality-gates.md`](references/quality-gates.md)。

## 公开发布与许可声明

Photo Decode 当前以 **source-available（源码公开）+ 非商业许可** 发布，允许个人、教育、研究与其他非商业使用。由于存在非商业限制，我们不会把它误称为 OSI 定义下的开源软件。

详见 [`LICENSE.md`](LICENSE.md) 与 [`NOTICE.md`](NOTICE.md)。

## 来源说明

Photo Decode 是在持续测试和用户反馈中形成的扩展工作流，其视觉解构方向受到 **ZzzLc0405/photo-abstract-editorial** 的启发。本仓库不包含、不重新分发上游 Prompt 文件、文档正文或示例图片。

## 版本

**v1.0.0 — 首个稳定公开发布候选版**

详见 [`RELEASE_NOTES.md`](RELEASE_NOTES.md) 与 [`CHANGELOG.md`](CHANGELOG.md)。
