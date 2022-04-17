class Bodybuilder():
    """
    Bodybuilder class
    Author : Min
    Date : 2022-04-17
    """

    # 클래스 변수(모든 인스턴스가 공유)
    bodybuilder_count = 0

    def __init__(self, name, qual):
        self._name = name
        # self.bodybuilder_count = 10
        self._qual = qual
        Bodybuilder.bodybuilder_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._name, self._qual)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._qual)

    def __del__(self):
        Bodybuilder.bodybuilder_count -= 1

    def detail_info(self):
        print('Now ID value :  {}'.format(id(self)))
        print('Bodybuilder Strength Detail Info : {} {}'. format(self._name, self._qual.get('power')))

# self 의미
bodybuilder1 = Bodybuilder('Kim', {'body': 'good', 'power': 400, 'income': 3000})
bodybuilder2 = Bodybuilder('Hwang', {'body': 'awesome', 'power': 500, 'income': 10000})
bodybuilder3 = Bodybuilder('Min', {'body': 'average', 'power': 300, 'income': 2000})

# ID 값 확인
print(id(bodybuilder1))
print(id(bodybuilder2))
print(id(bodybuilder3))

print(bodybuilder1._name == bodybuilder2._name)
print(bodybuilder1 is bodybuilder2)

# dir & __dict__ 값 확인
print(dir(bodybuilder1))
print(dir(bodybuilder2))

print()
print()

print(bodybuilder1.__dict__)
print(bodybuilder2.__dict__)

# Doctring
print(Bodybuilder.__doc__)
print()

# 실행
bodybuilder1.detail_info()
Bodybuilder.detail_info(bodybuilder1)
bodybuilder2.detail_info()
Bodybuilder.detail_info(bodybuilder2)
bodybuilder3.detail_info()
Bodybuilder.detail_info(bodybuilder3)

# 에러 발생
# Bodybuilder.detail_info()

print()
print()

# 비교
print(bodybuilder1.__class__, bodybuilder2.__class__, bodybuilder3.__class__)
print(id(bodybuilder1.__class__), id(bodybuilder2.__class__), id(bodybuilder3.__class__))

# 공유 확인
print(bodybuilder1.bodybuilder_count)
print(bodybuilder2.bodybuilder_count)
print(bodybuilder3.bodybuilder_count)
print(bodybuilder1.__dict__)
print(bodybuilder2.__dict__)
print(bodybuilder3.__dict__)
print(dir(bodybuilder1))

# 접근
print(bodybuilder1.bodybuilder_count)
print(Bodybuilder.bodybuilder_count)

# 인스턴스 하나 삭제 후 결과 확인
del bodybuilder2

print(bodybuilder1.bodybuilder_count)
print(Bodybuilder.bodybuilder_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 없을 시 상위(클래스 변수, 부모클래스 변수))