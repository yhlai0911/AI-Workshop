# Key-Value Stores#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/storing/kv_stores/

# Key-Value Stores#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/kv_stores/#key-value-stores)

Key-Value stores are the underlying storage abstractions that power our [Document Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/) and [Index Stores](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/).

We provide the following key-value stores:

- Simple Key-Value Store: An in-memory KV store. The user can choose to call persist on this kv store to persist data to disk.
```
persist
```

- MongoDB Key-Value Store: A MongoDB KV store.
See the [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/storage/kvstore/) for more details.

Note: At the moment, these storage abstractions are not externally facing.

