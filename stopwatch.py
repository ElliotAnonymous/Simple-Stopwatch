#python 3.7.1
#this program creating date 17/10/2020
import time 
import datetime
from datetime import datetime
print("Date Time ")
print(datetime.now())
print()
print("Hello my name is prem and i am\nmake normal program.")
print()
while (True):
  print("Enter Number Of Seconds :  ")

  userinput = int(input())
  print("Stop watch started.....")
  print()
  while userinput!=0:
    print(str(userinput) + "  seconds remaining ⏳")
    print()
    time.sleep(1)
    userinput = userinput-1
  print ("The time is up ")
  print()
  print("Next key 😋 ")


