/* MIT License
 * Copyright (c) 2025 Example Author
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction...
 */

#include <stdio.h>
#include "libA_1.h"
#include "libB_1.h"
#include "libC_1.h"

int util_func(int);

int main(void) {
    printf("AutoFOSS Demo Start\n");
    int a = libA_1_func(10);
    int b = libB_1_func(20);
    int c = libC_1_func(30);
    int u = util_func(a + b + c);
    printf("Result: %d\n", u);
    return 0;
}
