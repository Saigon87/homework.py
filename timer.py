import time

a = int(input())
for a in reversed(range(a)):
    time.sleep(1)
    print(a)

print('Бум!')
