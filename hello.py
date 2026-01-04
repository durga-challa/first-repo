print("Hello,i am starting my coding journey")
name ="ammu"
age = 19
print(name,age)
age =input("Enter your age: ")
print("Hello durga",age) 
#operators in python
a = 10
b = 5
print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication   
print(a / b) # division
print(a % b) # modulus
print(a ** b) # exponentiation
print(a // b) # floor division
# comparison operators
print(a == b) # equal to
print(a != b) # not equal to
print(a > b)  # greater than
print(a < b)  # less than
print(a >= b) # greater than or equal to
print(a <= b) # less than or equal to
# logical operators
print(a > 5 and b < 10) # logical and
print(a > 5 or b > 10)  # logical or
print(not(a > 5))        # logical not
# assignment operators
c = a + b   # c = 15
c += a      # c = c + a
print(c)
c -= b      # c = c - b
print(c)
c *= a      # c = c * a
print(c)
c /= b      # c = c / b
print(c)
c %= a      # c = c % a
print(c)
c **= b     # c = c ** b
print(c)
c //= a     # c = c // a
print(c)
from calendar import month


month = input("Enter month name: ").lower()
if month == "january":
    print("it is january")
elif month == "february":
    print("it is february")
else:
    print("it is another month")
from posixpath import join


text = "python"
print(text[0])
print(text[-1])
print(text[1:3])
print(text[-5:-2])
text ="PYTHON"
print(text.lower())
print(text.upper())
print(text[3].lower())
print(text.replace("P","p"))
text ="durga"
print(text.replace("durga","DURGA BHAVANI"))
text ="hello python programming"
print(text.split())
words =["hello", "python", "programming"]
print("-".join(words))
text ="banana"
print(text.count("a"))

outside = "raining"
if outside == "raining":
    print("take an umbrella")
    if outside == "raining":
        print("wear a raincoat")
    else:
        print("wear normal clothes")
exercise = "regularly"
if(exercise == "regularly"):
    print("you will be fit")
else:
    print("start exercising")


habit = input("Enter your habit: ").lower()
if (habit == "dancing" or habit == "reading"):
    print("you can acheive your goals") 
else:
    print("develop reading habit")



