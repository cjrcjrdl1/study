# 클래스 예제2
# (1,2) + (2,3) = (3,5)
# (3,5) * 10 = (30,50)
# Max((30,50)) = 50

# 여러개의 인자를 받을 때에는 *을 사용 (튜플형식)

class Vector():
    def __init__(self, *args):
        '''
        Example of making -> v = Vector(3, 5)
        '''
        # 만약 args값에 아무것도 안들어오면 (0,0)으로 초기화
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Return the vector informations'''
        return 'Vector -> (%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, m):
        return Vector(self._x * m, self._y * m)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(1,2)
v2 = Vector(44,55)
v3 = Vector()

# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v3) # (0,0) 초기화
print(v1 * 10)
print(v2 * 10)
print(bool(v1))
print(bool(v2))
print(bool(v3))
