#include <stdio.h>
#include <math.h>

// Function to compute real roots of (p+1)(p^2 + 1)^2 = 0
// Returns number of real roots and stores them in p_real array
int solve_real_p(double *p_real) {
    int count = 0;

    // Factor 1: (p+1) = 0
    p_real[count++] = -1;

    // Factor 2: (p^2 + 1)^2 = 0 -> p^2 + 1 = 0
    // Check for real roots
    double discriminant = -1;  // p^2 = -1
    if (discriminant >= 0) {
        p_real[count++] = sqrt(discriminant);
        p_real[count++] = -sqrt(discriminant);
    }

    return count;  // number of real roots
}
