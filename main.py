# def plus(a,b):
#   if type(b) is int or type(b) is float:
#     return a+b
#   else:
#     return None

# print(plus(12,10.4))

# def age_check(age):
#   print(f"you are {age}")
#   if age < 18:
#     print("You can't drink")
#   elif age == 18:
#     print("You are new to this!")
#   elif age > 20 and age < 25:
#     print("You are still kind of young")
#   else:
#     print("Enjoy your drink")

# age_check(18)

# days = ('Mon','Tue','Wed','Thu','Fri')

# for day in days:
#   if day == "Wed":
#     break
#   else:
#     print(day)

# for letter in "nicolas":
#   print(letter)


# 모듈 전체 임포트
# import math

# print(math.ceil(1.2))

#모듈 부분 임포트
# from math import ceil, fsum

#모듈 기능 이름 변경
# from math import fsum as sexy_sum


# print(ceil(1.2))
# print(fsum([1,2,3,4,5,6,7]))

# calculator.py에서 만든 모듈 불러와서 사용하기
from calculator import plus, minus
print(plus(1,4))
print(minus(1,2))