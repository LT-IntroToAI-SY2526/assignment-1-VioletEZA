# Assignment 1: AI-Generated Python Problems
# Name: [Emma Adan]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[I'm learning Python basics as a Junior in highschool and Im taking an intro to ai class. 
I have some experience with java and html. Can you create 5 practice problems that cover:
 Variables and basic data types, Conditionals (if/elif/else), Loops (for and while), Functions, and Basic list operations 
 Make them progressively slightly more challenging. Make sure each problem has clear instructions and example inputs/outputs.]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Topic: Variables and basic data types]
[Task:Write a program that asks the user for their name, favorite snack, and how many of that snack they eat per week. Then print a sentence using those values. ]

name = str(input("Enter your name: "))
snack = str(input("Enter a snack: "))
amount = int(input("Enter how many times you eat it per week: "))
print(name + "eats " + str(amount) + " " + snack + " per week")
____
PROBLEM 2: [Topic: Conditionals]
[Task:Ask the user for their test score (0–100). Print a message based on the score:
90 and above: "A – Excellent!"
80–89: "B – Good job!"
70–79: "C – You passed."
60–69: "D – Try harder."
Below 60: "F – Better luck next time." ]

score = int(input("Enter your score: "))
if score >= 90:
    print("A Excellent!")
elif 80<=score and score<=89:
    print("B Good job!")
elif 70<=score and score<=79:
    print("C You passed")
elif 60<=score<=69:
    print("D Try harder")
else:
    print("F Better luck next time.")
____
PROBLEM 3: [Topic: While Loops]
[Task: Write a program that counts down from a number entered by the user to 0 using a while loop. Print each number on a new line.]

start = int(input("Enter a number: "))
while start > 0:
    print(start)
    start = start-1
____
PROBLEM 4: [Topic: For Loops]
[Task: Write a program that prints the multiplication table for a number from 1 to 10.]

userNum = int(input("Enter a number: "))
num = int(10)
for i in range(1,11):
    print(userNum * num)
    num = num - 1
____
PROBLEM 5: [Topic: Functions & List Operations]
[Task: Write a function called double_numbers(numbers) that takes a list of numbers and returns a new list where each number is doubled.]

doubled_list = [1,2,4,6]
def double_numbers(lst: list[int]): 
    doubled = []
    for num in lst:
        doubled.append(num * 2)
        print(doubled)
    return doubled
    
____
Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
name = str(input("Enter your name: "))
snack = str(input("Enter a snack: "))
amount = int(input("Enter how many times you eat it per week: "))
print(name + " eats " + str(amount) + " " + snack + " per week")


print("\nTesting Problem 2:")
score = int(input("Enter your score: "))
if score >= 90:
    print("A Excellent!")
elif 80<=score and score<=89:
    print("B Good job!")
elif 70<=score and score<=79:
    print("C You passed")
elif 60<=score<=69:
    print("D Try harder")
else:
    print("F Better luck next time.")


print("\nTesting Problem 3:")
start = int(input("Enter a number: "))
while start > 0:
    print(start)
    start = start-1


print("\nTesting Problem 4:")
userNum = int(input("Enter a number: "))
num = int(10)
for i in range(1,11):
    print(userNum * num)
    num = num - 1

print("\nTesting Problem 5:")
def double_numbers(lst: list[int]): 
    doubled = []
    for num in lst:
        doubled.append(num * 2)
    return doubled
list = [1,2,4]
result = double_numbers(list)

print("List:", list)
print("Doubled:", result)


assert double_numbers([1,2,4,6]) == ([2,4,8,12]), "double_numbers failed"


