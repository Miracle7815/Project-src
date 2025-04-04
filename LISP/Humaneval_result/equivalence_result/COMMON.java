Based on the provided API method, `common(int[] l1, int[] l2)`, which finds the common elements between two integer arrays and returns them in sorted order, we can partition the equivalence classes for the input parameters `l1` and `l2` as follows:

- class:
    1. `l1`: is null; 2. `l2`: can be any integer array
- class:
    1. `l1`: is an empty array; 2. `l2`: can be any integer array
- class:
    1. `l1`: has elements with no common elements with `l2`; 2. `l2`: can be any integer array
- class:
    1. `l1`: has elements with some common elements with `l2`; 2. `l2`: can be any integer array
- class:
    1. `l1`: has elements with all common elements with `l2`; 2. `l2`: can be any integer array
- class:
    1. `l1`: has duplicate elements; 2. `l2`: can be any integer array
- class:
    1. `l1`: has elements in unsorted order; 2. `l2`: can be any integer array
- class:
    1. `l1`: has elements in sorted order; 2. `l2`: can be any integer array

By testing the API method with inputs from each of these equivalence classes, we can ensure comprehensive coverage of the functionality provided by the `common` method.