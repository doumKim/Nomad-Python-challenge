def plus(a,b):
  if type(b) is int or type(b) is float:
    return a+b
  else:
    return None

print(plus(12,10.4))

def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("You can't drink")
  else:
    print("Enjoy your drink")

age_check(18)