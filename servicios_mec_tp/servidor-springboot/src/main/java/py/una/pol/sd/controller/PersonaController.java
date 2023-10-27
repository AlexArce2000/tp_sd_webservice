package py.una.pol.sd.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import py.una.pol.sd.model.Persona;
import py.una.pol.sd.service.PersonaService;

@RestController
@RequestMapping("/personas")
public class PersonaController {

	@Autowired
	PersonaService personaService;

	@GetMapping("/saludo")
	public String index() {
		return "Hola mundo caluroso de Springboot";
	}

    @GetMapping(value = "/listar", produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE} )
    public ResponseEntity<List<Persona>> getPersonas() 
	{
		List<Persona> r = personaService.getPersonas();

		return new ResponseEntity<>(r, HttpStatus.OK);
    }

    @GetMapping(value = "listar_todos_estudiantes", produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE} )
    public ResponseEntity<List<Persona>> getEstudiantes() 
	{
		List<Persona> r = personaService.getPersonas();

		return new ResponseEntity<>(r, HttpStatus.OK);
    }

    @GetMapping(value = "listar_estudiante", produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE} )
    public ResponseEntity<List<Persona>> getEstudiante() 
	{
		List<Persona> r = personaService.getPersonas();

		return new ResponseEntity<>(r, HttpStatus.OK);
    }
    @GetMapping(value = "listar_docente", produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE} )
    public ResponseEntity<List<Persona>> getDocente() 
	{
		List<Persona> r = personaService.getPersonas();

		return new ResponseEntity<>(r, HttpStatus.OK);
    }
    @GetMapping(value = "listar_todos_docentes", produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE} )
    public ResponseEntity<List<Persona>> getDocentes() 
	{
		List<Persona> r = personaService.getPersonas();

		return new ResponseEntity<>(r, HttpStatus.OK);
    }

    @GetMapping(value = "listar_calif", produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE} )
    public ResponseEntity<List<Persona>> getCalif() 
	{
		List<Persona> r = personaService.getPersonas();

		return new ResponseEntity<>(r, HttpStatus.OK);
    }

    @GetMapping(value = "listar_info_billetaje", produces = {MediaType.APPLICATION_JSON_VALUE, MediaType.APPLICATION_XML_VALUE} )
    public ResponseEntity<List<Persona>> getInfobilletaje() 
	{
		List<Persona> r = personaService.getPersonas();

		return new ResponseEntity<>(r, HttpStatus.OK);
    }


	@PostMapping(value = "/crear", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> create(@RequestBody Persona per) {


		if(per != null && per.getCedula() != null) {
			System.out.println("Persona recepcionada "+ per.getNombre());
			
			personaService.crear(per); 

			return new ResponseEntity<>("Se recepcionó correctamente la persona: " + per.toString(), HttpStatus.OK);
		}else{

			System.out.println("Datos mal enviados por el cliente");
			return new ResponseEntity<>("Debe enviar el campo cédula. ", HttpStatus.BAD_REQUEST);
		}


        
    }
	@DeleteMapping("/eliminar/{cedula}")
    public ResponseEntity<String> eliminarPersona(@PathVariable Integer cedula) {
        boolean eliminado = personaService.eliminarPorCedula(cedula);
        
        if (eliminado) {
            return new ResponseEntity<>("Persona con cédula " + cedula + " eliminada correctamente.", HttpStatus.OK);
        } else {
            return new ResponseEntity<>("No se encontró una persona con cédula " + cedula + ".", HttpStatus.NOT_FOUND);
        }
    }

	@PutMapping("/editar_becas/{cedula}")
	public ResponseEntity<String> actualizarBeca(@PathVariable Integer cedula, @RequestBody Map<String, String> requestBody) {
		String becar = requestBody.get("becar"); // Obtén el valor de "becar" del mapa
	
		// Llama al servicio para actualizar el campo 'becar'
		Persona personaActualizada = personaService.actualizarBecar(cedula, becar);
	
		if (personaActualizada != null) {
			return new ResponseEntity<>("Campo 'becar' de la persona con cédula " + cedula + " actualizado correctamente.", HttpStatus.OK);
		} else {
			return new ResponseEntity<>("No se encontró una persona con cédula " + cedula + ".", HttpStatus.NOT_FOUND);
		}
	}
	

	


	
	



}
