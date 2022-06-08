from tokenize import Number


BREAK_NUMBER = 20
i = 0

while i <= BREAK_NUMBER:
    if i % 2 == 0:
        print(i)
    else:
        pass
    i += 1


bool_flag = True
while bool_flag:
    val = input("8文字以上入力してください : ")
    
    if len(val) >= 8:
        break
    
print(val)

for i in range(0,10):
    if i % 3 == 0:
        continue
    else:
        print(i)
    