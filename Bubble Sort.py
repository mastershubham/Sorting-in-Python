def bubbleSort(List):
    n = len(List)
    isSwapped = False
    if n == 0:
        return L
    else:
        for i in range(1,n):
            for j in range(n-i):
                if List[j] > List[j+1]:
                    List[j],List[j+1] = List[j+1],List[j]
                    isSwapped = True
            if isSwapped == False:
                break
        return List

