# python3
def build_heap(data):
    swaps = []
    
    return swaps
def main():
    
    n = input(input())
    data = list(map(int, input().split()))
    
    assert len(data) == n
    
    swaps = build_heap(data)
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
   
                  
if __name__ == "__main__":
    main()
