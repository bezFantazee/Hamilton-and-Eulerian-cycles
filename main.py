def EulerianCycle(start, clear_v=0):
    #проверка на изолированные вершины
    if len(graph[start]) == 0:
        way.clear()
        return
    way.append(start)
    #условие выхода из рекурсии
    if start == 1 and all(all(value is True for value in d.values()) for d in markEdges):
        return
    #выбор следующей вершины
    for vertex in graph[start]:
        if not markEdges[start][vertex] and vertex not in badEdges[start]:
            markEdges[start][vertex] = True
            markEdges[vertex][start] = True
            badEdges[start].clear()
            EulerianCycle(vertex)
            return
    #откат назад
    if len(way) < 2:
        way.clear()
        return
    a = way.pop()
    b = way.pop()
    badEdges[b].append(a)
    badEdges[a].clear()
    markEdges[a][b]=False
    markEdges[b][a]=False
    EulerianCycle(b, a)
    return


#проверка на существование эйлерова цикла
def EulerianCheck(g):
    for vertex in g:
        if len(vertex) % 2 != 0:
            return False
    return True

def HamiltonCycle(start):
    #проверка на изолированные вершины
    if len(graph[start]) == 0:
        way.clear()
        return
    way.append(start)
    markVertex[start]=True
    #условие выхода из рекурсии
    if start == 1 and all(markVertex):
        return
    #выбор следующей вершины
    for vertex in graph[start]:
        if vertex == 1 and all(markVertex):
            HamiltonCycle(vertex)
            return
        if not markVertex[vertex] and vertex not in badEdges[start]:
            HamiltonCycle(vertex)
            return
    #откат назад
    if len(way) < 2:
        way.clear()
        return
    a = way.pop()
    b = way.pop()
    badEdges[b].append(a)
    badEdges[a].clear()
    markVertex[a]=False
    markVertex[b]=False
    HamiltonCycle(b)


n, k = map(int, input().split())  #n-количество вершин, k-количество ребер
graph = []
markEdges=[]
markVertex=[]
badEdges=[]
way=[]
for i in range(n+1):
    graph.append([])
    markEdges.append({})
    badEdges.append([])
    markVertex.append(False)
markVertex[0] = True
for i in range(k):
    a, b = map(int, input().split())  #a, b-смежные вершины
    graph[a].append(b)
    graph[b].append(a)
    markEdges[a][b]=False
    markEdges[b][a]=False
#выбор действия
op = int(input("Выберите операцию: "))
if op == 1:
    if EulerianCheck(graph):
        EulerianCycle(1)
elif op == 2:
    HamiltonCycle(1)
else:
    print("Выбрана некорректная операция")
if way:
    print("Ответ: ", *way)
else:
    print("Нет ответа")
