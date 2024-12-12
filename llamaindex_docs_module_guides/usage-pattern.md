# Usage Pattern#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/

# Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#usage-pattern)

The usage pattern guide covers setup + usage of the QueryPipeline more in-depth.

```
QueryPipeline
```

## Setting up a Pipeline#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#setting-up-a-pipeline)

Here we walk through a few different ways of setting up a query pipeline.

### Defining a Sequential Chain#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#defining-a-sequential-chain)

Some simple pipelines are purely linear in nature - the output of the previous module directly goes into the input of the next module.

Some examples:

- prompt -> LLM -> output parsing
- prompt -> LLM -> prompt -> LLM
- retriever -> response synthesizer
These workflows can easily be expressed in the QueryPipeline through a simplified chain syntax.

```
QueryPipeline
```

```
chain
```

```
from llama_index.core.query_pipeline import QueryPipeline

# try chaining basic prompts
prompt_str = "Please generate related movies to {movie_name}"
prompt_tmpl = PromptTemplate(prompt_str)
llm = OpenAI(model="gpt-3.5-turbo")

p = QueryPipeline(chain=[prompt_tmpl, llm], verbose=True)
```

```
from llama_index.core.query_pipeline import QueryPipeline

# try chaining basic prompts
prompt_str = "Please generate related movies to {movie_name}"
prompt_tmpl = PromptTemplate(prompt_str)
llm = OpenAI(model="gpt-3.5-turbo")

p = QueryPipeline(chain=[prompt_tmpl, llm], verbose=True)
```

### Defining a DAG#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#defining-a-dag)

Many pipelines will require you to setup a DAG (for instance, if you want to implement all the steps in a standard RAG pipeline).

Here we offer a lower-level API to add modules along with their keys, and define links between previous module outputs to next
module inputs.

```
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.core.response_synthesizers import TreeSummarize

# define modules
prompt_str = "Please generate a question about Paul Graham's life regarding the following topic {topic}"
prompt_tmpl = PromptTemplate(prompt_str)
llm = OpenAI(model="gpt-3.5-turbo")
retriever = index.as_retriever(similarity_top_k=3)
reranker = CohereRerank()
summarizer = TreeSummarize(llm=llm)

# define query pipeline
p = QueryPipeline(verbose=True)
p.add_modules(
    {
        "llm": llm,
        "prompt_tmpl": prompt_tmpl,
        "retriever": retriever,
        "summarizer": summarizer,
        "reranker": reranker,
    }
)
p.add_link("prompt_tmpl", "llm")
p.add_link("llm", "retriever")
p.add_link("retriever", "reranker", dest_key="nodes")
p.add_link("llm", "reranker", dest_key="query_str")
p.add_link("reranker", "summarizer", dest_key="nodes")
p.add_link("llm", "summarizer", dest_key="query_str")
```

```
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.core.response_synthesizers import TreeSummarize

# define modules
prompt_str = "Please generate a question about Paul Graham's life regarding the following topic {topic}"
prompt_tmpl = PromptTemplate(prompt_str)
llm = OpenAI(model="gpt-3.5-turbo")
retriever = index.as_retriever(similarity_top_k=3)
reranker = CohereRerank()
summarizer = TreeSummarize(llm=llm)

# define query pipeline
p = QueryPipeline(verbose=True)
p.add_modules(
    {
        "llm": llm,
        "prompt_tmpl": prompt_tmpl,
        "retriever": retriever,
        "summarizer": summarizer,
        "reranker": reranker,
    }
)
p.add_link("prompt_tmpl", "llm")
p.add_link("llm", "retriever")
p.add_link("retriever", "reranker", dest_key="nodes")
p.add_link("llm", "reranker", dest_key="query_str")
p.add_link("reranker", "summarizer", dest_key="nodes")
p.add_link("llm", "summarizer", dest_key="query_str")
```

## Running the Pipeline#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#running-the-pipeline)

### Single-Input/Single-Output#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#single-inputsingle-output)

The input is the kwargs of the first component.

If the output of the last component is a single object (and not a dictionary of objects), then we return that directly.

Taking the pipeline in the previous example, the output will be a Response object since the last step is the TreeSummarize response synthesis module.

```
Response
```

```
TreeSummarize
```

```
output = p.run(topic="YC")
# output type is Response
type(output)
```

```
output = p.run(topic="YC")
# output type is Response
type(output)
```

### Multi-Input/Multi-Output#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#multi-inputmulti-output)

If your DAG has multiple root nodes / and-or output nodes, you can try run_multi. Pass in an input dictionary containing module key -> input dict. Output is dictionary of module key -> output dict.

```
run_multi
```

If we ran the prev example,

```
output_dict = p.run_multi({"llm": {"topic": "YC"}})
print(output_dict)

# output dict is {"summarizer": {"output": response}}
```

```
output_dict = p.run_multi({"llm": {"topic": "YC"}})
print(output_dict)

# output dict is {"summarizer": {"output": response}}
```

### Defining partials#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#defining-partials)

If you wish to prefill certain inputs for a module, you can do so with partial! Then the DAG would just hook into the unfilled inputs.

```
partial
```

You may need to convert a module via as_query_component.

```
as_query_component
```

Here's an example:

```
summarizer = TreeSummarize(llm=llm)
summarizer_c = summarizer.as_query_component(partial={"nodes": nodes})
# can define a chain because llm output goes into query_str, nodes is pre-filled
p = QueryPipeline(chain=[prompt_tmpl, llm, summarizer_c])
# run pipeline
p.run(topic="YC")
```

```
summarizer = TreeSummarize(llm=llm)
summarizer_c = summarizer.as_query_component(partial={"nodes": nodes})
# can define a chain because llm output goes into query_str, nodes is pre-filled
p = QueryPipeline(chain=[prompt_tmpl, llm, summarizer_c])
# run pipeline
p.run(topic="YC")
```

### Batch Input#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#batch-input)

If you wish to run the pipeline for several rounds of single/multi-inputs, set batch=True in the function call - supported by run, arun, run_multi, and arun_multi. Pass in a list of individual single/multi-inputs you would like to run. batch mode will return a list of responses in the same order as the inputs.

```
batch=True
```

```
run
```

```
arun
```

```
run_multi
```

```
arun_multi
```

```
batch
```

Example for single-input/single-output: p.run(field=[in1: Any, in2: Any], batch=True) --> [out1: Any, out2: Any]

```
p.run(field=[in1: Any, in2: Any], batch=True)
```

```
[out1: Any, out2: Any]
```

```
output = p.run(topic=["YC", "RAG", "LlamaIndex"], batch=True)
# output is [ResponseYC, ResponseRAG, ResponseLlamaIndex]
print(output)
```

```
output = p.run(topic=["YC", "RAG", "LlamaIndex"], batch=True)
# output is [ResponseYC, ResponseRAG, ResponseLlamaIndex]
print(output)
```

Example for multi-input/multi-output: p.run_multi("root_node": {"field": [in1: Any, in2, Any]}, batch=True) --> {"output_node": {"field": [out1: Any, out2: Any]}}

```
p.run_multi("root_node": {"field": [in1: Any, in2, Any]}, batch=True)
```

```
{"output_node": {"field": [out1: Any, out2: Any]}}
```

```
output_dict = p.run_multi({"llm": {"topic": ["YC", "RAG", "LlamaIndex"]}})
print(output_dict)

# output dict is {"summarizer": {"output": [ResponseYC, ResponseRAG, ResponseLlamaIndex]}}
```

```
output_dict = p.run_multi({"llm": {"topic": ["YC", "RAG", "LlamaIndex"]}})
print(output_dict)

# output dict is {"summarizer": {"output": [ResponseYC, ResponseRAG, ResponseLlamaIndex]}}
```

### Intermediate outputs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#intermediate-outputs)

If you wish to obtain the intermediate outputs of modules in QueryPipeline, you can use run_with_intermediates or run_multi_with_intermediates for single-input and multi-input, respectively.

```
run_with_intermediates
```

```
run_multi_with_intermediates
```

The output will be a tuple of the normal output and a dictionary containing module key -> ComponentIntermediates. ComponentIntermediates has 2 fields: inputs dict and outputs dict.

```
ComponentIntermediates
```

```
inputs
```

```
outputs
```

```
output, intermediates = p.run_with_intermediates(topic="YC")
print(output)
print(intermediates)

# output is (Response, {"module_key": ComponentIntermediates("inputs": {}, "outputs": {})})
```

```
output, intermediates = p.run_with_intermediates(topic="YC")
print(output)
print(intermediates)

# output is (Response, {"module_key": ComponentIntermediates("inputs": {}, "outputs": {})})
```

## Defining a Custom Query Component#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#defining-a-custom-query-component)

You can easily define a custom component: Either passing a function to a FnComponent or subclassing a CustomQueryComponent.

```
FnComponent
```

```
CustomQueryComponent
```

### Passing a Function to FnComponent#

```
FnComponent
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#passing-a-function-to-fncomponent)

Define any function and pass it to FnComponent. The positional argument names (args) will get converted to required input keys, and the keyword argument names (kwargs) will get converted to optional input keys.

```
FnComponent
```

```
args
```

```
kwargs
```

NOTE: We assume there is only a single output.

```
from llama_index.core.query_pipeline import FnComponent


def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


add_component = FnComponent(fn=add, output_key="output")

# input keys to add_component are "a" and "b", output key is 'output'
```

```
from llama_index.core.query_pipeline import FnComponent


def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


add_component = FnComponent(fn=add, output_key="output")

# input keys to add_component are "a" and "b", output key is 'output'
```

### Subclassing a CustomQueryComponent#

```
CustomQueryComponent
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#subclassing-a-customquerycomponent)

Simply subclass a CustomQueryComponent, implement validation/run functions + some helpers, and plug it in.

```
CustomQueryComponent
```

```
from llama_index.core.query_pipeline import CustomQueryComponent
from typing import Dict, Any


class MyComponent(CustomQueryComponent):
    """My component."""

    # Pydantic class, put any attributes here
    ...

    def _validate_component_inputs(
        self, input: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Validate component inputs during run_component."""
        # NOTE: this is OPTIONAL but we show you here how to do validation as an example
        return input

    @property
    def _input_keys(self) -> set:
        """Input keys dict."""
        return {"input_key1", ...}

    @property
    def _output_keys(self) -> set:
        # can do multi-outputs too
        return {"output_key"}

    def _run_component(self, **kwargs) -> Dict[str, Any]:
        """Run the component."""
        # run logic
        ...
        return {"output_key": result}
```

```
from llama_index.core.query_pipeline import CustomQueryComponent
from typing import Dict, Any


class MyComponent(CustomQueryComponent):
    """My component."""

    # Pydantic class, put any attributes here
    ...

    def _validate_component_inputs(
        self, input: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Validate component inputs during run_component."""
        # NOTE: this is OPTIONAL but we show you here how to do validation as an example
        return input

    @property
    def _input_keys(self) -> set:
        """Input keys dict."""
        return {"input_key1", ...}

    @property
    def _output_keys(self) -> set:
        # can do multi-outputs too
        return {"output_key"}

    def _run_component(self, **kwargs) -> Dict[str, Any]:
        """Run the component."""
        # run logic
        ...
        return {"output_key": result}
```

For more details check out our [in-depth query transformations guide](https://docs.llamaindex.ai/en/stable/examples/pipeline/query_pipeline/).

## Ensuring outputs are compatible#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/pipeline/usage_pattern/#ensuring-outputs-are-compatible)

By linking modules within a QueryPipeline, the output of one module goes into the input of the next module.

```
QueryPipeline
```

Generally you must make sure that for a link to work, the expected output and input types roughly line up.

We say roughly because we do some magic on existing modules to make sure that "stringable" outputs can be passed into
inputs that can be queried as a "string". Certain output types are treated as Stringable - CompletionResponse, ChatResponse, Response, QueryBundle, etc. Retrievers/query engines will automatically convert string inputs to QueryBundle objects.

```
CompletionResponse
```

```
ChatResponse
```

```
Response
```

```
QueryBundle
```

```
string
```

```
QueryBundle
```

This lets you do certain workflows that would otherwise require boilerplate string conversion if you were writing this yourself, for instance,

- LLM -> prompt, LLM -> retriever, LLM -> query engine
- query engine -> prompt, query engine -> retriever
If you are defining a custom component, you should use _validate_component_inputs to ensure that the inputs are the right type, and throw an error if they're not.

```
_validate_component_inputs
```

