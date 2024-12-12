# Index Stores#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/

# Index Stores#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/#index-stores)

Index stores contains lightweight index metadata (i.e. additional state information created when building an index).

See the [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/storage/index_store/) for more details.

### Simple Index Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/#simple-index-store)

By default, LlamaIndex uses a simple index store backed by an in-memory key-value store.
They can be persisted to (and loaded from) disk by calling index_store.persist() (and SimpleIndexStore.from_persist_path(...) respectively).

```
index_store.persist()
```

```
SimpleIndexStore.from_persist_path(...)
```

### MongoDB Index Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/#mongodb-index-store)

Similarly to document stores, we can also use MongoDB as the storage backend of the index store.

```
MongoDB
```

```
from llama_index.storage.index_store.mongodb import MongoIndexStore
from llama_index.core import VectorStoreIndex

# create (or load) index store
index_store = MongoIndexStore.from_uri(uri="<mongodb+srv://...>")

# create storage context
storage_context = StorageContext.from_defaults(index_store=index_store)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)

# or alternatively, load index
from llama_index.core import load_index_from_storage

index = load_index_from_storage(storage_context)
```

```
from llama_index.storage.index_store.mongodb import MongoIndexStore
from llama_index.core import VectorStoreIndex

# create (or load) index store
index_store = MongoIndexStore.from_uri(uri="<mongodb+srv://...>")

# create storage context
storage_context = StorageContext.from_defaults(index_store=index_store)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)

# or alternatively, load index
from llama_index.core import load_index_from_storage

index = load_index_from_storage(storage_context)
```

Under the hood, MongoIndexStore connects to a fixed MongoDB database and initializes new collections (or loads existing collections) for your index metadata.

```
MongoIndexStore
```

> Note: You can configure the db_name and namespace when instantiating MongoIndexStore, otherwise they default to db_name="db_docstore" and namespace="docstore".

Note: You can configure the db_name and namespace when instantiating MongoIndexStore, otherwise they default to db_name="db_docstore" and namespace="docstore".

```
db_name
```

```
namespace
```

```
MongoIndexStore
```

```
db_name="db_docstore"
```

```
namespace="docstore"
```

Note that it's not necessary to call storage_context.persist() (or index_store.persist()) when using an MongoIndexStore
since data is persisted by default.

```
storage_context.persist()
```

```
index_store.persist()
```

```
MongoIndexStore
```

You can easily reconnect to your MongoDB collection and reload the index by re-initializing a MongoIndexStore with an existing db_name and collection_name.

```
MongoIndexStore
```

```
db_name
```

```
collection_name
```

A more complete example can be found [here](https://docs.llamaindex.ai/en/stable/examples/docstore/MongoDocstoreDemo/)

### Redis Index Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/#redis-index-store)

We support Redis as an alternative document store backend that persists data as Node objects are ingested.

```
Node
```

```
from llama_index.storage.index_store.redis import RedisIndexStore
from llama_index.core import VectorStoreIndex

# create (or load) docstore and add nodes
index_store = RedisIndexStore.from_host_and_port(
    host="127.0.0.1", port="6379", namespace="llama_index"
)

# create storage context
storage_context = StorageContext.from_defaults(index_store=index_store)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)

# or alternatively, load index
from llama_index.core import load_index_from_storage

index = load_index_from_storage(storage_context)
```

```
from llama_index.storage.index_store.redis import RedisIndexStore
from llama_index.core import VectorStoreIndex

# create (or load) docstore and add nodes
index_store = RedisIndexStore.from_host_and_port(
    host="127.0.0.1", port="6379", namespace="llama_index"
)

# create storage context
storage_context = StorageContext.from_defaults(index_store=index_store)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)

# or alternatively, load index
from llama_index.core import load_index_from_storage

index = load_index_from_storage(storage_context)
```

Under the hood, RedisIndexStore connects to a redis database and adds your nodes to a namespace stored under {namespace}/index.

```
RedisIndexStore
```

```
{namespace}/index
```

> Note: You can configure the namespace when instantiating RedisIndexStore, otherwise it defaults namespace="index_store".

Note: You can configure the namespace when instantiating RedisIndexStore, otherwise it defaults namespace="index_store".

```
namespace
```

```
RedisIndexStore
```

```
namespace="index_store"
```

You can easily reconnect to your Redis client and reload the index by re-initializing a RedisIndexStore with an existing host, port, and namespace.

```
RedisIndexStore
```

```
host
```

```
port
```

```
namespace
```

A more complete example can be found [here](https://docs.llamaindex.ai/en/stable/examples/docstore/RedisDocstoreIndexStoreDemo/)

### Couchbase Index Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/index_stores/#couchbase-index-store)

Couchbase can be used as the storage backend for the index store.

```
from llama_index.storage.index_store.couchbase import CouchbaseIndexStore
from llama_index.core import VectorStoreIndex

from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions
from datetime import timedelta

# create couchbase client
auth = PasswordAuthenticator("DB_USERNAME", "DB_PASSWORD")
options = ClusterOptions(authenticator=auth)

cluster = Cluster("couchbase://localhost", options)

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=5))

# create (or load) docstore and add nodes
index_store = CouchbaseIndexStore.from_couchbase_client(
    client=cluster,
    bucket_name="llama-index",
    scope_name="_default",
    namespace="default",
)

# create storage context
storage_context = StorageContext.from_defaults(index_store=index_store)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)

# or alternatively, load index
from llama_index.core import load_index_from_storage

index = load_index_from_storage(storage_context)
```

```
from llama_index.storage.index_store.couchbase import CouchbaseIndexStore
from llama_index.core import VectorStoreIndex

from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions
from datetime import timedelta

# create couchbase client
auth = PasswordAuthenticator("DB_USERNAME", "DB_PASSWORD")
options = ClusterOptions(authenticator=auth)

cluster = Cluster("couchbase://localhost", options)

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=5))

# create (or load) docstore and add nodes
index_store = CouchbaseIndexStore.from_couchbase_client(
    client=cluster,
    bucket_name="llama-index",
    scope_name="_default",
    namespace="default",
)

# create storage context
storage_context = StorageContext.from_defaults(index_store=index_store)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)

# or alternatively, load index
from llama_index.core import load_index_from_storage

index = load_index_from_storage(storage_context)
```

Under the hood, CouchbaseIndexStore connects to a Couchbase operational database and adds your nodes to a collection named {namespace}_index in the specified {bucket_name} and {scope_name}.

```
CouchbaseIndexStore
```

```
{namespace}_index
```

```
{bucket_name}
```

```
{scope_name}
```

> Note: You can configure the namespace, bucket and scope when instantiating CouchbaseIndexStore. By default, the collection used is index_store_data. Apart from alphanumeric characters, -, _ and % are only allowed as part of the collection name. The store will automatically convert other special characters to _.

Note: You can configure the namespace, bucket and scope when instantiating CouchbaseIndexStore. By default, the collection used is index_store_data. Apart from alphanumeric characters, -, _ and % are only allowed as part of the collection name. The store will automatically convert other special characters to _.

```
namespace
```

```
bucket
```

```
scope
```

```
CouchbaseIndexStore
```

```
index_store_data
```

```
-
```

```
_
```

```
%
```

```
_
```

You can easily reconnect to your Couchbase client and reload the index by re-initializing a CouchbaseIndexStore with an existing client, bucket_name, scope_name and namespace.

```
CouchbaseIndexStore
```

```
client
```

```
bucket_name
```

```
scope_name
```

```
namespace
```

