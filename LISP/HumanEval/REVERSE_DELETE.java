package humaneval.correct;
import java.util.ArrayList;
public class REVERSE_DELETE {
    public static ArrayList<Object> reverse_delete(String s, String c) {
        String new_s = "";
        for(int i = 0; i < s.length(); i++) {
            if(c.indexOf(s.charAt(i)) == -1) {
                new_s += s.charAt(i);
            }
        }
        String reverse_s = "";
        for(int i = new_s.length() - 1; i >= 0; i--) {
            reverse_s += new_s.charAt(i);
        }
        ArrayList<Object> res = new ArrayList<>();
        res.add(new_s);
        res.add(reverse_s.equals(new_s));
        return res;
    }
}
