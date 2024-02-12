#This is a comment
#This is another comment


print("Hello World!")
print("Hello Class!")
print("Chewbacca is cool")
print(4.7)

C=10
c=11
print(C)
print(c)

my_user_name = "Is4460"
gpa = 4.0
print(my_user_name)
print(gpa)

name = "Alex"
print("My name is "+ name + " not Peter")
print(f"My name is {name} not Peter")

number = 1122 * 3344
print(str(number)[0:3])

def add_numbers(f,g):
  output= f+g
  return output

print(add_numbers(4,5))
print(add_numbers(g=6,f=7))


name2 = "James" #global
def say_hello():
  name2= "Herbert"#local
  return f"hello {name2}"
print(say_hello())