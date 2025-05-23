package humaneval.correct;
public class SEARCH {
    public static int search(int[] lst) {
        int max = -1;
        for (Integer i : lst) {
            if (i > max)
                max = i;
        }
        int result = -1;
        int[] frq = new int[max + 1];
        for (int i = 0; i < lst.length; i += 1)  frq[lst[i]] += 1;
        for (int i = 0; i < frq.length; i += 1) if (frq[i] >= i && frq[i] > 0) result = i;
        
        return result;
    }
}
