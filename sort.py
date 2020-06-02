’‘’
bubble sort
Time complexity: O(n^2) 
Space complexity: O(1)
‘’‘
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] >= array[j]:
                array[i], array[j] = array[j], array[i]
    return array

’‘’
select sort
Time complexity: O(n^2) 
Space complexity: O(1)
‘’‘
def select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]

    return array

#-------------------------------------------------------
’‘’
insert sort
Time complexity: O(n^2) 
Space complexity: O(1)
‘’‘
def insert_sort(array):
    for i in range(1, len(array)):
        while i>0 and array[i-1] > array[i]:
            array[i-1], array[i] = array[i], array[i-1]
            i-=1
            
    return array
’‘’
shell sort
Time complexity: O(nlogn) 
Space complexity: O(1)
‘’‘
def shell_sort(array):
    gap = len(array)//2
    while gap:
        for i in range(gap, len(array)):
            while i>0 and array[i-gap] > array[i]:
                array[i-gap], array[i] = array[i], array[i-gap]
                i-=1
        gap //= 2
    return array

’‘’
shell sort
Time complexity: O(nlogn) 
Space complexity: O(1)
‘’‘
def quick_sort(array, l, pivot):

    def helper(array, l, pivot):
        r = pivot - 1
        while l <= r:
            if array[l] > array[pivot] and array[r] < array[pivot]:
                array[l], array[r] = array[r], array[l]
            if array[l] <= array[pivot]: l += 1
            if array[r] >= array[pivot]: r -= 1

        array[l], array[pivot] = array[pivot], array[l]

        return l

    if l < pivot:
        q = helper(array, l, pivot)
        quick_sort(array, l, q-1)
        quick_sort(array, q+1, pivot)
        
    return array
    
              
if __name__ == '__main__':
    array = [1, 4, 5, 3, 4, 2, 4]
    print(quick_sort(array, 0, len(array)-1))
    print(bubble_sort(array))
    print(select_sort(array))
    print(insert_sort(array))
    print(shell_sort(array))
