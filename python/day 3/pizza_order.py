print("welcome to the pizza dilivary!")
size = input("enter the size of pizza you want --> S - small , M - medium , L - large\n")
add_pep = input("add peporani ? --> Y-yes , N-no\n")
add_cheez = input("add extra cheez ? --> Y-yes , N-no\n")


bill = 0
if size == "S" or size == "small":
    bill = 15
elif size =="M" or size == "medium":
    bill = 20
elif size =="L" or size == "large" :
    bill = 25
else:
    print(" ERROR you have typed the wrong input")

if add_pep == "yes":
    if size == "S" or size == "small":
        bill+=2
    else :
        bill += 3

if add_cheez == "yes":
    bill+=1

print(f"your final bill is : ${bill}")