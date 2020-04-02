# Kwaku co-relation filter

simple kwaky filter component that takes a graph and produces a new graph where nodes are connected base on sharing a relation with a third node in the original graph (Examples: creating a sibling or co-authorship relation).

The input, other than the input graph, is:

'''json
{
   input_relation: string,
   reverse: boolean,
   output_relation: string
}
'''
both attributes are labels of relations. Reverse indicate whether the input relation should be considered for in edges or outedges. For example, for the new graph to contain co-authorship relations, the configuration would be
'''json
{
  input_relation: "author",
  output_relation: "coauthor"
}
'''
