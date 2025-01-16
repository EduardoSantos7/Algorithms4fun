class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        address = []
        addresses = []
        self._rec(s, 0, address, addresses)
        return addresses

    def _rec(self, s, i, address, addresses):
        if len(address) == 4:
            if i == len(s):
                addresses.append('.'.join(address))
        else:
            for j in range(i+1, i+4):
                next_int = s[i:j]
                if j <= len(s) and self._is_valid(next_int):
                    address.append(next_int)
                    self._rec(s, j, address, addresses)
                    address.pop()

    def _is_valid(self, next_int):
        return 0 <= int(next_int) <= 255 and (next_int == '0' or not next_int.startswith('0'))