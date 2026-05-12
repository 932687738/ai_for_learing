# 第 34 课：模型基础设施：GPU、TPU、部署与推理加速

## 0. 本课定位

本课补齐模型基础设施、GPU、TPU、推理加速和 inference 工程。第 24 课已讲 KV Cache、量化、投机解码、vLLM、Triton，本课面向工程选型和部署运维。

## 1. 学习目标

完成本课后，你应该能：

1. 解释训练、微调、批量推理、在线推理、实时推理的资源差异。
2. 区分 GPU、TPU、CPU、本地 NPU 的典型适用场景。
3. 理解 batching、KV cache、quantization、speculative decoding、parallelism。
4. 设计 API 模型、本地模型、混合模型的部署架构。
5. 从吞吐、延迟、成本、可靠性和合规角度做基础设施选型。

## 2. 核心概念

| 概念 | 作用 |
| --- | --- |
| GPU | 通用深度学习加速，生态成熟 |
| TPU | Google 面向张量计算的专用加速器 |
| KV Cache | 缓存 Transformer 历史 key/value，降低自回归解码成本 |
| Quantization | 降低权重 / 激活精度，减少显存和提升吞吐 |
| Batching | 多请求合批，提高吞吐 |
| Streaming | 降低首 token 体感延迟 |
| Speculative Decoding | 小模型草稿 + 大模型验证，提高解码速度 |

## 3. 部署模式

```text
API-first
  -> 低运维、快上线、依赖供应商

Self-hosted
  -> 强控制、强合规、需要 GPU / 推理服务运维

Hybrid
  -> 敏感任务本地，通用任务 API，成本和能力折中
```

## 4. Java 企业系统接入建议

业务服务不要直接管理 GPU 推理细节。推荐分层：

```text
Spring Boot 业务服务
  -> AI Gateway
  -> Provider Adapter
  -> Hosted API / vLLM / TensorRT-LLM / Ollama / Triton
```

AI Gateway 负责：

- 模型路由。
- 限流和超时。
- 熔断和降级。
- 请求审计。
- 成本统计。
- eval 采样。

## 5. 常见误区

1. 只看单次请求延迟，不看吞吐和成本。
2. 低估显存需求和上下文长度影响。
3. 把模型部署和业务服务混在一个进程。
4. 没有容量规划、限流、排队和降级。
5. 忽略模型版本、镜像版本、驱动版本的可复现性。

## 6. 实践任务

1. 为企业客服系统设计 API-first 架构。
2. 为内网知识库设计 self-hosted Llama 推理架构。
3. 估算 100 QPS、平均 2k token 输入、500 token 输出的成本指标。
4. 设计 AI Gateway 的日志字段。

## 7. 阶段验收标准

- 能解释基础设施选型与业务需求的关系。
- 能设计模型网关和推理服务边界。
- 能说明推理加速不是单点技术，而是系统工程。

## 8. 本课使用的信息源

- OpenAI Realtime API：https://platform.openai.com/docs/api-reference/realtime
- vLLM 文档：https://docs.vllm.ai/
- NVIDIA TensorRT-LLM：https://nvidia.github.io/TensorRT-LLM/
- Google Cloud TPU：https://cloud.google.com/tpu/docs

## 9. 问答记录

暂无。

## 10. 外部补充

暂无。

## 11. 结构化补充（整改）

### 核心讲解

- 基础设施选型必须从业务 SLA 反推，不是从硬件热度出发。
- GPU/TPU/推理引擎选择要结合吞吐、时延、成本和运维复杂度。
- 生产链路应通过 AI Gateway 隔离业务与推理实现细节。

### 拓展阅读

- vLLM Docs: https://docs.vllm.ai/
- TensorRT-LLM: https://nvidia.github.io/TensorRT-LLM/
- Google TPU Docs: https://cloud.google.com/tpu/docs

### 问答记录

- 2026-05-12：已加入统一学习闭环，后续补容量估算模板。

### 外部补充

- 暂无（可补充真实 QPS/Token 规模数据）。

### 本课掌握检查

- 你能否根据 QPS 和 token 规模给出容量估算思路？
- 你能否说明何时应选 API-first、self-hosted 或 hybrid？

### 下一课前置条件

- 给出一版基础设施选型决策记录（背景、决策、后果、备选）。

## 12. 跨章节边界（去重指引）

- 本课主讲：基础设施选型、部署形态与容量治理。
- 第 24 课主讲：推理优化机制与内核技术，本课仅引用其技术结论。
- 第 14 课主讲：应用工程化治理，本课输出基础设施能力供其接入。
- 第 36 课主讲：新兴生态工具评估，本课提供基础设施可行性判断标准。

## 回归评测记录（2026-05-12）

- run_id: `baseline-2026-05-12`
- case: `E34-infra-decision`
- result: `PASS`
- 记录：`study/projects/27-36-min-eval-regression-run-2026-05-12.md`

## 可运行示例（Java，整改新增）

```java
public class CapacityEstimatorDemo {
    // 粗略估算：tokensPerSec = qps * (inputTokens + outputTokens)
    static long estimateTokensPerSec(int qps, int inputTokens, int outputTokens) {
        return (long) qps * (inputTokens + outputTokens);
    }

    public static void main(String[] args) {
        long tps = estimateTokensPerSec(100, 2000, 500);
        System.out.println("Estimated tokens/sec = " + tps); // 250000
        System.out.println("Use this as baseline for infra sizing.");
    }
}
```

## 学习状态

- 状态：未开始（内容已就绪）
- 最近更新：2026-05-12
- 进入下一课条件：学员明确回复“这节课已经学会”
