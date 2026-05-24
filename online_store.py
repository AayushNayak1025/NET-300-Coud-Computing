purchase = float(input("Enter total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ").lower()

discount = 0


if purchase < 1000:
    discount = 0

elif purchase <= 4999:
    discount = 5

elif purchase <= 14999:
    discount = 10

else:
    discount = 20


main_discount_amount = purchase * discount / 100


discounted_amount = purchase - main_discount_amount


loyalty_discount_amount = 0

if member == "yes":
    loyalty_discount_amount = discounted_amount * 5 / 100
    discounted_amount -= loyalty_discount_amount


total_discount = main_discount_amount + loyalty_discount_amount

print("\n__________BILL SUMMARY__________")
print("Original Amount: NPR", purchase)
print("Main Discount:", discount, "%")
print("Main Discount Amount: NPR", round(main_discount_amount, 2))

if member == "yes":
    print("Loyalty Member Discount: 5%")
    print("Loyalty Discount Amount: NPR", round(loyalty_discount_amount, 2))

print("Total Discount Received: NPR", round(total_discount, 2))
print("Final Payable Amount: NPR", round(discounted_amount, 2))