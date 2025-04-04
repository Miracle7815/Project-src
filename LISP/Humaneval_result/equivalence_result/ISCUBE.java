Based on the provided API method `iscube(int a)` from the given Java class, where the method determines if the input integer `a` is a perfect cube or not, we can partition the following equivalence classes for the input parameter `a`:

- class:
    1. `a`: is a perfect cube (e.g., 8, 27, 64)
- class:
    1. `a`: is not a perfect cube (e.g., 5, 10, 15)
- class:
    1. `a`: is a negative perfect cube (e.g., -8, -27, -64)
- class:
    1. `a`: is a perfect cube with decimals (e.g., 1.5, 3.375) - as the method implicitly converts input to integer, these would be equivalent to equivalent whole numbers
- class:
    1. `a`: is zero, as the cube of zero is zero

It is important to test both positive and negative cases along with boundary values to ensure the robustness of the method.