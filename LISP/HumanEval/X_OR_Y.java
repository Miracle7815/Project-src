package humaneval.correct;
public class X_OR_Y {
    public static int x_or_y(int n, int x, int y) {
        if (n == 1) return y;
        for (int i = 2; i < n; i += 1) {
            if (n % i == 0) return y;
        }
        return x;
    }
}
