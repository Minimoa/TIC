from collections import deque

n,m = map(int,input().split(" "))
graph = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0
def bfs(i,j):
  global cnt
  queue = deque([(i,j)])
  graph[i][j] = 0
  cnt += 1 
  while queue:
    x,y = queue.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny] == 1:
          graph[nx][ny] = 0
          queue.append((nx,ny))
          cnt += 1

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      bfs(i,j)


print(cnt)

###

from collections import deque

n,m = map(int,input().split(" "))
graph = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
 
def bfs(x,y): 
  queue = deque([(x,y)]) 
  while queue:
    x,y = queue.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] +1
          queue.append((nx,ny)) 
  return graph[n-1][m-1]
 

print(bfs(0,0))



