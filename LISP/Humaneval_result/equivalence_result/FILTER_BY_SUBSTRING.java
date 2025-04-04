Based on the provided API method, we need to consider the inputs `strings` and `substring` to partition the equivalence classes for testing the `filter_by_substring` method. 

Here are the equivalence classes for the inputs:
- class:
    1. `strings`: is null; 2. `substring`: can be any string
- class:
    1. `strings`: is an empty list; 2. `substring`: can be any string
- class:
    1. `strings`: contains strings that do not contain the `substring`; 2. `substring`: is a string that is not present in any of the strings in `strings`
- class:
    1. `strings`: contains strings that do not contain the `substring`; 2. `substring`: is a string that is present in some of the strings in `strings`
- class:
    1. `strings`: contains strings that contain the `substring`; 2. `substring`: is a string that is present in some of the strings in `strings`
- class:
    1. `strings`: contains strings that contain the `substring`; 2. `substring`: is a string that is not present in any of the strings in `strings`

By testing with inputs from each of these equivalence classes, we can ensure good coverage of the `filter_by_substring` method.