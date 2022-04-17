# 객체 지향 프로그래밍(OOP)의 장점 : 코드 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트 등

# 규모가 큰 프로젝트는 함수 중심이고 데이터가 방대하여 복잡함

# 클래스 중심은 데이터 중심이고 객체로 관리함

# 일반적인 코딩

# 보디빌더1
bodybuilder_1 = 'Kim'
bodybuilder_qual_1 = [
    {'body': 'good'},
    {'power': 400},
    {'income': 3000}
]

# 보디빌더2
bodybuilder_2 = 'Hwang'
bodybuilder_qual_2 = [
    {'body': 'awesome'},
    {'power': 500},
    {'income': 10000}
]

# 보디빌더3
bodybuilder_3 = 'Min'
bodybuilder_qual_3 = [
    {'body': 'average'},
    {'power': 300},
    {'income': 2000}
]

# 리스트 구조
# 리스트 구조는 관리가 불편
# 인덱스 접근 시 실수 가능성이 있고 삭제 또한 불편
bodybuilder_name_list = ['Kim', 'Hwang', 'Min']
bodybuilder_qual_list = [
    {'body': 'good', 'power': 400, 'income': 3000},
    {'body': 'awesome', 'power': 500, 'income': 10000},
    {'body': 'average', 'power': 300, 'income': 2000}
]

del bodybuilder_name_list[0]
del bodybuilder_qual_list[0]

print(bodybuilder_name_list)
print(bodybuilder_qual_list)

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

bodybuilder_dicts = [
    {'bodybuilder': 'Kim', 'bodybuilder_qual':{'body': 'good', 'power': 400, 'income': 3000}},
    {'bodybuilder': 'Kim', 'bodybuilder_qual':{'body': 'awesome', 'power': 500, 'income': 10000}},
    {'bodybuilder': 'Kim', 'bodybuilder_qual':{'body': 'average', 'power': 300, 'income': 2000}}
]

del bodybuilder_dicts[0]
print(bodybuilder_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성이 증가, 코드 반복 최소화, 메소드 활용

class Bodybuilder():
    def __init__(self, name, qual):
        self._name = name
        self._qual = qual

    def __str__(self):
        return 'str : {} - {}'.format(self._name, self._qual)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._qual)

    def __reduce__(self):
        pass

bodybuilder1 = Bodybuilder('Kim', {'body': 'good', 'power': 400, 'income': 3000})
bodybuilder2 = Bodybuilder('Hwang', {'body': 'awesome', 'power': 500, 'income': 10000})
bodybuilder3 = Bodybuilder('Min', {'body': 'average', 'power': 300, 'income': 2000})

print(bodybuilder1) # __str__ 호출이 된다.
print(bodybuilder2)
print(bodybuilder3)

print(dir(bodybuilder1))

print()
print()

bodybuilder_list = []

bodybuilder_list.append(bodybuilder1)
bodybuilder_list.append(bodybuilder2)
bodybuilder_list.append(bodybuilder3)

print(bodybuilder_list) # __repr__ 호출이 된다.

print()
print()

# 반복(__str__ 사용)
for a in bodybuilder_list:
    print(a)
    # print(repr(a))