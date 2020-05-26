# !usr/bin/python
# Filename:critAndmax.py


class Crit:

    # 递减前暴击
    beCrit = 0
    # 递减后暴击
    afCrit = 0
    # 最终暴击
    finalCrit = 0

    def __init__(self, critvalue):
        self.critvalue = critvalue
        # print(self.critvalue)

    # 计算递减前暴击
    def beforeCrit(self):
        if ( 0 < self.critvalue < 40):
            Crit.beCrit = self.critvalue
        elif ( 40 <= self.critvalue < 68):
            Crit.beCrit = (self.critvalue - 8)/0.8
        elif ( 68 <= self.critvalue < 86):
            Crit.beCrit = (self.critvalue - 23)/0.6
        elif ( 86 <= self.critvalue < 100):
            Crit.beCrit = (self.critvalue - 44)/0.4
        else:
            raise InputLimitException('critvalue', self.critvalue)
            # print('beforeCrit Value Error')
        # print('beforeCrit' + str(Crit.beCrit))

    # 计算递减后暴击
    def afterCrit(self):
        # print(str(Crit.finalCrit))
        if ( 0 < Crit.finalCrit < 40):
            Crit.afCrit = Crit.finalCrit
        elif ( 40 <= Crit.finalCrit < 75):
            Crit.afCrit = Crit.finalCrit * 0.8 + 8
        elif ( 75 <= Crit.finalCrit < 105):
            Crit.afCrit = Crit.finalCrit * 0.6 + 23
        elif ( 105 <= Crit.finalCrit < 140):
            Crit.afCrit = Crit.finalCrit * 0.4 + 44
        else:
            raise InputLimitException('finalCrit', Crit.finalCrit)
            # print('afterCrit Value Error')
        # print('afterCrit' + str(Crit.afCrit))

    # 加算类buff
    def plusBuff(self,plusValue):
        Crit.finalCrit = Crit.beCrit + plusValue
        # print('plusBuff' + str(Crit.finalCrit))

    # 乘算类buff
    def multiplyBuff(self,multiplyValue):
        Crit.finalCrit = Crit.afCrit * multiplyValue
        # print('multiplyBuff' + str(Crit.finalCrit))


class Max:

    # 递减前极大
    beMax = 0
    # 递减后极大
    afMax = 0
    # 最终极大
    finalMax = 0

    def __init__(self, Maxvalue):
        self.Maxvalue = Maxvalue
        # print(self.Maxvalue)

    # 计算递减前极大
    def beforeMax(self):
        if ( 0 < self.Maxvalue < 40):
            Max.beMax = self.Maxvalue
        elif ( 40 <= self.Maxvalue < 70):
            Max.beMax = (self.Maxvalue - 10)/0.75
        elif ( 70 <= self.Maxvalue < 90):
            Max.beMax = (self.Maxvalue - 30)/0.5
        elif ( 90 <= self.Maxvalue < 100):
            Max.beMax = (self.Maxvalue - 60)/0.25
        else:
            raise InputLimitException('Maxvalue', self.Maxvalue)
            # print('beforeMax Value Error')
        # print('beforeMax' + str(Max.beMax))

    # 计算递减后极大
    def afterMax(self):
        # print(str(Max.finalMax))
        if ( 0 < Max.finalMax < 40):
            Max.afMax = Max.finalMax
        elif ( 40 <= Max.finalMax < 80):
            Max.afMax = Max.finalMax * 0.75 + 10
        elif ( 80 <= Max.finalMax < 120):
            Max.afMax = Max.finalMax * 0.5 + 30
        elif ( 120 <= Max.finalMax < 160):
            Max.afMax = Max.finalMax * 0.25 + 60
        else:
            raise InputLimitException('finalMax', Max.finalMax)
            # print('afterMax Value Error')
        # print('afterMax' + str(Max.afMax))

    # 加算类buff
    def plusBuff(self,plusValue):
        Max.finalMax = Max.beMax + plusValue
        # print('plusBuff' + str(Max.finalMax))

    # 乘算类buff
    def multiplyBuff(self,multiplyValue):
        Max.finalMax = Max.afMax * multiplyValue
        # print('multiplyBuff' + str(Max.finalMax))


class InputLimitException(Exception):
        def __init__(self, name, value):
            self.name = name
            self.value = str(value)
        def __str__(self):
            print("输入值不在指定范围内|" + self.name + ':' + self.value)


if __name__ == '__main__':

    a = Crit(86)
    a.beforeCrit()
    a.plusBuff(0)
    a.afterCrit()
    a.multiplyBuff(1.12)

    print("----------------------------------------------------------")

    b = Max(80.8)
    b.beforeMax()
    b.plusBuff(17.25)
    b.afterMax()
    b.multiplyBuff(1.12)