import csv
from Building import Building
class Calls:
    def __init__(self,callsfile_Name,building_Name):
        # Reading from the csv file
        self.building = Building(building_Name)
        self.elevList = []
        self.flag=0
        for i in range(len(self.building.elevatorData)):
            self.elevList.append(self.building.getElev(i))
        with open(callsfile_Name, mode='r') as file: # getting all the calls from the csv file
            # reading the CSV file
            self.rowNum=0
            csvFile = csv.reader(file)
            self.calls = []
            self.fullCalls=[]
            for lines in csvFile:
                self.calls.append([int(lines[2]), int(lines[3]), int(lines[5])])
                self.fullCalls.append(lines)
                self.rowNum += 1
           # print(self.calls[2])

    def checkIfValid(self):#Function to check if a given calls file fits the building
        for i in range(len(self.calls)):
            for j in range(len(self.elevList)):
                if (self.elevList[j].max < self.calls[i][0] or self.elevList[j].max < self.calls[i][1] or  self.elevList[j].min > self.calls[i][0] or self.elevList[j].min > self.calls[i][1]):
                    self.flag = 1
                    break
#calls list structure: [src,dest,assignedElevator]
    def getFulCallList(self):
        return self.fullCalls
    def assign(self,index,elev_ID): # assigns the elevator to the call
        self.calls[index][2]=elev_ID
    #assigns the elevator to the call
    def getCalls(self): # returns the list of calls which we have got from the csv file.
        return self.calls
    #returns a call at a specific index
    def getCallByIndex(self,index):
        #print("length",len(self.calls),"type call=" ,self.calls[index] , "index= ", index)
        return self.calls[index]
    #return list of calls
