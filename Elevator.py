class Elevator:
    # list struct: [id,speed,minfloor,max,closeTime,openTime,startTime,stopTime]
    def __init__(self,elev):
        self.speed= float(elev[1])
        self.min=int(elev[2])
        self.max=int(elev[3])
        self.closeTime=int(elev[4])
        self.openTime=int(elev[5])
        self.startTime=int(elev[6])
        self.stopTime=int(elev[7])
        self.id=int(elev[0])
        self.callList=[]
        self.state=0 # rest
    def getSpeed(self):
        return self.speed
    def get_closeTime(self):
        return self.closeTime
    def get_openTime(self):
        return self.openTime
    def get_startTime(self):
        return self.startTime
    def get_stopTime(self):
        return self.stopTime
    def getID(self):
        return self.id
    def assignCall(self,src,dest,flag):
        #print("Elev index= ",self.id)
        self.callList.append([src,dest,flag])
        #print("call list size after addition ",len(self.callList))
    def getCall(self,callIndex):
        return self.callList[callIndex]
    def removeCall(self,index):
        self.callList.pop(index)
    def getCallList(self):
        return self.callList
    def getState(self):
        return self.state
    def setState(self,i):#i changed the state of the elev , 1==UP , -1==down ,0== not moving
        self.state=i

