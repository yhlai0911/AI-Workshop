# Module Usage#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/

# Module Usage#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#module-usage)

Currently the following LlamaIndex modules are supported within a QueryPipeline. Remember, you can define your own!

### LLMs (both completion and chat)#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#llms-both-completion-and-chat)

- Base class: LLM
```
LLM
```

- [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/)
- If chat model:
- Input: messages. Takes in any List[ChatMessage] or any stringable input.
```
messages
```

```
List[ChatMessage]
```

- Output: output. Outputs ChatResponse (stringable)
```
output
```

```
ChatResponse
```

- If completion model:
- Input: prompt. Takes in any stringable input.
```
prompt
```

- Output: output. Outputs CompletionResponse (stringable)
```
output
```

```
CompletionResponse
```

### Prompts#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#prompts)

- Base class: PromptTemplate
```
PromptTemplate
```

- [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/)
- Input: Prompt template variables. Each variable can be a stringable input.
- Output: output. Outputs formatted prompt string (stringable)
```
output
```

### Query Engines#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#query-engines)

- Base class: BaseQueryEngine
```
BaseQueryEngine
```

- [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/)
- Input: input. Takes in any stringable input.
```
input
```

- Output: output. Outputs Response (stringable)
```
output
```

```
Response
```

### Query Transforms#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#query-transforms)

- Base class: BaseQueryTransform
```
BaseQueryTransform
```

- [Module Guide](https://docs.llamaindex.ai/en/stable/optimizing/advanced_retrieval/query_transformations/)
- Input: query_str, metadata (optional). query_str is any stringable input.
```
query_str
```

```
metadata
```

```
query_str
```

- Output: query_str. Outputs string.
```
query_str
```

### Retrievers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#retrievers)

- Base class: BaseRetriever
```
BaseRetriever
```

- [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/)
- Input: input. Takes in any stringable input.
```
input
```

- Output: output. Outputs list of nodes List[BaseNode].
```
output
```

```
List[BaseNode]
```

### Output Parsers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#output-parsers)

- Base class: BaseOutputParser
```
BaseOutputParser
```

- [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/structured_outputs/output_parser/)
- Input: input. Takes in any stringable input.
```
input
```

- Output: output. Outputs whatever type output parser is supposed to parse out.
```
output
```

### Postprocessors/Rerankers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#postprocessorsrerankers)

- Base class: BaseNodePostprocessor
```
BaseNodePostprocessor
```

- [Module Guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/)
- Input: nodes, query_str (optional). nodes is List[BaseNode], query_str is any stringable input.
```
nodes
```

```
query_str
```

```
nodes
```

```
List[BaseNode]
```

```
query_str
```

- Output: nodes. Outputs list of nodes List[BaseNode].
```
nodes
```

```
List[BaseNode]
```

### Response Synthesizers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#response-synthesizers)

- Base class: BaseSynthesizer
```
BaseSynthesizer
```

- Module Guide
- Input: nodes, query_str. nodes is List[BaseNode], query_str is any stringable input.
```
nodes
```

```
query_str
```

```
nodes
```

```
List[BaseNode]
```

```
query_str
```

- Output: output. Outputs Response object (stringable).
```
output
```

```
Response
```

### Other QueryPipeline objects#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#other-querypipeline-objects)

You can define a QueryPipeline as a module within another query pipeline. This makes it easy for you to string together complex workflows.

```
QueryPipeline
```

### Custom Components#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/#custom-components)

See our [custom components guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#defining-a-custom-query-component) for more details.

