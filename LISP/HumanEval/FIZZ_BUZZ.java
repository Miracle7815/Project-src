package humaneval.correct;
public class FIZZ_BUZZ {
    public static int fizz_buzz(int n) {
        int result = 0;
        for (int i = 0; i < n; i += 1){
            if (i % 11 == 0 || i % 13 == 0) {
                for (int j = 0; j < (i + "").length(); j += 1){
                    if ((i + "").substring(j, j + 1).equals("7"))
                        result += 1;
                }
            }
        }
        return result;
    }
}
