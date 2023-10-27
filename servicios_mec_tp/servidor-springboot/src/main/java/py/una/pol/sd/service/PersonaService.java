package py.una.pol.sd.service;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import py.una.pol.sd.model.Persona;
import py.una.pol.sd.repository.PersonaRepository;

@Service
public class PersonaService {


    @Autowired
    PersonaRepository repository;
  
    public List<Persona> getPersonas(){

        return repository.findAll();
    }      
    
    public Persona crear(Persona p){

        return repository.save(p);
    }

    public boolean eliminarPorCedula(Integer cedula) {
        if (cedula == null) {
            return false; // Cédula inválida
        }
        try {
            repository.deleteById(cedula);
            return true; // Si la persona no existe en la base de datos
        } catch (Exception e) {
            e.printStackTrace(); // Imprimir el stack trace para entender el error
            return false;
        }
    }

    public Persona actualizarBecar(Integer cedula, String becar) {
        Persona persona = repository.findByCedula(cedula);
        if (persona != null) {
            persona.setBecar(becar); // Establece el valor "SI" en el campo becar
            return repository.save(persona);
        } else {
            return null; // Persona no encontrada
        }
    }

    
    
}
