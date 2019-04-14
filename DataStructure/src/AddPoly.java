
public class AddPoly {
    private static final int MAX_DEGREE = 50;

    public static void main(String[] args) {
        polynomial A = new polynomial(3, new float[]{4, 3, 5, 0});
        polynomial B = new polynomial(4, new float[]{3,1,0,2,1});

        polynomial C = new polynomial();
        C = C.addPoly(A, B);

        System.out.print("\n A(x) = ");
        polynomial.printPoly(A);
        System.out.print("\n B(x) = ");
        polynomial.printPoly(B);
        System.out.print("\n C(x) = ");
        polynomial.printPoly(C);

    }

    static class polynomial {
        int degree;
        float[] coef;

        private polynomial() {
            degree = 0;
            coef = new float[MAX_DEGREE];
        }

        private polynomial(int degree, float[] coef) {
            this.degree = degree;
            this.coef = coef;
        }

        private polynomial addPoly(polynomial A, polynomial B) {
            polynomial C = new polynomial();
            int A_index = 0, B_index = 0, C_index = 0;
            int A_degree = A.degree, B_degree = B.degree;
            C.degree = Math.max(A_degree, B_degree);

            while(A_index <= A.degree && B_index <= B.degree) {
                if (A_degree > B_degree) {
                    C.coef[C_index++] = A.coef[A_index++];
                    A_degree--;
                } else if (A_degree == B_degree) {
                    C.coef[C_index++] = A.coef[A_index++] + B.coef[B_index++];
                    A_degree--;
                    B_degree--;
                } else {
                    C.coef[C_index++] = B.coef[B_index++];
                    B_degree--;
                }
            }
            return C;
        }

        private static void printPoly(polynomial P) {
            int i, degree;
            degree = P.degree;

            for (i=0; i <= P.degree; i++) {
                System.out.print(String.format("%3.0fx^%d", P.coef[i], degree--));
                if (i < P.degree) System.out.print(" +");
            }
            System.out.println();
        }
    }
}

