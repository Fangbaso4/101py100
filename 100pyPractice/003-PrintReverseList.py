print("method one :")
l =  ['one', 'two', 'three']
l.reverse()
for i in l:
    print(i)

print("method two :")
l = ['one','two','three']
for i in l[::-1]:
    print(i)

print("method three :")
l = ['one','two','three']
for i in reversed(l):
    print(i)