# Retriever Modules#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/

# Retriever Modules#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/#retriever-modules)

We are actively adding more tailored retrieval guides.
In the meanwhile, please take a look at the [API References](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/).

## Index Retrievers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/#index-retrievers)

Please see [the retriever modes](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/) for more details on how to get a retriever from any given index.

If you want to import the corresponding retrievers directly, please check out our [API reference](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/).

## Comprehensive Retriever Guides#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/#comprehensive-retriever-guides)

Check out our comprehensive guides on various retriever modules, many of which cover advanced concepts (auto-retrieval, routing, ensembling, and more).

### Advanced Retrieval and Search#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/#advanced-retrieval-and-search)

These guides contain advanced retrieval techniques. Some are common like keyword/hybrid search, reranking, and more.
Some are specific to LLM + RAG workflows, like small-to-big and auto-merging retrieval.

- [Define Custom Retriever](https://docs.llamaindex.ai/en/stable/examples/query_engine/CustomRetrievers/)
- [BM25 Hybrid Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/)
- [Simple Query Fusion](https://docs.llamaindex.ai/en/stable/examples/retrievers/simple_fusion/)
- [Reciprocal Rerank Fusion](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/)
- [Auto Merging Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/auto_merging_retriever/)
- [Metadata Replacement](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataReplacementDemo/)
- [Composable Retrievers](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/)
### Auto-Retrieval#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/#auto-retrieval)

These retrieval techniques perform semi-structured queries, combining semantic search with structured filtering.

- [Auto-Retrieval (with Pinecone)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/pinecone_auto_retriever/)
- [Auto-Retrieval (with Lantern)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternAutoRetriever/)
- [Auto-Retrieval (with Chroma)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/chroma_auto_retriever/)
- [Auto-Retrieval (with BagelDB)](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BagelAutoRetriever/)
- [Auto-Retrieval (with Vectara)](https://docs.llamaindex.ai/en/stable/examples/retrievers/vectara_auto_retriever/)
- [Multi-Doc Auto-Retrieval](https://docs.llamaindex.ai/en/stable/examples/query_engine/multi_doc_auto_retrieval/multi_doc_auto_retrieval/)
### Knowledge Graph Retrievers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/#knowledge-graph-retrievers)

- [Knowledge Graph RAG Retriever](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_rag_query_engine/)
### Composed Retrievers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/#composed-retrievers)

These are retrieval techniques that are composed on top of other retrieval techniques - providing higher-level capabilities like
hierarchical retrieval and query decomposition.

- [Query Fusion](https://docs.llamaindex.ai/en/stable/examples/retrievers/reciprocal_rerank_fusion/)
- [Recursive Table Retrieval](https://docs.llamaindex.ai/en/stable/examples/query_engine/pdf_tables/recursive_retriever/)
- [Recursive Node Retrieval](https://docs.llamaindex.ai/en/stable/examples/retrievers/recursive_retriever_nodes/)
- [Braintrust](https://docs.llamaindex.ai/en/stable/examples/retrievers/recurisve_retriever_nodes_braintrust/)
- [Router Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/router_retriever/)
- [Ensemble Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval/)
- [Multi-Doc Auto-Retrieval](https://docs.llamaindex.ai/en/stable/examples/query_engine/multi_doc_auto_retrieval/multi_doc_auto_retrieval/)
### Managed Retrievers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/#managed-retrievers)

- [Google](https://docs.llamaindex.ai/en/stable/examples/managed/GoogleDemo/)
- [Vectara](https://docs.llamaindex.ai/en/stable/examples/managed/vectaraDemo/)
- [VideoDB](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever/)
- [Zilliz](https://docs.llamaindex.ai/en/stable/examples/managed/zcpDemo/)
- [Amazon Bedrock](https://docs.llamaindex.ai/en/stable/examples/retrievers/bedrock_retriever/)
### Other Retrievers#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retrievers/#other-retrievers)

These are guides that don't fit neatly into a category but should be highlighted regardless.

- [Multi-Doc Hybrid](https://docs.llamaindex.ai/en/stable/examples/retrievers/multi_doc_together_hybrid/)
- [You Retriever](https://docs.llamaindex.ai/en/stable/examples/retrievers/you_retriever/)
- [Text-to-SQL](https://docs.llamaindex.ai/en/stable/examples/index_structs/struct_indices/SQLIndexDemo/)
- [DeepMemory (Activeloop)](https://docs.llamaindex.ai/en/stable/examples/retrievers/deep_memory/)
- [Pathway](https://docs.llamaindex.ai/en/stable/examples/retrievers/pathway_retriever/)
