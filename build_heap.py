# python3
def heap(data):
    swaps = []
    ipt = len(data)
    for i in range (ipt // 2, -1, -1):
        j = i
        while True:
            right = j * 2 + 2
            left = j * 2 + 1
            smallest = j 
            if right < ipt and data[right] < data[smallest]:
                smallest = right
            if left < ipt and data[left] < data[smallest]:
                smallest = left
            if smallest != j:
                swaps.append((j, smallest))
                data[j], data[smallest] = data[smallest], data[j]
                j = smallest
            else:
                break
                return swaps
def main():
    mode = input()
    if "I" in mode:
        ipt= int(input())
        data = list(map(int, input().split()))
   elif "F" in mode:
    filename = input()
    if 'a' in filename:
        return
    with open(f"tests/{filename}") as f:
        ipt = int(f.readline())
        data = list(map(int, f.readline().split()))
        assert len(data) == ipt
swaps = build_heap(data)

print(len(swaps))
for i, j in swaps:
    print(i, j)
    
    
if __name__ == "__main__":
    main()
    
    

