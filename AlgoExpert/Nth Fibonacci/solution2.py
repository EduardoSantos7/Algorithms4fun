def getNthFib(n, mem={1: 0, 2: 1}):
    if n in mem:
        return mem[n]
    else:
        mem[n] = getNthFib(n - 1, mem) + getNthFib(n - 2, mem)
        return mem[n]
