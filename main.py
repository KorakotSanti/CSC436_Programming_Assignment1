import sys
from itertools import combinations

def getCombo(rLen:int, relation:list):
    """Return different combination of relations"""
    res = set()
    for i in range(rLen+1):
        for subset in combinations(relation,i):
            if len(subset)==0:
                continue
            else:
                res.add(subset)
    return sorted([list(item) for item in res],key=len)

def checkDependencies(functionalD:dict):
    """
    Return a new dictionary of dependencies 
    by expanding the functional depencies as
    much as they can
    """

    # dictionary to hold a new dependcies
    res = {}

    # get a list of all keys
    keylist = [key for key in functionalD]

    # traverse through the key list
    for i in range(len(keylist)):

        # get a new list of keys that are not including the current key looking at
        templist = keylist[:i] + keylist[i+1:]
        # get a temp new val for the key
        tempval = keylist[i]+functionalD[keylist[i]]
        
        # since order of dictionary is not sorted in any way
        # need to traverse through the depencies at least 3 times to make sure
        # we are getting all the values based on depencies
        for j in range(3):
            for key in templist:
                # this checks if our tempval is a key
                if all([i in tempval for i in key]) == True:
                    tempval+=functionalD[key]

        # sort the value and remove all duplicates
        res[keylist[i]]= "".join(sorted(set(tempval)))
    return res

def getMinkey(res:list):
    """
    This function returns a finalized list of candidate keys
    """

    result = []
    mini = len(res[0])

    # check for the minimal length of key that is not 1
    for i in range(1,len(res)):
        if len(res[i]) != 1 and len(res[i]) < mini:
            mini = len(res[i])
    
    # get all the possible results
    for item in res:
        if len(item) <= mini:
            result+=[item]

    # final check to make sure that the keys whose length is not 1
    # does not contain a key another candidate key with a length of
    fRes =[]
    for item in result:
        check = True
        for char in item:
            if char in result:
                check = False
                break
        if len(item) == 1:
            check = True
        
        if check:
            fRes += ["".join(sorted(item))]

    return fRes

def findCandidateKey(relation:list, functionalD:dict):
    """
    returns a list of candidate keys
    """

    # use the functional dependencies keys to find full functional definition
    rdep = checkDependencies(functionalD)

    # res list and sorting relation and turning it into a string
    res = []
    relation = "".join(sorted(relation))
    
    # traverse through all the key for the functional dependencies 
    # to find all possible candidate keys
    for item in rdep:

        # this check if one of the depend key equals to a relation right away
        # if so it is a candidate key
        if rdep[item] == relation:
            res += [item]
            continue

        # compare the key value and the relation to find the missing values
        missing = list(set(relation) - set(rdep[item]))

        # using the missing values create different combination of values
        combo = getCombo(len(missing), missing)

        # check all combo to see if it is a candidate key
        for c in combo:
            temp = "".join(sorted(item+"".join(c)))
            tempval = "".join(sorted(item+"".join(c)))
            for j in range(3):
                for key in functionalD:
                    if all([i in tempval for i in key]):
                        tempval+=functionalD[key]

            if "".join(sorted(set(tempval))) == relation:
                res+=[temp]
    # turn list into a set and back into a list
    # to remove all duplicates 
    res = list(set(res))
    return getMinkey(res)
    
if __name__ == "__main__":
    # get the length of the relation
    rLen = int(sys.argv[1])
    # get the relation as a list
    relation = sys.argv[2:2+rLen]

    print(relation)
    # get number of functional dependencies
    fLen = int(sys.argv[2+rLen])
    # get functional dependencies into as a list
    functional = sys.argv[3+rLen:]

    # put functional dependencies into hashmap
    funcD = {}

    for f in functional:
        x = f.split(',')
        funcD[x[0]] = x[1]
    for key in funcD:
        print(f"{key} => {funcD[key]}")
    
    candidateKey = findCandidateKey(relation,funcD)

    for key in candidateKey:
        print("The candidate keys are: \n -----------------------")
        print(key)
    print()
    