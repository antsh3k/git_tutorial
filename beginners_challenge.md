# Instructions

# --- Christmas Wrapping Challenge ---

The elves in the workshop are in a wrapping frenzy! Every day, they receive boxes of presents that need to be wrapped before Santa's big night. However, there’s a twist: the elves only have a limited number of wrapping materials, and they want to minimize waste.

The wrapping requirements are simple:
- Each present comes in a box with dimensions: length, width, and height.
- To wrap a box, you need enough material to cover all six sides plus a little extra for the smallest side as a spare.

The list of presents which need to be wrapped can be generated in __challenge_1.py__

For example, if a box has dimensions `2x3x4`:
- The surface area of the box is `2 × (2 × 3 + 3 × 4 + 4 × 2) = 52`.
- The smallest side of the box is `2 × 3 = 6`, so you need an additional `6` units of wrapping material.
- The total material needed is `52 + 6 = 58`.

Your task is to calculate how much total wrapping material is needed for all the boxes on the elves’ list.

---

### Input:

The elves will provide you with a list of box dimensions in the following format:

```
2x3x4
1x1x10
```


Each line represents the dimensions of a single box: `length x width x height`.

---

### Output:

Write a program that:
1. Reads a list of dimensions.
2. Calculates the total wrapping material needed for all the boxes.
3. Prints the total.

---

### Example:

Given the input:

```
2x3x4
1x1x10
```

Your program should output:

Total wrapping material needed: 101


---

### Challenge:

Can you modify your program to also calculate the ribbon needed for each box? For ribbon:
- You need enough to wrap around the smallest perimeter of the box.
- You also need a bow, which uses material equal to the volume of the box.

For example, for a box with dimensions `2x3x4`:
- The smallest perimeter is `2 × (2 + 3) = 10`.
- The volume of the box is `2 × 3 × 4 = 24`.
- The total ribbon needed is `10 + 24 = 34`.

If you’re up for it, modify your program to calculate **both** wrapping material and ribbon needed! Good luck!
