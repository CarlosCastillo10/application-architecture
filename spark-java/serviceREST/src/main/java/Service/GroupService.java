package Service;

import Database.DataRepository;
import com.google.gson.Gson;

import static spark.Spark.get;
import static spark.Spark.halt;

/**
 * @author carloscastillo
 * @author andrespalacios
 * @author gersonsantos
 */
public class GroupService {
    public static void main(String[] args){

        // http://0.0.0.0:4567/group/7
        get("/group/:nro_group", (req, res) -> {
            var nroGroup = Integer.parseInt(req.params(":nro_group"));
            Gson gson = new Gson();
            res.type("application/json");
            if(nroGroup == 7){
                res.status(200);
            }else{
                halt(404);
            }
            return gson.toJson(DataRepository.getGroup());
        });

        /**
         * http://0.0.0.0:4567/group/7/student/1
         * http://0.0.0.0:4567/group/7/student/2
         * http://0.0.0.0:4567/group/7/student/3
         */
        get("/group/:nro_group/student/:pos_student", (req, res) -> {
            var nroGroup = Integer.parseInt(req.params(":nro_group"));
            var pos = Integer.parseInt(req.params(":pos_student"));
            Gson gson = new Gson();
            res.type("application/json");

            var student = DataRepository.searchStudentByPos(pos);
            if(nroGroup == 7 && student.isPresent()){
                res.status(200);
            }else{
                halt(404);
            }

            return gson.toJson(student.get());
        });
    }
}
