def xor(n):
    val = n % 4
    if val == 0:
        return n
    if val == 1:
        return 1
    if val == 2:
        return n + 1
    return 0

def solution(start, length):

    res = 0
    st = start - 1
    
    for i in range(length):
        sp = st + length - i
        res ^= xor(st) ^ xor(sp)
        st = sp + i

    return res

