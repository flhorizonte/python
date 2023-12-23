
#time complexity = O(n^2)

def count_equal_numbers(nums):
   n = len(nums)
   print("Quantidade: ", n)
   for i in range(n - 1):
       print("i", i)
       for j in range(i + 1, n):
           print("j", j)
           if nums[i] == nums[j]:
            return True
   return False

# time complexity = O(n)

def count_equal_numbers_set(nums) -> bool:
    ver = set()
    for num in nums:
        if num in ver:
            return True
        ver.add(num)
    return False

#print(count_equal_numbers([3,3,1]))
print(count_equal_numbers_set([3,3,1]))
