package humaneval.correct;
import java.util.ArrayList;
public class MIN_SUBARRAY_SUM {
    public static long min_subarray_sum(ArrayList<Long> nums) {
        long max_sum = 0;
        long s = 0;
        for(long num : nums) {
            s += -num;
            if(s < 0) {
                s = 0;
            }
            max_sum = Math.max(s, max_sum);
        }
        if(max_sum == 0) {
            max_sum = -nums.get(0);
            for(int i = 1; i < nums.size(); i++) {
                max_sum = Math.max(max_sum, -nums.get(i));
            }
        }
        long min_sum = -max_sum;
        return min_sum;
    }
}
