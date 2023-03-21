# Tercera-pre-entrega-Varas
![logo de coder](https://user-images.githubusercontent.com/54871540/226503225-1b3a8488-d9de-4737-bd7a-97d870330896.png)

Repositorio para la 3er Pre-Entrega del trabajo final del curso de Coderhouse

En este proyecto web con Django, busqué generar una web de manejo de la base de datos de una librería que permite dar de alta:

    -Empleados
    
    -Clientes
    
    -Autores
    
    -Libros
    
    -Generos(para los libros)
    
Pasos para el funcionamiento de la página:

    1° Clonar el repositorio
    
    2° Instalar los paquetes a traves de requirements.txt
    
    3° Iniciar el servidor
    
    4° Una vez iniciado debería empezar dentro de la página home para permitirnos navegar a traves de la barra de navegación de la web a las diferentes secciones, 
    c/u tiene una seccion de carga de datos (a excepción de Generos que solo tiene para carga de datos, a futuro pienso cambiarlo para que te muestre todos los libros
    pertenecientes a ese genero), para generar un registro en la base de datos correspondiente a la sección, y una de busqueda, que nos permitira buscar un registro
    dentro de la base de datos, también correspondiente a su sección. 
    
        Los modelos de la carga de datos para cada formulario son los siguientes:
        
           Empleado: dni (entero unico, por lo que no pueden existir dos registros con un mismo dni)
                      nombre (char)
                      apellido (char)
                      nacimiento (datetime con formato de fecha español 'dia/mes/año')
                      genero (char con dos opciones M- Masculino | F- Femenino)
                      
            Cliente: dni (entero unico, por lo que no pueden existir dos registros con un mismo dni)
                     nombre (char)
                     apellido (char)
                     email (campo de mail)
                     telefono (utiliza el paquete django-phonenumber-field para darle el formato Argentino de numero de telefono)
                     
            Autor:   nombre (char)
                     apellido (char)
                     nacimiento (datetime con formato de fecha español 'dia/mes/año')
                     muerte (datetime con formato de fecha español 'dia/mes/año' que puede ser null en caso de que el autor no falleciera)
            Genero:  nombre (char)
            Libro:   titulo(char)
                     autor(foreign key que referencia a la base de datos de Autores, en caso de no haber un autor cargado todavía aparece como "Vacio")
                     genero(foreign key que referencia a la base de datos de Generos, en caso de no haber un genero cargado todavía aparece como "Vacio")
      
      *5° En las secciones de busqueda nos solicita un campo para buscar un registro especifico de la base de datos, salvo para autores que nos solicita Nombre y Apellido del autor para buscarlo
             
