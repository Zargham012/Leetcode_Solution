class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            next_seq = ""
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                next_seq += str(count) + result[i]
                i += 1
            result = next_seq
        return result