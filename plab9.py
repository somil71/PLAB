arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

if len(arr) <= 1:
    print(0)
else:
    jumps = 0
    current_max = 0
    farthest = 0
    
    for i in range(len(arr) - 1):
        farthest = max(farthest, i + arr[i])
        
        if i == current_max:
            jumps += 1
            current_max = farthest
            
            if current_max >= len(arr) - 1:
                break
    
    if farthest < len(arr) - 1:
        print(-1)
    else:
        print(jumps)
