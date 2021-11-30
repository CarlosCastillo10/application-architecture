package Database;

import Model.Group;
import Model.Student;

import java.util.List;
import java.util.Optional;

/**
 * @author carloscastillo
 * @author andrespalacios
 * @author gersonsantos
 */
public class DataRepository {
    private static List<Student> students;
    static {
        students = List.of(
                new Student(1, "cacastillo19@utpl.edu.ec", "Carlos Castillo"),
                new Student(2, "aepalacios7@utpl.edu.ec", "Andrés Palacios"),
                new Student(3, "gmsantos2@utpl.edu.ec", "Gerson Santos")
        );
    }

    private static Group group = new Group(7, students);

    /**
     *
     * @return Group object
     */
    public static Group getGroup(){
        return group;
    }

    /**
     * Search a student according to their position
     * @param pos: Student position
     * @return Optional
     */
    public static Optional<Student> searchStudentByPos(int pos){
        return group.students().stream().filter(student -> student.pos() == pos).findFirst();
    }
}
