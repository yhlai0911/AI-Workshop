# Building a basic agent#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/agent/

# Building a basic agent#

[#](https://docs.llamaindex.ai/en/stable/understanding/agent/#building-a-basic-agent)

In LlamaIndex, an agent is a semi-autonomous piece of software powered by an LLM that is given a task and executes a series of steps towards solving that task. It is given a set of tools, which can be anything from arbitrary functions up to full LlamaIndex query engines, and it selects the best available tool to complete each step. When each step is completed, the agent judges whether the task is now complete, in which case it returns a result to the user, or whether it needs to take another step, in which case it loops back to the start.

In LlamaIndex, you can either use our prepackaged agents/tools or [build your own agentic workflows from scratch](https://docs.llamaindex.ai/en/stable/understanding/workflows/), covered in the "Building Workflows" section. This section covers our prepackaged agents and tools.

## Getting started#

[#](https://docs.llamaindex.ai/en/stable/understanding/agent/#getting-started)

You can find all of this code in [the tutorial repo](https://github.com/run-llama/python-agents-tutorial).

To avoid conflicts and keep things clean, we'll start a new Python virtual environment. You can use any virtual environment manager, but we'll use poetry here:

```
poetry
```

```
poetry init
poetry shell
```

```
poetry init
poetry shell
```

And then we'll install the LlamaIndex library and some other dependencies that will come in handy:

```
pip install llama-index python-dotenv
```

```
pip install llama-index python-dotenv
```

If any of this gives you trouble, check out our more detailed [installation guide](https://docs.llamaindex.ai/en/stable/understanding/getting_started/installation/).

## OpenAI Key#

[#](https://docs.llamaindex.ai/en/stable/understanding/agent/#openai-key)

Our agent will be powered by OpenAI's GPT-3.5-Turbo LLM, so you'll need an [API key](https://platform.openai.com/). Once you have your key, you can put it in a .env file in the root of your project:

```
GPT-3.5-Turbo
```

```
.env
```

```
OPENAI_API_KEY=sk-proj-xxxx
```

```
OPENAI_API_KEY=sk-proj-xxxx
```

If you don't want to use OpenAI, we'll show you how to use other models later.

## Bring in dependencies#

[#](https://docs.llamaindex.ai/en/stable/understanding/agent/#bring-in-dependencies)

We'll start by importing the components of LlamaIndex we need, as well as loading the environment variables from our .env file:

```
.env
```

```
from dotenv import load_dotenv

load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
```

```
from dotenv import load_dotenv

load_dotenv()
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
```

## Create basic tools#

[#](https://docs.llamaindex.ai/en/stable/understanding/agent/#create-basic-tools)

For this simple example we'll be creating two tools: one that knows how to multiply numbers together, and one that knows how to add them.

```
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)
```

```
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)
```

As you can see, these are regular vanilla Python functions. The docstring comments provide metadata to the agent about what the tool does: if your LLM is having trouble figuring out which tool to use, these docstrings are what you should tweak first.

After each function is defined we create FunctionTool objects from these functions, which wrap them in a way that the agent can understand.

```
FunctionTool
```

## Initialize the LLM#

[#](https://docs.llamaindex.ai/en/stable/understanding/agent/#initialize-the-llm)

GPT-3.5-Turbo is going to be doing the work today:

```
GPT-3.5-Turbo
```

```
llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
```

```
llm = OpenAI(model="gpt-3.5-turbo", temperature=0)
```

You could also pick another popular model accessible via API, such as those from [Mistral](https://docs.llamaindex.ai/en/stable/understanding/examples/llm/mistralai/), [Claude from Anthropic](https://docs.llamaindex.ai/en/stable/understanding/examples/llm/anthropic/) or [Gemini from Google](https://docs.llamaindex.ai/en/stable/understanding/examples/llm/gemini/).

## Initialize the agent#

[#](https://docs.llamaindex.ai/en/stable/understanding/agent/#initialize-the-agent)

Now we create our agent. In this case, this is a [ReAct agent](https://klu.ai/glossary/react-agent-model), a relatively simple but powerful agent. We give it an array containing our two tools, the LLM we just created, and set verbose=True so we can see what's going on:

```
verbose=True
```

```
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)
```

```
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)
```

## Ask a question#

[#](https://docs.llamaindex.ai/en/stable/understanding/agent/#ask-a-question)

We specify that it should use a tool, as this is pretty simple and GPT-3.5 doesn't really need this tool to get the answer.

```
response = agent.chat("What is 20+(2*4)? Use a tool to calculate every step.")
```

```
response = agent.chat("What is 20+(2*4)? Use a tool to calculate every step.")
```

This should give you output similar to the following:

```
Thought: The current language of the user is: English. I need to use a tool to help me answer the question.
Action: multiply
Action Input: {'a': 2, 'b': 4}
Observation: 8
Thought: I need to add 20 to the result of the multiplication.
Action: add
Action Input: {'a': 20, 'b': 8}
Observation: 28
Thought: I can answer without using any more tools. I'll use the user's language to answer
Answer: The result of 20 + (2 * 4) is 28.
The result of 20 + (2 * 4) is 28.
```

```
Thought: The current language of the user is: English. I need to use a tool to help me answer the question.
Action: multiply
Action Input: {'a': 2, 'b': 4}
Observation: 8
Thought: I need to add 20 to the result of the multiplication.
Action: add
Action Input: {'a': 20, 'b': 8}
Observation: 28
Thought: I can answer without using any more tools. I'll use the user's language to answer
Answer: The result of 20 + (2 * 4) is 28.
The result of 20 + (2 * 4) is 28.
```

As you can see, the agent picks the correct tools one after the other and combines the answers to give the final result. Check the [repo](https://github.com/run-llama/python-agents-tutorial/blob/main/1_basic_agent.py) to see what the final code should look like.

Congratulations! You've built the most basic kind of agent. Next you can find out how to use [local models](https://docs.llamaindex.ai/en/stable/understanding/agent/local_models/) or skip to [adding RAG to your agent](https://docs.llamaindex.ai/en/stable/understanding/agent/rag_agent/).

