class Solution:
    def toHexspeak(self, num: str) -> str:
        hexspeak = hex(int(num))[2:].replace("0", "O").replace("1", "I").upper()
        print(hexspeak)
        def is_valid_hexspeak(hexspeak) -> bool:
            return all([True if c in "ABCDEFIO" else False for c in hexspeak])
        return hexspeak if is_valid_hexspeak(hexspeak) else "ERROR"