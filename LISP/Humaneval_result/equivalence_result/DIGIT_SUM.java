Based on the provided API method, which calculates the sum of ASCII values of characters in a string that are uppercase letters, we can partition the following equivalence classes for the input parameter `s`:

- class:
    1. `s`: is null
- class:
    1. `s`: is an empty string
- class:
    1. `s`: contains only lowercase letters
- class:
    1. `s`: contains only uppercase letters
- class:
    1. `s`: contains a mix of uppercase and lowercase letters
- class:
    1. `s`: contains special characters or digits along with letters

These equivalence classes cover a range of scenarios to ensure comprehensive testing of the `digit_sum` method.