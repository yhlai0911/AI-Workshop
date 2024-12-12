# Usage Pattern (Retrieval)#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern_retrieval/

# Usage Pattern (Retrieval)#

[#](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern_retrieval/#usage-pattern-retrieval)

## Using RetrieverEvaluator#

```
RetrieverEvaluator
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern_retrieval/#using-retrieverevaluator)

This runs evaluation over a single query + ground-truth document set given a retriever.

The standard practice is to specify a set of valid metrics with from_metrics.

```
from_metrics
```

```
from llama_index.core.evaluation import RetrieverEvaluator

# define retriever somewhere (e.g. from index)
# retriever = index.as_retriever(similarity_top_k=2)
retriever = ...

retriever_evaluator = RetrieverEvaluator.from_metric_names(
    ["mrr", "hit_rate"], retriever=retriever
)

retriever_evaluator.evaluate(
    query="query", expected_ids=["node_id1", "node_id2"]
)
```

```
from llama_index.core.evaluation import RetrieverEvaluator

# define retriever somewhere (e.g. from index)
# retriever = index.as_retriever(similarity_top_k=2)
retriever = ...

retriever_evaluator = RetrieverEvaluator.from_metric_names(
    ["mrr", "hit_rate"], retriever=retriever
)

retriever_evaluator.evaluate(
    query="query", expected_ids=["node_id1", "node_id2"]
)
```

## Building an Evaluation Dataset#

[#](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern_retrieval/#building-an-evaluation-dataset)

You can manually curate a retrieval evaluation dataset of questions + node id's. We also offer synthetic dataset generation over an existing text corpus with our generate_question_context_pairs function:

```
generate_question_context_pairs
```

```
from llama_index.core.evaluation import generate_question_context_pairs

qa_dataset = generate_question_context_pairs(
    nodes, llm=llm, num_questions_per_chunk=2
)
```

```
from llama_index.core.evaluation import generate_question_context_pairs

qa_dataset = generate_question_context_pairs(
    nodes, llm=llm, num_questions_per_chunk=2
)
```

The returned result is a EmbeddingQAFinetuneDataset object (containing queries, relevant_docs, and corpus).

```
EmbeddingQAFinetuneDataset
```

```
queries
```

```
relevant_docs
```

```
corpus
```

### Plugging it into RetrieverEvaluator#

```
RetrieverEvaluator
```

[#](https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern_retrieval/#plugging-it-into-retrieverevaluator)

We offer a convenience function to run a RetrieverEvaluator over a dataset in batch mode.

```
RetrieverEvaluator
```

```
eval_results = await retriever_evaluator.aevaluate_dataset(qa_dataset)
```

```
eval_results = await retriever_evaluator.aevaluate_dataset(qa_dataset)
```

This should run much faster than you trying to call .evaluate on each query separately.

```
.evaluate
```

