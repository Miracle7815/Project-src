package humaneval.correct;
import java.util.ArrayList;
import java.util.List;
public class PARSE_NESTED_PARENS {
    public static List<Integer> parse_nested_parens(String paren_string) {
        String[] paren_groups = paren_string.split(" ");
        List<Integer> result = new ArrayList<Integer>();
        for (String paren_group : paren_groups) {
            int depth = 0;
            int max_depth = 0;
            for (char c : paren_group.toCharArray()){
                if (c == '('){
                    depth += 1;
                    max_depth = Math.max(depth, max_depth);
                } else {
                    depth -= 1;
                }
            }
            result.add(max_depth);
        }
        return result;
    }
}
