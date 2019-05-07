#-*- coding: utf-8 -*-

# tuple 和 list 都是列表数据，不同的是 tuple 不可以更改

t = (1, 2)
l = [1, 2]
# 如果像下面这样操作会报错
# t[1] = 3
l.append(3)
print(t)
print(l)

# 如果要定义一个只有一个元素的 tuple，如果你这么定义会存在岐义,因为 () 可以表示 tuple
# 也可以表示数学公式的小括号，所以，只有一个元素的tuple定义的时候必须加一个逗号
t = (1,)
print(t)
a = (1)
print(a)