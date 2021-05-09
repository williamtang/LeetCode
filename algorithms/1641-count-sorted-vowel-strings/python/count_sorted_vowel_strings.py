class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5

        lst = [1, 1, 1, 1, 1]
        for i in range(2, n+1):
            temp = [sum(lst[:1]), sum(lst[:2]), sum(
                lst[:3]), sum(lst[:4]), sum(lst)]
            print(temp)
            lst = temp

        return sum(lst)
