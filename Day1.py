import heapq
def count(arr1,arr2):
    #heapify these lists

    # heapq.heapify(arr1)
    # heapq.heapify(arr2)
    # sorted_arr1 = [heapq.heappop(arr1) for _ in range(len(arr1))]
    # sorted_arr2 = [heapq.heappop(arr2) for _ in range(len(arr2))]

    res = 0

    occ_dict = {}
    for j in arr2:
        if j in occ_dict:
            occ_dict[j] += 1
        else:
            occ_dict[j] = 1
            

    for i in arr1:
       if i in occ_dict:
        val = occ_dict[i]*i
        res += val
        
        
       else:
        val = 0*i
        res += val

    print(res)
    return res

# Open the file in read mode
with open('input.txt', 'r') as file:
    arr1 = []
    arr2 = []
    for line in file:
        # Split each line into two numbers and append to respective lists
        num1, num2 = map(int, line.split())
        arr1.append(num1)
        arr2.append(num2)

# arr1 = [3,4,2,1,3,3]
# arr2 = [4,3,5,3,9,3]
count(arr1,arr2)
