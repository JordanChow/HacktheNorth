import csv
fileOut = open("Analysis.txt", "w")
inspection = {}
album = []
def addCity(dictionary, cityKey):
    dictionary[cityKey] = []

def addUniqueKey(dictionary, cityKey, incidentID):
    dictionary[cityKey].append(incidentID)
    

def fileInput():
    with open("result.csv") as fileIn:
        fileIn.readline()
        reader = csv.reader(fileIn)

        
        for line in reader:
            pic = line[0]
            ide = line[1].lower().strip()
            message = line[2].lower().strip()
            
            if ide not in inspection and message != "''":
                    if ide not in inspection:
                        addCity(inspection, ide)
                    addUniqueKey(inspection, ide, message)
            album.append(pic)

def fileOutput():
    fileOut.write("Message ID followed by the comment.")
    for k,v in inspection.items():
        fileOut.write(str(k)+"|||"+str(v))
        fileOut.write("\n")
        
        print(str(k)+str(v))
        print("\n")

    print("\n\n\n\n")
    fileOut.write("\n\n\n\n")
    fileOut.write("Pictures (Seperated by commas):\n")
    fileOut.write(str(album))
    #print(inspection.values())
        #print(inspection.values())
        #fileOut.write(key)

fileInput()

fileOutput()
fileOut.close()

