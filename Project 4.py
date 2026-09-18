def can_ship(weights: list[int], days: int, capacity: int) -> bool:
    used_days = 1
    current_load = 0

    for weight in weights:
        if current_load + weight > capacity:
            used_days += 1
            current_load = 0
        current_load += weight

    return used_days <= days


def minimum_capacity(weights: list[int], days: int) -> int:
    left, right = max(weights), sum(weights)

    while left < right:
        middle = (left + right) // 2
        if can_ship(weights, days, middle):
            right = middle
        else:
            left = middle + 1

    return left


def main() -> None:
    n, days = map(int, input().split())
    weights = list(map(int, input().split()))
    print(minimum_capacity(weights, days))


if __name__ == "__main__":
    main()
