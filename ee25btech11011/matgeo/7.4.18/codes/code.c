#include <stdio.h>
#include <math.h>

// Function to compute the circle equation parameters
void solve_circle(double *params) {
    double a1 = params[0];
    double b1 = params[1];
    double c1 = params[2];
    double a2 = params[3];
    double b2 = params[4];
    double c2 = params[5];
    double area = params[6];

    // Use direct numeric value of pi
    double pi = 3.141592653589793;

    // Compute determinant to check if lines intersect
    double det = a1 * b2 - a2 * b1;
    if (fabs(det) < 1e-10) {
        printf("Lines are parallel or coincident. Cannot determine center.\n");
        return;
    }

    // Solve for intersection point (center)
    double rhs1 = -c1;
    double rhs2 = -c2;

    double h = (rhs1 * b2 - b1 * rhs2) / det;
    double k = (a1 * rhs2 - rhs1 * a2) / det;

    // Compute radius from area = πr²
    if (area <= 0) {
        printf("Area must be positive.\n");
        return;
    }
    double r = sqrt(area / pi);

    // Compute circle coefficients
    double D = -2 * h;
    double E = -2 * k;
    double F = h * h + k * k - r * r;

    // Store results in params array
    params[7] = h;
    params[8] = k;
    params[9] = r;
    params[10] = D;
    params[11] = E;
    params[12] = F;
}

int main() {
    double params[13];

    printf("Enter coefficients of first line (a1 b1 c1) for a1*x + b1*y + c1 = 0:\n");
    scanf("%lf %lf %lf", &params[0], &params[1], &params[2]);

    printf("Enter coefficients of second line (a2 b2 c2) for a2*x + b2*y + c2 = 0:\n");
    scanf("%lf %lf %lf", &params[3], &params[4], &params[5]);

    printf("Enter area of the circle (numeric):\n");
    scanf("%lf", &params[6]);

    solve_circle(params);

    printf("\n--- Results ---\n");
    printf("Center (h, k): (%.3f, %.3f)\n", params[7], params[8]);
    printf("Radius: %.3f\n", params[9]);
    printf("Equation: x^2 + y^2 %+.3fx %+.3fy %+.3f = 0\n",
           params[10], params[11], params[12]);

    return 0;
}
