package humaneval.correct;
import java.util.ArrayList;
import java.util.Arrays;
public class GET_CLOSET_VOWEL {
    public static String get_closet_vowel(String word) {
        if(word.length() < 3) return "";
        ArrayList<Character> vowels = new ArrayList<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        for(int i = word.length() - 2; i > 0; i--) {
            if(vowels.contains(word.charAt(i))) {
                if(!vowels.contains(word.charAt(i + 1)) && !vowels.contains(word.charAt(i - 1))) {
                    return word.substring(i, i + 1);
                }
            }
        }
        return "";
    }
}
