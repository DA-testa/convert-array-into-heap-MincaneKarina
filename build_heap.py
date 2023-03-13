# python3


def build_heap(data):

    
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    a = 0
    for i in range(0,len(data)-1):
        if data[i] < data[i+1]:
            a = a + 1
    if a != len(data)-1:
        
        n=int(len(data))
        if len(data) % 2 !=0:
            rightChild = data[-1]
            #print(rightChild)
            leftChild = data[data.index(rightChild) - 1]
            #print(leftChild)
            parent = data[data.index(leftChild)//2]
            firstParentindex = data.index(parent)
            #print(parent)
            for i in range (n-2, -2, -1):
                if leftChild<rightChild:
                    child = leftChild
                else: child = rightChild
                if  child < parent:
                    index1 = data.index(child)
                    index2 = data.index(parent)
                    #i[b], i[a] = i[a], i[b]
                    swaps.append([index2, index1])
                    data[index2], data[index1] = data[index1], data[index2]
                    #print(data)
                    parent = data[index2]
                    #print(parent)

                if data.index(parent) == 0:
                    parent = data[firstParentindex]
                    #print(parent)
                    leftChild = data[data.index(parent)*2 +1]
                    rightChild = data[data.index(parent)*2 +2]
                else:
                    parent = data[data.index(parent) -1]
                    leftChild = data[data.index(parent)*2 +1]
                    rightChild = data[data.index(parent)*2 +2]


                
    return swaps
#parent i/2
#leftChild 2i
#rightChild 2i+1
    
def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    
    text = input()
    if "I" in text:
    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in text:
        filename = input()
        with open ("./" + filename, mode="r") as file:
            n = file.readline()
            data = file.readline()
            data = list(map(int, data.split()))
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
