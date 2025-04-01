"""
Python built-in functions  
Python标准内置函数使用
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