package humaneval.correct;
public class DECODE_SHIFT {
    public static String encode_shift(String string){
        StringBuilder sb = new StringBuilder();
        for (char c : string.toCharArray()) {
            c = (char)((((int) c + 5 - (int)('a')) % 26) + (int)('a'));
            sb.append(c);
        }
        return sb.toString();
    }
    public static String decode_shift(String string) {
        StringBuilder sb = new StringBuilder();
        for (char c : string.toCharArray()) {
            c = (char)((((int) c + 21 - (int)('a')) % 26) + (int)('a'));
            sb.append(c);
        }
        return sb.toString();
    }
}
