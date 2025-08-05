class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def calculate_happy(numbers):
            total = 0
            for num in numbers:
                total += int(num) ** 2

            if total == 1:
                return True
            if total in seen:
                return False
                
            seen.add(total)
            return calculate_happy(str(total))
        
        return calculate_happy(str(n))
        
