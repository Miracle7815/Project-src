Based on the provided API method, we can identify the following equivalence classes for testing the `rolling_max` method:

- class:
    1. `numbers`: is an empty list
- class:
    1. `numbers`: contains only one element
- class:
    1. `numbers`: contains multiple elements with increasing values
- class:
    1. `numbers`: contains multiple elements with decreasing values
- class:
    1. `numbers`: contains multiple elements with random values
- class:
    1. `numbers`: contains multiple elements with alternating increasing and decreasing values
- class:
    1. `numbers`: contains multiple elements with all elements being the same

By testing the `rolling_max` method with inputs from each of these equivalence classes, we can ensure that the method behaves correctly under various scenarios and handles different types of input data effectively.