"""Verification script for Session 2 solutions (computational problems)."""


def problem1():
    """Verify Problem 1: Fermat's Little Theorem computations."""
    # (a) 3^2027 mod 17
    a = pow(3, 2027, 17)
    assert a == 7, f"1(a): expected 7, got {a}"

    # (b) 7^1958 mod 23
    b = pow(7, 1958, 23)
    assert b == 1, f"1(b): expected 1, got {b}"

    # (c) 4^691 mod 31
    c = pow(4, 691, 31)
    assert c == 4, f"1(c): expected 4, got {c}"

    print("Problem 1: PASSED")


def problem2():
    """Verify Problem 2: last digit of 7^100."""
    result = pow(7, 100, 10)
    assert result == 1, f"2: expected 1, got {result}"
    print("Problem 2: PASSED")


def problem3():
    """Verify Problem 3: n^7 - n divisible by 42 for all n."""
    for n in range(-500, 501):
        assert (n**7 - n) % 42 == 0, f"3: failed for n={n}"
    print("Problem 3: PASSED (checked n in -500..500)")


def problem4():
    """Verify Problem 4: solving linear/quadratic congruences."""
    # (a) 5x ≡ 6 (mod 8), answer x ≡ 6
    assert (5 * 6) % 8 == 6, "4(a): 5*6 mod 8 != 6"

    # (b) 12x ≡ 5 (mod 19), answer x ≡ 2
    assert (12 * 2) % 19 == 5, "4(b): 12*2 mod 19 != 5"

    # (c) x^2 + y^2 ≡ 1 (mod 13), verify 12 solutions and list matches
    solutions = []
    for x in range(13):
        for y in range(13):
            if (x * x + y * y) % 13 == 1:
                solutions.append((x, y))
    assert len(solutions) == 12, f"4(c): expected 12 solutions, got {len(solutions)}"

    print(f"Problem 4: PASSED (4c solutions: {solutions})")


def problem7():
    """Verify Problem 7: 3x^3 + 4y^3 ≡ 1715 (mod 19) has a solution."""
    target = 1715 % 19
    # Claimed solution: (3, 0)
    assert (3 * 27 + 4 * 0) % 19 == target, "7: (3,0) is not a solution"

    # Also brute-force find all solutions
    solutions = []
    for x in range(19):
        for y in range(19):
            if (3 * x**3 + 4 * y**3) % 19 == target:
                solutions.append((x, y))
    assert (3, 0) in solutions
    print(f"Problem 7: PASSED (solution (3,0) verified; {len(solutions)} total solutions mod 19)")


def problem9():
    """Verify Problem 9: points on y^2 = x^3 + 2 over F_7."""
    affine_points = []
    for x in range(7):
        for y in range(7):
            if (y * y) % 7 == (x**3 + 2) % 7:
                affine_points.append((x, y))

    expected = [(0, 3), (0, 4), (3, 1), (3, 6), (5, 1), (5, 6), (6, 1), (6, 6)]
    assert affine_points == expected, f"9: expected {expected}, got {affine_points}"
    total = len(affine_points) + 1  # +1 for point at infinity
    assert total == 9, f"9: expected 9 total points, got {total}"
    print(f"Problem 9: PASSED (affine points: {affine_points}, total: {total})")


if __name__ == "__main__":
    problem1()
    problem2()
    problem3()
    problem4()
    problem7()
    problem9()
    print("\nAll verifications passed!")
