"""
文件异常和标准库初探
- 读取文件的全部内容
- 标准库使用
- base64, collections,hashlib,random,ospath,heapq,iter
"""

## 读取文件内容
from pathlib import Path
#path = Path('test.txt')
#contents = path.read_text(encoding='utf-8')
#print(contents)


## Base64标准库
import base64
content = 'Man is distinguished, not only by his reason, but by this singular ' \
'passion from other animals, which is a lust of the mind, that by a perseverance' \
' of delight in the continued and indefatigable generation of knowledge, exceeds ' \
'the short vehemence of any carnal pleasure.'

print(base64.b64encode(content.encode()))

## Collections模块
from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]

counter = Counter(words)
for elem, count in counter.most_common(3):
    print(elem, count)

## hashlib
import hashlib
print(hashlib.md5('123456'.encode()).hexdigest())

# hasher = hashlib.md5()
# with open('Python-3.7.1.tar.xz','rb') as file:
#     data = file.read(512)
#     while data:
#         hasher.update(data)
#         data = file.read(512)

# print(hasher.hexdigest())

## heapq模块
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
print(heapq.nlargest(3, list1))


## itertools迭代器
import itertools

for value in itertools.permutations('ABCD'):
    print(value)

for value in itertools.combinations('ABCDE', 2):
    print(value)

for value in itertools.product('ABCD','123'):
    print(value)

it = itertools.cycle(('A', 'B', 'C'))
print(next(it))
print(next(it))
print(next(it))
print(next(it))