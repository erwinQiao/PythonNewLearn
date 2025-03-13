"""
用户输入和while循环
1. input使用
2. 求模运算
3. while循环
4. break and continue
5. while在列表字典中循环

"""
# 求模运算
print(4%3)
print(5%3)
print(7%3)

# while循环
current_numer = 1
while current_numer <=5:
    print(current_numer)
    current_numer += 1

## 退出值设定
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message!= 'quit':
    message = input(prompt)
    print(message)

## 使用标志 flag
prompt = "\nTell me something, and I will repeat it back to you: "
prompt+="\n Enter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

## 使用break退出循环
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

## 在循环中使用continue
current_numer = 0
while current_numer < 10:
    current_numer += 1
    if current_numer % 2 ==0:
        continue
    print(current_numer)

# while在列表中循环
unconfirmed_users = ['alice','brain','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

## 删除特定值的所有元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

for  pet in pets:
    if pet == 'cat':
        pets.remove('cat')
print(pets)

## while字典
responses = {}

polling_active = True
while polling_active:
	name = input('\n Please input your name: ')
	response = input(" which would you like to climb someday:")

	responses[name] = response

	repeat = input("Would you like to let another respond? (yes)/no")
	if repeat == 'no':
		polling_active= False

print("\n----Ploo Results----")
for name, response in responses.item():
	print(f"{name} you like to climb {response}")

## for 循环
for i in range(1,10):
    result +=i
print(result)

for i in range(1,10,2):
    print(i, end= ' ')

## while循环
print("jinbuzhdao")
number = 0      
none =True
while none:
	number += 1
	if number %2 ==0 and number %5 ==3 and number %7 ==2:
		print("dadui l ")
		none = False

## 嵌套循环
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}")

while True:
    for i in range(1,10):
        for j in range(1,10):
            print(f"{i}*{j}={i*j}")
            break