class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        bit_width = 32
        for _ in range(bit_width):
            result <<= 1
            result |= (n & 1)
            n >>= 1
        return result