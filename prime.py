pp=int(input())
if pp>1:
  for i in range(2,pp):
    if(pp%i==0):
      print("no")
      break    
  else:
    print("yes")
else:
  print("no")
