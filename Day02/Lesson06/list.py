users = ['Tar','Kop','Tonmint','Not','Bank']

data = ['Tar', 23, True]

emptylist = []

print("Tar" in users)
print("Tar" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Tonmint'))

print(users[0:2])
print(users[0:])
print(users[-3:-1])

#len = ดูว่ามีกี่ตัว
print(len(data))
# print(len(users))

#เพิ่มค่า เข้าไป ในตัวแปรทีกำหนด
users.append('Who')
print(users)

users += ['Bank']
print(users)

users.extend(['Who3','Who4'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'BigBro')
print(users)

users[2:2] = ['BigSis', 'BigDaddy']
print(users)

users[1:3] = ['GG','Man', 'Girl','BB']
print(users)

users.remove('GG')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['BB']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=False)
# print(nums)
# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"B", True])
print(mylist)

# Tuples

mytuple = tuple(('DD', 22, True))

anothertuple = (1,3,2,5,9,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('B')
newtuple = tuple(newlist)
print(newtuple)

(one, tow, *hey) = anothertuple
print(one)
print(tow)
print(hey)

print(anothertuple.count(2))
