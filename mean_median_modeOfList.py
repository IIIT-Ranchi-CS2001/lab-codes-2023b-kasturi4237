
nums = [int(num) for num in input("Enter numbers(space separated): ").split(" ")]
print(nums)
mean = sum(nums) / len(nums)
median = sorted(nums)[len(nums) // 2] if (len(nums) % 2 != 0) else (sorted(nums)[len(nums) // 2] + sorted(nums)[len(nums) // 2 - 1]) / 2
mode = 0
maxfreq = 0
for e in nums:
    if(nums.count(e) > maxfreq):
        maxfreq = nums.count(mode)
        mode = e

print("Mean: %f\nMedian: %f\nMode: %d\n" % (mean, median, mode))

