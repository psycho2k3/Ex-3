#------------------------------------------------------------------------------------
# Task 1: Function for Basic Real-Life Calculation

# TODO: Define a function called 'calculate_discount' that takes an item's price and discount percentage as parameters, 
#       and returns the discounted price.
#       Example: If the price is 100 and the discount is 20%, it should return 80.

def calculate_discount (price, discount_perc):
    discount_amount = price * (discount_perc/100)
    discount_price = price - discount_amount
    return discount_price

# TODO: Call the 'calculate_discount' function with a price of 250 and a discount of 15%, and print the result.

print(calculate_discount(250, 15))

#------------------------------------------------------------------------------------
# Task 2: Function with Multiple Parameters and Conditional Logic

# TODO: Define a function called 'shipping_cost' that takes the weight of a package and the destination 
#       (either "domestic" or "international") as parameters, and returns the shipping cost based on the following:
#       - For domestic shipping: $5 per kg.
#       - For international shipping: $15 per kg.

def shipping_cost(package_weight, destination):
    if destination == "Domestic":
        shipping_cost_per_kg = package_weight * 5
    elif destination == "International":
        shipping_cost_per_kg = package_weight * 15
    else:
        print("INVALID!!")
    return shipping_cost_per_kg
 
# TODO: Call the 'shipping_cost' function with a weight of 3kg and an "international" destination, and print the result.

print(shipping_cost(3, "International"))

#------------------------------------------------------------------------------------
# Task 3: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.

def check_attendance (students, absentees):
    return[student for student in students if student in absentees]

# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.

students_list = ["Alice", "Bob", "Charlie", "David"]
absentees_list = ["Bob", "David"]

absent = check_attendance(students_list, absentees_list)
print(absent)


#------------------------------------------------------------------------------------
# Task 4: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.

def calculate_avg_grade(grades):

# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.

# students_list = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

#------------------------------------------------------------------------------------
# Task 5: Function Returning a Function (Higher-Order Function)

# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.

# def operation_selector (str(+) or str(*)):
    
# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.

# TODO: Use 'operation_selector.