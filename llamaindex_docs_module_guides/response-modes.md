# Response Modes#

原始連結：https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/response_modes/

# Response Modes#

[#](https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/response_modes/#response-modes)

Right now, we support the following options:

- refine: create and refine an answer by sequentially going through each retrieved text chunk.
  This makes a separate LLM call per Node/retrieved chunk.
```
refine
```

Details: the first chunk is used in a query using the
  text_qa_template prompt. Then the answer and the next chunk (as well as the original question) are used
  in another query with the refine_template prompt. And so on until all chunks have been parsed.

```
text_qa_template
```

```
refine_template
```

If a chunk is too large to fit within the window (considering the prompt size), it is split using a TokenTextSplitter
  (allowing some text overlap between chunks) and the (new) additional chunks are considered as chunks
  of the original chunks collection (and thus queried with the refine_template as well).

```
TokenTextSplitter
```

```
refine_template
```

Good for more detailed answers.

- compact (default): similar to refine but compact (concatenate) the chunks beforehand, resulting in less LLM calls.
```
compact
```

```
refine
```

Details: stuff as many text (concatenated/packed from the retrieved chunks) that can fit within the context window
  (considering the maximum prompt size between text_qa_template and refine_template).
  If the text is too long to fit in one prompt, it is split in as many parts as needed
  (using a TokenTextSplitter and thus allowing some overlap between text chunks).

```
text_qa_template
```

```
refine_template
```

```
TokenTextSplitter
```

Each text part is considered a "chunk" and is sent to the refine synthesizer.

```
refine
```

In short, it is like refine, but with less LLM calls.

```
refine
```

- tree_summarize: Query the LLM using the summary_template prompt as many times as needed so that all concatenated chunks
  have been queried, resulting in as many answers that are themselves recursively used as chunks in a tree_summarize LLM call
  and so on, until there's only one chunk left, and thus only one final answer.
```
tree_summarize
```

```
summary_template
```

```
tree_summarize
```

Details: concatenate the chunks as much as possible to fit within the context window using the summary_template prompt,
  and split them if needed (again with a TokenTextSplitter and some text overlap). Then, query each resulting chunk/split against
  summary_template (there is no refine query !) and get as many answers.

```
summary_template
```

```
TokenTextSplitter
```

```
summary_template
```

If there is only one answer (because there was only one chunk), then it's the final answer.

If there are more than one answer, these themselves are considered as chunks and sent recursively
  to the tree_summarize process (concatenated/splitted-to-fit/queried).

```
tree_summarize
```

Good for summarization purposes.

- simple_summarize: Truncates all text chunks to fit into a single LLM prompt. Good for quick
  summarization purposes, but may lose detail due to truncation.
```
simple_summarize
```

- no_text: Only runs the retriever to fetch the nodes that would have been sent to the LLM,
  without actually sending them. Then can be inspected by checking response.source_nodes.
```
no_text
```

```
response.source_nodes
```

- accumulate: Given a set of text chunks and the query, apply the query to each text
  chunk while accumulating the responses into an array. Returns a concatenated string of all
  responses. Good for when you need to run the same query separately against each text
  chunk.
```
accumulate
```

- compact_accumulate: The same as accumulate, but will "compact" each LLM prompt similar to
  compact, and run the same query against each text chunk.
```
compact_accumulate
```

```
compact
```

See [Response Synthesizer](https://docs.llamaindex.ai/en/stable/module_guides/querying/response_synthesizers/) to learn more.

