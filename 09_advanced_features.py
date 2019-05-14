#-*- codinig: utf-8 -*-
from collections import Iterable
from os import listdir

# 学习一下 python 的高级特性

# 切片
'''
取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
取前3个元素，应该怎么做？

笨办法：

>>> [L[0], L[1], L[2]]
['Michael', 'Sarah', 'Tracy']
'''

# 稍微好一点我们可以用循环来做
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

def slice(n):
    r = []
    for i in range(n):
        r.append(L[i])
    return r
print(slice(3))

'''
对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
对应上面的问题，取前3个元素，用一行代码就可以完成切片：
'''
print(L[0:3])
print(L[:3])
print(L[-5: -2])
print(L[:-2])
print(L[-4:])

L = list(range(100))
print(L[::5])
# 原样复制一个list，重新开辟一块内存空间
B = L[:]
# 以上切片操作对 tuple 也同样适用




#Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
Person = { 'name': 'honest', 'age': 21, 'gender': 1 }
for i in Person:
    print(i, Person[i])
# 如果你只想迭代 value，可以像下面这样
for i in Person.values():
    print(i)
# 如果要同时迭代key和value，可以像下面这样
print(Person.items())
for k, v in Person.items():
    print(k, v)


#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

'''
最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
'''
print(enumerate(['a', 'b', 'c']))
for k, v in enumerate(['a', 'b', 'c']):
    print(k, v)



# 列表生成式
'''
上面我们用 list 配合 range 生成了列表，但是他只能创建简单的列表
如果我们需要生成稍微复杂点的列表就不行了
但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
'''
def list_generate(start, end):
    L = []
    for x in range(start, end):
        L.append(x * x)
    return L
print(list_generate(1, 10))

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
print([x * x for x in range(1, 10)])
'''
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
'''
print([x * x for x in range(1, 10) if x % 2 == 0])
# 还可以使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
print(['文件' + d for d in listdir('./')])
print(listdir('./'))

#列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

#最后把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print([i.lower() for i in L])

'''
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
所以我们可以通过上面所学的知识来改进一下这个生成式
'''
L = ['Hello', 123, 'IBM', 456]
print([i.lower() for i in L if isinstance(i, str)])
