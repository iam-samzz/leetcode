'''Substrings of Length K with All Distinct Characters

    Task: Given a string s and an integer k, count how many substrings 
    of length k contain no repeated characters.'''


def func(st,k):
    n = len(st)

    if k > n or k <= 0:
        return 0
    
    #window state
    window_freq = {}

    #result state
    no_of_noRepatition = 0

    left = 0

    for right in range(n):

        if st[right] not in window_freq:
            window_freq[st[right]] = 1
        else:
            window_freq[st[right]] += 1

        window_size = right - left + 1

        if window_size == k:

            # means that, if some char inside window is repeated, then len(win_freq) will be less than the k , only if all char are unique, then len(win_freq) == k
            if len(window_freq) == k:
                no_of_noRepatition += 1

            #removing left most in the window
            window_freq[st[left]] -= 1
            if window_freq[st[left]] == 0:
                del window_freq[st[left]]

            #moving left front
            left += 1
    return no_of_noRepatition

print(func("havefunonleetcode",5))