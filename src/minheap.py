import heapq

def sort_k_sorted_array(arr, k):
    n = len(arr)
    heap = arr[:k+1]
    heapq.heapify(heap)

    sorted_index = 0
    
    for i in range(k+1, n):
        arr[sorted_index] = heapq.heappop(heap)
        heapq.heappush(heap, arr[i])
        sorted_index += 1

    while heap:
        arr[sorted_index] = heapq.heappop(heap)
        sorted_index += 1

    return arr

# Beispielverwendung
array = [3, 2, 1, 5, 4, 7, 6, 5]
k = 2
print(sort_k_sorted_array(array, k))  # Ausgabe: [1, 2, 3, 4, 5, 5, 6, 7]

