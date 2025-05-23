package humaneval.correct;
public class FIND_CLOSEST_ELEMENTS {
    public static double[] find_closest_elements(double[] numbers) {
        double[] result = new double[2];
        double distance = Double.MAX_VALUE;
        for (int i = 0; i < numbers.length; i += 1){
            for (int j = i + 1; j < numbers.length; j += 1){
                double new_distance = Math.abs(numbers[i] - numbers[j]);
                if (new_distance < distance){
                    distance = new_distance;
                    if (numbers[i] < numbers[j]){
                        result[0] = numbers[i];
                        result[1] = numbers[j];
                    } else{
                        result[0] = numbers[j];
                        result[1] = numbers[i];
                    }
                }
            }
        }
        return result;
    }
}
