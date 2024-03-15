room = int(input( ))
num = 0
for l in range (1,5):
  for p in range (1,9):
    num+=1
    if(num) == room:
      print(p,' ',l)
      p=0
