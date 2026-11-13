#Name:Huxley Harmon
#Class: 6th Hour
#Assignment: HW15


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
x=1
for i in range(5,0,-1):
    print(i)
else:
    print("Hello World")

#2. Create a for loop that counts up and prints only even numbers between 1 and 30.

for h in range(1,31):
    if h % 2 == 0:
        print(h)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for k in range(1,31):

    if k % 3 == 0:
        continue
    else:
        print(k)


#4. Create a for loop that prints 5 different animals from a list.
animals= ["wolf"], ["kitten"], ["lion"], ["mouse"], ["monkey"]
for c in animals:
    print(c)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for text in input("peak")[::-1]:
    print(text)
#6. Create a list containing 10 integers of your choice and print the list.
int_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(int_list)
#7. Create two empty variables named evenNumbers and oddNumbers.
x= "evenNumbers"
y= "oddNumbers"
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.

#9. Create a variable that asks the user for an integer and an empty integer variable.

#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)