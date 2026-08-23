shopping_list = []

# adds items
shopping_list.append("Milk") # adds at end
shopping_list.append("Bread")
shopping_list.append("Eggs")

print("Shopping List:", shopping_list)

# remove items
shopping_list.remove("Eggs")
print("After removing Eggs:", shopping_list)

# loop through list
print("Items to buy:")
for items in shopping_list:
    print("-", items)
