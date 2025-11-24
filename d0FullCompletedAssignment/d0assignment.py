import json


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

def main(memberInfo, memberPaidInfo):
    memberInfoDict = {}
    memberPaidInfoDict = {}
    memberInfoAndPaidInfo = {}
    with open(memberInfo, "r") as file:
        print()
        
    with open(memberPaidInfo, "r") as file:
        print()
if __name__ == "__main__":
    main("memberInfo.csv", "memberPaidInfo.csv")