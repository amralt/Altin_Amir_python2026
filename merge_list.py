
def merge_list(lst1, lst2):
    new_lst = list()
    l, r = 0, 0
    while l < len(lst1) and r < len(lst2) :
        if lst1[l] < lst2[r]:
            new_lst.append(lst1[l])
            l+= 1
        else :
            new_lst.append(lst2[r])
            r+= 1
    while l < len(lst1):
        new_lst.append(lst1[l])
        l+=1
    while r > len(lst2):
        new_lst.append(lst2[r])
        r+=1
    return new_lst

def inplace_merge_list(lst1:list, lst2:list):
    n = len(lst1) 
    m = len(lst2)
    a = [None]*m
    lst1.extend(a)
    
    i = n-1
    j = m-1
    k = n + m - 1 # это указатель, куда вставляем
    while i >= 0 and j >= 0:
        if lst1[i] > lst2[j]:
            lst1[k] = lst1[i]
            i -= 1
        else:
            lst1[k] = lst2[j]
            j-= 1
        k-=1
    while j >= 0:
        lst1[k] = lst2[k]
        j -= 1
        k -= 1

lst1 = sorted([1,3423,23,54,2])
lst2 = sorted([0, 90, 9223,29, 9])
print(merge_list(lst1, lst2))

print('old lst1: ', lst1)
inplace_merge_list(lst1, lst2)
print('new lst1: ', lst1)