package humaneval.correct;
public class DOUBLE_THE_DIFFERENCE {
    public static int double_the_difference(double[] lst) {
        int result = 0;
        for (Double d : lst) {
            if ((int) d.doubleValue() == d) {
                int d_int = (int) d.doubleValue();
                if (d_int % 2 == 1 && d_int >= 0) {
                    result += d_int * d_int;
                }
            }
        }
        return result;
    }
}
