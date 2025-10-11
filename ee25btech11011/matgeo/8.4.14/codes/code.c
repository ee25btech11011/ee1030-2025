#include <stdio.h>
#include <math.h>

int main() {
    // Ellipse: x^2 + 4y^2 = 4
    // Latus rectum endpoints y < 0
    double x1 = sqrt(3.0);
    double x2 = -sqrt(3.0);
    double y1 = -0.5;
    double y2 = -0.5;

    // Midpoint (vertex of parabola)
    double vx = (x1 + x2) / 2.0;
    double vy = (y1 + y2) / 2.0;

    // Length of latus rectum
    double L = x1 - x2; // horizontal distance
    double a = L / 4.0; // parabola parameter

    // Parabola equations: x^2 = 4a(y - vy)
    // Case 1: a positive
    double f1 = -4 * a * vy; // move vy to RHS
    printf("Equation of parabola 1:\n");
    printf("x^2 - %.3lf*y = %.3lf\n", 4*a, f1);

    // Case 2: a negative
    a = -a;
    double f2 = -4 * a * vy;
    printf("Equation of parabola 2:\n");
    printf("x^2 - %.3lf*y = %.3lf\n", 4*a, f2);

    return 0;
}
