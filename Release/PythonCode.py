#Import regex library
import re

#Description:
#   These functions are designed to be used with the solution the Python File is included with.
#   Read each function Description for further documentation.


#Description:
#	Reads file named "CS210_Project_Three_Input_File" from same directory as this Python File. Opens in read only mode.
#Example:
#	fileObject = ReadFile()
#Return:
#	Returns file object containing opened file in read only mode.


def ReadFile():
    #Call open() function to open specified file in read only mode.
    file = open("CS210_Project_Three_Input_File", "r")
    #Returns
    return file


#Description:
#	Creates dictionary object containing each grocery item in CS210_Project_Three_Input_File and the number of times they were purchased.
#    Takes no parameters, returns a dictionary object
#Example:
#	itemDict = BuildItemDict()
#Return:
#	Dictionary object with grocery items as keys, quantity as values.


def BuildItemDict():

    #Initialize empty dictionary object at the call of the function.
    itemDict = {}
    #Call ReadFile() function, assign file object return to file variable
    file = ReadFile()
    #Iterate over contents in file to generate dictionary
    for contents in file:
        #Regex to match for item names only; newline character (\n) is included when iterating over file, messes up formatting later
        #Match Object is returned from re.search() function, assigned to item variable
        item = re.search("[\w ]+", contents)
        #Reassign item to the .group() method of the re.search object, as this will contain the matched text of the regex
        item = item.group()
        #Evaluate if item already exists in dictionary
        if item not in itemDict.keys():
            #If is does not, create a new entry and assign value of new key to 1
            itemDict.update({item : 1})
        else:
            #If it does, get existing quantity of value
            quantity = itemDict.get(item)
            #Add 1 to quantity 
            quantity = quantity+ 1
            #Update dictionary with new quantity
            itemDict.update({item : quantity})
    #Return dictionary to function call
    return itemDict


#Description:
#	Using built dicrionary from BuildItemDict(), outputs a printed list of items purchased and their quantities. Takes no parameters, returns nothing.
#Example:
#	printItemsPurchased()
#Return:
#	Prints formatted dictionary to console.


def PrintItemsPurchased():
    #Call BuildItemDict() to create a dictionary of grocery items in the input file CS210_Project_Three_Input_File
    itemDict = BuildItemDict()
    #Print dictionary with prettified formatting
    print("Product Names and Number Purchased")
    print("-".center(34,'-'))
    for contents in itemDict:
        print(contents + ": " + str(itemDict[contents]))


#Description:
#	Using built dicrionary from BuildItemDict(), validates input to see if specified item exists.
#   String type is accepted as a parameter.
#Example:
#	quantityOfItem = GetSpecifiedItem("Peas")
#Return:
#	If Peas exists in the list, returns quantity of them to quantityOfItem variable, else -1.


def GetSpecifiedItem(itemInput):
    #Call BuildItemDict() to create a dictionary of grocery items in the input file CS210_Project_Three_Input_File
    itemDict = BuildItemDict()
    #Validate if input string matches a key in dictionary
    if itemInput in itemDict.keys():
        #Return value of key if input matches.
        return itemDict[itemInput]
    else:
        #Return -1 if no item is matched.
        return -1


#Description:
#    Call to create a file containing items from CS210_Project_Three_Input_File and their frequencies in integer format
#Example:
#	CreateFrequencyFile()
#Return:
#	A file called frequency.dat will be created in the same directory as this Python file


def CreateFrequencyFile():
    #Call BuildItemDict() to create a dictionary of grocery items in the input file CS210_Project_Three_Input_File
    itemDict = BuildItemDict()
    #Creat and open a file named frequency.dat in write mode
    freqFile = open('frequency.dat', 'w')
    #Iterate over dictionary and write key-value pairs into file with a space separating key and value and a new line for each pair
    for contents in itemDict:
        freqFile.write(contents + " " + str(itemDict[contents]) + "\n")
    #Close file stream
    freqFile.close()