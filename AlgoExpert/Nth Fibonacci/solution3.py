def getNthFib(n):
    mem = [0, 1]
    if n < 3:
        return mem[n - 1]
    for x in range(3, n + 1):
        new_val = mem[0] + mem[1]
        mem[0] = mem[1]
        mem[1] = new_val
    return mem[1]