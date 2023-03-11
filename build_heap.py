# python3


def build_heap(data):

    
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    a = 0
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            a = a+1
    if a == len(data)-1:
        swaps = 0
        
    else:
        
        n=int(len(data))
        if len(data) % 2 !=0:
            rightChild = data[-1]
            print(rightChild)
            leftChild = data[data.index(rightChild) - 1]
            print(leftChild)
            parent = data[data.index(leftChild)//2]
            print(parent)
            for i in range (n-2, -1, -1):
                if rightChild < parent:
                    index1 = data.index(rightChild)
                    index2 = data.index(parent)
                    #i[b], i[a] = i[a], i[b]
                    #swaps.append()
                    data[index2], data[index1] = data[index1], data[index2]
                    print(data)
                    leftChild = data[i]
                    #print(leftChild)
                    parent = data[data.index(leftChild)//2]
                   # print(parent)
                if leftChild < parent:
                    index1 = data.index(leftChild)
                    index2 = data.index(parent)
                    #i[b], i[a] = i[a], i[b]
                    #swaps.append()
                    data[index2], data[index1] = data[index1], data[index2]
                    print(data)
                rightChild = data[i+1]
                print(rightChild)
                #leftChild = data[i]
                parent=leftChild
                print(parent)
                #print(leftChild)
                #leftChild = data[data.index(parent)*2]
                parent = data[data.index(leftChild)//2]
                


        else:
            leftChild = data[-1]
                
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
    #print(len(swaps))
    #for i, j in swaps:
       # print(i, j)


if __name__ == "__main__":
    main()
