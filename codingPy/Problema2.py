'''
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
the first element will represent a list of comma-separated numbers sorted in ascending order,
the second element will represent a second list of comma-separated numbers (also sorted).
Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr
in sorted order. If there is no intersection, return the string false.
'''
def FindIntersection(strArr):
    arr1 = strArr[0]
    arr2 = strArr[1]
    resultado = []
    numros_str1 = arr1.split(",")
    numros_str2 = arr2.split(",")
    numros_int1 = list(map(int,numros_str1))
    numros_int2 = list(map(int,numros_str2))
    for i in numros_int1:
        for j in numros_int2:
            if i == j :
                resultado.append(i)
    str_resultado = str(resultado)
    x = str_resultado.replace('[','')
    y = x.replace(']','')
    z = y.replace(' ','')
    if z == "":
        return False
    else:
        return z
    


print(FindIntersection(["1, 2, 3, 4, 5", "6, 7, 8, 9, 10"]))