# python3
def sift_down(arr, i, n, swaps):
    min_index = i
    left_child = 2*i + 1
    right_child = 2*i + 2
    
    if left_child < n and arr[left_child] < arr[min_index]:
        min_index = left_child
    
    if right_child < n and arr[right_child] < arr[min_index]:
        min_index = right_child
    
    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))
        sift_down(arr, min_index, n, swaps)

def build_heap(arr):
    n = len(arr)
    swaps = []
    for i in range(n//2 - 1, -1, -1):
        sift_down(arr, i, n, swaps)
    return swaps

n = int(input())
arr = list(map(int, input().split()))

swaps = build_heap(arr)

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])

