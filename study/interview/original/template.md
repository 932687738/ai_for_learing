# Spring AI 核心概念与 ReAct/Transformer 辨析

## 一、Spring AI 中的 Transform（转换器）

`Transform` 在 Spring AI 中有两大核心作用：**ETL 管道中的数据预处理** 和 **模型输出的结构化转换**。

### 1.1 ETL 管道中的数据转换

在 RAG（检索增强生成）流程的 ETL 阶段，`Transform` 负责清洗、优化与扩充原始数据。主要实现包括：

- **文本分割**：`TokenTextSplitter` 按 Token 大小切分长文本。
- **格式统一**：`ContentFormatTransformer` 将 PDF、HTML 等转为纯文本。
- **元数据丰富**：`KeywordMetadataEnricher` / `SummaryMetadataEnricher` 自动提取关键词和摘要。

可以组合多个 Transformer 形成流水线：

```java
// 伪代码示例：文档处理流水线
List<Document> transformedDocs = keywordEnricher.apply(
    tokenTextSplitter.apply(rawDocs)
);
1.2 结构化输出转换
将模型生成的非结构化文本转换为 Java 对象。Spring AI 的 ChatClient 结合 BeanOutputConverter 可轻松实现：

java
// 定义一个期望的Java记录（Record）
record ActorsFilms(String actor, List<String> movies) {}

// 使用ChatClient发起请求，并直接将输出映射为ActorsFilms对象
ActorsFilms films = ChatClient.create(chatModel)
    .prompt()
    .user(u -> u.text("为{actor}生成5部电影的作品年表。").param("actor", "汤姆·汉克斯"))
    .call()
    .entity(ActorsFilms.class);  // 直接得到对象

System.out.println(films.actor());  // 输出：汤姆·汉克斯
films.movies().forEach(System.out::println); // 输出电影列表
小结：Transform 既充当数据“精炼厂”（为向量库准备高质量输入），又充当输出“翻译官”（将自由文本转为结构化数据）。

二、Spring AI 中的 Advisor（顾问）
Advisor 实现面向切面编程（AOP），允许在调用 AI 模型的前后动态插入横切逻辑，无需修改业务代码。

2.1 常见内置 Advisor
Advisor 名称	作用
LoggerAdvisor	记录请求/响应日志及耗时
RetryAdvisor	调用失败时自动重试
CacheAdvisor	缓存相同请求的响应
RateLimiterAdvisor	限制调用频率
MessageHistoryAdvisor	管理多轮对话历史
CircuitBreakerAdvisor	熔断保护
2.2 使用方式
java
ChatClient chatClient = ChatClient.create(chatModel)
    .advisors(
        new LoggerAdvisor(),           // 记录日志
        new RetryAdvisor(3),           // 最多重试3次
        new CacheAdvisor(cacheManager) // 启用缓存
    )
    .build();

String response = chatClient.prompt("Hello AI")
    .advisors(anotherAdvisor)          // 单次调用可临时增加 Advisor
    .call()
    .content();
2.3 自定义 Advisor
java
public class SafeWordAdvisor implements Advisor {
    @Override
    public ChatResponse aroundCall(AdvisorChain chain, ChatRequest request) {
        // 前置：检查请求是否包含敏感词
        if (containsSensitiveWords(request.getUserText())) {
            return new ChatResponse("请求包含敏感内容，已拒绝");
        }
        // 继续调用下一个 Advisor 或最终模型
        ChatResponse response = chain.next(request);
        // 后置：对响应进行脱敏
        response = desensitize(response);
        return response;
    }
}
2.4 Transformer vs Advisor 对比
维度	Transformer	Advisor
作用阶段	ETL 管道（调用前数据准备）	模型调用时的请求/响应拦截
主要对象	Document 文档块	Prompt / ChatResponse
典型场景	文本切分、格式统一、元数据丰富	日志、重试、缓存、限流、对话历史
是否直接影响模型调用	不直接调用模型	直接包裹模型调用过程
小结：Advisor 是为 AI 调用注入横切关注点的机制，以声明式、可组合的方式增强 ChatClient，保持业务逻辑简洁。

三、ReAct 与 Transformer 的区别
两者完全不同：ReAct 是一种 AI 智能体的工作模式，Transformer 是一种神经网络架构。

3.1 核心差异
对比维度	Transformer 架构	ReAct 模式
定义	基于自注意力机制的神经网络架构，是大语言模型的基础	推理与行动结合的提示策略，全称 Reasoning + Acting
目的	高效捕捉文本长距离依赖，进行语义理解与生成	通过“思考-行动-观察”循环调用外部工具，解决复杂任务
运行逻辑	基于已学习参数，对输入进行一次性计算预测输出	迭代循环：思考 → 行动 → 观察
对外交互能力	无（知识止于训练数据）	有（调用搜索引擎、API、计算器等）
典型应用	GPT、BERT、T5 等大模型的基础架构	AutoGPT、智能客服、数据分析智能体
3.2 关系说明
在 ReAct 模式的实现中，基于 Transformer 架构的大模型通常充当“思考”步骤的核心引擎。模型决定下一步行动，由外部系统执行，再将观察结果返回模型，开始下一轮循环。

类比：Transformer 是发动机（提供动力），ReAct 是智能驾驶系统（规划路线、调用工具、达成目标）。

四、总结
Transform：负责数据处理（ETL 中的转换）和输出结构化，是数据“精炼厂”和输出“翻译官”。

Advisor：负责 AI 调用的横切关注点（日志、重试、缓存等），是 AOP 风格的拦截器。

ReAct vs Transformer：ReAct 是智能体的工作范式，Transformer 是底层网络架构；两者处于不同抽象层次，且常协同工作（Transformer 模型作为 ReAct 智能体的“大脑”）。