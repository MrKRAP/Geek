nums_sum = 0


def num_sum(nums, nums_sum):
    for el in nums:
        try:
            nums_sum += int(el)
        except:
            return nums_sum, False

    return nums_sum, True


num = input("Enter :").split()
while num_sum(num, nums_sum)[1]:
    print(num_sum(num, nums_sum)[0])
    nums_sum = num_sum(num, nums_sum)[0]
    num = input("Enter : ").split()
else:
    print(num_sum(num, nums_sum)[0])
