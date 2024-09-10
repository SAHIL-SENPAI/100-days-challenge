name = input("enter your name")
length = len(name)


print(type(name))
print(type(length))

#we cant concatinate str with int
#print("length of name is : " + length)

#solution

print("length of name is : " + str(length)) #type conversion
