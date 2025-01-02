class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        if k > 0:
            current_sum = sum(code[1:k+1])
            ans[0] = current_sum

            for l in range(1, n):
                r = (l + k) % n
                current_sum += code[r] - code[l]
                ans[l] = current_sum

            return ans

        current_sum = sum(code[k:])
        ans[0] = current_sum

        for l in range(1, n):
            r = (l - k) % n
            current_sum += -code[-l] + code[-r]
            ans[-l] = current_sum

        return ans
