# Using LLMs#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/models/llms/

# Using LLMs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/#using-llms)

## Concept#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/#concept)

Picking the proper Large Language Model (LLM) is one of the first steps you need to consider when building any LLM application over your data.

LLMs are a core component of LlamaIndex. They can be used as standalone modules or plugged into other core LlamaIndex modules (indices, retrievers, query engines). They are always used during the response synthesis step (e.g. after retrieval). Depending on the type of index being used, LLMs may also be used during index construction, insertion, and query traversal.

LlamaIndex provides a unified interface for defining LLM modules, whether it's from OpenAI, Hugging Face, or LangChain, so that you
don't have to write the boilerplate code of defining the LLM interface yourself. This interface consists of the following (more details below):

- Support for text completion and chat endpoints (details below)
- Support for streaming and non-streaming endpoints
- Support for synchronous and asynchronous endpoints
## Usage Pattern#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/#usage-pattern)

The following code snippet shows how you can get started using LLMs.

If you don't already have it, install your LLM:

```
pip install llama-index-llms-openai
```

```
pip install llama-index-llms-openai
```

Then:

```
from llama_index.llms.openai import OpenAI

# non-streaming
resp = OpenAI().complete("Paul Graham is ")
print(resp)
```

```
from llama_index.llms.openai import OpenAI

# non-streaming
resp = OpenAI().complete("Paul Graham is ")
print(resp)
```

Find more details on [standalone usage](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_standalone/) or [custom usage](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_custom/).

## A Note on Tokenization#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/#a-note-on-tokenization)

By default, LlamaIndex uses a global tokenizer for all token counting. This defaults to cl100k from tiktoken, which is the tokenizer to match the default LLM gpt-3.5-turbo.

```
cl100k
```

```
gpt-3.5-turbo
```

If you change the LLM, you may need to update this tokenizer to ensure accurate token counts, chunking, and prompting.

The single requirement for a tokenizer is that it is a callable function, that takes a string, and returns a list.

You can set a global tokenizer like so:

```
from llama_index.core import Settings

# tiktoken
import tiktoken

Settings.tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo").encode

# huggingface
from transformers import AutoTokenizer

Settings.tokenizer = AutoTokenizer.from_pretrained(
    "HuggingFaceH4/zephyr-7b-beta"
)
```

```
from llama_index.core import Settings

# tiktoken
import tiktoken

Settings.tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo").encode

# huggingface
from transformers import AutoTokenizer

Settings.tokenizer = AutoTokenizer.from_pretrained(
    "HuggingFaceH4/zephyr-7b-beta"
)
```

## LLM Compatibility Tracking#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/#llm-compatibility-tracking)

While LLMs are powerful, not every LLM is easy to set up. Furthermore, even with proper setup, some LLMs have trouble performing tasks that require strict instruction following.

LlamaIndex offers integrations with nearly every LLM, but it can be often unclear if the LLM will work well out of the box, or if further customization is needed.

The tables below attempt to validate the initial experience with various LlamaIndex features for various LLMs. These notebooks serve as a best attempt to gauge performance, as well as how much effort and tweaking is needed to get things to function properly.

Generally, paid APIs such as OpenAI or Anthropic are viewed as more reliable. However, local open-source models have been gaining popularity due to their customizability and approach to transparency.

Contributing: Anyone is welcome to contribute new LLMs to the documentation. Simply copy an existing notebook, setup and test your LLM, and open a PR with your results.

If you have ways to improve the setup for existing notebooks, contributions to change this are welcome!

Legend

- ✅ = should work fine
- ⚠️ = sometimes unreliable, may need prompt engineering to improve
- 🛑 = usually unreliable, would need prompt engineering/fine-tuning to improve
### Paid LLM APIs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/#paid-llm-apis)

[gpt-3.5-turbo](https://colab.research.google.com/drive/1vvdcf7VYNQA67NOxBHCyQvgb2Pu7iY_5?usp=sharing)

[gpt-3.5-turbo-instruct](https://colab.research.google.com/drive/1Ne-VmMNYGOKUeECvkjurdKqMDpfqJQHE?usp=sharing)

[gpt-4](https://colab.research.google.com/drive/1QUNyCVt8q5G32XHNztGw4YJ2EmEkeUe8?usp=sharing)

[claude-3 opus](https://colab.research.google.com/drive/1xeFgAmSLpY_9w7bcGPvIcE8UuFSI3xjF?usp=sharing)

[claude-3 sonnet](https://colab.research.google.com/drive/1xeFgAmSLpY_9w7bcGPvIcE8UuFSI3xjF?usp=sharing)

[claude-2](https://colab.research.google.com/drive/1IuHRN67MYOaLx2_AgJ9gWVtlK7bIvS1f?usp=sharing)

[claude-instant-1.2](https://colab.research.google.com/drive/1ahq-2kXwCVCA_3xyC5UMWHyfAcjoG8Gp?usp=sharing)

### Open Source LLMs#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/#open-source-llms)

Since open source LLMs require large amounts of resources, the quantization is reported. Quantization is just a method for reducing the size of an LLM by shrinking the accuracy of calculations within the model. Research has shown that up to 4Bit quantization can be achieved for large LLMs without impacting performance too severely.

[llama2-chat-7b 4bit](https://colab.research.google.com/drive/1ByiIaBqCwbH9QXJOQWqOfUdsq4LEFq-g?usp=sharing)

[llama2-13b-chat](https://colab.research.google.com/drive/1dpIv3iYQCV4OBB8z2ZRS7y4wUfsfNlO3?usp=sharing)

[llama2-70b-chat](https://colab.research.google.com/drive/11h_Av5RG3tGjuOrZ-VKifd9UzcRPeN1J?usp=sharing)

[Mistral-7B-instruct-v0.1 4bit](https://colab.research.google.com/drive/1-f5v48TnX5rGdaMdWTr8XsjTGrWZ6Q7Y?usp=sharing)

[zephyr-7b-alpha](https://colab.research.google.com/drive/1asitB49g9LMGrlODgY2J-g_xRExRM_ud?usp=sharing)

```
zyphyr-7b-alpha
```

[zephyr-7b-beta](https://colab.research.google.com/drive/1C55IGyJNDe14DsHkAIIpIjn76NvK5pc1?usp=sharing)

```
zyphyr-7b-alpha
```

```
zyphyr-7b-beta
```

[stablelm-zephyr-3b](https://colab.research.google.com/drive/1X_hEUkV62wHmMty3tNLIfJtp4IC6QNYN?usp=sharing)

[starling-lm-7b-alpha](https://colab.research.google.com/drive/1z2tZMr4M9wBFU6YX8fvAZ7WLTa3tWKEm?usp=sharing)

[phi-3-mini-4k-instruct](https://github.com/run-llama/llama_index/tree/main/docs/docs/examples/benchmarks/phi-3-mini-4k-instruct.ipynb)

## Modules#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/#modules)

We support integrations with OpenAI, Hugging Face, PaLM, and more.

See the full [list of modules](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/modules/).

## Further reading#

[#](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/#further-reading)

- [Embeddings](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/)
- [Prompts](https://docs.llamaindex.ai/en/stable/module_guides/models/prompts/)
- [Local LLMs](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/local/)
- [Running Llama2 Locally](https://replicate.com/blog/run-llama-locally)
