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
