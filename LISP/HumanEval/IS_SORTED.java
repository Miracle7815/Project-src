package humaneval.correct;
import java.util.HashMap;
public class IS_SORTED {
    public static boolean is_sorted(int[] lst) {
        HashMap<Integer, Integer> count_num = new HashMap<>();
        for(int i = 0; i < lst.length; i++) {
            count_num.put(lst[i], 0);
        }
        for(int i = 0; i < lst.length; i++) {
            count_num.put(lst[i], count_num.get(lst[i]) + 1);
        }
        for(int i = 0; i < lst.length; i++) {
            if(count_num.get(lst[i]) > 2) return false;
        }
        for(int i = 0; i < lst.length - 1; i++) {
            if(lst[i] > lst[i + 1]) return false;
        }
        return true;
    }
}
