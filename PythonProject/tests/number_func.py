def insert_five_to_maximize_number(n):
    s = str(n)
    if n >= 0:
        for i, ch in enumerate(s):
            if int(ch) < 5:
                return int(s[:i] + '5' + s[i:])
        return int(s + '5')
    else:
        for i, ch in enumerate(s[1:]):  # skip '-'
            if int(ch) > 5:
                return int(s[:i+1] + '5' + s[i+1:])
        return int(s + '5')




test_cases = [
    (268, 5268),
    (670, 6750),
    (0, 5),
    (768, 7685),
    (567, 5675),
    (-123, -1235),
    (-762, -5762),
    (-263, -2563),
    (-555, -5555),
]

for n, expected in test_cases:
    result = insert_five_to_maximize_number(n)
    assert result == expected, f"Failed for {n}: expected {expected}, got {result}"
print("All tests passed!")