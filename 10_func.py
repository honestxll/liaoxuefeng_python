# 看一下高阶函数和一些函数的其它概念

'''
变量可以指向函数
以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：
'''
print(abs(-10))
f = abs
print(f(-10))

try:
    abs = 10
    print(abs(-10))
except Exception as e:
    print(e)

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)
print(add(10, -10, f))


'''
python 内建了 map 和 reduce 函数
其实和 js 的差不多
'''
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4])
print(r)
# 返回的 r 是一个 Iterator
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce
def add(x, y):
    return x + y
l = [1, 2, 3, 4, 5]
r = reduce(add, l)
print(r)

#Python内建的filter()函数用于过滤序列。
def is_odd(n):
    return n % 2 == 1
r = list(filter(is_odd, [1, 2, 3, 4, 5, 6]))
print(r)
print([x % 2 == 1 for x in [1, 2, 3, 4, 5, 6]])

#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()
r = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(r)

#Python内置的sorted()函数就可以对list进行排序：
l = [36, 5, -12, 9, -21]
r = sorted(l)
print(r)
#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
#因为之前我将 abs 变成了一个变量，所以这里，需要将这个变量清除掉
del abs
r = sorted(l, key=abs)
print(r)

'''
函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
'''
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f())

'''
闭包
注意到返回的函数在其定义内部引用了局部变量args
所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
所以，闭包用起来简单，实现起来可不容易
'''
# num1, num2 = [11, 12]
# print(num1, num2)
print(list(range(1, 4)))
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

'''
你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：全是9
原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())




# 匿名函数

'''
当我们在传入函数时，有些时候，不需要显式的定义函数，直接传入匿名函数更方便
在Python中，对匿名函数提供了有限支持
'''
L = [1,2,3,4,5,6,7]
r = list(map(lambda x: x*x, L))
print(r)

'''
通过对比，可以看出，匿名函数 lambda x: x*x 其实就是
def f(x):
    return x*x
用匿名函数有个好处，因为函数没有名字，所以不用担心函数名冲突
此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
'''
f = lambda x: x * x
r = list(map(f, L))
print(r)
# 取1到19的奇数
print(list(filter(lambda x: x%2 == 1, range(1, 20))))




# 装饰器

'''
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
'''
def now():
    import time
    r = time.strftime('%Y-%m-%d, %H:%I:%S', time.localtime(time.time()))
    print(r)
f = now
f()
#函数对象有一个__name__属性，可以拿到函数的名字：

print(now.__name__, f.__name__)

'''
现在，假设我们要增强now()函数的功能
比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper

@log
def now():
    print('2015-3-25')
now()

#把@log放到now()函数的定义处，相当于执行了语句：
#now = log(now)
#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper():
            print('%s %s():' % (text, func.__name__))
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()

'''
写一个装饰器用来计算函数的执行时间
这里以一个判断数字是否为质数的函数为例
我们想知道1-9999里，有多少数是质数
'''
# 质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数。
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
def prime_nums():
    for i in range(2, 10000):
        if is_prime(i):
            print(i)
# prime_nums()

# 以上就是基本的函数，下面我们将添加装饰器计算函数运行的时间
def display_time(func):
    def wrapper():
        import time
        t1 = time.time()
        func()
        t2 = time.time()
        print('函数执行了{:.4}s'.format(t2 - t1))
    return wrapper

@display_time
def show_prime():
    for i in range(1, 10000):
        if (is_prime(i)):
            print(i)
# show_prime()

# 现在我们想计算出质数的个数，所以我们可以把 show_prime 这个函数改一下
# 把函数统计的结果在装饰器中返回出来
def display_time(func):
    def wrapper():
        import time
        t1 = time.time()
        result = func()
        t2 = time.time()
        print('函数执行了{:.4}s'.format(t2 - t1))
        return result
    return wrapper

@display_time
def prime_count():
    count = 0
    for i in range(2, 10000):
        if is_prime(i):
            count = count + 1
    return count
# result = prime_count()
# print(result)

# 最后如果我们想在函数中传递参数，可以这样
def display_time(func):
    def wrapper(*args):
        import time
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print('函数执行了{:.4}s'.format(t2 - t1))
        return result
    return wrapper

@display_time
def prime_count(maxnum):
    count = 0
    for i in range(2, maxnum):
        if is_prime(i):
            count += 1
    return count
result = prime_count(10000)
print('2 到 9999 之间一共有 %d 个质数' % result)



'''
偏函数
把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
'''
import functools
int2 = functools.partial(int, base=2)
print(int2('100000'))