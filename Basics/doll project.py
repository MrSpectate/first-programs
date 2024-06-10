doll_price = 100
money = int(input('How much money do you have? '))

if money >= doll_price:
    print("You can buy that doll.")
elif money >= 70:
    print("That's a cheaper doll.")
elif money >= 50:
    print("That's the cheapest doll.")
else:
    print("You cannot afford a doll.")
print("thank you for coming ")
print("God bless you")