def plus(a,b):
  if type(b) is int or type(b) is float:
    return a+b
  else:
    return None

print(plus(12,10.4))

def age_check(age):
  print(f"you are {age}")

age_check(18)