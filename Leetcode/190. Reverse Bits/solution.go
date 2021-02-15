func reverseBits(num uint32) uint32 {
    ans := uint32(0)
    power := uint32(31)

    for num != 0 {
        ans += (num & 1) << power
        num >>= 1
        power -= 1
    }

    return ans
}