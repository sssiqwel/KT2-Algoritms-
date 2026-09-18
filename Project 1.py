def lower_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        middle = (left + right) // 2
        if nums[middle] < target:
            left = middle + 1
        else:
            right = middle

    return left


def main() -> None:
    n, target = map(int, input().split())
    nums = list(map(int, input().split())) if n > 0 else []
    print(lower_bound(nums, target))


if __name__ == "__main__":
    main()
