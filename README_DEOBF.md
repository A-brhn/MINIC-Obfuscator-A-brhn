# De-Obfuscator for MINIC (drop-in)

Add `deobfuscator.py` to the project root.

## Usage

```bash
# Example: deobfuscate the obfuscated code from example.txt -> example_deobf.txt
python deobfuscator.py -i example_obf.txt -o example_deobf.txt --prettify
```

What it reverses (based on the obfuscator in this repo):

- Removes `if (false) { ... }` and `while (false) { ... }` blocks entirely.
- Removes obvious dead declarations like `int unused = 1234;`, `int nothing = 0;`, `int dummy = 0;`.
- Rewrites `a - (-b)` back to `a + b` and `i = i - (-1)` to `i = i + 1`.
- Optional: renames locals sequentially (v1, v2, ...) to improve readability after random renaming.


## Control-Flow Flattening Recovery

This extended deobfuscator attempts to reverse simple `while(selector){ switch(selector){ case ... } }` patterns and reconstruct the original straight-line code where possible.
