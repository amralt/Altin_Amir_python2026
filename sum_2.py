#O(n^2)
def get_s(lst, n):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if (n == lst[i] + lst[j]):
                return [i,j]
            
# тут отсортировано O(n)
def get_s_fast(lst, n):
    left , right = 0, len(lst)-1
    while left < right:
        if n > lst[right] + lst[left]:
            left +=1
        elif n < lst[right] + lst[left]:
            right -= 1
        else:
            return [left, right]
            
    
print(get_s_fast([0,1,2,3,4,5,6,7,8], 25))
print(get_s_fast([0,1,2,3,4,5,6,7,8], 5))

