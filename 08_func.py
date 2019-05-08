#-*- coding:utf-8 -*-

'''
函数的使用
在这里我将定义一个求绝对值的函数做为示例
'''

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-4))

"""
如果你想定义一个什么都不做的函数
或者你想好了要写一个函数，但是没有相好里面的内容
可以像下面这样
pass 也可以用在其他语句里面，如 if
"""

def foo():
    pass

'''
上面那个求绝对值的函数，如果传入不恰当类型的参数时，就会报一个错误
我们可以在自己写函数的时候做一下判断
'''
# print(my_abs('ss'))
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print(my_abs2('x'))

'''
函数也可以返回多个值
'''

def calc(x, y):
    sum = x + y
    diff = x - y
    return sum, diff
print(calc(3, 2))
# 返回的是一个 tuple 不过我们可以用类似 es6 中的解构的形式来把值给变量
sum, diff = calc(4, 5)
print(sum, diff)