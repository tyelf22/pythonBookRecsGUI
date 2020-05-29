''' Tyson Elfors
5/29/20
CS-1410
Project 3 - Book Reccomendations
'''

"""I declare that the following source code was written solely by me.
I understand that copying any source code, in whole or in part, constitues cheating,
and that I will receive a zero on this project if I am found in violation of this policy."""

#module variables  
bookArr = []
readerObj = {}

readerArr = [] #temp var for converting to dict

masterDotProds = []

masterFriendList = []

#Read file into list and dict
with open('booklist.txt') as allBooks:
    for line in allBooks:
        stripped = line.strip('\n')
        splitLines = tuple(stripped.split(","))
        bookArr.append(splitLines)
with open('ratings.txt') as allRatings:
    for line in allRatings:
        stripped = line.strip('\n')
        readerArr.append(stripped)
    it = iter(readerArr)
    res_dct = dict(zip(it, it))
listOfStrsDict = dict((k, list(v.split(" "))) for k,v in res_dct.items())
removeSpacesDict = dict((k.lower(), list(filter(None, v))) for k,v in listOfStrsDict.items())
listIntDict = dict((k, [int(s) for s in v]) for k,v in removeSpacesDict.items())
readerObj = listIntDict


def addDotProd(arr1, arr2):
    '''Calculate the dot product given two arrays'''
    resList = []
    total = 0
    for i in range(0, len(arr1)):
        resList.append(arr1[i] * arr2[i])
    for i in resList:
        total += i
    return total  


def recommend(person, howMany=2):
    '''Produce the reccomended books given each friend'''
    howManyInt = int(howMany) #convert arg to an integer
    
    pers = person

    listOfFriendDots = []
    for friend in masterFriendList: #get each key from friendlist
        listOfFriendDots.append(readerObj.get(friend))


    zippedListOfFriends = []
    for items in zip(*listOfFriendDots[:howManyInt]): #zip all of the dot prods
        zippedListOfFriends.append(items)
        
        
    persDots = readerObj.get(pers)

    
    maxOfFriendDots = []
    for tup in zippedListOfFriends:
        maxOfFriendDots.append(max(tup)) #find the max number from each dot prod

    zippedTotal = list(zip(maxOfFriendDots, persDots))
    iterator = 1
    for tup in zippedTotal: #determine if book should be recommended
        if tup[0] >= 3 and tup[1] == 0:
            newVal = zippedTotal.index(tup)
            zippedTotal[newVal] = iterator
            iterator += 1

    iterate = 1
    listOfIndexes = []
    for tup in zippedTotal:
        if tup == iterate:
            listOfIndexes.append(zippedTotal.index(tup)) 
            iterate += 1

    listOfBooks = []
    print(f"Recommendations for {person} : ") #print the recommended books
    for i in listOfIndexes:
        listOfBooks.append(bookArr[i])
    print(listOfBooks)
    return '\n'.join(map(str, listOfBooks))
    


# def friends(arrOfDotProds, person, howMany):
def friends(person, howMany=2):
    '''Calculates the two best friends of a person'''
    global masterFriendList
    masterFriendList = []

    listOfReaderObj = list(readerObj.keys()) #Create a list of the  best friends
    howManyInt = int(howMany) #convert to int

    result = list(zip(masterDotProds, listOfReaderObj)) #zip prods to friend names
    newRes = list(filter(lambda x: x[1] != person, result)) #filter out the person name
    newRes.sort(key=lambda x: x[0]) #sort the results by the first value in dict

    newResList = newRes[-howManyInt:] #number of friends to retrieve

    for tup in newResList:
        masterFriendList.append(tup[1])
    print("{person}'s five best friends : ", masterFriendList)
    

    print("masterFriendList = ", masterFriendList)

    masterFriendList.sort()

    if len(masterFriendList) > 2:
        return '\n'.join(map(str, masterFriendList))
    else:   
        return ', '.join(map(str, masterFriendList)) 
    
#initialize person to find dot prod
def dotProd(person, howMany=2):
    '''Calculate the dot products of each person of a given person'''
    global masterDotProds
    masterDotProds = [] #reset list so func can be called multiple times

    initialValue = readerObj.get(person) #get the value for key of person

    for k,v in readerObj.items():
        res = addDotProd(initialValue, v) #call addDotProd to calculate the dot prods
        masterDotProds.append(res)

    return masterDotProds 

def report(howMany=2):
    '''Get the two best friends and recommendations for each user'''
    listOfReaders = list(readerObj.keys())
    listOfReaders.sort() #sort list of readers alphabetically

    result = ""
    for reader in listOfReaders:
        global masterDotProds #need to set global variables in order to reset on multiple function calls
        global masterFriendList
        masterDotProds = []
        masterFriendList = []
        dotProd(reader)
        result += f"\n{reader}: {friends(reader)}\n{recommend(reader)}\n" #format the result for report
    return result    
