class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        max_length = 0
        frequency = {}
        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            max_freq = max(max_freq, frequency[s[right]])
            while (right - left + 1) - max_freq > k:
                frequency[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length            