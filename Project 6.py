def minimum_rooms(meetings: list[tuple[int, int]]) -> int:
    if not meetings:
        return 0

    starts = sorted(start for start, _ in meetings)
    ends = sorted(end for _, end in meetings)
    start_index = 0
    end_index = 0
    occupied = 0
    answer = 0

    while start_index < len(meetings):
        if starts[start_index] < ends[end_index]:
            occupied += 1
            answer = max(answer, occupied)
            start_index += 1
        else:
            occupied -= 1
            end_index += 1

    return answer


def main() -> None:
    n = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(n)]
    print(minimum_rooms(meetings))


if __name__ == "__main__":
    main()