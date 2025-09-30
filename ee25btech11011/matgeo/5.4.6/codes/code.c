#include <stdio.h>

void compute_inverse(double* inv) {
    double a = 10, b = -2;
    double c = -5, d = 1;

    double det = a*d - b*c;

    if(det == 0) {
        // Fill zero if not invertible
        inv[0] = inv[1] = inv[2] = inv[3] = 0;
    } else {
        // Fill inverse in row-major order
        inv[0] = d/det;   // [0,0]
        inv[1] = -b/det;  // [0,1]
        inv[2] = -c/det;  // [1,0]
        inv[3] = a/det;   // [1,1]
    }
}
