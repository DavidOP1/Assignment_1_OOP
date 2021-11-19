import Calls
from Building import Building
from Calls import Calls
import sys
from OfflineElevAlgo import OfflineElevAlgo
import csv

if __name__ == '__main__':
  list = sys.argv
  building = list[1]
  calls = list[2]
  output = list[3]
  call=Calls(calls,building)
  call.checkIfValid()
  if(call.flag==0):
   p1= OfflineElevAlgo(calls,building,output)
   p1.allocateAnElevator()
   p1.writeAssignedCallsToFile()
  else:
    print("Structure is not valid for inserted call list")


