# Special Method(Magic Method)란?
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# 파이썬의 핵심 -> Sequence(시퀀스), Iterator(반복), Functions(함수), Class(클래스)

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 100

print(n + 100, n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제
class Bodybuilder:
    def __init__(self, name, income):
        self._name = name
        self._income = income

    def __str__(self):
        return 'Bodybuilder Info : {}, {}'.format(self._name, self._income)

    def __add__(self, x):
        print('Called : __add__')
        return self._income + x._income

    def __sub__(self, x):
        print('Called : __sub__')
        return self._income - x._income

    def __le__(self, x):
        print('Called : __le__')
        if self._income <= x._income:
            return True
        else:
            return False

    def __ge__(self, x):
        print('Called : __ge__')
        if self._income >= x._income:
            return True
        else:
            return False


# 인스턴스 생성
b1 = Bodybuilder('Kim', 3000)
b2 = Bodybuilder('Hwang', 10000)

print(b1 + b2)

# 일반적인 계산
print(b1._income + b2._income)

# special method(magic method)
print(b1 <= b2)
print(b1 >= b2)
print(b1 - b2)
print(b2 - b1)
print(b1)
print(b2)