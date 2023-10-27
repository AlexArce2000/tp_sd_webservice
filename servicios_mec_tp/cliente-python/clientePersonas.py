import sys
import datetime
import configparser
import requests
from requests.structures import CaseInsensitiveDict
from requests.exceptions import HTTPError
import os

#Variables globales para verificacion
api_personas_url_base = None
archivo_config = 'ConfigFile.properties'



def cls():
    """
    Limpia la pantalla de la consola.
    """
    # Comprobamos si el sistema operativo es Windows o no
    if os.name == 'nt':
        _ = os.system('cls')  # Para sistemas Windows
    else:
        _ = os.system('clear')  # Para sistemas Unix/Linux

# Uso de la función cls para limpiar la pantalla
cls()

def cargar_variables():
    config_parser = configparser.RawConfigParser()
    config_parser.read(archivo_config)

    global api_personas_url_listar, api_personas_url_crear, api_personas_url_eliminar, api_personas_url_editar_becas, api_personas_url_listar_todos_estudiantes, api_personas_url_listar_estudiante, api_personas_url_listar_docente, api_personas_url_listar_todos_docentes, api_personas_url_listar_calif, api_personas_url_listar_info_billetaje
    api_personas_url_listar = config_parser.get('SeccionApi', 'api_personas_url_listar')
    api_personas_url_crear = config_parser.get('SeccionApi', 'api_personas_url_crear')
    api_personas_url_eliminar = config_parser.get('SeccionApi', 'api_personas_url_eliminar')
    api_personas_url_editar_becas = config_parser.get('SeccionApi', 'api_personas_url_editar_becas')
    api_personas_url_listar_todos_estudiantes = config_parser.get('SeccionApi', 'api_personas_url_listar_todos_estudiantes')
    api_personas_url_listar_estudiante = config_parser.get('SeccionApi', 'api_personas_url_listar_estudiante')
    api_personas_url_listar_docente = config_parser.get('SeccionApi','api_personas_url_listar_docente')
    api_personas_url_listar_todos_docentes = config_parser.get('SeccionApi','api_personas_url_listar_todos_docentes')
    api_personas_url_listar_calif = config_parser.get('SeccionApi','api_personas_url_listar_calif')
    api_personas_url_listar_info_billetaje = config_parser.get('SeccionApi','api_personas_url_listar_info_billetaje')


def crear(cedula: int, nombre, apellido, calificacion, comentariocalif, materias, fechanacimiento, promedio, historialviajes,infodeviajes, situacioneconomica, anioegreso, matriculadocente, lugartrabajodocente, becar):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {'cedula': cedula, 
             'nombre' : nombre,
             'apellido' : apellido,
             'calificacion' : calificacion, 
             'comentariocalif' : comentariocalif,
             'materias' : materias,
             'fechanacimiento': fechanacimiento,
             'promedio': promedio,
             'historialviajes': historialviajes,
             'infodeviajes' : infodeviajes,
             'situacioneconomica' :  situacioneconomica,
             'anioegreso' : anioegreso,
             'matriculadocente' : matriculadocente,
             'lugartrabajodocente' : lugartrabajodocente,
             'becar' : becar,
            }
    
    r = requests.post(api_personas_url_crear, headers=headers, json=datos)
    if (r.status_code >= 200 and r.status_code < 300):
        # Validar response
        print(r)
        
    else:
        print( "Error " + str(r.status_code))
        print(str(r.json()))


def listar():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {}

    r = requests.get(api_personas_url_listar, headers=headers, json=datos)
    if r.status_code == 200:
        # Validar response
        listado = r.json()
        for item in listado:
            print(f"Cédula: {item['cedula']}, Nombre: {item['nombre']}, Apellido: {item['apellido']}, Calificacion: {item['calificacion']}, Comentario: {item['comentariocalif']}")
        return listado
    else:
        print(f"Error {r.status_code}")
        return []
######################### GESTION DE DOCENTES ##################################
def listar_docente(matricula: int):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {}

    r = requests.get(api_personas_url_listar_docente, headers=headers, json=datos)
    if r.status_code == 200:
        listado = r.json()
        print("\nLista de docentes registrados: ")
        print("\n")
        for item in listado:
            if item['lugartrabajodocente'] is not None:
                if( item['matriculadocente']== matricula ):
                    print(f"Nombre: {item['nombre']}, Apellido: {item['apellido']}, Cedula: {item['cedula']}, Anio_de_egreso: {item['anioegreso']}, Matricula: {item['matriculadocente']} ,Lugar_de_Trabajo: {item['lugartrabajodocente']}")
        print("\n")
        return listado
    else:
        print(f"Error {r.status_code}")
        return []


def listar_todos_docentes():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {}

    r = requests.get(api_personas_url_listar_todos_docentes, headers=headers, json=datos)
    if r.status_code == 200:
        listado = r.json()
        print("\nLista de docentes registrados: ")
        print("\n")
        for item in listado:
            if item['lugartrabajodocente'] is not None:    
                print(f"Nombre: {item['nombre']}, Apellido: {item['apellido']}, Cedula: {item['cedula']}, Anio_de_egreso: {item['anioegreso']}, Matricula: {item['matriculadocente']} ,Lugar_de_Trabajo: {item['lugartrabajodocente']}")
        print("\n")
        return listado
    else:
        print(f"Error {r.status_code}")
        return []


#########################################################################################




######################### GESTION DE ESTUDIANTES ##################################
def listar_estudiante(ci:int):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {}

    r = requests.get(api_personas_url_listar_estudiante, headers=headers, json=datos)
    if r.status_code == 200:
        listado = r.json()
        print("\nLista de estudiantes registrados: ")
        print("\n")
        for item in listado:
            if item['lugartrabajodocente'] is None:
                if( item['cedula']== ci ):
                    print(f"Cédula: {item['cedula']}, Nombre: {item['nombre']}, Apellido: {item['apellido']}, Fecha_de_nacimiento: {item['fechanacimiento']}, Promedio: {item['promedio']}")        
        print("\n")
        return listado
    else:
        print(f"Error {r.status_code}")
        return []


def listar_todos_estudiantes():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {}

    r = requests.get(api_personas_url_listar_todos_estudiantes, headers=headers, json=datos)
    if r.status_code == 200:
        # Validar response
        listado = r.json()
        print("\nLista de estudiantes registrados: ")
        for item in listado:
                if item['lugartrabajodocente'] is None:     
                    print(f"Cédula: {item['cedula']}, Nombre: {item['nombre']}, Apellido: {item['apellido']}, Fecha_de_nacimiento: {item['fechanacimiento']}, Promedio: {item['promedio']}")        
        print("\n")
        return listado
    else:
        print(f"Error {r.status_code}")
        return []

#########################################################################################

def eliminar(cedula: int):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    url_eliminar = f"{api_personas_url_eliminar}/{cedula}"

    try:
        with requests.delete(url_eliminar, headers=headers) as r:
            r.raise_for_status()
            if r.status_code == 204:
                return True
            else:
                print(f"Persona con cédula {cedula} eliminada con éxito.")
                return False
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
        return False
    except Exception as err:
        print(f"Error: {err}")
        return False
    



######################### GESTION DE CALIFICACIONES ##################################
def listar_calif(ci:int):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {}
    
    flag=1
    r = requests.get(api_personas_url_listar_calif, headers=headers, json=datos)
    if r.status_code == 200:
        listado = r.json()
        print("\nLista de estudiantes registrados: ")
        print("\n")
        for item in listado:
            if item['lugartrabajodocente'] is None:
                if( item['cedula']== ci ):
                    flag=0
                    print(f"Nombre: {item['nombre']}, Apellido: {item['apellido']}, Materia: {item['cedula']}, Calificacion: {item['calificacion']} ,Comentario: {item['comentariocalif']}")        
        if(flag==1):
            print(f"El alumno con CI nro {ci} no se encuentra registrado")
        print("\n")
        return listado
    else:
        print(f"Error {r.status_code}")
        return []

    
##################################################################################
#######################     EDITAR BECAS    ######################################

def editar_becar(cedula: int, nuevobecar: str):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {
        'becar': nuevobecar
    }

    url = f"{api_personas_url_editar_becas}/{cedula}"  

    r = requests.put(url, json=datos, headers=headers)  # Enviar datos como JSON en el cuerpo de la solicitud

    if r.status_code == 200:
        print("Campo 'becar' actualizado correctamente.")
    else:
        print("Error al actualizar el campo 'becar'.")
        print("Respuesta del servidor: " + str(r.status_code))
        print(r.text)

##################################################################################


######################### GESTION DE CALIFICACIONES ##################################
def listar_info_billetaje(ci:int):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {}
    
    flag=1
    r = requests.get(api_personas_url_listar, headers=headers, json=datos)
    if r.status_code == 200:
        listado = r.json()
        print("\nLista de estudiantes registrados: ")
        print("\n")
        for item in listado:
            if item['lugartrabajodocente'] is None:
                if( item['cedula']== ci ):
                    flag=0
                    print(f"Historial de viajes: {item['historialviajes']}, Informe adicional: {item['infodeviajes']}")        
        if(flag==1):
            print(f"El alumno con CI nro {ci} no se encuentra registrado")
        print("\n")
        return listado
    else:
        print(f"Error {r.status_code}")
        return []

    
##################################################################################
######################### GESTION DE BECAS ##################################
def beca_listar(ci:int):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {}
    
    flag=1
    r = requests.get(api_personas_url_listar, headers=headers, json=datos)
    if r.status_code == 200:
        listado = r.json()
        print("\nLista de estudiantes registrados: ")
        print("\n")
        for item in listado:
            if item['lugartrabajodocente'] is None:
                if( item['cedula']== ci ):
                    flag=0
                    print(f"Nombre: {item['nombre']}, Apellido: {item['apellido']}, Promedio: {item['promedio']}, Situacion Economica: {item['situacioneconomica']}")        
        if(flag==1):
            print(f"El alumno con CI nro {ci} no se encuentra registrado")
        print("\n")
        return listado
    else:
        print(f"Error {r.status_code}")
        return []

    
##################################################################################
######################### GESTION DE BECAS ##################################
def beca_listar(ci:int):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    datos = {}
    
    flag=1
    r = requests.get(api_personas_url_listar, headers=headers, json=datos)
    if r.status_code == 200:
        listado = r.json()
        print("\nLista de estudiantes registrados: ")
        print("\n")
        for item in listado:
            if item['lugartrabajodocente'] is None:
                if( item['cedula']== ci ):
                    flag=0
                    print(f"Nombre: {item['nombre']}, Apellido: {item['apellido']}, Promedio: {item['promedio']}, Situacion Economica: {item['situacioneconomica']}, Becado: {item['becar']}")        
        if(flag==1):
            print(f"El alumno con CI nro {ci} no se encuentra registrado")
        print("\n")
        return listado
    else:
        print(f"Error {r.status_code}")
        return []

    
##################################################################################


#######################################################
######  Procesamiento principal
#######################################################

def mostrar_menu():
    print("Servicios:")
    print("1. Gestion de datos del docente")
    print("2. Gestion de datos del estudiante")
    print("3. Gestion de calificaciones")
    print("4. Gestion de billetaje electronico")
    print("5. Gestion de becas")
    print("6. Salir")

def main():
    #cargar_variables()

    while True:
        cls()
        print("Iniciando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        cargar_variables()

        mostrar_menu()
        opcion = input("Ingrese su opción: ")
#(cedula: int, nombre: str, apellido: str, calificacion: int, comentariocalif: str, materias: str, 
# fechanacimiento: str, promedio: float, historialviajes: str, infodeviajes: str,situacioneconomica: str, anioegreso: int, 
# matriculadocente: str, lugartrabajodocente: str, becar: str):

        if opcion == "9":
            cedula = int(input("Ingrese cedula: "))
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            calificacion = input("Ingrese calificacion: ")
            comentariocalif = (input("Ingrese comentario: "))
            materias = (input("Ingrese materia en caso de registrar estudiante: "))
            fechanacimiento = (input("Ingrese la fecha de nacimiento en caso de registrar estudiante: "))
            promedio = (input("Ingrese el promedio en caso de registrar estudiante: "))
            historialviajes = (input("Ingrese el historial de viajes en caso de registrar estudiante: "))
            infodeviajes = (input("Ingrese la informaciond de viajes en caso de registrar estudiante: "))
            sistuacioneconomica = (input("Ingrese la situacion economica en caso de registrar estudiante: "))
            anioegreso = (input("Ingrese el anio egreso en caso de ser docente: "))
            matriculadocente= input("Ingrese la matricula en caso de ser docente: ")
            lugartrabajodocente= input("Ingrese el lugar de trabajo de ser docente: ")
            becar= input("Ingrese si es becado o no SOLO: SI o NO: ")
            crear(cedula, nombre, apellido, calificacion, comentariocalif, materias,fechanacimiento, promedio,historialviajes, infodeviajes, sistuacioneconomica, anioegreso, lugartrabajodocente, matriculadocente,becar)
            i=input("Presione ENTER para continuar...")
        if opcion == "1":
            print("#####################################")
            print("# Información acerca de Docentes #")
            print("#####################################")
            print("1. Buscar docente")
            print("2. Listar docentes")
            op=int(input("Ingrese opción: "))
            if(op==1):
                matricula=str(input("Ingrese el nro de matricula: "))
                listar_docente(matricula)
            elif(op==2):
                listar_todos_docentes()
            i=input("Presione cualquir tecla continuar...")
        elif opcion == "2":
            print("#####################################")
            print("# Información acerca de estudiantes #")
            print("#####################################")
            print("1. Buscar estudiante")
            print("2. Listar estudiantes")
            op=int(input("Ingrese opción: "))
            if(op==1):
                numeroCI=int(input("Ingrese numero de CI del estudiante: "))
                listar_estudiante(numeroCI)
            elif op==2:
                listar_todos_estudiantes()
            i=input("Presione ENTER para continuar...")
        elif opcion == "3":
            print("\n*****************************")
            print("****** CALIFICACIONES *******")
            print("*****************************")
            print("LISTA DE CALIFICACIONES: ")
            ci=int(input("Ingrese el CI de un estudiante: "))
            listar_calif(ci)
            i=input("Presione ENTER para continuar...")    
        elif opcion == "4":
            print("\n-----------------------------------------")
            print("| Gestion de Billetaje Electronico        |")
            print("-------------------------------------------")
            print("HISTORIAL E INFORMACION ADICIONAL")
            ci=int(input("Ingrese el CI de un estudiante: "))
            listar_info_billetaje(ci)
            i=input("Presione ENTER para continuar...")     
        elif opcion == "5":
            print("\n-----------------------------------------")
            print("|          Gestion de Becas                |")
            print("-------------------------------------------")
            print("HISTORIAL E INFORMACION ADICIONAL")
            ci=int(input("Ingrese el CI de un estudiante: "))
            beca_listar(ci)
            print("______________________")
            print("Menú Beca: ")
            print("1. Actualizar beca ")
            print("2. Salir")
            op = int(input("Ingrese opción: "))
            if(op == 1):
                print(f"Acutalizar estado becado del estudiante {ci} a: ")
                print("1. SI : para otorgar")
                print("2. NO : para quitar")
                op1=int(input("Ingrese opción: "))
                if(op1==1):
                    varStr="SI"
                    editar_becar(ci,varStr)
                    beca_listar(ci)
                elif(op1==2):
                    varStr="NO"
                    editar_becar(ci,varStr)
                    beca_listar(ci)
            i=input("Presione ENTER para continuar...")                     
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    print("Finalizando " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()

