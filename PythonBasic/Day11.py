"""
Python built-in functions  
Python标准内置函数使用
- 标准函数
- 迭代器函数
- 运算函数
"""

# help
#print(help())
#print(help(print))
#print(help('os'))


# format()
print(format(20,'0=20'))
print(format(521, '021'))
print(format('mrsoft','<20'))
print(format(123,'.1f'))

# repr()
s1 = "hello, \n world!"
print(repr(s1))
print(str(s1))

class Student:
    def __init__(self,name):
        self.name = name

s = Student('mrsoft')
print(repr(s))

# bool()
print(bool(0))
print(bool())
print(bool(list[1,2,3]))

# complex()
print(complex(1,2))
print(complex(1))
print(complex('1+2j'))

# sum
print(sum([1,2,3,4,5]))
print(sum(range(101)))
print(sum([1,2,3,4,5],10)) # 列表计算之后，再加10
print(sum([],1))

# range()
print(list(range(10)))
print(list(range(1,10)))
print(list(range(-10)))

# dict
d1 = dict(mr = "mrsoft", python = "python")
print(d1)

d2 = dict([('mr','mrsoft'),('python','python')])
print(d2)

#print(dict(3 = 'a', b = 'b', c = 'c'))

# bytes()
b = bytes([1,2,3])
print(b)
print(type(b))

print(bytes('hello','utf-8'))
print(bytes('hello','ascii'))
print(bytes(10))

# sorted()
c = ['a','b','c','d','e','A','B','*']
print(sorted(c))
print(sorted(c,reverse=True))
print(sorted(c, key=str.lower))

# zip
num = [1,2,3]
name = ['mrsoft','python','java']
print(list(zip(num,name)))
print(zip(num,name))
print(list(zip(num,name,range(3))))

for i in zip(num,name):
    print(i)
print(dict(zip(num,name)))
print(zip())

print(list(zip(num)))
print(list(zip(name)))

n1 = [1,2,3]
n2 = [4,5,6]
c = zip(n1,n2)
print(list(zip(*c)))

# next
s = iter('dfasfd')
print(next(s))
print(next(s),'x')

# filter
def odd(num):
    return num % 2 == 0

print(list(filter(odd,[1,2,3,4,5,6,7,8,9])))
print(filter(odd,[1,2,3,4,5,6,7,8,9]))

# map
num1 = [25105,29233,20320]
print(list(map(chr,num1)))

# dir()
print(dir([]))
list= [1,2,3]
print(dir(list))