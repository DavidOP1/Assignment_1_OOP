import json
import Elevator
class Building:
#list struct: [id,speed,minfloor,max,closeTime,openTime,startTime,stopTime]
    def Building(self,building):
        file = open('data.json', )
        data = json.load(building)
        self.elevatorData = []
        k = 0
        # Reading from the json file.
        for i in dict['_elevators']:
            self.elevatorData.append([])
            for j in i:
                self.elevatorData[k].append(i[j])
            # print(j," ",i[j])
            k += 1
        file.close()
    def getElev(self,index):
        return Elevator.Elevator(self.elevatorData[index])