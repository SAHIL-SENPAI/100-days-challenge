def calculate_love_score(name1,name2):
    name = (name1+name2).upper()
    check_list = ['T','R','U','E']
    count = 0
    
    for letter in name:
        for i in check_list:
            if letter == i:
                count += 1

    check_list = ['L','O','V','E']  

    ans = str(count)
    count = 0 

    for letter in name:
        for i in check_list:
            if letter == i:
                count += 1
    
    ans += str(count)
    print(ans + " love points")
   
                        


name = input("enter you name: ")
name_2 = input("enter your partner's name: ")
calculate_love_score(name,name_2)