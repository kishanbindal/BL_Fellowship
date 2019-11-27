def bubbleSort(a):

    for i in range(0,len(a)):

        for j in range(0,len(a)-1):

            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

