w={'Q':9, 'R':5, 'B':3, 'N':3, 'P':1, 'K':0}
white = black = 0

for _ in range(8):
    row =input()

    for c in row:
        if c in w:
            white += w[c]
        elif c.upper() in w:
            black += w[c.upper()]

if white > black:
    print("White")
elif black > white:
    print("Black")
else:
    print("Draw")