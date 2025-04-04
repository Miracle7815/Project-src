Certainly! Let's partition the equivalence classes for the `number` parameter in the `truncate_number` method.

The method `truncate_number` returns the fractional part of a given `double` number by using the modulus operation with `1.0`. This means it will return the decimal part of the number, discarding the integer part.

Here are the equivalence classes:

- class:
    1. `number`: is positive and has a fractional part (e.g., 3.5, 10.99)
- class:
    1. `number`: is positive and has no fractional part (i.e., it is a whole number, e.g., 4.0, 100.0)
- class:
    1. `number`: is negative and has a fractional part (e.g., -3.5, -10.99)
- class:
    1. `number`: is negative and has no fractional part (i.e., it is a whole number, e.g., -4.0, -100.0)
- class:
    1. `number`: is zero (0.0)

These classes cover all possible scenarios for the input `number` in terms of sign and presence/absence of a fractional part.