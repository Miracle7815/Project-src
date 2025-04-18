package humaneval.correct;
public class IS_MULTIPLY_PRIME {
    public static boolean is_prime(int n) {
        for (int i = 2; i < n; i += 1) {
            if (n % i == 0)
                return false;
        }
        return true;
    }
    public static boolean is_multiply_prime(int a) {
        for (int i = 2; i < a; i += 1){
            if (! is_prime(i)) continue;
            for (int j = i; j < a; j += 1) {
                if (! is_prime(j)) continue;
                for (int k = j; k < a; k += 1) {
                    if (! is_prime(k)) continue;
                    if (i * j * k == a)
                        return true;
                }
            }
        }
        return false;
    }
}
