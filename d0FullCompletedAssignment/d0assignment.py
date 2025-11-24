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

def getDataFromMemberPaidInfo(directory, memberPaidInfo) -> list[dict]:
    memberPaidInfoList = []
    memberPaidInfoFile = os.path.join(directory, "CSV Files", memberPaidInfoFile)
    with open(memberPaidInfoFile, "r") as file:
        next(file) #skips first line
        print()
        for entry in file:
            memberPaidInfoDict = {}
            seperatedData = entry.split(",")
            
def main(memberInfoFile, memberPaidInfoFile):
    memberInfoAndPaidInfoDict = {}
    memberInfoAndPaidInfoList = []
    directory = os.path.dirname(os.path.abspath(__file__))
    memberInfoList = getDataFromMemberInfo(directory, memberInfoFile)
    print()
    
if __name__ == "__main__":
    main("memberInfo.csv", "memberPaidInfo.csv")