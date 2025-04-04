The provided method `add_even_at_odd` takes an array of integers and calculates the sum of even numbers at odd indices in the array.

To partition the equivalence classes for testing this method, we can consider the following classes for the input array `lst`:
- class:
    1. `lst`: is null
- class:
    1. `lst`: is an empty array
- class:
    1. `lst`: contains only odd numbers
- class:
    1. `lst`: contains only even numbers
- class:
    1. `lst`: contains a mix of odd and even numbers

Additionally, we can consider the following classes for the behavior of the method:
- class:
    1. There are even numbers at odd indices in the array
- class:
    1. There are no even numbers at odd indices in the array

By testing with inputs from these equivalence classes, we can ensure comprehensive coverage of the method's functionality.