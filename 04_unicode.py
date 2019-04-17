#-*- coding: utf8 -*-
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：

print(ord('中'))
print(chr(66))

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

x = b'ABC'
print(x)

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))

# 要计算str包含多少个字符，可以用len()函数
print(len('你好世界'))

# 格式化
# 们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串
# 而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式
print('你好%s，你的分数是 %d 分' % ('陈实', 99))

# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
# 不过这种方式写起来比%要麻烦得多：
print('{0}的成绩是{1}分'.format('小明', 69))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))