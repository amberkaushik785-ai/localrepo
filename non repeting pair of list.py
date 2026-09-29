L = [1, 2, 3, 4, 5]

for i in range(0, len(L)):
    for j in range(i+1, len(L)):
        print("{},{}".format(L[i], L[j]))
        
