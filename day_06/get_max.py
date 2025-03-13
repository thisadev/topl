arr = [3, 45, 32, 65, 76, 12]
max = arr[0]
i = 1
while i < len(arr):
    if arr[i] > max:
        max = arr[i]
    else:
        max = max
    i += 1
result = max
print(result)
