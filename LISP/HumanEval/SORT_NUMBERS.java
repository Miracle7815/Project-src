package humaneval.correct;
import java.util.*;
public class SORT_NUMBERS {
    public static String sort_numbers(String numbers) {
        final HashMap<String, Integer> value_map = new HashMap<String, Integer>();
        value_map.put("zero", 0);
        value_map.put("one", 1);
        value_map.put("two", 2);
        value_map.put("three", 3);
        value_map.put("four", 4);
        value_map.put("five", 5);
        value_map.put("six", 6);
        value_map.put("seven", 7);
        value_map.put("eight", 8);
        value_map.put("nine", 9);
        ArrayList<String> number_array = new ArrayList<String>(Arrays.asList(numbers.split(" ")));
        Collections.sort(number_array, new Comparator<String>(){
            public int compare(String n1, String n2) {
                return value_map.get(n1) - value_map.get(n2);
            }
        });
        
        String result = "";
        for (String number : number_array){
            result += number + " ";
        }
        return result.trim();
    }
}
