

arr = [i for i in range(0, 9)]

def sum(input):
    mid = len(input)//2
    if mid==0:
        return 0
    print(mid)
    print(input[:mid])
    print(input[mid])
    print(input[mid+1:])
    print( sum(input[:mid]) + input[mid] + sum(input[mid+1:]))
    print("cat\n")
    return sum(input[:mid]) + input[mid] + sum(input[mid+1:])


print(sum(arr))

#array[not including : including]
