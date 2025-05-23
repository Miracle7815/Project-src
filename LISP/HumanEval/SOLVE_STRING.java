package humaneval.correct;
public class SOLVE_STRING {
    public static String solve_string(String s) {
        int flg = 0;
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isAlphabetic(c)){
                if (Character.isLowerCase(c)) sb.append(Character.toUpperCase(c));
                else sb.append(Character.toLowerCase(c));
                flg = 1;
            }
            else sb.append(c);
        }
        if (flg == 0) {
            sb = new StringBuilder();
            for (int i = s.length() - 1; i >= 0; i -= 1) sb.append(s.charAt(i));
        }
        return sb.toString();
    }
}
