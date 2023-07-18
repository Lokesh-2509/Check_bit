def is_bth_bit_set(A, B):
    mask = 1 << B
    if A & mask:
        return 1
    else:
        return 0
A = 5
B = 2
result = is_bth_bit_set(A, B)
print(result)
