n,m = map(int,input().split())

parent = [i for i in range(n+2)]

def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]


def union_parent(a,b):
  a = find_parent(a)
  b = find_parent(b)
  if a<b : 
    parent[b] = a
  else:
    parent[a] = b

def is_same_parent(a,b):
  a = find_parent(a)
  b = find_parent(b)
  if a== b:
    return True
  return False

for _ in range(m):
  cmd,a,b = map(int,input().split())
  if cmd == 0:
    union_parent(a,b)
  else:
    if find_parent(a) == find_parent(b):
      print("YES")
    else:
      print("NO")

    