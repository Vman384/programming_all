import java.text.CollationElementIterator;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class GradeRegister {
    private ArrayList<Integer> gradeRegister;
    private Integer numberPassed;

    public GradeRegister() {
        this.gradeRegister = new ArrayList<>();
        this.numberPassed = 0;
    }

    public void addGrade(Integer grade){
        this.gradeRegister.add(grade);
    }

    public ArrayList getgradeRegister(){
        return this.gradeRegister;
    }

    public Integer averagePassing(int passGrade){
        int total = 0;
        for (int grade : this.gradeRegister){
            if (grade>=passGrade){
                total += grade;
                this.numberPassed += 1;
            }
        }
        int average = total / this.gradeRegister.size();
        return average;
    }

    public Integer passPercent(int passGrade){
        this.numberPassed = 0;
        this.averagePassing(passGrade);
        int passPercent = this.numberPassed / this.gradeRegister.size() * 100;
        return passPercent;
    }

    public ArrayList<String> gradeDistribution(){
        String less50 = "";
        String less60 = "";
        String less70 = "";
        String less80 = "";
        String less90 = "";
        String more90 = "";
        for (Integer grade : gradeRegister) {
            if (grade <= 50) {
                less50 += "*";
            }  else if (grade < 60) {
                less60+= "*";
            }else if (grade < 70) {
                less70+= "*";
            }else if (grade < 80) {
                less80+= "*";
            }
            else if (grade<90){
                    less90+="*";
            }
            else{
                more90 += "*";
            }       
        }
        ArrayList<String> dist = new ArrayList<String>();
        Collections.addAll(dist, less50,less60,less70,less80,less90,more90);
        return dist;
    }
}
