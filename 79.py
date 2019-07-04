mum,pop=map(int,input().split())
mqn=mum*pop
for j in range(0,mqn+1):
 if(j**2==0):
  print("yes")
  break
else:
 print("no")
