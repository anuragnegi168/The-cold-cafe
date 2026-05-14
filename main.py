import menu
import disc
import tax
import service

print("========= Royal Palace Restaurant =========")
print("1. Pizza        ₹250")
print("2. Burger       ₹120")
print("3. Pasta        ₹180")
print("4. Cold Drink   ₹60")
print("5. Sandwich     ₹150")
print("6. Coffee       ₹90")
print("============================================")

Name = input("Hello Customer Please enter your name : ")
Type = input("Hello Customer what is your customer type (Regular/VIP): ").upper()

choice1 = int(input("Please input Ehat item do you want: "))
qty1 = int(input("Please input the quantity: "))

if choice1 == 1:
    total1 = menu.pizza(qty1)
elif choice1 == 2:
    total1 = menu.burger(qty1)
elif choice1 == 3:
    total1 = menu.pasta(qty1)
elif choice1 == 4:
    total1 = menu.cold_drink(qty1)
elif choice1 == 5:
    total1 = menu.sandwich(qty1)
elif choice1 == 6:
    total1 = menu.coffee(qty1)
else:
    print("wrong choice")


choice2 = int(input("Please input What item do you want: "))
qty2 = int(input("Please input the quantity: "))

if choice2 == 1:
    total2 = menu.pizza(qty2)
elif choice2 == 2:
    total2 = menu.burger(qty2)
elif choice2 == 3:
    total2 = menu.pasta(qty2)
elif choice2 == 4:
    total2 = menu.cold_drink(qty2)
elif choice2 == 5:
    total2 = menu.sandwich(qty2)
elif choice2 == 6:
    total2 = menu.cofee(qty2)
else:
    print("wrong choice")
    

choice3 = int(input("Please input Ehat item do you want: "))
qty3 = int(input("Please input the quantity: "))

if choice3 == 1:
    total3 = menu.pizza(qty3)
elif choice3 == 2:
    total3 = menu.burger(qty3)
elif choice3 == 3:
    total3 = menu.pasta(qty3)
elif choice3 == 4:
    total3 = menu.cold_drink(qty3)
elif choice3 == 5:
    total3 = menu.sandwich(qty3)
elif choice3 == 6:
    total3 = menu.cofee(qty3)
else:
    print("wrong choice")
