Based on the provided API method, we can identify the following input parameters that need to be considered for partitioning the equivalence classes:

- class:
    1. `s`: is null; 2. `n`: can be any integer
- class:
    1. `s`: is an empty string; 2. `n`: can be any integer
- class:
    1. `s`: contains words with the exact number of consonants equal to `n`; 2. `n`: can be any integer
- class:
    1. `s`: contains words with the number of consonants not equal to `n`; 2. `n`: can be any integer
- class:
    1. `s`: contains words with special characters or numbers; 2. `n`: can be any integer
- class:
    1. `s`: contains words with only vowels; 2. `n`: can be any integer

By testing the API method with inputs from each of these equivalence classes, we can ensure comprehensive coverage of the functionality provided by the `select_words` method.