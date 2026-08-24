point1 = (2,3)
point2 = (5,7)

print("Point 1:", point1)
print("Point 2:", point2)

# calculate distance
# We calculate distance using the formula √((x2−x1)² + (y2−y1)²)
distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
print("Distance between points:", distance)
print(distance)