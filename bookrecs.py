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
    howManyInt = int(howMany)
    
    pers = person

    listOfFriendDots = []
    for friend in masterFriendList:
        listOfFriendDots.append(readerObj.get(friend))


    zippedListOfFriends = []
    for items in zip(*listOfFriendDots[:howManyInt]):
        zippedListOfFriends.append(items)
        
        
    persDots = readerObj.get(pers)

    
    maxOfFriendDots = []
    for tup in zippedListOfFriends:
        maxOfFriendDots.append(max(tup)) 

    zippedTotal = list(zip(maxOfFriendDots, persDots))
    iterator = 1
    for tup in zippedTotal:
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

    listOfReaderObj = list(readerObj.keys()) #Create a list of the two best friends
    howManyInt = int(howMany)
    print("second master of dot prods", masterDotProds)

    result = list(zip(masterDotProds, listOfReaderObj))
    newRes = list(filter(lambda x: x[1] != person, result))
    newRes.sort(key=lambda x: x[0])

    newResList = newRes[-howManyInt:]

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
    masterDotProds = []

    initialValue = readerObj.get(person)

    for k,v in readerObj.items():
        res = addDotProd(initialValue, v)
        masterDotProds.append(res)

    return masterDotProds

def report(howMany=2):
    listOfReaders = list(readerObj.keys())
    listOfReaders.sort()

    result = ""
    for reader in listOfReaders:
        global masterDotProds
        global masterFriendList
        masterDotProds = []
        masterFriendList = []
        dotProd(reader)
        result += f"\n{reader}: {friends(reader)}\n{recommend(reader)}\n"
    return result    
