def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def sort_array(arr):
    merge_sort(arr)

def find_mode(arr):
    sort_array(arr)
    mode = arr[0]
    max_count = 1
    current_count = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            current_count += 1
        else:
            current_count = 1
        
        if current_count > max_count:
            max_count = current_count
            mode = arr[i]
    
    return mode

# Beispielverwendung
array = [1, 3, 2, 2, 1, 4, 4, 3, 5, 2, 5]
print(find_mode(array))  # Ausgabe: 2
