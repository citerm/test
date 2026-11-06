for left in range(5, 0, -1):
    row = ""
    for right in range(5, 0, -1):
        row += f"{left} * {right} = {left * right:2d}   "
    print(row.rstrip())
