
def func(st, k):

    n = len(st)

    #window state
    window = []

    #return state
    ans = []

    left = 0

    for right in range(n):
        window.append(st[right])

        window_size = len(window)

        if window_size == k:
  
            ans.append(window.copy())

            window.pop(0)

            #  left += 1 -> no need here
            
    return ans
print(func([3,4,5,6,6,2,31,2,0,9],3))
