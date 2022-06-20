#[2021-07-19] Challenge #399 [Easy] Letter value sum

#Build lists

#lettersum = lambda s: sum([ord(c)-96 for c in s])  
#for s in ["", "a", "z", "cab", "excellent", "microspectrophotometries"]:
#    print(lettersum(s))

from itertools import count
from tabnanny import verbose


def lettersumfunc(theWord, verbose=False):
    theLettersum = 0
    x = list(theWord)
    for i in x:
        theLettersum += (ord(i)-96)
        if verbose:
            print(i)
            print(theLettersum)
    if verbose:
        print('the word \'' + theWord + '\' sums to: ' + str(theLettersum) + '\n')
    return(theLettersum)

def greaterThanFunc(dictionary, HowMuchGreaterThan, verbose=False):
    numGreaterThan319 = 0
    for each in dictionary:
        theLetterSum = int(lettersumfunc(each))
        if (theLetterSum >= int(HowMuchGreaterThan)):
            numGreaterThan319 += 1
            print('Bonus Item 1: ' + 'the word \'' + each + '\' sums to: ' + str(theLetterSum) + '\n')
    if verbose:
        print(numGreaterThan319)
    return(numGreaterThan319)

def oddSumFunc(dictionary, verbose=False):
    oddNumCounter = 0 
    for each in dictionary:
        theLetterSum = int(lettersumfunc(each))
        if ((theLetterSum % 2) != 0):
            oddNumCounter += 1
            if verbose:
                print (oddNumCounter)
        else:
            pass
            if verbose:
                print('the word \'' + each + '\' sums to: ' + str(theLetterSum))
    print('Bonus item 2: there are ' + str(oddNumCounter) + ' odd string sums in this particular dictionary' + '\n')
    return(oddNumCounter)

def mostCommonSum(dictionary, verbose=False):
    listofSums = [0]
    biggestQuantityofSums = 0
    count = 0
    for each in range(1, 400):
        listofSums.append(0)
    for each in dictionary:
        theLetterSum = int(lettersumfunc(each))
        listofSums[(theLetterSum+1)] += 1
    if verbose:
        print(listofSums)
    for each in listofSums:
        count += 1
        if each > biggestQuantityofSums:
            biggestQuantityofSums = each
            theSumWithTheMostOccurances = count
            if verbose:
                print(listofSums[count])
    print('Bonus Item 3: ' + str(biggestQuantityofSums) + ' is the most common sum in this particular dictionary with ' + str(theSumWithTheMostOccurances) + ' occurances' + '\n')
    return(biggestQuantityofSums)

def findTheWordPairings(dictionary, verbose=False):
    theDictTuple = []
    counter = 0
    for each in dictionary:
        theDictTuple.append((each, int(lettersumfunc(each))))
        if verbose:
            print(theDictTuple)
    for each in theDictTuple:
       # print(each)
        for something in theDictTuple:
      #      print(something)
            if ((each[1] == something[1]) and ((len(each[0]) == len(something[0])-11) or (len(each[0]) == (len(something[0]))+11))):
                    counter += 1
                    print('this should work... ' + each[0] + ' and ' + something[0] + 'with a total sum of ' + str(each[1]) + ' and ' + str(something[1]))
    print('did it work?')
    return()







import requests
dictionary = ((requests.get('https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt')).text).splitlines()

verbose_prints = False


#lettersumfunc('masspectromitor')

print(lettersumfunc('zyzzyva'.lower(),verbose_prints))
greaterThanFunc(dictionary, 319)
oddSumFunc(dictionary, False)
mostCommonSum(dictionary)
#findTheWordPairings(dictionary, False)
print('ThisIsATest')
