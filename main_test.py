from main import *

run_cases = [
    (
        "My dog loves playing fetch in the backyard.",
        (10, {"a", "o", "e", "i"}),
    ),
    ("Dogs are the best pets ever!", (8, {"o", "e", "a"})),
]

submit_cases = run_cases + [
    ("Golden retrievers are known for their loyalty.", (14, {"e", "o", "a", "i"})),
    ("", (0, set())),
    (
        "Can I take my dog to the park today?",
        (10, {"o", "I", "a", "e"}),
    ),
    ("woof", (2, {"o"})),
    ("Labradors are friendly and energetic", (12, {"e", "a", "i", "o"})),
    ("Adopt don't shop", (4, {"o", "A"})),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Text: {input1}")
    print(f"Expecting: {expected_output}")
    result = count_vowels(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()