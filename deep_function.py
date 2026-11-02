#1
def make_greeting(name, greeting="Hello", punct="!"):
    return greeting , name , punct
print(make_greeting("Dana"))
print(make_greeting("Avi", "Good morning"))
print(make_greeting("Noa", punct="?"))
#2
def average(*numbers):
    try:
           if len(numbers) == 0:
                raise ValueError
           return round(sum(numbers) / len(numbers))
    except ValueError:
         return "error: need at least one number"
print(average(15,30))
#3

