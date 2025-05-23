package humaneval.correct;
import java.util.ArrayList;
public class EXCHANGE {
    public static String exchange(ArrayList<Integer> lst1, ArrayList<Integer> lst2) {
        int odd = 0, even = 0;
        for(int i : lst1) {
            if((i % 2) == 1) odd++;
        }
        for(int i : lst2) {
            if((i % 2) == 0) even++;
        }
        if(even >= odd) {
            return "YES";
        }
        return "NO";
    }
}
