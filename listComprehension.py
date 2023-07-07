#Find all of the numbers from 1–1000 that are divisible by 8
div0 = [x for x in range(1,1001) if x % 8 == 0]

#Find all of the numbers from 1–1000 that have a 6 in them
div1 = [x for x in range(1,1001) if "6" in str(x)]

#Count the number of spaces in a string
string1 = "Practice Problems to Drill List Comprehension in Your Head."
div2 = len([x for x in string1 if x == " "])

#Remove all of the vowels in a string
div3 = "".join([x for x in string1 if x not in ["a","e","i","o","u"]])

#Find all of the words in a string that are less than 5 letters
palabra = string1.split()
div4 = [x for x in palabra if len(x) < 5]

#Use a dictionary comprehension to count the length of each word in a sentence
div5 = {word:len(word) for word in palabra}

#Use list comprehension to contruct a new list but add 6 to each item.
lst1=[44,54,64,74,104]
div6 = [str(x)+"6" for x in lst1]

#Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a 
#list of the names of vehicles with weight below 5000 kilograms. In the same list 
#comprehension make the key names all upper case.
dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
div7 = [x.upper() for x in dict if dict[x] < 5000]
print(div7)
