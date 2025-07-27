class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        S=n*(n+1)//2
        k=n//m
        Q = m*(k*(k+1))//2
        S=S-Q
        return S-Q

          