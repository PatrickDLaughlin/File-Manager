import os

#Introduction, Purpose, Author
def intro():
    print("This python application is intended to create and manage cases\nAuthor: Patrick Laughlin AvePoint Technical Support")
    os.system("PAUSE")
    os.system("CLS")

#Checks if the case number is correct
def caseNumCheck():
    #This Part Checks the case number for the letter C at the beginning
    C = 'C'
    if C in casenum:
        pass
    else:
        print('Case # missing letter C')
        pass
    numcount = len(casenum)
    
    #This part checks if the case number is the correct number of digits (14)
    if numcount == 15:
        pass
    else:
        print('Case is not the correct number digits')
        pass
    
    #This part checks if the case has already been made
    dirlist = []
    for root, dirs, files in os.walk('C:\\Users\\patrick.laughlin\\Documents\\Cases'):
        dirlist += dirs
    print(dirlist)

#Sets the case # to a global variable
def setCaseNum():
    
    global casenum 
    casenum = input("Please enter case number #")
    caseNumCheck()
    print("Is the case number " + casenum + " correct? Y or N")
    x = input()

#Creates Directory with case# as name
def makeCaseDir():
    dirPath = "C:\\Users\\patrick.laughlin\\Documents\\Cases\\"
    casePath = dirPath + casenum
    os.mkdir(casePath)
    print("Directory " + casePath + " created")

#Menu
def menu():
    print('Please select an option:')
    print('1. Create new case')
    x = input()
    if x == '1':
        os.system("CLS")
        setCaseNum()
        makeCaseDir()

def main():
    intro()
    menu()
    os.system("PAUSE")

main()