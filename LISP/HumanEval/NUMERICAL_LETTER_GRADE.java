package humaneval.correct;
public class NUMERICAL_LETTER_GRADE {
    public static String[] numerical_letter_grade(double[] grades) {
        String[] letter_grade = new String[grades.length];
        for (int i = 0; i < grades.length; i += 1) {
            double gpa = grades[i];
            if (gpa == 4.0)
                letter_grade[i] = "A+";
            else if (gpa > 3.7)
                letter_grade[i] = "A";
            else if (gpa > 3.3)
                letter_grade[i] = "A-";
            else if (gpa > 3.0)
                letter_grade[i] = "B+";
            else if (gpa > 2.7)
                letter_grade[i] = "B";
            else if (gpa > 2.3)
                letter_grade[i] = "B-";
            else if (gpa > 2.0)
                letter_grade[i] = "C+";
            else if (gpa > 1.7)
                letter_grade[i] = "C";
            else if (gpa > 1.3)
                letter_grade[i] = "C-";
            else if (gpa > 1.0)
                letter_grade[i] = "D+";
            else if (gpa > 0.7)
                letter_grade[i] = "D";
            else if (gpa > 0.0)
                letter_grade[i] = "D-";
            else
                letter_grade[i] = "E";
        }
        return letter_grade;
    }
}
