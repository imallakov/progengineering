class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.map[row][col] = '*'
        elif result == 'hit':
            self.map[row][col] = 'x'
        elif result == 'sink':
            self.map[row][col] = 'x'
            self.mark_sunk_ship(row, col)

    def mark_sunk_ship(self, row, col):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 10 and 0 <= c < 10 and self.map[r][c] != '.':
                self.map[r][c] = '*'
                r += dr
                c += dc

    def cell(self, row, col):
        return self.map[row][col]


sm = SeaMap()
sm.shoot(2, 0, 'sink')
sm.shoot(6, 9, 'hit')

for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
