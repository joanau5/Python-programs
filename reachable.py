import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    node_dict = defaultdict(set)
    for line in file:
        node_dict[line[0]].add(line[2])
    file.close()
    return node_dict


def graph_as_str(graph : {str:{str}}) -> str:
    strr = ''
    for k, v in sorted(graph.items(), key = (lambda item: item[0])):
        strr += '  ' + str(k) + ' -> ' + str(sorted(v)) + '\n'
    return strr

        
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    reached = set()
    exploring_list = [start]
    while len(exploring_list) != 0:
        key_node = exploring_list.pop()
        reached.add(key_node)
        if graph.get(key_node, set(key_node)).issubset(reached) == False:
            exploring_list.extend(list(graph.get(key_node)))
            
    return reached





if __name__ == '__main__':
    # Write script here
    file = input("Specify the file name representing the graph:")
    print()
    print("Graph: str (one source node) -> [str] (sorted list of destination nodes)")
    graph = read_graph(file)
    print(graph_as_str(graph))
    while True:
        node = input("Specify one start node (or terminate):")
        if graph.get(node, "Entry error:" + node+"; Illegal:not a source node" + '\n'+ "Please enter a legal String"):
            print("")
            print("")
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
