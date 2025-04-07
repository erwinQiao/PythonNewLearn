"""
文件和异常
- 读取文件的全部内容
"""

## 读取文件内容
from pathlib import Path
path = Path('test.txt')
contents = path.read_text(encoding='utf-8')
print(contents)

