from bisect import bisect_left as bl
import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
t=sorted(a)

for i in range(n):
  a[i]=bl(t,a[i])+1
bit=[0]*(n+1)
def getSum(i):
  s=0
  while i:
    s+=bit[i]
    i-=i&-i
  return s
def update(i,x):
  while i<=n:
    bit[i]+=x
    i+=i&-i
for i in range(n):
  print(i+1-getSum(a[i]), end=' ')
  update(a[i],1)