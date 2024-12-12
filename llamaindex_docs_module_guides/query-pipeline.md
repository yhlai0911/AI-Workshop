# Query Pipeline#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/

# Query Pipeline#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/#query-pipeline)

Warning

Query Pipelines have recently gone into a feature-freeze/deprecation phase. If you want to orchestrate modules, we suggest checking out [workflows](https://docs.llamaindex.ai/en/stable/module_guides/workflow/).

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/#concept)

LlamaIndex provides a declarative query API that allows you to chain together different modules in order to orchestrate simple-to-advanced workflows over your data.

This is centered around our QueryPipeline abstraction. Load in a variety of modules (from LLMs to prompts to retrievers to other pipelines), connect them all together into a sequential chain or DAG, and run it end2end.

```
QueryPipeline
```

NOTE: You can orchestrate all these workflows without the declarative pipeline abstraction (by using the modules imperatively and writing your own functions). So what are the advantages of QueryPipeline?

```
QueryPipeline
```

- Express common workflows with fewer lines of code/boilerplate
- Greater readability
- Greater parity / better integration points with common low-code / no-code solutions (e.g. LangFlow)
- [In the future] A declarative interface allows easy serializability of pipeline components, providing portability of pipelines/easier deployment to different systems.
Our query pipelines also propagate callbacks throughout all sub-modules, and these integrate with our [observability partners](https://docs.llamaindex.ai/en/stable/module_guides/observability/).

To see an interactive example of QueryPipeline being put in use, check out the [RAG CLI](https://docs.llamaindex.ai/en/stable/getting_started/starter_tools/rag_cli/).

```
QueryPipeline
```

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/#usage-pattern)

Here are two simple ways to setup a query pipeline - through a simplified syntax of setting up a sequential chain to setting up a full compute DAG.

```
from llama_index.core.query_pipeline import QueryPipeline

# sequential chain
p = QueryPipeline(chain=[prompt_tmpl, llm], verbose=True)

# DAG
p = QueryPipeline(verbose=True)
p.add_modules({"prompt_tmpl": prompt_tmpl, "llm": llm})
p.add_link("prompt_tmpl", "llm")

# run pipeline
p.run(prompt_key1="<input1>", ...)
```

```
from llama_index.core.query_pipeline import QueryPipeline

# sequential chain
p = QueryPipeline(chain=[prompt_tmpl, llm], verbose=True)

# DAG
p = QueryPipeline(verbose=True)
p.add_modules({"prompt_tmpl": prompt_tmpl, "llm": llm})
p.add_link("prompt_tmpl", "llm")

# run pipeline
p.run(prompt_key1="<input1>", ...)
```

More information can be found in our usage pattern guides below.

- [Usage Pattern Guide](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/)
- [Module Usage](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/module_usage/)
## Module Guides#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/#module-guides)

Check out our QueryPipeline [end-to-end guides](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/modules/) to learn standard to advanced ways to setup orchestration over your data.

```
QueryPipeline
```

