package humaneval.correct;
public class TRI {
    public static int[] tri(int n) {
        int[] sequence = new int[n + 1];
        if(n == 0) {
            sequence[0] = 1;
            return sequence;
        }
        sequence[0] = 1;
        sequence[1] = 3;
        for(int i = 2; i < n + 1; i++) {
            if(i % 2 == 0) sequence[i] = i / 2 + 1;
            else sequence[i] = sequence[i - 1] + sequence[i - 2] + (i + 3) / 2;
        }
        return sequence;
    }
}
