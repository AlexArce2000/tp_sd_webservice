package py.una.pol.sd.model;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class Persona {

  @Id
  private Integer cedula;
  private String nombre;
  private String apellido;
  private Integer calificacion;
  private String comentariocalif;
  private String materias;
  private String fechanacimiento;
  private Double promedio;
  private String historialviajes;
  private String infodeviajes;
  private String situacioneconomica;
  private Integer anioegreso;
  private String matriculadocente;
  private String lugartrabajodocente;
  private String becar;

public String getBecar(){
    return becar;
}

public void setBecar(String becar){
    this.becar = becar;
}


public Integer getAnioegreso(){
    return anioegreso;
}

public void setAnioegreso(Integer anioegreso){
    this.anioegreso = anioegreso;
}

  
public String getLugartrabajodocente() {
    return lugartrabajodocente;
}

public void setLugardetrabajo(String lugartrabajodocente) {
    this.lugartrabajodocente = lugartrabajodocente;
}

public String getMatriculadocente() {
    return matriculadocente;
}

public void setMatriculadocente(String matriculadocente) {
    this.matriculadocente = matriculadocente;
}

  
public String getSituacioneconomica() {
    return situacioneconomica;
}

public void setSituacioneconomica(String situacioneconomica) {
    this.situacioneconomica = situacioneconomica;
}

public String getInfodeviajes() {
    return infodeviajes;
}

public void setInfodeviajes(String infodeviajes) {
    this.infodeviajes = infodeviajes;
}

public String getHistorialviajes() {
    return historialviajes;
}

public void setHistorialviajes(String historialviajes) {
    this.historialviajes = historialviajes;
}

public Double getPromedio() {
    return promedio;
}

public void setPromedio(Double promedio) {
    this.promedio = promedio;
}

public String getFechanacimiento() {
    return fechanacimiento;
}

public void setFechanacimiento(String fechanacimiento) {
    this.fechanacimiento = fechanacimiento;
}


public String getMaterias() {
    return materias;
}

public void setMaterias(String materias) {
    this.materias = materias;
}

protected Persona() {}

  public Persona(Integer cedula, String nombre, String apellido, Integer calificacion, String comentariocalif,String materias,String fechanacimiento, Double promedio, String historialviajes, String infodeviajes, String situacioneconomica, String matriculadocente, String lugartrabajodocente, Integer anioegreso, String becar) {
    this.cedula = cedula;
    this.nombre = nombre;
    this.apellido = apellido;
    this.calificacion = calificacion;
    this.comentariocalif = comentariocalif;
    this.materias = materias;
    this.fechanacimiento = fechanacimiento;
    this.promedio = promedio;
    this.historialviajes = historialviajes;
    this.infodeviajes = infodeviajes;
    this.situacioneconomica = situacioneconomica;
    this.anioegreso = anioegreso;
    this.matriculadocente = matriculadocente;
    this.lugartrabajodocente = lugartrabajodocente;
    this.becar = becar;
  }

  @Override
  public String toString() {
    return String.format(
        "Persona[cedula=%d, nombre='%s', apellido='%s', calificacion='%d', comentariocalif='%s', materias='%s', fechanacimiento='%s', promedio='%.2f', historialviajes='%s', infodeviajes='%s', situacioneconomica='%s', matriculadocente='%s', becar='%s']",
        cedula, nombre, apellido, calificacion, comentariocalif, materias, fechanacimiento, promedio, historialviajes, infodeviajes, situacioneconomica, matriculadocente, becar);
  }

public Integer getCedula() {
    return cedula;
}

public String getNombre() {
    return nombre;
}

public String getApellido() {
    return apellido;
}

public Integer getCalificacion(){
    return calificacion;
}

public String getComentariocalif(){
    return comentariocalif;
}


public void setCedula(Integer cedula) {
    this.cedula = cedula;
}

public void setNombre(String nombre) {
    this.nombre = nombre;
}

public void setApellido(String apellido) {
    this.apellido = apellido;
}

public void setCalificacion(Integer calificacion){
    this.calificacion = calificacion;
}

public void setComentario_calif(String comentariocalif){
    this.comentariocalif = comentariocalif;
}
 
  
}
