def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

a = sum_many(1,2,3,4,5)
print(a)

def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3,4)
print(result)

sum, mul = sum_and_mul(3,4)
print(sum, mul)
print(sum)
print(mul)

def say_myself(name, man=True, old=26):
    print("나의 이름은 %s입니다." %name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", False, 15)


#a042 = input("input Test, 아무거나 입력해주세요!!")
#print(a042)

for i in range(0,10):
    print(i, end=' ')

file = open("newFile.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    file.write(data)
file.close()


f= open("newFile.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f= open("newFile.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


f = open("newFile.txt", 'r')
data = f.read()
print(data)
f.close()

file = open("newFile.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" %i
    file.write(data)
file.close()