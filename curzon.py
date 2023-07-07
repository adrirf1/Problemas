def curzon(num):
    curzon = (2**num)+1
    curzon2 =  (2*num)+1
    if curzon % curzon2 == 0:
        return True
    else:
        return False
