"""
in bubble sort in first iteration the largest value is set at the end that is the righest of the list
"""

def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp



nums = [5,8,4,6,9,2]
print(nums)
sort(nums)

print(nums)
