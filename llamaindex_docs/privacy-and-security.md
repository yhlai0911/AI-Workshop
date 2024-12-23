# Privacy and Security#

原始連結：https://docs.llamaindex.ai/en/stable/understanding/using_llms/privacy/

# Privacy and Security#

[#](https://docs.llamaindex.ai/en/stable/understanding/using_llms/privacy/#privacy-and-security)

By default, LLamaIndex sends your data to OpenAI for generating embeddings and natural language responses. However, it is important to note that this can be configured according to your preferences. LLamaIndex provides the flexibility to use your own embedding model or run a large language model locally if desired.

## Data Privacy#

[#](https://docs.llamaindex.ai/en/stable/understanding/using_llms/privacy/#data-privacy)

Regarding data privacy, when using LLamaIndex with OpenAI, the privacy details and handling of your data are subject to OpenAI's policies. And each custom service other than OpenAI has its policies as well.

## Vector stores#

[#](https://docs.llamaindex.ai/en/stable/understanding/using_llms/privacy/#vector-stores)

LLamaIndex offers modules to connect with other vector stores within indexes to store embeddings. It is worth noting that each vector store has its own privacy policies and practices, and LLamaIndex does not assume responsibility for how it handles or uses your data. Also by default, LLamaIndex has a default option to store your embeddings locally.

