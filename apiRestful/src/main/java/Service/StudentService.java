package Service;

import Database.DataRepository;
import Model.Student;
import com.google.gson.Gson;
import spark.Request;
import java.util.List;
import static spark.Spark.*;

/**
 * @author carloscastillo
 * @author jhandrylopez
 * author gersonsantos
 */

public class StudentService {
    public static void main(String[] args){

        get("/students", (req, res) -> {
           Gson gson = new Gson();
           res.type("application/json");
           return gson.toJson(DataRepository.getStudents());
        });


        get("/students/filter", (req, res) -> {
            var key = req.queryParams().stream().toList().get(0);
            Gson gson = new Gson();
            res.type("application/json");
            List<Student> students = validateFilter(key, req);

            if(students != null && !students.isEmpty()){
                res.status(200);
            }else{
                return halt(404);
            }

            return gson.toJson(students);
        });


        get("/student/:pos", (req, res) -> {
            var pos = Integer.parseInt(req.params(":pos"));
            Gson gson = new Gson();
            res.type("application/json");
            Student student = DataRepository.searchStudentByPos(pos);
            if(student != null){
                res.status(200);
            }else{
                halt(404);
            }
            return gson.toJson(student);
        });


        post("/student", (req, res) -> {
            var dataStudent = req.body().toString();
            int position = DataRepository.addStudent(dataStudent);
            res.type("application/json");

            if(position > 0){
                res.status(201);
            }else{
                halt(400);
            }

            return "Location: https://88e4-190-110-60-131.ngrok.io/student/" + position;
        });


        put("/student/:pos", (req, res) -> {
            var pos = Integer.parseInt(req.params(":pos"));
            var dataStudent = req.body().toString();
            int position = DataRepository.putStudent(pos, dataStudent);
            res.type("application/json");

            if(position > 0){
                res.status(204);
            }else{
                halt(409);
            }
            return halt(204);
        });


        delete("/student/:pos", (req, res) -> {
            try {
                var pos = Integer.parseInt(req.params(":pos"));
                DataRepository.deleteStudentByPos(pos);
                res.type("application/json");
                res.status(204);
            }catch (Exception e){
                halt(400);
            }

            return halt(204);
        });

    }

    private static List<Student> validateFilter(String key, Request req){
        try {
            var value = req.queryParams(key);
            List<Student> students = null;
            if(key.equals("name")){
                students = DataRepository.searchStudentByName(value);
            }else{
                if(key.equals("lastname")){
                    students = DataRepository.searchStudentByLastname(value);
                }else{
                    if(key.equals("age")){
                        students = DataRepository.searchStudentByAge(Integer.parseInt(value));
                    }
                }
            }
            return students;
        }catch(Exception e){
            return null;
        }
    }
}
