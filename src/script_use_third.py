/* Mozilla Public License Version 2.0
 * Copyright (c) 2025 Example Author
 */

# SPDX-License-Identifier: MIT
import os
def read_lib_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
if __name__ == '__main__':
    print('Reading libA_1.c header:')
    print(read_lib_file('third_party/libA/libA_1.c').splitlines()[:5])
