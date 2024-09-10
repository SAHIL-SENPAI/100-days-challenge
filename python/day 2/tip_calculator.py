print("*******************************")
print("Welcome to the tip calculator !")
print("*******************************\n\n")

bill = float(input("what is the total bill   $"))
tip = int(input("how much tip would you like to give ? 10 , 12 or 15 ?"))
people = int(input("how many people to split the bill into ? "))

tip_in_percentage = tip / 100
total_tip = bill*tip_in_percentage
total_bill = bill+total_tip
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)

print(f"each person should pay : ${final_amount}")
