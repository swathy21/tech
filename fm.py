e=int(input())
p,s=map(int,input().split())
for i in range(p+1,s):
  if e==i:
    print("yes")
    break
else:
  print("no")
