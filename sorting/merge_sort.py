def merge_sort(arr,low,high):
    #base case
    if low == high:
        return
    
    mid = (low + high) // 2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)

    merge(arr,low,mid,high)

    #merge


def merge(arr,low,mid,high):
    temp = []
    p1 = low
    p2 = mid+1

    while p1 < mid+1 and p2 < high+1:
        if arr[p1] <= arr[p2]:
            temp.append(arr[p1])
            p1+=1
        elif arr[p2] < arr[p1]:
            temp.append(arr[p2])
            p2 += 1

    while p1 < mid + 1:
        temp.append(arr[p1])
        p1+= 1
    while p2 < high+1:
        temp.append(arr[p2])
        p2+=1

    x=0
    for i in range(low,high+1):

        arr[i] = temp[x]
        x += 1


x = [5,6,1,3,6,8,9,5,4,2,1,76,2]
merge_sort(x,0,len(x)-1)
print(x)