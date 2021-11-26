package Model;

/**
 * @author carloscastillo
 */
public class Student{

    private String name;
    private String lastname;
    private int age;

    public Student(){}

    public Student(String name, String lastname, int age){
        this.name= name;
        this.lastname = lastname;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
