# Agents#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/

# Agents#

[#](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/#agents)

Putting together an agent in LlamaIndex can be done by defining a set of tools and providing them to our ReActAgent implementation. We're using it here with OpenAI, but it can be used with any sufficiently capable LLM:

```
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent


# define sample Tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)

# initialize llm
llm = OpenAI(model="gpt-3.5-turbo-0613")

# initialize ReAct agent
agent = ReActAgent.from_tools([multiply_tool], llm=llm, verbose=True)
```

```
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent


# define sample Tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)

# initialize llm
llm = OpenAI(model="gpt-3.5-turbo-0613")

# initialize ReAct agent
agent = ReActAgent.from_tools([multiply_tool], llm=llm, verbose=True)
```

These tools can be Python functions as shown above, or they can be LlamaIndex query engines:

```
from llama_index.core.tools import QueryEngineTool

query_engine_tools = [
    QueryEngineTool(
        query_engine=sql_agent,
        metadata=ToolMetadata(
            name="sql_agent", description="Agent that can execute SQL queries."
        ),
    ),
]

agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True)
```

```
from llama_index.core.tools import QueryEngineTool

query_engine_tools = [
    QueryEngineTool(
        query_engine=sql_agent,
        metadata=ToolMetadata(
            name="sql_agent", description="Agent that can execute SQL queries."
        ),
    ),
]

agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True)
```

You can learn more in our [Agent Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/).

## Native OpenAIAgent#

[#](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/#native-openaiagent)

We have an OpenAIAgent implementation built on the [OpenAI API for function calling](https://openai.com/blog/function-calling-and-other-api-updates) that allows you to rapidly build agents:

```
OpenAIAgent
```

- [OpenAIAgent](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent/)
- [OpenAIAgent with Query Engine Tools](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_with_query_engine/)
- [OpenAIAgent Query Planning](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_query_plan/)
- [OpenAI Assistant](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_agent/)
- [OpenAI Assistant Cookbook](https://docs.llamaindex.ai/en/stable/examples/agent/openai_assistant_query_cookbook/)
- [Forced Function Calling](https://docs.llamaindex.ai/en/stable/examples/agent/openai_forced_function_call/)
- [Parallel Function Calling](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_parallel_function_calling/)
- [Context Retrieval](https://docs.llamaindex.ai/en/stable/examples/agent/openai_agent_context_retrieval/)
## Agentic Components within LlamaIndex#

[#](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/#agentic-components-within-llamaindex)

LlamaIndex provides core modules capable of automated reasoning for different use cases over your data which makes them essentially Agents. Some of these core modules are shown below along with example tutorials.

SubQuestionQueryEngine for Multi Document Analysis

- [Sub Question Query Engine (Intro)](https://docs.llamaindex.ai/en/stable/examples/query_engine/sub_question_query_engine/)
- [10Q Analysis (Uber)](https://docs.llamaindex.ai/en/stable/examples/usecases/10q_sub_question/)
- [10K Analysis (Uber and Lyft)](https://docs.llamaindex.ai/en/stable/examples/usecases/10k_sub_question/)
Query Transformations

- [How-To](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/)
- [Multi-Step Query Decomposition](https://docs.llamaindex.ai/en/stable/examples/query_transformations/HyDEQueryTransformDemo/) ([Notebook](https://github.com/jerryjliu/llama_index/blob/main/docs/docs/examples/query_transformations/HyDEQueryTransformDemo.ipynb))
Routing

- [Usage](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/)
- [Router Query Engine Guide](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine/) ([Notebook](https://github.com/jerryjliu/llama_index/blob/main/docs../../examples/query_engine/RouterQueryEngine.ipynb))
LLM Reranking

- [Second Stage Processing How-To](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/)
- [LLM Reranking Guide (Great Gatsby)](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/LLMReranker-Gatsby/)
Chat Engines

- [Chat Engines How-To](https://docs.llamaindex.ai/en/stable/module_guides/deploying/chat_engines/)
## Using LlamaIndex as a Tool within an Agent Framework#

[#](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/#using-llamaindex-as-a-tool-within-an-agent-framework)

LlamaIndex can be used as a Tool within an agent framework - including LangChain, ChatGPT. These integrations are described below.

### LangChain#

[#](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/#langchain)

We have deep integrations with LangChain.
LlamaIndex query engines can be easily packaged as Tools to be used within a LangChain agent, and LlamaIndex can also be used as a memory module / retriever. Check out our guides/tutorials below!

Resources

- [Building a Chatbot Tutorial](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/chatbots/building_a_chatbot/)
- [OnDemandLoaderTool Tutorial](https://docs.llamaindex.ai/en/stable/examples/tools/OnDemandLoaderTool/)
### ChatGPT#

[#](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/agents/#chatgpt)

LlamaIndex can be used as a ChatGPT retrieval plugin (we have a TODO to develop a more general plugin as well).

Resources

- [LlamaIndex ChatGPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin#llamaindex)
