package Database;

import Model.Student;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

/**
 * @author carloscastillo
 * @author jhandrylopez
 * author gersonsantos
 */
public class DataRepository {

    private static List<Student> students;

    static {
        students = List.of(
             new Student("Carlos", "Castillo", 22),
             new Student("Carlos", "Lopez", 21),
             new Student("Jhandry", "Lopez", 24),
             new Student("Gerson", "Santos", 21)
        );
    }


    public static List<Student> getStudents(){
        return students;
    }


    public static Student searchStudentByPos(int pos){
        pos -= 1;
        if(pos < students.size() && pos >= 0){
            return students.get(pos);
        }
        return null;
    }


    public static List<Student> searchStudentByName(String name){
        return students.stream().filter(student ->
                student.getName().toLowerCase().equals(name.toLowerCase())
        ).collect(Collectors.toList());
    }


    public static List<Student> searchStudentByLastname(String lastname){
        return students.stream().filter(student ->
                student.getLastname().toLowerCase().equals(lastname.toLowerCase())
        ).collect(Collectors.toList());
    }


    public static List<Student> searchStudentByAge(int age){
        return students.stream().filter(student ->
                student.getAge() == age
        ).collect(Collectors.toList());
    }


    public static int addStudent(String dataStudent) throws IOException {
        try {
            ArrayList<Student> tmpStudents = new ArrayList<>();
            Student student = new ObjectMapper().readValue(dataStudent, Student.class);
            for(int index = 0; index < students.size(); index++){
                tmpStudents.add(students.get(index));
                if(index == students.size() - 1){
                    tmpStudents.add(student);
                }
            }
            students = tmpStudents;
        }catch (Exception e){
            return 0;
        }
        return students.size();
    }


    public static int putStudent(int pos, String dataStudent) throws IOException {
        try{
            ArrayList<Student> tmpStudents = new ArrayList<>();
            pos -= 1;
            Student student = new ObjectMapper().readValue(dataStudent, Student.class);
            if(pos < students.size() && pos >= 0){
                for(int index = 0; index < students.size(); index++){
                    if(index != pos){
                        tmpStudents.add(students.get(index));
                    }else{
                        tmpStudents.add(student);
                    }
                }
                students = tmpStudents;
            }else{
                return -1;
            }
        }catch (Exception e){
            return 0;
        }
        return pos + 1;
    }


    public static void deleteStudentByPos(int pos){
        ArrayList<Student> tmpStudents = new ArrayList<>();
        pos -= 1;
        if(pos < students.size() && pos >= 0){
            for(int index = 0; index < students.size(); index++){
                if(index != pos){
                    tmpStudents.add(students.get(index));
                }
            }
            students = tmpStudents;
        } else {
            throw new RuntimeException("");
        }

    }
}
