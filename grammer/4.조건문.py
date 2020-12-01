print("\n*************************************ex1*************************************")
# [ 비교연산자 ]
# x < y	x가 y보다 작다
# x > y	x가 y보다 크다
# x == y	x와 y가 같다
# x != y	x와 y가 같지 않다
# x >= y	x가 y보다 크거나 같다
# x <= y	x가 y보다 작거나 같다

# [if ~ else 조건문]
a=1
b=2

if a==b:
 print("같다.")
else:
 print("다르다")

# 만약에 a 와 b 의 값이 같다면 "print("같다.")" 를 실행하고 a 와 b 가 같지 않다면 "print("다르다.")" 를 실행시켜라
# 즉, if 조건에 따라서 실행 위치가 결정이 된다. 실행문은 들여쓰기를 해야 에러가 발생하지 않는다.
# else 문이 없다면 if 문까지만 실행하고 만다. 즉 없어도 된다는 거다.








print("\n*************************************ex2*************************************")
# [ if ~ elif ~ else 조건문 ]
a=1
b=2

if a>b:
 print("a가 크다")
elif a<b:
 print("b가 크다")
else:
 print("a와 b는 같다.")

# 조건문을 여러가지로 사용하고 싶다면 elif 를 사용하여 조건을 추가하면 된다. if 와 elif 모두 만족하지 않느다면 else 를 실행 시킨다.







print("\n*************************************ex3*************************************")
#[ bool 자료형 ]

# True : 참
a=True

# False : 거짓
b=False

# and , or , not 연산자
   # x or y: x와 y 둘중에 하나만 참이어도 참
   # x and y:	x와 y 모두 참이어야 참
   # not x	: x가 거짓이면 참이다


print("True and False:", a and b)
print("True or False:", a or b)
print("True and True:", a and a)
print("True or True:", a or a)
print("False and False:", b and b)
print("False or False:", b or b)
print("not True:", not a)
print("not False:", not b)






print("\n*************************************ex4*************************************")
# 컴퓨터에서 1은 True, 0은 False로 해석 가능
a=1
b=0
print("1 and 0:", a and b)
print("1 or 0:", a or b)
print("1 and 1:", a and a)
print("1 or 1:", a or a)
print("0 and 0:", b and b)
print("0 or 0:", b or b)
print("not 1:", not a)
print("not 0:", not b)
