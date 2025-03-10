"""
字典
1. 字典简单应用

"""

# 字典的定义
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

## 添加键值对
alien_0['x_posotion'] = 0
alien_0['y_position'] = 25
print(alien_0)

## 空字典开始
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

## 修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0)

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position:{alien_0['x_position']}")
print(alien_0)

## 删除键值对
del alien_0['speed']
print(alien_0)

## 由类似的对象组成的字典
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby'}
print(favorite_languages)

## get()方法
alien_0 = {'color':'green','speed':'slow'}
#print(alien_0['points'])

point_value = alien_0.get('points','No point value assigned.')
print(point_value)

personal_information = {
    'name':'erwinQiao',
    'first name':'erwin',
    'last name':'qiaow',
    'age':25,
    'city':'shanghai'
}

print(personal_information)

## 遍历字典
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}

for key, value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

favoreite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}
for name, language in favoreite_languages.items():
    print(f"{name.title()} is favorite language is {language.title()}.")
