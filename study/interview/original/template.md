Spring AI 核心技术与实践指南
1. 概述
   本文档总结了 Spring AI 框架中的关键技术点，包括核心组件、检索优化、提示词设计、输出检测、文本补全、问题转换、多智能体协作及工作流模式等，并提供可复用的代码示例。

2. Transformer 与 Advisor
   2.1 Transformer
   负责数据转换，如文档分割、内容增强、结构化输出格式化。

java
// 文档分割示例
TextSplitter splitter = new TokenTextSplitter();
List<Document> chunks = splitter.split(document);

// 结构化输出转换
BeanOutputConverter<MyPojo> converter = new BeanOutputConverter<>(MyPojo.class);
MyPojo result = chatClient.prompt()
.user("Extract info...")
.call()
.entity(MyPojo.class);
2.2 Advisor
实现横切关注点（记忆、RAG、日志、安全等），采用责任链模式。

java
// 自定义回答验证 Advisor
public class ResponseValidationAdvisor implements CallAdvisor {
@Override
public AdvisedResponse adviseCall(AdvisedRequest request, CallAdvisorChain chain) {
AdvisedResponse response = chain.nextCall(request);
String content = response.response().getResult().getOutput().getText();
if (!isValid(content)) {
throw new RuntimeException("Invalid response");
}
return response;
}

    @Override
    public int getOrder() { return 0; }
}

// 使用 Advisor
ChatClient client = ChatClient.builder(chatModel)
.addAdvisors(new MessageChatMemoryAdvisor(), new QuestionAnswerAdvisor())
.build();
3. 检索效率优化
   3.1 架构与索引
   分片与副本：合理选择分片键，控制分片大小（10GB-50GB），使用副本提升吞吐。

向量索引：HNSW（低延迟）、IVF（内存友好）、DiskANN（SSD平衡）。

yaml
# Elasticsearch 索引配置示例
settings:
number_of_shards: 3
number_of_replicas: 1
index:
refresh_interval: 30s
3.2 查询优化
java
// 使用路由精确查找
@Document(indexName = "orders", routing = "customerId")
public class Order { ... }

// 查询时指定 routing
SearchRequest request = SearchRequest.of(q -> q
.index("orders")
.routing("cust_123")
.query(...)
);
3.3 缓存策略
java
@Cacheable(value = "aiResponses", key = "#prompt")
public String getCompletion(String prompt) {
return chatClient.prompt(prompt).call().content();
}
4. 提示词设计
   4.1 核心原则
   清晰明确、提供角色与背景、使用分隔符、指定输出格式。

4.2 结构化模板
text
# Role
你是一位资深Python面试官

# Task
提出3个关于装饰器的问题

# Constraints
由浅入深，每个问题附带预期答案

# Output Format
JSON: [{"question": "", "expected_answer": ""}]
4.3 Spring AI 中实践
java
// 使用 PromptTemplate
PromptTemplate template = new PromptTemplate("Translate to {lang}: {text}");
Prompt prompt = template.create(Map.of("lang", "French", "text", "Hello"));
String response = chatClient.prompt(prompt).call().content();
5. 回答检测机制
   5.1 检测维度
   事实准确性、安全性、格式合规、相关性、逻辑一致性、来源可溯。

5.2 实现方案
5.2.1 规则校验
java
public boolean isValidJson(String response) {
try { new ObjectMapper().readTree(response); return true; }
catch (Exception e) { return false; }
}
5.2.2 LLM-as-Judge
java
public String selfCorrect(String originalQuestion, String firstAnswer) {
return chatClient.prompt()
.user("Check the following answer for accuracy. If wrong, correct it.\n"
+ "Question: " + originalQuestion + "\nAnswer: " + firstAnswer)
.call().content();
}
5.2.3 集成到 Advisor
参见第 2.2 节 ResponseValidationAdvisor 示例。

6. 文本补全实现
   6.1 极简模式
   java
   @Service
   public class CompletionService {
   private final ChatClient chatClient;

   public CompletionService(ChatClient.Builder builder) {
   this.chatClient = builder.build();
   }

   public String complete(String prompt) {
   return chatClient.prompt().user(prompt).call().content();
   }
   }
   6.2 结构化输出
   java
   record Champion(String first, String last, List<Integer> years) {}

Champion champion = chatClient.prompt()
.user("Current chess world champion and years")
.call()
.entity(Champion.class);
6.3 流式输出
java
@GetMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
public Flux<String> stream(@RequestParam String prompt) {
return chatClient.prompt().user(prompt).stream().content();
}
6.4 参数调优
java
ChatResponse response = chatClient.prompt()
.user(prompt)
.options(ChatOptions.builder()
.temperature(0.7)
.maxTokens(500)
.build())
.call();
7. 问题转换提高精准度
   7.1 基于 LLM 的重写
   java
   @Component
   public class QueryRewriteAdvisor implements CallAdvisor {
   private final ChatClient rewriteClient;

   public QueryRewriteAdvisor(ChatClient.Builder builder) {
   this.rewriteClient = builder
   .defaultSystem("Rewrite the user query into a clear, precise form. Output only the rewritten query.")
   .build();
   }

   @Override
   public AdvisedResponse adviseCall(AdvisedRequest request, CallAdvisorChain chain) {
   String rewritten = rewriteClient.prompt()
   .user("Original: " + request.userText())
   .call()
   .content();
   AdvisedRequest newRequest = AdvisedRequest.from(request).withUserText(rewritten).build();
   return chain.nextCall(newRequest);
   }

   @Override
   public int getOrder() { return 1; }
   }
   7.2 多查询生成
   java
   List<String> variants = List.of(
   "How to optimize retrieval in Spring AI",
   "Spring AI retrieval performance tuning",
   "Boost query speed in Spring AI"
   );
   // 并行检索后合并结果
   7.3 HyDE（假设性文档嵌入）
   java
   String hypotheticalAnswer = chatClient.prompt()
   .user("Write a detailed answer to: " + userQuestion)
   .call()
   .content();
   // 用 hypotheticalAnswer 的向量进行检索
8. 多 Agent 串行交互
   8.1 A → B → C 顺序执行
   使用 Spring AI Alibaba 的 SequentialAgent。

java
ReactAgent agentA = ReactAgent.builder()
.name("writer")
.model(chatModel)
.instruction("Write content based on: {input}")
.outputKey("article")
.build();

ReactAgent agentB = ReactAgent.builder()
.name("reviewer")
.model(chatModel)
.instruction("Review and improve: {article}")
.outputKey("reviewed")
.build();

ReactAgent agentC = ReactAgent.builder()
.name("polisher")
.model(chatModel)
.instruction("Polish: {reviewed}")
.outputKey("final")
.build();

SequentialAgent workflow = SequentialAgent.builder()
.name("blogPipeline")
.subAgents(List.of(agentA, agentB, agentC))
.build();

workflow.invoke("Spring AI basics");
8.2 A → B → A 循环（LoopAgent）
java
LoopAgent loopAgent = LoopAgent.builder()
.name("planningLoop")
.subAgents(List.of(plannerAgent, reviewerAgent))
.condition(state -> {
int score = extractScore(state.get("review_result"));
return score < 80;   // 继续循环直到评分达标
})
.maxIterations(5)
.build();
8.3 基于外部记忆的双向交互
java
ChatMemory memory = new InMemoryChatMemory();
Agent a = new ReactAgent(..., memory);
Agent b = new ReactAgent(..., memory);
// 多轮交替调用，共享对话历史
9. 子任务拆解与 CoT/ToT
   9.1 任务拆解（规划→执行→聚合）
   java
   // 伪代码示例：协调器动态拆解任务
   public class Orchestrator {
   public String execute(String goal) {
   List<String> subTasks = decompose(goal);   // LLM 分解
   List<String> results = new ArrayList<>();
   for (String task : subTasks) {
   results.add(workerAgent.act(task));
   }
   return aggregator.merge(results);
   }

   private List<String> decompose(String goal) {
   String response = chatClient.prompt()
   .user("Break this goal into 3-5 subtasks: " + goal)
   .call().content();
   return parseSubtasks(response);
   }
   }
   9.2 Chain-of-Thought (CoT)
   java
   String prompt = """
   Question: Roger has 5 tennis balls. He buys 2 more cans of 3 balls each. How many does he have?
   Let's think step by step:
    1. Roger starts with 5 balls.
    2. Each can has 3 balls, and he buys 2 cans → 2 * 3 = 6 balls.
    3. Total = 5 + 6 = 11.
       Answer: 11
       Now answer: {question}
       """;
       9.3 Tree-of-Thoughts (ToT)
       需要编程实现树的搜索。伪代码框架：

java
public class TreeOfThoughts {
public String solve(String problem) {
List<Node> currentLevel = List.of(new Node(problem, null));
for (int depth = 0; depth < maxDepth; depth++) {
List<Node> nextLevel = new ArrayList<>();
for (Node node : currentLevel) {
List<String> thoughts = generateThoughts(node.state);
for (String thought : thoughts) {
String newState = evaluate(thought);
nextLevel.add(new Node(newState, node));
}
}
currentLevel = prune(nextLevel, beamWidth);
}
return bestLeaf(currentLevel).getSolution();
}
}
10. 工作流模式详解
    10.1 链式工作流 (Chain)
    java
    public class ChainWorkflow {
    private final ChatClient client;
    private final List<String> prompts; // 顺序执行的角色提示词

    public String execute(String input) {
    String result = input;
    for (String prompt : prompts) {
    result = client.prompt(prompt + "\n" + result).call().content();
    }
    return result;
    }
    }
    10.2 路由工作流 (Routing)
    java
    LlmRoutingAgent router = LlmRoutingAgent.builder()
    .name("router")
    .model(chatModel)
    .subAgents(List.of(weatherAgent, newsAgent, financeAgent))
    .build();

router.invoke("What's the weather in London?"); // 自动选 weatherAgent
10.3 并行化工作流 (Parallelization)
java
ParallelizationWorkflow workflow = new ParallelizationWorkflow(chatClient);
List<String> tasks = List.of("Impact on customers", "Impact on employees", "Impact on suppliers");
List<String> results = workflow.parallel(
"Analyze how market change affects stakeholders",
tasks,
maxConcurrency = 4
);
10.4 编排器-工作者 (Orchestrator-Workers)
java
// 使用 @ParallelAgent 注解（Spring AI Alibaba）
@ParallelAgent
public class Orchestrator {
@SubAgent
public String researchAgent(String topic) { ... }

    @SubAgent
    public String writerAgent(String outline) { ... }
    
    @ParallelTask
    public List<String> gatherData(String[] sources) { ... }
}
10.5 评估器-优化器 (Evaluator-Optimizer)
java
public class IterativeRefinement {
public String refine(String initialDraft) {
String current = initialDraft;
for (int i = 0; i < maxIterations; i++) {
String feedback = evaluator.evaluate(current);
if (isAcceptable(feedback)) break;
current = optimizer.improve(current, feedback);
}
return current;
}
}
10.6 多智能体路由与监督模式
工具调用模式：监督者将其他 Agent 作为工具调用。

交接模式：Agent 通过 transfer_to 将控制权移交。

java
// 交接模式示例（概念）
Agent supportAgent = new HandoffAgent("support", chatModel);
Agent technicalAgent = new HandoffAgent("technical", chatModel);
supportAgent.registerHandoff("technical_issue", technicalAgent);
11. 总结
    模式/技术	核心用途	典型组件
    Transformer	数据格式转换、文档处理	DocumentTransformer, BeanOutputConverter
    Advisor	横切关注点（记忆、RAG、安全）	CallAdvisor, MessageChatMemoryAdvisor
    问题转换	提高查询精度	QueryRewriteAdvisor, HyDE
    CoT/ToT	复杂推理	提示工程 + 树搜索算法
    链式工作流	固定顺序流水线	SequentialAgent
    路由工作流	智能任务分发	LlmRoutingAgent
    并行工作流	并发独立任务	ParallelizationWorkflow
    编排器-工作者	动态任务拆解	@ParallelAgent, Orchestrator
    评估器-优化器	迭代改进	自定义循环
    以上内容涵盖了 Spring AI 开发中的常见场景，可根据实际需求选择组合使用。