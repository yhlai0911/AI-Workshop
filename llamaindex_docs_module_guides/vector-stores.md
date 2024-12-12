# Vector Stores#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/

# Vector Stores#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/#vector-stores)

Vector stores contain embedding vectors of ingested document chunks
(and sometimes the document chunks as well).

## Simple Vector Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/#simple-vector-store)

By default, LlamaIndex uses a simple in-memory vector store that's great for quick experimentation.
They can be persisted to (and loaded from) disk by calling vector_store.persist() (and SimpleVectorStore.from_persist_path(...) respectively).

```
vector_store.persist()
```

```
SimpleVectorStore.from_persist_path(...)
```

## Vector Store Options & Feature Support#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/#vector-store-options-feature-support)

LlamaIndex supports over 20 different vector store options.
We are actively adding more integrations and improving feature coverage for each.

For more details, see [Vector Store Integrations](https://docs.llamaindex.ai/en/stable/community/integrations/vector_stores/).

## Example Notebooks#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/#example-notebooks)

- [Alibaba Cloud OpenSearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AlibabaCloudOpenSearchIndexDemo/)
- [Astra DB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AstraDBIndexDemo/)
- [Async Index Creation](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AsyncIndexCreationDemo/)
- [Azure AI Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/)
- [Azure Cosmos DB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureCosmosDBMongoDBvCoreDemo/)
- [Baidu](https://docs.llamaindex.ai/en/stable/examples/vector_stores/BaiduVectorDBIndexDemo/)
- [Caasandra](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CassandraIndexDemo/)
- [Chromadb](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/)
- [Couchbase](https://docs.llamaindex.ai/en/stable/examples/vector_stores/CouchbaseVectorStoreDemo/)
- [Dash](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DashvectorIndexDemo/)
- [Databricks](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DatabricksVectorSearchDemo/)
- [Deeplake](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DeepLakeIndexDemo/)
- [DocArray HNSW](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayHnswIndexDemo/)
- [DocArray in-Memory](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DocArrayInMemoryIndexDemo/)
- [DuckDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/)
- [Espilla](https://docs.llamaindex.ai/en/stable/examples/vector_stores/EpsillaIndexDemo/)
- [Jaguar](https://docs.llamaindex.ai/en/stable/examples/vector_stores/JaguarIndexDemo/)
- [LanceDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanceDBIndexDemo/)
- [Lantern](https://docs.llamaindex.ai/en/stable/examples/vector_stores/LanternIndexDemo/)
- [Metal](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MetalIndexDemo/)
- [Milvus](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo/)
- [Milvus Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusHybridIndexDemo/)
- [MyScale](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MyScaleIndexDemo/)
- [ElasticSearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ElasticsearchIndexDemo/)
- [FAISS](https://docs.llamaindex.ai/en/stable/examples/vector_stores/FaissIndexDemo/)
- [Hnswlib](https://docs.llamaindex.ai/en/stable/examples/vector_stores/HnswlibIndexDemo/)
- [MongoDB Atlas](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearch/)
- [Neo4j](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Neo4jVectorDemo/)
- [OpenSearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/OpensearchDemo/)
- [Pinecone](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo/)
- [Pinecone Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PineconeIndexDemo-Hybrid/)
- [PGvectoRS](https://docs.llamaindex.ai/en/stable/examples/vector_stores/PGVectoRsDemo/)
- [Postgres](https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/)
- [Redis](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RedisIndexDemo/)
- [Qdrant](https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/)
- [Qdrant Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/qdrant_hybrid/)
- [Rockset](https://docs.llamaindex.ai/en/stable/examples/vector_stores/RocksetIndexDemo/)
- [Simple](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SimpleIndexDemo/)
- [Supabase](https://docs.llamaindex.ai/en/stable/examples/vector_stores/SupabaseVectorIndexDemo/)
- [Tair](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TairIndexDemo/)
- [TiDB](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TiDBVector/)
- [Tencent](https://docs.llamaindex.ai/en/stable/examples/vector_stores/TencentVectorDBIndexDemo/)
- [Timesacle](https://docs.llamaindex.ai/en/stable/examples/vector_stores/Timescalevector/)
- [Upstash](https://docs.llamaindex.ai/en/stable/examples/vector_stores/UpstashVectorDemo/)
- [Vearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VearchDemo/)
- [Vespa](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VespaIndexDemo/)
- [Vertex AI Vector Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/VertexAIVectorSearchDemo/)
- [Weaviate](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo/)
- [Weaviate Hybrid Search](https://docs.llamaindex.ai/en/stable/examples/vector_stores/WeaviateIndexDemo-Hybrid/)
- [Zep](https://docs.llamaindex.ai/en/stable/examples/vector_stores/ZepIndexDemo/)
