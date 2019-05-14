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

'''
可以变参数
也就是说传说的参数个数是可变的
可以是1个、2个到任意个，还可以是0个
'''

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(calc2(12, 2 ,3))

'''
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('honest', 25, sex = 1, job = 'Engineer')

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person2(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)
person2('Tom', 3, city = 'nanjing', job = 'nurse')
# 但是如果函数中定义了一个可变参数，后面跟着的命名关键字就不需要再一个特殊分隔符*了
def person3(name, age, *args, city, job):
     print('name:', name, 'age:', age, 'args:', args, 'city:', city, 'job:', job)
person3('Jack', 2, 3, 4, 5, city = 'hefei', job = 'chef')

def test(name, age):
    print('name:', name, 'age:', age)
d = { 'age': 23, 'name': 'sss' }
test(**d)

'''
递归函数，在函数的内部，可以调用自身
举个例子，我们要计算 n 的阶乘，n! = 1 x 2 x 3 x ... x n
'''
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(3))
