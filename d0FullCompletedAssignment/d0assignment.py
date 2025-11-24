import json
import os

"""
Given CSV files with specific columns, cleans the data in the CSV file so that the output file contains
member id, full name, and paid amount. The output file will be a seperate JSON file

Also reports the highest paid amount with the members info
Parameters: 
memberInfo : string
    CSV file as a string containing member info
memberPaidInfo : string
    CSV file as a string containing paid info

"""

def getDataFromMemberInfo(directory, memberInfoFile) -> list[dict]:
    memberInfoList = []
    memberInfoFile = os.path.join(directory, "CSV Files", memberInfoFile)
    with open(memberInfoFile, "r") as file:
        next(file) #skips first line
        for entry in file:
            memberInfoDict = {}
            seperatedData = entry.split(",")
            memberInfoDict["memberId"] = seperatedData[0] #seperatedData[0] is the member id in the csv file
            seperatedData[2] = seperatedData[2].replace("\n", "") #removes \n in the string
            if seperatedData[1] == "":
                continue
            else:
                memberInfoDict["firstName"] = seperatedData[1]
                memberInfoDict["lastName"] = seperatedData[2]
            memberInfoList.append(memberInfoDict)
    return memberInfoList

def mergeDataFromMemberPaidInfo(directory, memberPaidInfoFile, memberInfoList) -> list[dict]:
    memberPaidInfoFile = os.path.join(directory, "CSV Files", memberPaidInfoFile)
    with open(memberPaidInfoFile, "r") as file:
        next(file) #skips first line
        index = 0
        for entry in file:
            seperatedData = entry.split(",")
            memberId = seperatedData[0]
            memberExists = False
            for memberInfoEntry in memberInfoList:
                if memberInfoEntry["memberId"] == memberId:
                    if seperatedData[1] == "":
                        memberExists = True
                    else:
                        fullNameList = seperatedData[1].split(" ")
                        firstName = fullNameList[0]
                        lastName = fullNameList[1]
                        #checking if name conflict
                        if firstName != memberInfoList[index]["firstName"] or lastName != memberInfoList[index]["lastName"]:
                            memberInfoList.remove(memberInfoEntry)
                            memberExists = False
                        else:
                            memberExists = True
                    break
            if memberExists:
                memberInfoList[index]["paidAmount"] = seperatedData[2].replace("\n", "")
                index+=1
    return memberInfoList

def printStats(highestPaidList) -> None:   
    highestPaidPerson = highestPaidList[0]
    print("Person with the highest paid amount:")
    for key in highestPaidPerson:
        print("\t" + str(key) + " : " + str(highestPaidPerson[key]))
    totalPaidAmount = 0
    for person in highestPaidList:
        totalPaidAmount += int(person["paidAmount"])
    print("Total Paided Amount: " + str(totalPaidAmount))
    
def main(memberInfoFile, memberPaidInfoFile):
    directory = os.path.dirname(os.path.abspath(__file__))
    memberInfoList = getDataFromMemberInfo(directory, memberInfoFile)
    memberInfoAndPaidInfoList = mergeDataFromMemberPaidInfo(directory, memberPaidInfoFile, memberInfoList)
    highestPaidList = sorted(memberInfoAndPaidInfoList, key=lambda d: d["paidAmount"], reverse=True)
    printStats(highestPaidList)
    
    
if __name__ == "__main__":
    main("memberInfo.csv", "memberPaidInfo.csv")