shopping_list = []

# adds items
shopping_list.append("Bags") # adds at end
shopping_list.append("Makeup")
shopping_list.append("jewellery")

print("Shopping List:", shopping_list)

# remove items
shopping_list.remove("Makeup")
print("After removing Makeup:", shopping_list)

# loop through list
print("Items to buy:")
for items in shopping_list:
    print("*", items)
