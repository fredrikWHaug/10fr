
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_vaule = nums[mid]
        if target == mid_vaule:
            return mid
        elif target < mid_vaule:
            high = mid - 1
        else:
            low = mid + 1

def main():
    nums = [0, 2, 4, 6, 7, 8]
    target = 7
    index = binary_search(nums, target)
    print(index)

if __name__ == '__main__':
    main()