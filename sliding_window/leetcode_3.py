class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        def func(s_list):
            left = 0
            right = 0

            longest = None


            current_hash = {}


            for right in range(0,len(s_list)):

                if s_list[right] not in current_hash:
                    current_hash[s_list[right]] = 1

                    if longest == None:
                        longest = right - left + 1

                    else:
                        longest = max(longest,right-left+1)

                else:
                    current_hash[s_list[right]] += 1
                    #we fix the right there
                    #and move the left

                    while left <= right and len(current_hash) != right - left + 1:
                        current_hash[s_list[left]] -= 1
                        if current_hash[s_list[left]] == 0:
                            del current_hash[s_list[left]]
                        left += 1

                    longest = max(longest,right-left+1)
            if longest == None:
                return 0

            return longest
        return func(s)
