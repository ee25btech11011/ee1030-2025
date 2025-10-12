// code15.c
#include <stdio.h>
#include <math.h>

void roots(double *root1, double *root2) {
    double a = 6.0, b = -1.0, c = -2.0;
    double discriminant = b*b - 4*a*c;

    if (discriminant >= 0) {
        *root1 = (-b + sqrt(discriminant)) / (2*a);
        *root2 = (-b - sqrt(discriminant)) / (2*a);
    } else {
        *root1 = NAN;
        *root2 = NAN;
    }
}
