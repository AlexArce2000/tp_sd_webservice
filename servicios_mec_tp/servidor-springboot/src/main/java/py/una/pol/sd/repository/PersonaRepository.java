package py.una.pol.sd.repository;

import java.util.List;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import py.una.pol.sd.model.Persona;

@Repository
public interface PersonaRepository extends CrudRepository<Persona, Integer> {

    List<Persona> findAll();

    List<Persona> findByNombre(String nombre);

    List<Persona> findByApellido(String apellido);

    Persona findByCedula(Integer id);

    //AGREGADO
    List<Persona> findByCalificacion(Integer calificacion);

    List<Persona> findByComentariocalif(String comentariocalif);

    List<Persona> findByMaterias(String materias);

    List<Persona> findByFechanacimiento(String fechanacimiento);

    List<Persona> findByPromedio(Double promedio);

    List<Persona> findByHistorialviajes(String historialviajes);

    List<Persona> findByInfodeviajes(String infodeviajes);

    List<Persona> findBySituacioneconomica(String situacioneconomica);

    List<Persona> findByAnioegreso(Integer anioegreso);

    List<Persona> findByMatriculadocente(String matriculadocente);

    List<Persona> findByLugartrabajodocente(String lugartrabajodocente);

    List<Persona> findByBecar(String becar);

}
