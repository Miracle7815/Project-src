package humaneval.correct;
public class CLOSEST_INTEGER {
    public static int closest_integer(String value) {
        if (value.indexOf('.') >= 0) {
            while (value.charAt(value.length() - 1) == '0')
                value = value.substring(0, value.length() - 1);
        }
        double num = Double.parseDouble(value);
        int result = 0;
        if (value.length() >= 2 && value.substring(value.length() - 2).equals(".5")) {
            result = num > 0 ? (int)Math.ceil(num) : (int)Math.floor(num);
        } else if (value.length() > 0){
            result = (int)Math.round(num);
        }
        return result;
    }
}
