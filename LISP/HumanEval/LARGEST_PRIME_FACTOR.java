package humaneval.correct;
public class LARGEST_PRIME_FACTOR {
    public static boolean is_prime(int k) {
        if (k < 2)
            return false;
        for (int i = 2; i < k; i += 1){
            if (k % i == 0)
                return false;
        }
        return true;
    }
    public static int largest_prime_factor(int n) {
        int largest = 1;
        for (int j = 2; j < n; j += 1) {
            if (n % j == 0 && is_prime(j)){
                largest = j;
            }
        }
        return largest;
    }
}
