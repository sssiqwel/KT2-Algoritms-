def count_subarrays(nums: list[int], target: int) -> int:
    prefix_frequency = {0: 1}
    prefix_sum = 0
    answer = 0

    for value in nums:
        prefix_sum += value
        answer += prefix_frequency.get(prefix_sum - target, 0)
        prefix_frequency[prefix_sum] = prefix_frequency.get(prefix_sum, 0) + 1

    return answer


def main() -> None:
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))
    print(count_subarrays(nums, target))


if __name__ == "__main__":
    main()
