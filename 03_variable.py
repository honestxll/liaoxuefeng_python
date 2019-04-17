#-*- coding: utf-8 -*-
#字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等

introduce = 'I\'m "Tom"'
print(introduce)

# 多行文字你可以像这样来写
print("""
你好
某生人
""")

# 也可以直接加上换行符
print("你好\n某生人\t: D")


# 布尔值和我们常用的其它语言不太一样，首字母需要大写，其它小写
# 这里我会结合运算符一起演示 
# and or not 相当于 php　中的 && || !

print(True and False)
print(False or True)
print(not True)
print(not 1 > 2)
# 大写表示常量，但实际长仍然是变量，这只是一个习惯性的用法
PI = 3.1415936
print(PI)
print(10 / 3)
print(9 / 3) # 3.0
print(10 // 3) # 取整
print(10 % 3) # 取余
