# Prompts#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/

# Prompts#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/#prompts)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/#concept)

Prompting is the fundamental input that gives LLMs their expressive power. LlamaIndex uses prompts to build the index, do insertion,
perform traversal during querying, and to synthesize the final answer.

LlamaIndex uses a set of [default prompt templates](https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/prompts/default_prompts.py) that work well out of the box.

In addition, t[here](https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/prompts/chat_prompts.py) are some prompts written and used specifically for chat models like gpt-3.5-turbo [here](https://github.com/run-llama/llama_index/blob/main/llama-index-core/llama_index/core/prompts/chat_prompts.py).

```
gpt-3.5-turbo
```

Users may also provide their own prompt templates to further customize the behavior of the framework. The best method for customizing is copying the default prompt from the link above, and using that as the base for any modifications.

## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/#usage-pattern)

Using prompts is simple.

```
from llama_index.core import PromptTemplate

template = (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given this information, please answer the question: {query_str}\n"
)
qa_template = PromptTemplate(template)

# you can create text prompt (for completion API)
prompt = qa_template.format(context_str=..., query_str=...)

# or easily convert to message prompts (for chat API)
messages = qa_template.format_messages(context_str=..., query_str=...)
```

```
from llama_index.core import PromptTemplate

template = (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given this information, please answer the question: {query_str}\n"
)
qa_template = PromptTemplate(template)

# you can create text prompt (for completion API)
prompt = qa_template.format(context_str=..., query_str=...)

# or easily convert to message prompts (for chat API)
messages = qa_template.format_messages(context_str=..., query_str=...)
```

See our [Usage Pattern Guide](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/usage_pattern/) for more details.

## Example Guides#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/#example-guides)

Simple Customization Examples

- [Completion prompts](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/completion_prompts/)
- [Chat prompts](https://docs.llamaindex.ai/en/stable/examples/customization/prompts/chat_prompts/)
- [Prompt Mixin](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_mixin/)
Prompt Engineering Guides

- [Advanced Prompts](https://docs.llamaindex.ai/en/stable/examples/prompts/advanced_prompts/)
- [RAG Prompts](https://docs.llamaindex.ai/en/stable/examples/prompts/prompts_rag/)
Experimental

- [Prompt Optimization](https://docs.llamaindex.ai/en/stable/examples/prompts/prompt_optimization/)
- [Emotion Prompting](https://docs.llamaindex.ai/en/stable/examples/prompts/emotion_prompt/)
