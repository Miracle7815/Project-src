package humaneval.correct;
import java.util.ArrayList;
import java.util.Collections;
public class UNIQUE_DIGITS {
    public static ArrayList<Integer> unique_digits(ArrayList<Integer> x) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        for(int i : x) {
            int num = i;
            boolean all_odd = true;
            while(num > 0) {
                int curr_digit = num % 10;
                if((curr_digit % 2) == 0) {
                    all_odd = false;
                    break;
                }
                num /= 10;
            }
            if(all_odd) {
                res.add(i);
            }
        }
        Collections.sort(res);
        return res;
    }
}
