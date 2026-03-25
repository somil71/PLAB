# arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# arr.sort(reverse = True)
# print(arr)

arr = [i for i in range(10) if i % 2 == 0]
arr.sort(reverse = True)
print(arr)

arr = ["even" if i%2==0 else "odd" for i in range(5)]
arr.sort()
print(arr)