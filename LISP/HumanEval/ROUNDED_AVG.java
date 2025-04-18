package humaneval.correct;
public class ROUNDED_AVG {
    public static String rounded_avg(int n, int m) {
        if(m < n) return "-1";
        int summation = 0;
        for(int i = n; i < m + 1; i++) {
            summation += i;
        }
        double avg = ((double) summation)/((double) (m - n + 1));
        double rem = avg - Math.floor(avg);
        int avg_rounded = 0;
        if(rem <= 0.5) {
            avg_rounded = (int) Math.floor(avg);
        } else {
            avg_rounded = (int) Math.ceil(avg);
        }
        return Integer.toBinaryString(avg_rounded);
    }
}
