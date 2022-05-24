def linearSearch(numberList,numberToSearch):
    for index,elememt in enumerate(numberList):
        if elememt==numberToSearch:
            return index
    return -1

def binarySearch(numberList,numberToSearch):
    leftIndex=0
    midIndex=0;
    rightIndex=len(numberList)-1
    while leftIndex<rightIndex:
        midIndex=(leftIndex+rightIndex)//2
        midNumber=numberList[midIndex]
        if numberToSearch==midNumber:
            return midIndex
        if midNumber<numberToSearch:
            leftIndex=midIndex+1
        else:
            rightIndex=midIndex-1
    return -1

if __name__=='__main__':
    numberList=[1,9,12,17,24,31,49,56,62]
    i=binarySearch(numberList,12)
    print(i)