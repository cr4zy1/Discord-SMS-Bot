#This file contains methods to make adding and deleting emails from the csv easier
#Verison Beta 0.5

import re # if a problem requires regex, then you have 2 problems - unknown 
import csv

def addEmail(name,phoneNum):
    # old version, new one might be better, keeping for now
    #reg = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    #if re.search(reg,phoneNum): # if email is a valid email format (name@serice.xyz or name@service.xy)
    #file = open('phoneNumbers.csv', "a+")
    #file.write("\""+name.strip()+"\""+ "," + "\""+phoneNum.strip+"\"");
    #print("File Appended")
    #else:
    #    print("Invalid Email: " + phoneNum)

    with open("phoneNumbers.csv",'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        writer = [name,phoneNum]
        print(writer[0] + "\n" + writer[1])
        csvwriter.writerow(writer)
        print("file appended")

def getEmail(name):
    with open('phoneNumbers.csv') as csv_file: #opens the name and number csv file
        csv_reader = csv.reader(csv_file ,delimiter=",")# init stuff, sets the delimiter as ,
    
        
        for row in csv_reader: # checks if the name is in the file and stores the value of phoneNumber into the string phoneNum
            if row[0] == name:
                phoneNum = row[1]
                return phoneNum


def writeDatabase(names):
   # addEmail("name","PhoneNum")
    #line = 0
    #for i in names:
    #    addEmail(names[line][0],names[line][1])
    #    line+=1
    #print("File Write Complete")

    with open("phoneNumbers.csv",'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        #print(writer[0] + "\n" + writer[1])
        for i in names:
            csvwriter.writerow(i)
        print("file appended")


    
    
def getDatabase():
    names = [[""],[""]]
    with open('phoneNumbers.csv') as csv_file: #opens the name and number csv file
        csv_reader = csv.reader(csv_file ,delimiter=",")# init stuff, sets the delimiter as ,
        line = 0 

        for row in csv_reader: # checks if the name is in the file and stores the value of phoneNumber into the string phoneNum
            names.append(row)
          
    
    return names

