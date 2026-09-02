from collections import deque

def min_jumps(a, x, y):
    n = len(a)

    if x == y:
        return 0

    queue = deque()
    queue.append((x, 0))

    visited = set()
    visited.add(x)

    while queue:
        current, jumps = queue.popleft()

        # Anti-clockwise
        next_chair = (current + a[current]) % n

        if next_chair == y:
            return jumps + 1

        if next_chair not in visited:
            visited.add(next_chair)
            queue.append((next_chair, jumps + 1))

        # Clockwise
        next_chair = (current - a[current] + n) % n

        if next_chair == y:
            return jumps + 1

        if next_chair not in visited:
            visited.add(next_chair)
            queue.append((next_chair, jumps + 1))

    return -1


# Input
a = list(map(int, input("Enter jump distances: ").split()))
x = int(input("Enter source: "))
y = int(input("Enter destination: "))

print("Minimum jumps:", min_jumps(a, x, y))