def temp_conv(c):
    return 9 / 5 * c + 32

f = temp_conv(0)

print(f)

c = 32

f = (lambda c : 9 / 5 * c + 32)(c)

print(f)
