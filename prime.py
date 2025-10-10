x = int(input("enter the number:"))
if x >1:
  for i in range(1,x+1):
    if  x%i == 0:
      print("not prime")
      break

  else:
    print("prime")    
else:
  print("not prime")  