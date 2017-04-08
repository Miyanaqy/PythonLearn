def triangles():
    s,i = 1,1
    L1 = [1]
    while s < 10000:
        yield L1
        L2 = L1.copy()
        while i < s:
            L1[i] = L2[i - 1] + L2[i] 
            i += 1
        L1.append(1)
        i = 1
        s += 1
