package humaneval.correct;
public class FILE_NAME_CHECK {
    public static String file_name_check(String file_name) {
        String[] lst = file_name.split("\\.");
        if (lst.length != 2)
            return "No";
        if (! (lst[1].equals("txt") || lst[1].equals("exe") || lst[1].equals("dll")))
            return "No";
        if (lst[0].length() == 0)
            return "No";
        if (! (('a' <= lst[0].charAt(0) && lst[0].charAt(0) <= 'z') || ('A' <= lst[0].charAt(0) && lst[0].charAt(0) <= 'Z')))
            return "No";
        int digit_cnt = 0;
        for (char c : file_name.toCharArray()){
            if ('0' <= c && c <= '9')
                digit_cnt += 1;
        }
        if (digit_cnt > 3)  return "No";
        return "Yes";
    }
}
