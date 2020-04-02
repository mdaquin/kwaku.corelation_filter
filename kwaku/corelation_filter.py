

# it currently adds many edges that are duplicate
# ingraph should have an option to weigh them...
def create(config, ing, outg):
    lookfor = "inedges"
    if config["reverse"]:
        lookfor="outedges"    
    r = ing.search(query="outedges:author", size=5000)
    for node in r["hits"]:
        cnodes = []
        for edge in node[lookfor]:
            label = edge[1]
            node = edge[0]
            if config["reverse"]:
                label = edge[0]
                node = edge[1]
            if label == config["input_relation"]:
                if node not in cnodes:
                    cnodes.append(node)
        for i in range(0, len(cnodes)):
            for j in range(i+1, len(cnodes)):
                print("creating edge between node "+cnodes[i]+" and node "+cnodes[j])
                outg.update_node(cnodes[i], {"edges": [[cnodes[j], config["output_relation"]]]})
    return True
