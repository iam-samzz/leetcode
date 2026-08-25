def func(s,k):

    #fixed sliding window pattern
    vowels = {"a","e","i","o","u"}

    left = 0
    #window state
    window_vowel_count = 0

    #result state
    max_vowel_count = 0

    n = len(s)
    
    for right in range(n):
        if s[right] in vowels:
            window_vowel_count += 1

        current_window_size = right - left + 1

        if current_window_size >= k:

            max_vowel_count = max(max_vowel_count,window_vowel_count)

            if s[left] in vowels:
                window_vowel_count -= 1
            left += 1

    return max_vowel_count

print(func("abciiidef",3))
