def sort(width, height, length, mass):
    """
    Classify a package based on its dimensions and mass.

    Parameters:
    - width (int): Width of the package in cm.
    - height (int): Height of the package in cm.
    - length (int): Length of the package in cm.
    - mass (int): Mass of the package in kg.

    Returns:
    - str: One of 'STANDARD', 'SPECIAL', or 'REJECTED'.
    """
    volume = width * height * length

    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20

    return (
        "REJECTED" if is_bulky and is_heavy else
        "SPECIAL" if is_bulky or is_heavy else
        "STANDARD"
    )


def run_tests():
    """
    Runs a suite of test cases to validate the sort function.
    """
    test_cases = [
        ((100, 100, 50, 10), "STANDARD"),
        ((200, 100, 100, 10), "SPECIAL"),
        ((100, 150, 50, 10), "SPECIAL"),
        ((50, 50, 50, 25), "SPECIAL"),
        ((200, 200, 50, 25), "REJECTED"),
        ((100, 100, 100, 10), "SPECIAL"),
        ((150, 50, 50, 10), "SPECIAL"),
        ((50, 50, 50, 20), "SPECIAL"),
    ]

    for i, (inputs, expected) in enumerate(test_cases):
        result = sort(*inputs)
        print(f"Test {i + 1}: Input={inputs} → Expected={expected}, Got={result}")
        assert result == expected, f"Test {i + 1} failed: got '{result}', expected '{expected}'"

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()