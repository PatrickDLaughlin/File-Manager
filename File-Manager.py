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
    for root, dirs, files in os.walk('C:\\Users\\patrick.laughlin\\Documents\\Cases\\Active\\'):
        dirlist += dirs
    print(dirlist)
    if casenum in dirlist:
        print('Error: Duplicate case diretory exists')
    else:
        pass

#Sets the case # to a global variable
def setCaseNum():
    global casenum
    global contfname
    global contlname
     
    casenum = input("Please enter case number #")
    contfname = input("Please enter Responsible Contact's First Name:")
    contlname = input("Please enter Responsible Contact's Last Name :")
    caseNumCheck()
    print("Is the case info " + casenum + " " + contfname + " " + contlname + " correct? Y or N")
    x = input()

#Creates Directory with case# as name
def makeCaseDir():
    dirPath = "C:\\Users\\patrick.laughlin\\Documents\\Cases\\Active\\"
    casePath = dirPath + casenum + " " + contfname + " " + contlname
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