package humaneval.correct;
public class CHECK_IF_LAST_CHAR_IS_A_LETTER {
    public static boolean check_if_last_char_is_a_letter(String txt) {
        String[] parts = txt.split(" ");
        String last = " ";
        if(parts.length != 0) last = parts[parts.length - 1];
        if(txt.length() != 0 && txt.charAt(txt.length() - 1) == ' ') last = " ";
        if(txt.length() == 0) last = " ";
        int last_char_pos = Character.toLowerCase(last.charAt(0)) - 'a';
        return (last.length() == 1) && (0 <= last_char_pos && last_char_pos <= 25);
    }
}
