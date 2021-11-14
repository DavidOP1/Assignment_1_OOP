class Elevator:
    # list struct: [id,speed,minfloor,max,closeTime,openTime,startTime,stopTime]
    def Elevator(self,elev):
        self.speed=elev[1]
        self.closeTime=elev[4]
        self.openTime=elev[5]
        self.startTime=elev[6]
        self.stopTime=elev[7]
        self.index=elev[0]
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
    def getIndex(self):
        return self.index

