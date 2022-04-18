class Bodybuilder():
    """
    Bodybuilder class
    Author : Min
    Date : 2022-04-17
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    income_per_raise = 1.0

    def __init__(self, name, qual):
        self._name = name
        # self.bodybuilder_count = 10
        self._qual = qual

    def __str__(self):
        return 'str : {} - {}'.format(self._name, self._qual)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._name, self._qual)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Now ID value : {}'.format(id(self)))
        print('Bodybuilder Strength Detail Info : {} {}'. format(self._name, self._qual.get('income')))

    # Instance Method
    def get_income(self):
        return 'Before Bodybuilder income -> name : {}, income : {}'.format(self._name, self._qual.get('income'))

    # Instance Method -> 첫 인자값을 self를 받음
    def get_income_culc(self):
        return 'After Bodybuilder income -> name : {}, income : {}'.format(self._name, self._qual.get('income') * Bodybuilder.income_per_raise)

    # Class Method -> 클래스 값을 변경할 때 사용, 첫 인자값은 cls(클래스)를 받음
    @classmethod
    def raise_income(cls, per):
        if per <= 1:
            print('Please Enter at least 1')
            return
        cls.income_per_raise = per
        print('Succeed! income increased')

    # Static Method -> 아무 값도 전달받지 않음, 유연하게 만들고 싶을 때 사용
    @staticmethod
    def is_Hwang(inst):
        if inst._name == 'Hwang':
            return 'Yes! This is {}'.format(inst._name)
        return 'No.. This is not Hwnag'

# self 의미
bodybuilder1 = Bodybuilder('Kim', {'body': 'good', 'power': 400, 'income': 3000})
bodybuilder2 = Bodybuilder('Hwang', {'body': 'awesome', 'power': 500, 'income': 10000})
bodybuilder3 = Bodybuilder('Min', {'body': 'average', 'power': 300, 'income': 2000})

# 전체정보
bodybuilder1.detail_info()
bodybuilder2.detail_info()
bodybuilder3.detail_info()

# 수입정보(직접 접근)
print(bodybuilder1._qual.get('income'))
print(bodybuilder2._qual['income'])
print(bodybuilder3._qual['income'])

# 수입정보(인상 전)
print(bodybuilder1.get_income())
print(bodybuilder2.get_income())
print(bodybuilder3.get_income())

# 수입인상(클래스 메소드 미사용)
Bodybuilder.income_per_raise = 1.5

# 수입정보(인상 후)
print(bodybuilder1.get_income_culc())
print(bodybuilder2.get_income_culc())
print(bodybuilder3.get_income_culc())

# 수입인상(클래스 메소드 사용)
Bodybuilder.raise_income(2.0)

# 수입정보(인상 후)
print(bodybuilder1.get_income_culc())
print(bodybuilder2.get_income_culc())
print(bodybuilder3.get_income_culc())

# 인스턴스로 호출(스테이틱)
print(bodybuilder1.is_Hwang(bodybuilder1))
print(bodybuilder1.is_Hwang(bodybuilder2))
print(bodybuilder1.is_Hwang(bodybuilder3))

# 클래스로 호출(스테이틱)
print(Bodybuilder.is_Hwang(bodybuilder1))
print(Bodybuilder.is_Hwang(bodybuilder2))
print(Bodybuilder.is_Hwang(bodybuilder3))