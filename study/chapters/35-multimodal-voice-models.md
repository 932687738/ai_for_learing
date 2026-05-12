# 第 35 课：多模态与语音模型应用开发

## 0. 本课定位

本课补齐多模态和语音模型。多模态不只是“能看图”，还包括文本、图像、音频、视频、实时语音、多模态检索和多模态 eval。

## 1. 学习目标

完成本课后，你应该能：

1. 解释 text、image、audio、video、speech-to-text、text-to-speech、speech-to-speech。
2. 设计语音客服、会议纪要、图片理解、文档视觉解析等应用。
3. 理解 Realtime API、WebRTC / WebSocket、流式转写、低延迟语音交互。
4. 将多模态能力接入 Java / Spring AI 或 Python 服务。
5. 设计音频和图像 eval，避免只评文本结果。

## 2. 核心概念

| 能力 | 输入 | 输出 | 典型应用 |
| --- | --- | --- | --- |
| Speech-to-text | 音频 | 文本 | 转写、质检、会议纪要 |
| Text-to-speech | 文本 | 音频 | 语音播报、客服外呼 |
| Speech-to-speech | 音频 | 音频 | 实时语音助手 |
| Vision | 图像 / 截图 | 文本 / JSON | 票据识别、页面理解 |
| Multimodal RAG | 文本 + 图像 + 表格 | 答案 + 引用 | PDF、PPT、合同问答 |

## 3. 语音 Agent 架构

```text
麦克风 / 电话
  -> VAD
  -> streaming transcription
  -> intent / dialogue state
  -> tool calling / RAG
  -> response generation
  -> text-to-speech
  -> audio playback
```

关键指标：

- 首响延迟。
- 端到端延迟。
- 打断能力。
- 转写准确率。
- 工具调用正确率。
- 安全拒答和人工转接。

## 4. Java / Spring AI 落地

Spring AI 已提供多类模型抽象，包括 Chat、Embedding、Audio Transcription、Text to Speech 等。企业 Java 系统可以把语音能力设计成独立服务：

```text
Voice Gateway
  -> Transcription Service
  -> Dialogue Service
  -> RAG / Tool Service
  -> TTS Service
```

这样做的好处是音频流处理、业务决策和工具执行可以独立扩展。

## 5. 常见误区

1. 用文本聊天的思路直接套语音交互。
2. 忽略打断、静音检测、噪音、口音和延迟。
3. 转写错误不进入 eval。
4. 图片理解不保存原图、裁剪区域和模型解释。
5. 多模态系统没有人工复核入口。

## 6. 实践任务

1. 设计一个语音客服的状态机。
2. 为会议纪要系统设计音频转写 eval。
3. 为票据图片识别设计 JSON 输出 schema。
4. 比较普通 chat API 和 realtime speech-to-speech 的工程差异。

## 7. 阶段验收标准

- 能解释多模态应用的输入输出链路。
- 能设计语音 Agent 的低延迟架构。
- 能把多模态结果纳入 eval 和安全治理。

## 8. 本课使用的信息源

- OpenAI Audio API：https://platform.openai.com/docs/api-reference/audio
- OpenAI Realtime API：https://platform.openai.com/docs/api-reference/realtime
- Spring AI API：https://docs.spring.io/spring-ai/reference/api/

## 9. 问答记录

暂无。

## 10. 外部补充

暂无。

## 11. 结构化补充（整改）

### 核心讲解

- 多模态系统核心在于链路设计：采集、理解、决策、执行、反馈。
- 语音场景要优先处理实时性、打断和稳定性，而非只追求文本准确率。
- 评测要覆盖转写质量、工具调用正确率和用户体验指标。

### 拓展阅读

- OpenAI Audio API: https://platform.openai.com/docs/api-reference/audio
- OpenAI Realtime API: https://platform.openai.com/docs/api-reference/realtime

### 问答记录

- 2026-05-12：补结构化模板，后续补语音链路可运行样例。

### 外部补充

- 暂无（可补充你们语音交互或图像识别业务场景）。

### 本课掌握检查

- 你能否画出一个语音 Agent 的端到端时序？
- 你能否定义 3 个关键实时指标并给出监控方式？

### 下一课前置条件

- 提交一份语音/多模态最小可行架构草图与评测指标表。

## 12. 语音链路最小可运行样例（整改新增）

> 说明：以下示例用于演示“转写 -> 回复 -> 延迟统计”最小闭环，便于后续替换成真实业务工具链。

```python
import time
from openai import OpenAI

client = OpenAI()

audio_path = "sample.wav"  # 本地测试音频

t0 = time.time()
with open(audio_path, "rb") as f:
    transcript = client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",
        file=f
    )
t1 = time.time()

user_text = transcript.text
resp = client.responses.create(
    model="gpt-4.1-mini",
    input=f"请根据以下转写文本做简要总结：{user_text}"
)
t2 = time.time()

answer = resp.output_text

print("transcript:", user_text)
print("answer:", answer)
print("asr_latency_ms:", int((t1 - t0) * 1000))
print("e2e_latency_ms:", int((t2 - t0) * 1000))
```

建议监控字段：

- `asr_latency_ms`
- `llm_latency_ms`
- `e2e_latency_ms`
- `interrupt_count`

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E35-voice-chain`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
public class VoiceLatencyDemo {
    public static void main(String[] args) throws Exception {
        long t0 = System.currentTimeMillis();
        simulate("asr");
        long t1 = System.currentTimeMillis();
        simulate("llm");
        long t2 = System.currentTimeMillis();
        System.out.println("asr_latency_ms=" + (t1 - t0));
        System.out.println("e2e_latency_ms=" + (t2 - t0));
    }

    static void simulate(String stage) throws Exception {
        // 仅用于演示链路计时逻辑
        if ("asr".equals(stage)) Thread.sleep(120);
        else Thread.sleep(180);
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”
