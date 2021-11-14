import csv
class Calls:
    def Calls(self,calls):
        # Reading from the csv file
        with open(calls, mode='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            self.calls = []
            for lines in csvFile:
                self.calls.append([lines[2], lines[3], lines[5]])
    def assign(self,index):
        self.calls[2]=index
    #assigns the elevator to the call
    def getCalls(self):
        return self.calls
    #return list of calls
