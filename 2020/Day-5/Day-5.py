with open("day-5.txt", "r") as data:
    seats = data.readlines()

seats = [line[:-1] for line in seats]

seat_ids = []
for seat in seats:
    r = seat[:7]
    start = 0
    end = 127
    row, col = 0, 0
    for letter in r:
        if letter == "F":
            end = int((start + end + 1) / 2) - 1
        elif letter == "B":
            start = int((start + end + 1) / 2)
    row = start

    r = seat[7:]
    start = 0
    end = 7
    for letter in r:
        if letter == "L":
            end = int((start + end + 1) / 2) - 1
        elif letter == "R":
            start = int((start + end + 1) / 2)
    col = start

    sid = (row * 8) + col
    seat_ids.append(sid)


print(f"Solution 1: {max(seat_ids)}")
print(
    f"Solution 2: {[seat for seat in range(min(seat_ids), max(seat_ids)) if seat not in seat_ids][0]}"
)