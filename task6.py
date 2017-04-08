def because(target, *nums):
    n = 0
    while n < len(nums):
        m = n + 1
        while m < len(nums):
            if nums[n] + nums[m] == target:
                return n , m
            m += 1
        n += 1
    
a = because(9, *[2,11,7,15])
print(a)
