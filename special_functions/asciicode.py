print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord('0'))
print(ord(" "))
print(ord("!"))
print(ord("#"))

print("-"*30)
print(chr(52))
print(chr(97))

for i in range(33,127):
    print(i,chr(i))

print("-"*30)

text="Python"
print([ord(i) for i in text])

print(chr(ord("A")+3))
