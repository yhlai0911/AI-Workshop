# Tools#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/

# Tools#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#tools)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#concept)

Having proper tool abstractions is at the core of building [data agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/). Defining a set of Tools is similar to defining any API interface, with the exception that these Tools are meant for agent rather than human use. We allow users to define both a Tool as well as a ToolSpec containing a series of functions under the hood.

When using an agent or LLM with function calling, the tool selected (and the arguments written for that tool) rely strongly on the tool name and description of the tools purpose and arguments. Spending time tuning these parameters can result in larges changes in how the LLM calls these tools.

A Tool implements a very generic interface - simply define __call__ and also return some basic metadata (name, description, function schema).

```
__call__
```

We offer a few different types of Tools:

- FunctionTool: A function tool allows users to easily convert any user-defined function into a Tool. It can also auto-infer the function schema.
```
FunctionTool
```

- QueryEngineTool: A tool that wraps an existing [query engine](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/). Note: since our agent abstractions inherit from BaseQueryEngine, these tools can also wrap other agents.
```
QueryEngineTool
```

```
BaseQueryEngine
```

- Community contributed ToolSpecs that define one or more tools around a single service (like Gmail)
```
ToolSpecs
```

- Utility tools for wrapping other tools to handle returning large amounts of data from a tool
## FunctionTool#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#functiontool)

A function tool is a simple wrapper around any existing function (both sync and async are supported!).

```
from llama_index.core.tools import FunctionTool


def get_weather(location: str) -> str:
    """Usfeful for getting the weather for a given location."""
    ...


tool = FunctionTool.from_defaults(
    get_weather,
    # async_fn=aget_weather,  # optional!
)

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)
```

```
from llama_index.core.tools import FunctionTool


def get_weather(location: str) -> str:
    """Usfeful for getting the weather for a given location."""
    ...


tool = FunctionTool.from_defaults(
    get_weather,
    # async_fn=aget_weather,  # optional!
)

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)
```

For a better function definition, you can also leverage pydantic for the function arguments.

```
from pydantic import Field


def get_weather(
    location: str = Field(
        description="A city name and state, formatted like '<name>, <state>'"
    ),
) -> str:
    """Usfeful for getting the weather for a given location."""
    ...


tool = FunctionTool.from_defaults(get_weather)
```

```
from pydantic import Field


def get_weather(
    location: str = Field(
        description="A city name and state, formatted like '<name>, <state>'"
    ),
) -> str:
    """Usfeful for getting the weather for a given location."""
    ...


tool = FunctionTool.from_defaults(get_weather)
```

By default, the tool name will be the function name, and the docstring will be the tool description. But you can also override this.

```
tool = FunctionTool.from_defaults(get_weather, name="...", description="...")
```

```
tool = FunctionTool.from_defaults(get_weather, name="...", description="...")
```

## QueryEngineTool#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#queryenginetool)

Any query engine can be turned into a tool, using QueryEngineTool:

```
QueryEngineTool
```

```
from llama_index.core.tools import QueryEngineTool

tool = QueryEngineTool.from_defaults(
    query_engine, name="...", description="..."
)
```

```
from llama_index.core.tools import QueryEngineTool

tool = QueryEngineTool.from_defaults(
    query_engine, name="...", description="..."
)
```

## Tool Specs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#tool-specs)

We also offer a rich set of Tools and Tool Specs through [LlamaHub](https://llamahub.ai/) 🦙.

You can think of tool specs like bundles of tools meant to be used together. Usually these cover useful tools across a single interface/service, like Gmail.

To use with an agent, you can install the specific tool spec integration:

```
pip install llama-index-tools-google
```

```
pip install llama-index-tools-google
```

And then use it:

```
from llama_index.agent.openai import OpenAIAgent
from llama_index.tools.google import GmailToolSpec

tool_spec = GmailToolSpec()
agent = OpenAIAgent.from_tools(tool_spec.to_tool_list(), verbose=True)
```

```
from llama_index.agent.openai import OpenAIAgent
from llama_index.tools.google import GmailToolSpec

tool_spec = GmailToolSpec()
agent = OpenAIAgent.from_tools(tool_spec.to_tool_list(), verbose=True)
```

See [LlamaHub](https://llamahub.ai) for a full list of community contributed tool specs.

## Utility Tools#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#utility-tools)

Oftentimes, directly querying an API can return a massive volume of data, which on its own may overflow the context window of the LLM (or at the very least unnecessarily increase the number of tokens that you are using).

To tackle this, we’ve provided an initial set of “utility tools” in LlamaHub Tools - utility tools are not conceptually tied to a given service (e.g. Gmail, Notion), but rather can augment the capabilities of existing Tools. In this particular case, utility tools help to abstract away common patterns of needing to cache/index and query data that’s returned from any API request.

Let’s walk through our two main utility tools below.

### OnDemandLoaderTool#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#ondemandloadertool)

This tool turns any existing LlamaIndex data loader ( BaseReader class) into a tool that an agent can use. The tool can be called with all the parameters needed to trigger load_data from the data loader, along with a natural language query string. During execution, we first load data from the data loader, index it (for instance with a vector store), and then query it “on-demand”. All three of these steps happen in a single tool call.

```
BaseReader
```

```
load_data
```

Oftentimes this can be preferable to figuring out how to load and index API data yourself. While this may allow for data reusability, oftentimes users just need an ad-hoc index to abstract away prompt window limitations for any API call.

A usage example is given below:

```
from llama_index.readers.wikipedia import WikipediaReader
from llama_index.core.tools.ondemand_loader_tool import OnDemandLoaderTool

tool = OnDemandLoaderTool.from_defaults(
    reader,
    name="Wikipedia Tool",
    description="A tool for loading data and querying articles from Wikipedia",
)
```

```
from llama_index.readers.wikipedia import WikipediaReader
from llama_index.core.tools.ondemand_loader_tool import OnDemandLoaderTool

tool = OnDemandLoaderTool.from_defaults(
    reader,
    name="Wikipedia Tool",
    description="A tool for loading data and querying articles from Wikipedia",
)
```

### LoadAndSearchToolSpec#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#loadandsearchtoolspec)

The LoadAndSearchToolSpec takes in any existing Tool as input. As a tool spec, it implements to_tool_list , and when that function is called, two tools are returned: a load tool and then a search tool.

```
to_tool_list
```

```
load
```

```
search
```

The load Tool execution would call the underlying Tool, and the index the output (by default with a vector index). The search Tool execution would take in a query string as input and call the underlying index.

```
load
```

```
search
```

This is helpful for any API endpoint that will by default return large volumes of data - for instance our WikipediaToolSpec will by default return entire Wikipedia pages, which will easily overflow most LLM context windows.

Example usage is shown below:

```
from llama_index.tools.wikipedia import WikipediaToolSpec
from llama_index.core.tools.tool_spec.load_and_search import (
    LoadAndSearchToolSpec,
)

wiki_spec = WikipediaToolSpec()
# Get the search wikipedia tool
tool = wiki_spec.to_tool_list()[1]

# Create the Agent with load/search tools
agent = OpenAIAgent.from_tools(
    LoadAndSearchToolSpec.from_defaults(tool).to_tool_list(), verbose=True
)
```

```
from llama_index.tools.wikipedia import WikipediaToolSpec
from llama_index.core.tools.tool_spec.load_and_search import (
    LoadAndSearchToolSpec,
)

wiki_spec = WikipediaToolSpec()
# Get the search wikipedia tool
tool = wiki_spec.to_tool_list()[1]

# Create the Agent with load/search tools
agent = OpenAIAgent.from_tools(
    LoadAndSearchToolSpec.from_defaults(tool).to_tool_list(), verbose=True
)
```

### Return Direct#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#return-direct)

You'll notice the option return_direct in the tool class constructor. If this is set to True, the response from an agent is returned directly, without being interpreted and rewritten by the agent. This can be helpful for decreasing runtime, or designing/specifying tools that will end the agent reasoning loop.

```
return_direct
```

```
True
```

For example, say you specify a tool:

```
tool = QueryEngineTool.from_defaults(
    query_engine,
    name="<name>",
    description="<description>",
    return_direct=True,
)

agent = OpenAIAgent.from_tools([tool])

response = agent.chat("<question that invokes tool>")
```

```
tool = QueryEngineTool.from_defaults(
    query_engine,
    name="<name>",
    description="<description>",
    return_direct=True,
)

agent = OpenAIAgent.from_tools([tool])

response = agent.chat("<question that invokes tool>")
```

In the above example, the query engine tool would be invoked, and the response from that tool would be directly returned as the response, and the execution loop would end.

If return_direct=False was used, then the agent would rewrite the response using the context of the chat history, or even make another tool call.

```
return_direct=False
```

We have also provided an [example notebook](https://docs.llamaindex.ai/en/stable/examples/agent/return_direct_agent/) of using return_direct.

```
return_direct
```

## Debugging Tools#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/tools/#debugging-tools)

Often, it can be useful to debug what exactly the tool definition is that is being sent to APIs.

You can get a good peek at this by using the underlying function to get the current tool schema, which is levereged in APIs like OpenAI and Anthropic.

```
schema = tool.metadata.get_parameters_dict()
print(schema)
```

```
schema = tool.metadata.get_parameters_dict()
print(schema)
```

