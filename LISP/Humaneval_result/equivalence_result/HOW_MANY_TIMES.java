Based on the provided API method, we need to partition the equivalence classes for the input parameters `string` and `substring` to test the method `how_many_times`.

- class:
    1. `string`: is null; 2. `substring`: can be any non-null string
- class:
    1. `string`: is an empty string; 2. `substring`: can be any non-empty string
- class:
    1. `string`: is a non-empty string; 2. `substring`: is an empty string
- class:
    1. `string`: is a non-empty string; 2. `substring`: is a non-empty string that occurs multiple times in `string`
- class:
    1. `string`: is a non-empty string; 2. `substring`: is a non-empty string that does not occur in `string`
- class:
    1. `string`: is a non-empty string; 2. `substring`: is a non-empty string that occurs only once at the beginning or end of `string`