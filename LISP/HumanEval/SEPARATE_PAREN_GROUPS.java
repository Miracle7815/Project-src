package humaneval.correct;
import java.util.ArrayList;
import java.util.List;
public class SEPARATE_PAREN_GROUPS {
    public static List<String> separate_paren_groups(String paren_string) {
        List<String> result = new ArrayList<String>();
        String current_string = "";
        int current_depth = 0;
        for (char c : paren_string.toCharArray()) {
            if (c == '('){
                current_depth += 1;
                current_string += String.valueOf(c);
            } else if (c == ')'){
                current_depth -= 1;
                current_string += String.valueOf(c);
                if (current_depth == 0){
                    result.add(current_string);
                    current_string = "";
                }
            }
        }
        return result;
    }
}
