"""
In Selection sort the minimu value will be set at 1st place
"""

def sort(list):
    for i in range(len(list)-1):
        minpos = i
        for j in range(i,len(list)):
            if nums[j]<nums[minpos]:
                    minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)


nums = [5,8,4,6,9,2]
# print(nums)
sort(nums)

# print(nums)