from collections import defaultdict
import pyarrow.csv as pacsv
import pandas as pd
import json
import os
import time
def traslate_pk_id(pk):
    """pk_id를 id로 변환"""
    global pk_id_dict
    global df
    try:
        return pk_id_dict[str(pk).replace(".0", "")]
    except:
        return -1


def traslate_id_pk(id):
    """id를 pk_id로 변환"""
    global id_pk_dict
    global df
    try:
        return str(id_pk_dict[id]).replace(".0","")
    except:
        return -1

def bfs(graph, start_id, end_id):
    start_node = traslate_id_pk(start_id)
    end_node = traslate_id_pk(end_id)
    queue = [(start_node, [start_node])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        # print(path)
        if node in visited:
            continue
        visited.add(node)
        if node == end_node:
            for i in range(len(path)):
                path[i] = traslate_pk_id(path[i])
            return path
        for child in graph[node]:
            if child not in visited:
                queue.append((child, path + [child]))
    # print(len(visited))
    return None

def search(startID, endID):
    # print(startID, "start")/
    graph = defaultdict(list)
    file_list = [file.replace(".json", "") for file in os.listdir(currDir+"/network") if file.endswith(".json")]
    for node in file_list:
        with open(f"{currDir}/network/{node}.json", "r") as f:
            lines = json.load(f)
        for line in lines:
            neighbor = str(line).strip()
            graph[node].append(neighbor)
    path = bfs(graph, startID, endID)
    # print(startID, path)
    return path

def test():
    t = time.time()
    print(search("orapaduck", "test"))
    print(time.time()-t)

currDir = os.path.dirname(os.path.realpath(__file__))
df = pacsv.read_csv(f"{currDir}/name_id.csv").to_pandas()
id_pk_dict = { id:str(pk_id) for id, pk_id in zip(df["id"], df["pk_id"]) }
pk_id_dict = { str(pk_id):id for id, pk_id in zip(df["id"], df["pk_id"]) }

test()