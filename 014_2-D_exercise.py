# making a telephone numpad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for items in num_pad:
    for nums in items:
        print(nums, end=" ")
    print()