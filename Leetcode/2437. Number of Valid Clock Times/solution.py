class Solution:
    def countTime(self, t: str) -> int:
        mm = (6 if t[3] == '?' else 1) * (10 if t[4] == '?' else 1)
        match [t[0], t[1]]:
            case ('?', '?'):
                return mm * 24
            case ('?', ('0' | '1' | '2' | '3')):
                return mm * 3
            case ('?', _):
                return mm * 2
            case (('0' | '1'), '?'):
                return mm * 10
            case (_, '?'):
                return mm * 4
        return mm