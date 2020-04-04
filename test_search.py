import sys
sys.path.insert(1, '/home/mdaquin/code/ingraph/')
from ingraph.ingraph import InGraph
import json

graphid = "test_crf_graph"
es_url = "http://127.0.0.1:9200/"

graph = InGraph(graphid, es_url)

allnodes = graph.search(size=5000)

nodes = []
knownedges = []
edges = []

for node in allnodes["hits"]:
    nodes.append({"id": node["nodeid"], "group": 1})
    for edge in node["outedges"]:
        key = node["nodeid"]+"__"+edge[0]
        key2 = edge[0]+"__"+node["nodeid"]
        if key not in knownedges and key2 not in knownedges:
            knownedges.append(key)
            knownedges.append(key2)
            edges.append({"source": node["nodeid"], "target": edge[0], "value": 1})

print(json.dumps({"nodes": nodes, "links": edges}))

# create the json file for the force directed graph
