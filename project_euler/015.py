square = 20  # 2x2 matrix

square += 1  # a 2x2 grid has 3 lines down
ways = [[1 for _ in range(square)] for _ in range(square)]

# for border in range(square):  # untere zeile und rechte spalte = 1 weg
#     ways[border][square-1] = 1
#     ways[square-1][border] = 1  # Feld (n,n) wird zweimal auf 1 gesetzt

for col in range(1, square):  # Spalte 0 (die ganz rechte!) brauchst net
    for row in range(1,square):
        ways[row][col] = ways[row][col-1] + ways[row-1][col]

print ways[square-1][square-1]

