'''Find the length of the longest substring that contains at most 2 distinct characters.
Example: s = "eceba". (Answer is 3, from "ece").'''

def func(s):

    n = len(s)

    #window state 
    win = {}

    #result state
    long_len = None

    left = 0

    for right in range(n):
        if s[right] not in win:
            win[s[right]] = 1
        else:
            win[s[right]] += 1

        if len(win) <= 2:
            if long_len == None:
                long_len = right - left + 1
            else:
                long_len = max(long_len,right-left+1)
        else:

            while left <= right and len(win) > 2:
                win[s[left]] -= 1
                if win[s[left]]== 0:
                    del win[s[left]]
                left += 1
            long_len = max(long_len,right - left + 1)
    if long_len == None:
        return 0
    return long_len

print(func("eceba"))


