package humaneval.correct;
public class GET_MAX_TRIPLES {
    public static int get_max_triples(int n) {
        int[] A = new int[n];
        for (int i = 1; i <= n; i += 1)
            A[i - 1] = i * i - i + 1;
        
        int result = 0;
        for (int i = 0; i < n-2; i += 1) {
            for (int j = i + 1; j < n-1; j += 1) {
                for (int k = j + 1; k < n; k += 1) {
                    if ((A[i] + A[j] + A[k]) % 3 == 0) result += 1;
                }
            }
        }
        return result;
    }
}
