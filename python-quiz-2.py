#Python Quiz 2
#Fork this repository to your own GitHub account and complete the following tasks in the pythonquiz2.py file.

#Submit a URL link to your completed repository ON GITHUB on Moodle. 

#variables: show an example of variable assignment and usage. Be sure to print the variable to demonstrate its value.
x = 10           # integer variable
name = "Alice"   # string variable
print("x =", x)
print("name =", name)
#data types: demonstrate at least three different data types (e.g., integer, string, list) and print their types using the type() function.
num = 42                  # integer
text = "Hello, world!"    # string
my_list = [1, 2, 3, 4]    # list

print("num is of type:", type(num))
print("text is of type:", type(text))
print("my_list is of type:", type(my_list))


#functions: define a simple function that takes an argument and returns a value. Call the function and print the result.
def square(number):
    """Returns the square of a number."""
    return number * number

result = square(5)
print("The square of 5 is:", result)



#classes: create a simple class with an __init__ method and one other method. Instantiate the class and call the method, printing the result.

class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.speak())




