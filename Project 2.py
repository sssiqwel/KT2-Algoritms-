def main() -> None:
    n = int(input())
    nums = list(map(int, input().split()))

    prefix_sum = [0] * (n + 1)
    for index, value in enumerate(nums):
        prefix_sum[index + 1] = prefix_sum[index] + value

    q = int(input())
    answers = []

    for _ in range(q):
        left, right = map(int, input().split())
        answers.append(str(prefix_sum[right + 1] - prefix_sum[left]))

    print("\n".join(answers))


if __name__ == "__main__":
    main()