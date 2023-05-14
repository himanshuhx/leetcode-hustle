n=int(input())
x=int(input())
y=int(input())
c=int(input())
co=1
while True:
 if((n-y+c)>x or (n-y+c)>y):
  co+=1
  n-=y
  n+=c
 else:
  break
print(co)