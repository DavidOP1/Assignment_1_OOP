import json
import Elevator
class Building:
#list struct: [id,speed,minfloor,max,closeTime,openTime,startTime,stopTime]
    def __init__(self,building):
        file = open(building, )
        data = json.load(file) # getting all the info about the elevators from the json file
        self.elevatorData = []
        k = 0
        # Reading from the json file.
        p=0
        for i in data['_elevators']: # Taking the info from the json file and putting it into a list
            self.elevatorData.append([])
            p=0
            for j in i:
                if(p==0):  self.elevatorData[k].append(k)
                else :self.elevatorData[k].append(i[j])
                #print("length= ", self.elevatorData[k])
                p+=1
            k += 1
        file.close()
    def getElev(self,index):
        return Elevator.Elevator(self.elevatorData[index])#i Think this creates a new elev object