import sys
sys.path.insert(1, '/home/mdaquin/code/ingraph/')
from ingraph.ingraph import InGraph
from kwaku.corelation_filter import create

config = {
    "input_relation": "author",
    "reverse": True,
    "output_relation": "co-author",
    }

ingraphid  = "test_ptg_graph"
outgraphid = "test_crf_graph"
es_url = "http://127.0.0.1:9200/"

ingraph = InGraph(ingraphid, es_url)
outgraph = InGraph(outgraphid, es_url)

outgraph.delete_graph()
outgraph.create_graph(directed=True, labelled=True, weighted=False, multi=True)

print (create(config, ingraph, outgraph))





