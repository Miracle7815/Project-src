Certainly! We'll identify the equivalence classes for the parameters `strings` and `substring` to ensure comprehensive testing of the `filter_by_substring` method.

### Equivalence Classes

#### For `strings`:

1. **Class**: `strings` is null
   - Description: The input list is null.
   
2. **Class**: `strings` is empty
   - Description: The input list is empty but not null.
   
3. **Class**: `strings` contains only one string that includes the substring
   - Description: The input list contains exactly one string which includes the substring.
   
4. **Class**: `strings` contains only one string that does not include the substring
   - Description: The input list contains exactly one string which does not include the substring.
   
5. **Class**: `strings` contains multiple strings, some of which include the substring
   - Description: The input list contains multiple strings, where at least one string includes the substring and at least one does not.
   
6. **Class**: `strings` contains multiple strings, all of which include the substring
   - Description: The input list contains multiple strings, where all strings include the substring.
   
7. **Class**: `strings` contains multiple strings, none of which include the substring
   - Description: The input list contains multiple strings, where none of the strings include the substring.

#### For `substring`:

1. **Class**: `substring` is null
   - Description: The substring to search for is null.
   
2. **Class**: `substring` is an empty string
   - Description: The substring to search for is an empty string.
   
3. **Class**: `substring` is a non-empty string that exists in some elements of `strings`
   - Description: The substring to search for is a non-empty string that exists in some elements of the input list.
   
4. **Class**: `substring` is a non-empty string that does not exist in any element of `strings`
   - Description: The substring to search for is a non-empty string that does not exist in any element of the input list.

### Combined Equivalence Classes

Combining these, we get the following equivalence classes:

- **Class**:
  - `strings`: is null
  - `substring`: can be any string (null, empty, or non-empty)

- **Class**:
  - `strings`: is empty
  - `substring`: can be any string (null, empty, or non-empty)

- **Class**:
  - `strings`: contains only one string that includes the substring
  - `substring`: is a non-empty string that exists in the single element of `strings`

- **Class**:
  - `strings`: contains only one string that includes the substring
  - `substring`: is an empty string

- **Class**:
  - `strings`: contains only one string that does not include the substring
  - `substring`: is a non-empty string that does not exist in the single element of `strings`

- **Class**:
  - `strings`: contains multiple strings, some of which include the substring
  - `substring`: is a non-empty string that exists in some elements of `strings`

- **Class**:
  - `strings`: contains multiple strings, all of which include the substring
  - `substring`: is a non-empty string that exists in all elements of `strings`

- **Class**:
  - `strings`: contains multiple strings, none of which include the substring
  - `substring`: is a non-empty string that does not exist in any element of `strings`

- **Class**:
  - `strings`: contains only one string that includes the substring
  - `substring`: is null

- **Class**:
  - `strings`: contains multiple strings, some of which include the substring
  - `substring`: is null

- **Class**:
  - `strings`: contains multiple strings, all of which include the substring
  - `substring`: is null

- **Class**:
  - `strings`: contains multiple strings, none of which include the substring
  - `substring`: is null

These equivalence classes should cover a wide range of scenarios and edge cases for the `filter_by_substring` method.