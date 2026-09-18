def merge_intervals(intervals: list[tuple[int, int]]) -> list[list[int]]:
    intervals.sort()
    merged: list[list[int]] = []

    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged


def main() -> None:
    n = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]
    merged = merge_intervals(intervals)

    print(len(merged))
    for start, end in merged:
        print(start, end)


if __name__ == "__main__":
    main()
