# Lab Exercise 3: Simple Calculator and Area Calculation

print("----- SIMPLE CALCULATOR -----")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

print("\n----- AREA CALCULATIONS -----")

# Area of Circle
r = float(input("Enter radius of circle: "))
circle_area = 3.14 * r * r
print("Area of Circle =", circle_area)

# Area of Rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
rectangle_area = length * breadth
print("Area of Rectangle =", rectangle_area)

# Area of Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle_area = 0.5 * base * height
print("Area of Triangle =", triangle_area)
