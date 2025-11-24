import json
import os

"""
Overall Program Summary:

Given CSV files with specific columns, cleans the data in the CSV file so that the output file contains
member id, full name, and paid amount. The output file will be a seperate JSON file. Also prints out 
member with highest paid amount and the total amount paided.

"""


"""
Summary:
    Cleans the data in CSV by removing entries that have no name connected to the member id
Parameters:
    directory: a string that is the directory the current python file is located in
    memberInfoFile: the name of the csv we are cleaning
Return:
    list->dict: This is a list of dictonaries that contains all valid member info
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
            if seperatedData[1] == "": #if hole in data continue
                continue
            else: #else we put in the first and last name of the person
                memberInfoDict["firstName"] = seperatedData[1]
                memberInfoDict["lastName"] = seperatedData[2]
            memberInfoList.append(memberInfoDict)
    return memberInfoList

"""
Summary:
    Merges the data in the member paid info csv to the member info list. Making sure to avoid
    any name conflictions and that the member exists in the cleaned list of members
Parameters:
    directory: a string that is the directory the current python file is located in
    memberPaidInfoFile: the name of the csv file that contain the paid info for members
    memberInfoList: This is a list of dictonaries that contains all valid member info
Return:
    list->dict: This is a list of dictonaries that contains all valid member info along with 
    the paid amount
"""
def mergeDataFromMemberPaidInfo(directory, memberPaidInfoFile, memberInfoList) -> list[dict]:
    memberPaidInfoFile = os.path.join(directory, "CSV Files", memberPaidInfoFile)
    with open(memberPaidInfoFile, "r") as file:
        next(file) #skips first line
        index = 0 #index for memberInfoList to keep track of what paidAmount goes to what person
        for entry in file: #looping over all lines in csv
            seperatedData = entry.split(",")
            memberId = seperatedData[0]
            memberExists = False
            for memberInfoEntry in memberInfoList: #looping over memberInfo list to see if member exitsts
                if memberInfoEntry["memberId"] == memberId:
                    if seperatedData[1] == "":
                        memberExists = True
                    else:
                        fullNameList = seperatedData[1].split(" ")
                        firstName = fullNameList[0]
                        lastName = fullNameList[1]
                        #checking if name conflict
                        if firstName != memberInfoList[index]["firstName"] or lastName != memberInfoList[index]["lastName"]:
                            memberInfoList.remove(memberInfoEntry) #removes entry if name conflict
                            memberExists = False
                        else:
                            memberExists = True
                    break
            if memberExists:
                memberInfoList[index]["paidAmount"] = seperatedData[2].replace("\n", "")
                index+=1
    return memberInfoList

"""
Summary:
    Prints out the statistics related the member info and paid info. Prints out the
    member who has the highest paid amount. Also prints out the total paid amount by
    all valid members
Parameters:
    highestPaidList: a sorted list of dictonaries by the value of paidedAmount in the
    dictonaries. The dictonaries contain member info and paid amount info
"""
def printStats(highestPaidList) -> None:   
    highestPaidPerson = highestPaidList[0] 
    print("Person with the highest paid amount:")
    for key in highestPaidPerson:
        print("\t" + str(key) + " : " + str(highestPaidPerson[key]))
    totalPaidAmount = 0
    for person in highestPaidList:
        totalPaidAmount += int(person["paidAmount"])
    print("Total Paided Amount: " + str(totalPaidAmount))

"""
Summary:
    Saves all valid member info and paid info into a JSON file for more data analysis
Parameters:
    memberInfoAndPaidInfoList: This is a list of dictonaries that contains all valid member info along with 
    the paid amount
"""
def outputCleanedData(memberInfoAndPaidInfoList) -> None:
    with open("d0FullCompletedAssignment\\cleanedMemberInfoAndPaidInfo.json", "w") as file:
        json.dump(memberInfoAndPaidInfoList, file, indent=2)

"""
Summary:
    Calls all functions performing the data cleaning, printing statistics, and saving output
Parameters:
    memberInfoFile: the name of the csv file that contain the member info
    memberPaidInfoFile: the name of the csv file that contain the paid info
"""
def main(memberInfoFile, memberPaidInfoFile):
    directory = os.path.dirname(os.path.abspath(__file__))
    memberInfoList = getDataFromMemberInfo(directory, memberInfoFile)
    memberInfoAndPaidInfoList = mergeDataFromMemberPaidInfo(directory, memberPaidInfoFile, memberInfoList)
    #sorts list by paidAmount value located in each dictonary, highest paid amount at index 0
    highestPaidList = sorted(memberInfoAndPaidInfoList, key=lambda d: d["paidAmount"], reverse=True)
    printStats(highestPaidList)
    outputCleanedData(memberInfoAndPaidInfoList)
    
if __name__ == "__main__":
    main("memberInfo.csv", "memberPaidInfo.csv")