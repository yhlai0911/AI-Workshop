# Defining and Customizing Nodes#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/

# Defining and Customizing Nodes#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/#defining-and-customizing-nodes)

Nodes represent "chunks" of source Documents, whether that is a text chunk, an image, or more. They also contain metadata and relationship information
with other nodes and index structures.

Nodes are a first-class citizen in LlamaIndex. You can choose to define Nodes and all its attributes directly. You may also choose to "parse" source Documents into Nodes through our NodeParser classes.

```
NodeParser
```

For instance, you can do

```
from llama_index.core.node_parser import SentenceSplitter

parser = SentenceSplitter()

nodes = parser.get_nodes_from_documents(documents)
```

```
from llama_index.core.node_parser import SentenceSplitter

parser = SentenceSplitter()

nodes = parser.get_nodes_from_documents(documents)
```

You can also choose to construct Node objects manually and skip the first section. For instance,

```
from llama_index.core.schema import TextNode, NodeRelationship, RelatedNodeInfo

node1 = TextNode(text="<text_chunk>", id_="<node_id>")
node2 = TextNode(text="<text_chunk>", id_="<node_id>")
# set relationships
node1.relationships[NodeRelationship.NEXT] = RelatedNodeInfo(
    node_id=node2.node_id
)
node2.relationships[NodeRelationship.PREVIOUS] = RelatedNodeInfo(
    node_id=node1.node_id
)
nodes = [node1, node2]
```

```
from llama_index.core.schema import TextNode, NodeRelationship, RelatedNodeInfo

node1 = TextNode(text="<text_chunk>", id_="<node_id>")
node2 = TextNode(text="<text_chunk>", id_="<node_id>")
# set relationships
node1.relationships[NodeRelationship.NEXT] = RelatedNodeInfo(
    node_id=node2.node_id
)
node2.relationships[NodeRelationship.PREVIOUS] = RelatedNodeInfo(
    node_id=node1.node_id
)
nodes = [node1, node2]
```

The RelatedNodeInfo class can also store additional metadata if needed:

```
RelatedNodeInfo
```

```
metadata
```

```
node2.relationships[NodeRelationship.PARENT] = RelatedNodeInfo(
    node_id=node1.node_id, metadata={"key": "val"}
)
```

```
node2.relationships[NodeRelationship.PARENT] = RelatedNodeInfo(
    node_id=node1.node_id, metadata={"key": "val"}
)
```

### Customizing the ID#

[#](https://docs.llamaindex.ai/en/stable/module_guides/loading/documents_and_nodes/usage_nodes/#customizing-the-id)

Each node has an node_id property that is automatically generated if not manually specified. This ID can be used for
a variety of purposes; this includes being able to update nodes in storage, being able to define relationships
between nodes (through IndexNode), and more.

```
node_id
```

```
IndexNode
```

You can also get and set the node_id of any TextNode directly.

```
node_id
```

```
TextNode
```

```
print(node.node_id)
node.node_id = "My new node_id!"
```

```
print(node.node_id)
node.node_id = "My new node_id!"
```

