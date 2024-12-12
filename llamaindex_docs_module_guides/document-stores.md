# Document Stores#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/

# Document Stores#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/#document-stores)

Document stores contain ingested document chunks, which we call Node objects.

```
Node
```

See the [API Reference](https://docs.llamaindex.ai/en/stable/api_reference/storage/docstore/) for more details.

### Simple Document Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/#simple-document-store)

By default, the SimpleDocumentStore stores Node objects in-memory.
They can be persisted to (and loaded from) disk by calling docstore.persist() (and SimpleDocumentStore.from_persist_path(...) respectively).

```
SimpleDocumentStore
```

```
Node
```

```
docstore.persist()
```

```
SimpleDocumentStore.from_persist_path(...)
```

A more complete example can be found [here](https://docs.llamaindex.ai/en/stable/examples/docstore/DocstoreDemo/)

### MongoDB Document Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/#mongodb-document-store)

We support MongoDB as an alternative document store backend that persists data as Node objects are ingested.

```
Node
```

```
from llama_index.storage.docstore.mongodb import MongoDocumentStore
from llama_index.core.node_parser import SentenceSplitter

# create parser and parse document into nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# create (or load) docstore and add nodes
docstore = MongoDocumentStore.from_uri(uri="<mongodb+srv://...>")
docstore.add_documents(nodes)

# create storage context
storage_context = StorageContext.from_defaults(docstore=docstore)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

```
from llama_index.storage.docstore.mongodb import MongoDocumentStore
from llama_index.core.node_parser import SentenceSplitter

# create parser and parse document into nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# create (or load) docstore and add nodes
docstore = MongoDocumentStore.from_uri(uri="<mongodb+srv://...>")
docstore.add_documents(nodes)

# create storage context
storage_context = StorageContext.from_defaults(docstore=docstore)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

Under the hood, MongoDocumentStore connects to a fixed MongoDB database and initializes new collections (or loads existing collections) for your nodes.

```
MongoDocumentStore
```

> Note: You can configure the db_name and namespace when instantiating MongoDocumentStore, otherwise they default to db_name="db_docstore" and namespace="docstore".

Note: You can configure the db_name and namespace when instantiating MongoDocumentStore, otherwise they default to db_name="db_docstore" and namespace="docstore".

```
db_name
```

```
namespace
```

```
MongoDocumentStore
```

```
db_name="db_docstore"
```

```
namespace="docstore"
```

Note that it's not necessary to call storage_context.persist() (or docstore.persist()) when using an MongoDocumentStore
since data is persisted by default.

```
storage_context.persist()
```

```
docstore.persist()
```

```
MongoDocumentStore
```

You can easily reconnect to your MongoDB collection and reload the index by re-initializing a MongoDocumentStore with an existing db_name and collection_name.

```
MongoDocumentStore
```

```
db_name
```

```
collection_name
```

A more complete example can be found [here](https://docs.llamaindex.ai/en/stable/examples/docstore/MongoDocstoreDemo/)

### Redis Document Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/#redis-document-store)

We support Redis as an alternative document store backend that persists data as Node objects are ingested.

```
Node
```

```
from llama_index.storage.docstore.redis import RedisDocumentStore
from llama_index.core.node_parser import SentenceSplitter

# create parser and parse document into nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# create (or load) docstore and add nodes
docstore = RedisDocumentStore.from_host_and_port(
    host="127.0.0.1", port="6379", namespace="llama_index"
)
docstore.add_documents(nodes)

# create storage context
storage_context = StorageContext.from_defaults(docstore=docstore)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

```
from llama_index.storage.docstore.redis import RedisDocumentStore
from llama_index.core.node_parser import SentenceSplitter

# create parser and parse document into nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# create (or load) docstore and add nodes
docstore = RedisDocumentStore.from_host_and_port(
    host="127.0.0.1", port="6379", namespace="llama_index"
)
docstore.add_documents(nodes)

# create storage context
storage_context = StorageContext.from_defaults(docstore=docstore)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

Under the hood, RedisDocumentStore connects to a redis database and adds your nodes to a namespace stored under {namespace}/docs.

```
RedisDocumentStore
```

```
{namespace}/docs
```

> Note: You can configure the namespace when instantiating RedisDocumentStore, otherwise it defaults namespace="docstore".

Note: You can configure the namespace when instantiating RedisDocumentStore, otherwise it defaults namespace="docstore".

```
namespace
```

```
RedisDocumentStore
```

```
namespace="docstore"
```

You can easily reconnect to your Redis client and reload the index by re-initializing a RedisDocumentStore with an existing host, port, and namespace.

```
RedisDocumentStore
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

### Firestore Document Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/#firestore-document-store)

We support Firestore as an alternative document store backend that persists data as Node objects are ingested.

```
Node
```

```
from llama_index.storage.docstore.firestore import FirestoreDocumentStore
from llama_index.core.node_parser import SentenceSplitter

# create parser and parse document into nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# create (or load) docstore and add nodes
docstore = FirestoreDocumentStore.from_database(
    project="project-id",
    database="(default)",
)
docstore.add_documents(nodes)

# create storage context
storage_context = StorageContext.from_defaults(docstore=docstore)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

```
from llama_index.storage.docstore.firestore import FirestoreDocumentStore
from llama_index.core.node_parser import SentenceSplitter

# create parser and parse document into nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# create (or load) docstore and add nodes
docstore = FirestoreDocumentStore.from_database(
    project="project-id",
    database="(default)",
)
docstore.add_documents(nodes)

# create storage context
storage_context = StorageContext.from_defaults(docstore=docstore)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

Under the hood, FirestoreDocumentStore connects to a firestore database in Google Cloud and adds your nodes to a namespace stored under {namespace}/docs.

```
FirestoreDocumentStore
```

```
{namespace}/docs
```

> Note: You can configure the namespace when instantiating FirestoreDocumentStore, otherwise it defaults namespace="docstore".

Note: You can configure the namespace when instantiating FirestoreDocumentStore, otherwise it defaults namespace="docstore".

```
namespace
```

```
FirestoreDocumentStore
```

```
namespace="docstore"
```

You can easily reconnect to your Firestore database and reload the index by re-initializing a FirestoreDocumentStore with an existing project, database, and namespace.

```
FirestoreDocumentStore
```

```
project
```

```
database
```

```
namespace
```

A more complete example can be found [here](https://docs.llamaindex.ai/en/stable/examples/docstore/FirestoreDemo/)

### Couchbase Document Store#

[#](https://docs.llamaindex.ai/en/stable/module_guides/storing/docstores/#couchbase-document-store)

We support Couchbase as an alternative document store backend that persists data as Node objects are ingested.

```
Node
```

```
from llama_index.storage.docstore.couchbase import CouchbaseDocumentStore
from llama_index.core.node_parser import SentenceSplitter

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

# create parser and parse document into nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# create (or load) docstore and add nodes
docstore = CouchbaseDocumentStore.from_couchbase_client(
    client=cluster,
    bucket_name="llama-index",
    scope_name="_default",
    namespace="default",
)
docstore.add_documents(nodes)

# create storage context
storage_context = StorageContext.from_defaults(docstore=docstore)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

```
from llama_index.storage.docstore.couchbase import CouchbaseDocumentStore
from llama_index.core.node_parser import SentenceSplitter

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

# create parser and parse document into nodes
parser = SentenceSplitter()
nodes = parser.get_nodes_from_documents(documents)

# create (or load) docstore and add nodes
docstore = CouchbaseDocumentStore.from_couchbase_client(
    client=cluster,
    bucket_name="llama-index",
    scope_name="_default",
    namespace="default",
)
docstore.add_documents(nodes)

# create storage context
storage_context = StorageContext.from_defaults(docstore=docstore)

# build index
index = VectorStoreIndex(nodes, storage_context=storage_context)
```

Under the hood, CouchbaseDocumentStore connects to a Couchbase operational database and adds your nodes to a collection named under {namespace}_data in the specified {bucket_name} and {scope_name}.

```
CouchbaseDocumentStore
```

```
{namespace}_data
```

```
{bucket_name}
```

```
{scope_name}
```

> Note: You can configure the namespace, bucket and scope when instantiating CouchbaseIndexStore. By default, the collection used is docstore_data. Apart from alphanumeric characters, -, _ and % are only allowed as part of the collection name. The store will automatically convert other special characters to _.

Note: You can configure the namespace, bucket and scope when instantiating CouchbaseIndexStore. By default, the collection used is docstore_data. Apart from alphanumeric characters, -, _ and % are only allowed as part of the collection name. The store will automatically convert other special characters to _.

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
docstore_data
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

You can easily reconnect to your Couchbase database and reload the index by re-initializing a CouchbaseDocumentStore with an existing client, bucket_name, scope_name and namespace.

```
CouchbaseDocumentStore
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

