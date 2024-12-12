# Retriever Modes#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/

# Retriever Modes#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#retriever-modes)

Here we show the mapping from retriever_mode configuration to the selected retriever class.

```
retriever_mode
```

> Note that retriever_mode can mean different thing for different index classes.

Note that retriever_mode can mean different thing for different index classes.

```
retriever_mode
```

## Vector Index#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#vector-index)

Specifying retriever_mode has no effect (silently ignored).
vector_index.as_retriever(...) always returns a VectorIndexRetriever.

```
retriever_mode
```

```
vector_index.as_retriever(...)
```

## Summary Index#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#summary-index)

- default: SummaryIndexRetriever
```
default
```

- embedding: SummaryIndexEmbeddingRetriever
```
embedding
```

- llm: SummaryIndexLLMRetriever
```
llm
```

## Tree Index#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#tree-index)

- select_leaf: TreeSelectLeafRetriever
```
select_leaf
```

- select_leaf_embedding: TreeSelectLeafEmbeddingRetriever
```
select_leaf_embedding
```

- all_leaf: TreeAllLeafRetriever
```
all_leaf
```

- root: TreeRootRetriever
```
root
```

## Keyword Table Index#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#keyword-table-index)

- default: KeywordTableGPTRetriever
```
default
```

- simple: KeywordTableSimpleRetriever
```
simple
```

- rake: KeywordTableRAKERetriever
```
rake
```

## Knowledge Graph Index#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#knowledge-graph-index)

- keyword: KGTableRetriever
```
keyword
```

- embedding: KGTableRetriever
```
embedding
```

- hybrid: KGTableRetriever
```
hybrid
```

## Document Summary Index#

[#](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/retriever_modes/#document-summary-index)

- llm: DocumentSummaryIndexLLMRetriever
```
llm
```

- embedding: DocumentSummaryIndexEmbeddingRetrievers
```
embedding
```

