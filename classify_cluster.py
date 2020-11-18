import copy
#pinterest

def dfs(node, flag, nodes):
    lst = []
    if flag[node] == -1:
        flag[node] = 1
        # print(node)
        lst.append(node)
    for adjacent in nodes[node]:
        # print(node, adjacent,'adjacent')
        if flag[adjacent] == -1:
            lst += dfs(adjacent, flag, nodes)

    return lst
def count_connected_graph(nodes):
    nodes = get_complete_mappings(nodes)
    node_lst  = nodes.keys()
    flag = {}
    count = 0
    for node in node_lst:
        flag[node] = -1
    for node in node_lst:
        # print('big', node)
        if flag[node] == -1:
            lst = dfs(node, flag, nodes)
            print(lst)
            count += 1
    return count
def get_complete_mappings(nodes):
    new_nodes= copy.deepcopy(nodes)
    for k, v in nodes.items():
        for c in v:
            if k not in nodes[c]:
                new_nodes[c].append(k)
    return new_nodes

nodes = { 'A': ['B','I','K',],'B': ['A', 'D'],'C': ['E'],'D': ['B'],'E': [],'F': [],'G': ['K'],'I': [],'K': []}

rst = count_connected_graph(nodes)
print(rst)