package humaneval.correct;
public class FRUIT_DISTRIBUTION {
    public static int fruit_distribution(String s, int n) {
        int result = n;
        for (String str : s.split(" ")) {
            try {
                int cnt = Integer.parseInt(str);
                result -= cnt;
            } catch (Exception e) {
                continue;
            }
        }
        return result;
    }
}
