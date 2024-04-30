
def binary_search(target, nums):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = nums[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

def main():
    nums = [0, 1, 2, 3]
    target = 3
    print(binary_search(target, nums))

if __name__ == '__main__':
    main()