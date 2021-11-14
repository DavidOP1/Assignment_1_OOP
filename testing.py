import csv
import json
def info(building,calls,output):
  file = open('data.json', )
  data = json.load(building)
  elevatorData=[]
  k=0
  #Reading from the json file.
  for i in  dict['_elevators']:
    elevatorData.append([])
    for j in i:
      elevatorData[k].append(i[j])
     # print(j," ",i[j])
    k+=1
  file.close()
  #Reading from the csv file
  with open(calls, mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    calls = []
    for lines in csvFile:
      calls.append([lines[2], lines[3], lines[5]])

if __name__ == '__main__':
  #testing csv read
  # opening the CSV file

    # reading the CSV file
  with open('Calls_a.csv', mode='r') as file:

    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    calls=[]
    for lines in csvFile:
      calls.append([lines[2],lines[3],lines[5]])
    for i in calls:
      print(i)
  #save calls in format: list(list(src,dest,whichelevwasAssigned default -1))


  # print("as")
  # dict = {
  #   "_minFloor": -2,
  #   "_maxFloor": 10,
  #   "_elevators": [
  #     {
  #       "_id": 0,
  #       "_speed": 1.0,
  #       "_minFloor": -2,
  #       "_maxFloor": 10,
  #       "_closeTime": 2.0,
  #       "_openTime": 2.0,
  #       "_startTime": 3.0,
  #       "_stopTime": 3.0
  #     },
  #     {
  #       "_id": 1,
  #       "_speed": 2.0,
  #       "_minFloor": -2,
  #       "_maxFloor": 10,
  #       "_closeTime": 2.0,
  #       "_openTime": 2.0,
  #       "_startTime": 3.0,
  #       "_stopTime": 3.0
  #     }
  #   ]
  # }
  # info = []
  # k=0
  # for i in  dict['_elevators']:
  #   info.append([])
  #   for j in i:
  #     info[k].append(i[j])
  #   k+=1
  # print(info[1])