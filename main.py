from os import system,name
from time import sleep
while (True):
  n = int(input("\n\nHow many numbers from the \nFibonacci's sequence do you want to see?:"))
  t1 = 0
  t2 = 1
  tot = 0
  c = 1
  print("Fibonacci's Sequence: ",end="")
  while (c<=n):
    print(f"{tot},",end="",flush=True)
    tot = t1 + t2
    t1 = t2
    t2 = tot
    c += 1
    if c == 3:
      tot = 1
      t2 = 1
    
