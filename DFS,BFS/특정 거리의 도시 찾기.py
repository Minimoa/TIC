# 노드간 연결 정보를 딕셔너리로 만든다 
# 시작점에서 BFS하여 거리 정보를 1씩 업데이트 하면서 최단 거리 K를 만족하는 노드를 찾는다
# 없을 경우 -1을 출력한다 

from collections import deque

n,m,k,x= map(int,input().split(" "))
graph = {}
visited = [False] * (n+1)
distance = [0]*(n+1)

for i in range(n):
  graph.setdefault(i+1,[])

for _ in range(m):
  src,dst = map(int,input().split(" "))
  graph[src].append(dst)

result = []
 
def bfs(x):
  queue = deque([x])
  visited[x] = True 

  while queue:
    x = queue.popleft()
    for node in graph[x]:
      if not visited[node]:
        visited[node] = True
        queue.append(node)
        distance[node] = distance[x]+1 



bfs(x)

nothing = True
for i,v in enumerate(distance):
  if v == k :
    print(i)
    nothing = False

if nothing:
  print(-1)
  
  
 ####

from collections import deque
import sys

input = sys.stdin
n,m,k,x= map(int,input.readline().rstrip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a,b = map(int, input.readline().rstrip().split())

  graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

  
q = deque([x]) 

while q:
  cur = q.popleft()
  for next in graph[cur]:
    if graph[next] == -1: 
      distance[next] = distance[cur]+1  
      q.append(next)
 

nothing = True
for i in range(1,n+1):
  if distance[i] == k :
    print(i)
    nothing = False

if nothing:
  print(-1)
  
  
  
