# Response Synthesis Modules#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/response_synthesizers/

# Response Synthesis Modules#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/response_synthesizers/#response-synthesis-modules)

Detailed inputs/outputs for each response synthesizer are found below.

## API Example#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/response_synthesizers/#api-example)

The following shows the setup for utilizing all kwargs.

- response_mode specifies which response synthesizer to use
```
response_mode
```

- service_context defines the LLM and related settings for synthesis
```
service_context
```

- text_qa_template and refine_template are the prompts used at various stages
```
text_qa_template
```

```
refine_template
```

- use_async is used for only the tree_summarize response mode right now, to asynchronously build the summary tree
```
use_async
```

```
tree_summarize
```

- streaming configures whether to return a streaming response object or not
```
streaming
```

- structured_answer_filtering enables the active filtering of text chunks that are not relevant to a given question
```
structured_answer_filtering
```

In the synthesize/asyntheszie functions, you can optionally provide additional source nodes, which will be added to the response.source_nodes list.

```
synthesize
```

```
asyntheszie
```

```
response.source_nodes
```

```
from llama_index.core.data_structs import Node
from llama_index.core.schema import NodeWithScore
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer(
    response_mode="refine",
    service_context=service_context,
    text_qa_template=text_qa_template,
    refine_template=refine_template,
    use_async=False,
    streaming=False,
)

# synchronous
response = response_synthesizer.synthesize(
    "query string",
    nodes=[NodeWithScore(node=Node(text="text"), score=1.0), ...],
    additional_source_nodes=[
        NodeWithScore(node=Node(text="text"), score=1.0),
        ...,
    ],
)

# asynchronous
response = await response_synthesizer.asynthesize(
    "query string",
    nodes=[NodeWithScore(node=Node(text="text"), score=1.0), ...],
    additional_source_nodes=[
        NodeWithScore(node=Node(text="text"), score=1.0),
        ...,
    ],
)
```

```
from llama_index.core.data_structs import Node
from llama_index.core.schema import NodeWithScore
from llama_index.core import get_response_synthesizer

response_synthesizer = get_response_synthesizer(
    response_mode="refine",
    service_context=service_context,
    text_qa_template=text_qa_template,
    refine_template=refine_template,
    use_async=False,
    streaming=False,
)

# synchronous
response = response_synthesizer.synthesize(
    "query string",
    nodes=[NodeWithScore(node=Node(text="text"), score=1.0), ...],
    additional_source_nodes=[
        NodeWithScore(node=Node(text="text"), score=1.0),
        ...,
    ],
)

# asynchronous
response = await response_synthesizer.asynthesize(
    "query string",
    nodes=[NodeWithScore(node=Node(text="text"), score=1.0), ...],
    additional_source_nodes=[
        NodeWithScore(node=Node(text="text"), score=1.0),
        ...,
    ],
)
```

You can also directly return a string, using the lower-level get_response and aget_response functions

```
get_response
```

```
aget_response
```

```
response_str = response_synthesizer.get_response(
    "query string", text_chunks=["text1", "text2", ...]
)
```

```
response_str = response_synthesizer.get_response(
    "query string", text_chunks=["text1", "text2", ...]
)
```

## Example Notebooks#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/response_synthesizers/#example-notebooks)

- [Refine](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/refine/)
- [Structured Refine](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/structured_refine/)
- [Tree Summarize](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/tree_summarize/)
- [Custom Prompting](https://docs.llamaindex.ai/en/stable/examples/response_synthesizers/custom_prompt_synthesizer/)
