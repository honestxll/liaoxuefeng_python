#-*- coding: utf-8 -*-

# dist 就和 js 中的对象一样，有一个键值对

Person = {
    'name': 'honest',
    'age': 25,
    'gender': 1
}
Person['wife'] = 'xll'

for i in Person:
    print(i, Person[i])

# 如果我们通过一个字典中不存在的 key 取值的话，就会报错，所以我们可以通过 get 方法来取
print(Person.get('hobby'))

# set 和 dist 差不多，也是一组 key 的集合，但是它不存储 value
# 由于 key 不能重复，所以在 set 中，重复的元素会被自动过滤
s = set([1, 1, 2, 3, 4])
s.add(5)
s.remove(2)
print(s)
