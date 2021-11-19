from Building import Building
from Calls import Calls
import sys
import csv
class OfflineElevAlgo:
 def __init__(self,callsfile_Name,buildingfile_Name,outputfile_Name):
     self.call = Calls(callsfile_Name,buildingfile_Name) # creating a calls object
     self.building = Building(buildingfile_Name)# Creating a building object
     self.elevList=[] # Creating a list to store the elevator objects
     for i in range(len(self.building.elevatorData)): # for loop to add the elevators to the list
         self.elevList.append(self.building.getElev(i))
     self.out=outputfile_Name
 def allocateAnElevator(self):
        assignElevIndex=-1
        for i in range(len(self.call.getCalls())):#pass on all calls
         bestTime = sys.maxsize
         for j in range(len(self.building.elevatorData)):# pass on all elevators
             elev=self.elevList[j]
             elevTime=self.distTime(elev,self.call.getCallByIndex(i),j)
             if(elevTime<bestTime):#Check if we got a better time from a different elevator
                 bestTime=elevTime
                 assignElevIndex=j
             #increment by 1 index
         self.elevList[assignElevIndex].assignCall(self.call.getCallByIndex(i)[0],self.call.getCallByIndex(i)[1],0)#Assigining this call to the elevator
         self.call.assign(i,self.elevList[assignElevIndex].id)
 def writeAssignedCallsToFile(self):
#This function writes the assigned results to the output file.
  with open(self.out, 'w', encoding='UTF8', newline='') as f:
  #  create the csv writer
    writer = csv.writer(f)
    tempList=self.call.getFulCallList()
    for i in range(self.call.rowNum):
     tempList[i][5]=self.call.calls[i][2]
    writer.writerows(tempList)

 def distTime(self,elev,call,elevIndex):
     numOfFloors,time,ans,currentSrc,currentDest=0,0,0,0,0
     if(len(elev.callList)>0):#Checking if the elevator already moved
         pos=elev.getCall(0)[1]
     if(len(elev.callList)==0):
         pos=0
     elev.assignCall(call[0], call[1], 1) #Adding the new call to the list temporarily
     self.sort(elevIndex,1) #Sorting with newely added call
     for i in range(len(elev.callList)):
         currentSrc=elev.getCall(i)[0]
         currentDest=elev.getCall(i)[1]
         numOfFloors=abs(pos-currentSrc) + abs(currentSrc-currentDest)
         time = numOfFloors/elev.speed
         ans=ans+time+elev.stopTime+elev.startTime+2*(elev.openTime+elev.closeTime) # Calculating total travel time of elevator with all the calls in the list
         pos=currentDest
     for i in range(len(elev.getCallList())):#We remove the new call which we added temporarily for calculation purposes
      if(elev.getCall(i)[2]==1):
             elev.removeCall(i)
             break

     return ans

 def sort(self,elevIndex,index):
    n = len(self.elevList[elevIndex].getCallList())
    elev= self.elevList[elevIndex]
    if(elev.getCall(n-1)[0]<elev.getCall(0)[0]): #if new call is closer then last closest call swap
        self.swap(n-1,0,elevIndex)
    for i in range(1,n): # arrange the list accordingly with new call
        self.swap(i,n-1,elevIndex)
 def swap(self,j,k,elevIndex): #swap between certain indexes
     #k=j+1
     elev=self.elevList[elevIndex]
     temp = elev.callList[k]
     elev.callList[k]=elev.callList[j]
     elev.callList[j]=temp
