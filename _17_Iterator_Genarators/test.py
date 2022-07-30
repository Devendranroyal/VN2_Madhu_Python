def pow_two_gen(max=0):
    n = 0
    while n < max:
        yield 2 ** n  # value will be produced lazily   1 2 4 8 16 32 64 128 256 512
        n += 1

for each in pow_two_gen(10):
    print(each)