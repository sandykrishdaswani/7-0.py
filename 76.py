us=int(input())
if(us>1):
 for i in range(2,us):
  if(us%i==0):
   print("yes")
   break
 else:
  print("no")
