class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of digits
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        
        for i in range(len(digits)):
            # Check for a larger digit to the right
            for d in range(9, int(digits[i]), -1):
                if d in last and last[d] > i:
                    # Perform the swap
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    # Convert back to integer and return
                    return int(''.join(digits))
        
        return num

# Example usage
solution = Solution()
print(solution.maximumSwap(2736))  # Output: 7236
print(solution.maximumSwap(9973))  # Output: 9973

