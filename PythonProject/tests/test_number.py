

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