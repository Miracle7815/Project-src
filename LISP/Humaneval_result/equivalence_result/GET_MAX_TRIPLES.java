Based on the provided API method, we can identify the input parameter `n` as the only parameter that affects the behavior of the method. To effectively test this method, we can partition the equivalence classes for the input parameter `n` as follows:

- class:
    1. `n`: negative values
- class:
    1. `n`: zero
- class:
    1. `n`: positive values

For each class, test cases should be designed to cover boundary values, typical values, and extreme values to ensure comprehensive testing of the `get_max_triples` method.