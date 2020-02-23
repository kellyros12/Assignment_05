#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# KRos, 2020-Feb-21, Replaced lists with dictionary
# KRos, 2020-Feb-21, added loading and deleting functionality
# KRos, 2020-Feb-22, fixed the display functionality
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
lstRow = []
dictRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        print('Loading from', strFileName)
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dictRow = {'ID':lstRow[0], 'Title':lstRow[1], 'Artist':lstRow[2]}
            lstTbl.append(dictRow)
        objFile.close()
    elif strChoice == 'a':  
        # 2. Add dictionary to the 2-D list each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dictRow = {'ID':strID, 'Title':strTitle, 'Artist':strArtist}
        lstTbl.append(dictRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            strRow = ''
            for val in row.values(): # cycles through dictionary and gets values
                strRow += str(val) + ','
            strRow = strRow[:-1] # formatting
            print(strRow)
    elif strChoice == 'd':
        idDel = input("Which ID would you like to delete?: ")
        for row in lstTbl:
            if idDel in row.values():
                del lstTbl[lstTbl.index(row)] # deletes the index that contains user input
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

