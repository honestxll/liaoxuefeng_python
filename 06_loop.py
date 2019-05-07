#-*- coding: utf-8 -*-

# 写一个 1-10 列表相加的循环做为示例

l = list(range(1, 11))

sum = 0
for i in l:
    sum += i

print(sum)

# 再用 while 写一个 0 - 99 相加
sum = 0
n = 0
while n < 100:
    sum += n
    n += 1
print(sum)