Based on the provided API method, we need to partition the equivalence classes for the input parameters `lst1` and `lst2` to test the `total_match` method effectively. 

Here are the equivalence classes for the input parameters:
- class:
    1. `lst1`: is null; 2. `lst2`: can be any non-null list
- class:
    1. `lst1`: is an empty list; 2. `lst2`: can be any non-empty list
- class:
    1. `lst1`: contains multiple strings with varying lengths; 2. `lst2`: contains multiple strings with varying lengths, where the total length of `lst1` is less than or equal to the total length of `lst2`
- class:
    1. `lst1`: contains multiple strings with varying lengths; 2. `lst2`: contains multiple strings with varying lengths, where the total length of `lst1` is greater than the total length of `lst2`
- class:
    1. `lst1`: contains multiple strings with varying lengths; 2. `lst2`: contains multiple strings with varying lengths, where the total length of `lst1` is equal to the total length of `lst2`
- class:
    1. `lst1`: contains a single string; 2. `lst2`: contains a single string

By testing the `total_match` method with inputs from each of these equivalence classes, we can ensure comprehensive coverage of the method's functionality.