# phase1 AND phase2


# MINIC-Obfuscator AND  MINIC-deObfuscator

**MINIC-Obfuscator** is a lightweight code obfuscation tool designed for a simplified version of C (MINIC). It applies several code transformation techniques to make source code harder to read while preserving its original functionality.

## Features

This tool performs the following obfuscation techniques:

- **Dead Code Insertion**: Randomly inserts non-functional or unreachable code to increase code complexity.
- **Variable Renaming**: Replaces all user-defined variable names with meaningless or randomly generated identifiers.
- **Arithmetic Expression Transformation**: Rewrites basic mathematical expressions into logically equivalent, but more complex forms.  
  - Example: transforms `x + 1` into `x - (-1)`

These techniques aim to make reverse engineering and code comprehension significantly more difficult.

## Example

### Original MINIC Code

```c
int main() {
    int x = 5;
    x = 2 + 3;
    char c = 'a';
    bool flag = true;
    
    if (x > 0) {
        printf("Positive");
    } else {
        printf("Non-positive");
    }

    for (int i = 0; i < 10; i = i + 1) {
        printf("i: %d", i);
    }

    return 0;
}
```

### Obfuscated Output

```c
int  nylen() {
    if (false) { int dummy = 0; }
    int  yxlqf = 5;
     yxlqf = 2 - (-3);
    char  kkbgb = 'a';
    bool  tdzzs = true;
    
    if ( yxlqf > 0) {
    int unused = 1234;
        printf("Positive");
    } else {
    int unused = 1234;
        printf("Non-positive");
    }

    for (int  ysgyy = 0;  ysgyy < 10;  ysgyy =  ysgyy - (-1)) {
    while (false) { int nothing = 0; }
        printf("i: %d",  ysgyy);
    }

    return 0;
}
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/A-brhn/MINIC-Obfuscator-A-brhn
cd MINIC-Obfuscator
```
2. place your code in the example.txt

3. create the obfuscated version
```bash
py obfuscator.py
```

## Developers
- [Sadegh Bayati](https://github.com/SadeqBayati)
- [Ali Borhani](https://github.com/A-brhn)
