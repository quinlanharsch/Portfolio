package Checkpoint3;

public class Student {
    private String name;
    private double gpa;
    private String major;
    private void printInfo(){
        System.out.println("Name= "+this.name+
                         "\nGPA = "+this.gpa+
                         "\nMajor = "+this.major);
    }
    public static void main(String[] args){
        //Test Class
        Student s1 = new Student();
        s1.name = "Bob";
        s1.gpa = 3.46;
        s1.major = "Computer Science";

        Student s2 = new Student();
        s2.name = "Emma";
        s2.gpa = 3.98;
        s2.major = "Nuclear Engeneering";

        s1.printInfo();
        s2.printInfo();
    }
}