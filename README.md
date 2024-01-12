ACLARACION DE RUTAS = todas las rutas mencionadas deben comenzar con /AppJuegos/ para que funcionenen correctamente.
En principio, se hereda el padre.html en todos los html que se pueden acceder desde el menu (Inicio,Juegos PS4, Juegos PS5 y Estudios), estos html son los que se llaman "ver", ejemplo "verEstudios.html".
Hay 3 modelos: JuegosPS4, JuegosPS5 y EstudiosDeJuegos.
En views, estan las funciones con la posibilidad de agregar juegos o estudios desde una url habiendo instanciado la class con sus propiedades correspondientes, al ingresar a la url correspondiente, se creara el nuevo objeto en la base de datos.
Los paths son = agregarJuegosPS5, agregarJuegosPS4, agregarEstudios
Hablando de los formularios, hay 3 modelos de formularios identicos a los modelos anteriores.
En views, estan las funciones con la posibilidad de agregar juegos o estudios desde una url que permite acceder al formulario para crear el nuevo objeto en la base de datos.
Los paths son = juegosPS4Formulario, juegosPS5Formulario.
Ademas se pueden obtener resultados de busquedas de todos los modelos.
El orden es ir a la ruta (busquedaJuegosPS4,busquedaJuegosPS5) de lo que se quiera buscar y agregar el nombre o una parte y luego de buscar se enviara a otro html que mostrara el resultado sea exitoso o no.(buscarPS4,buscarPS5)

