# -*- coding:utf-8 -*-


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        num = len(code)
        result = [0] * num
        if k == 0:
            return result
        elif k > 0:
            for i in range(0, num):
                if k <= num - (i+1):
                    result[i] = sum(code[i+1:i+1+k])
                else:
                    result[i] = sum(code[i+1:]) + sum(code[0:k-num+(i+1)])
        else:
            k = -k
            code.reverse()
            for i in range(0, num):
                if k <= num - (i+1):
                    result[i] = sum(code[i+1:i+1+k])
                else:
                    result[i] = sum(code[i+1:]) + sum(code[0:k-num+(i+1)])
            result.reverse()

        return result
