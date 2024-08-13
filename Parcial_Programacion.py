import time;

#Funciones:

def mostrar_biblioteca(favoritos):
    #comprobar si hay canciones en favoritos
    #Si el tamaño de la lista es 0 significa que no contiene ningun elemento por ende procedemos  a mostrar el mensaje correspondiente , caso contrario
    #imprimimos en pantalla su contenido.
    if(len(favoritos)==0):
        print("La lista de favoritos esta vacia")
    else:
        print("      canciones favoritas      ");
        for cancion in favoritos:
            print("---------------------------");
            print ("Nombre: "+cancion);
    

def reproducir(indice,Duracion):
    #Se evalua mediante una condicion si la canción a reprodicir existe y se encuentra dentro del rango o cantidad de canciones predefinidas en un comienzo(4);
    if(indice>=1 and indice<=4):
        #Entra aca si el resultado de la expresión logica es VERDADERO; 
        indice-=1;
        print("Cargando",end="");
        for i in range(1,4,1):
            print(".",end="");
            time.sleep(1);
        print("\nReproduciendo")
        for i in range(1,Duracion[indice]+1,1):
            print(i)
            time.sleep(1);
        
        print("Fin de la canción");
    
    else:
        #Entra aca si el resultado de la expresión logica es FALSO;
        print("Error,No se encontró la cancion.")


def agregar_a_favoritos(favoritos,Musica):
    indice=int(input("Indique la cancion a agregar mediante si numero: "))
    if(indice>=1 and indice<=4):
         #Uso de la funcion append para agregar un elemento a la ultima posición de la lista Favoritos que se compartió por referencia.
         favoritos.append(Musica[indice-1]);
         print("Cancion Guardada con exito!");
    else:
         print("Error, Esa canción no existe!");
    

def buscar_musica(indice,Musica,Duracion):
    if(indice>=0 and indice<=3):
         print("-------------------cancion buscada-----------------------");
         print("Nombre:"+Musica[indice]+" Duración:"+str(Duracion[indice]));
         print("---------------------------------------------------------");
    else:
        print("Error,esa canción no existe!");


def mostrar_musica(Musica,Duracion):
 #Indice es una variable local para acceder al numero de la cancion como el de duracacion ya que coinciden en sus posiciones
 #tambien puede usarse una matriz para hacer el codigo mas simple y limpio pero desconozco si esta permitido o no;
 indice=0;
 print("              canciones                  ")
 for cancion in  Musica:
     indice=Musica.index(cancion);
     print("------------------------------------------")
     print(str(indice+1)+":"+cancion+" Duración:"+str(Duracion[indice])); 
 #Uso del time para esperar unos segundos antes de volver al menu principal (Con el fin de que sea posible obsevar las canciones)
 


#Algoritmo principal:

#Declaracion de variables o listas  a utilizar;
Musica=["Cancion 1","Cancion 2","Cancion 3","Cancion 4"];
Duracion=[30,40,10,32];
#(La lista duracion y música se llenoron  con valores aleatorios o genericos)
favoritos=[];
opcion=0;
numeroCancion=0;

#Parcial( Ejercicio Musica- Integrantes : .... )
print("-----Bienvenido al programa-----");
#Presentar un menú para que el usuario pueda hacer un uso de la mejor forma;
while(opcion!=6):
    print("\n----Menu----\n1)Ver musica disponible\n2)BuscarMusica \n3)Añadir a favoritos\n4)reproducir\n5)Ver mi biblioteca de canciones(favoritos)\n6)salir\n");
    opcion=int(input("Opcion->"));
    print("\n");
    if(opcion==1):
        #Llamar a la funcion mostrar Musica
        mostrar_musica(Musica,Duracion);
    elif(opcion==2):
        #Llamar a la funcion Buscar Musica
        numeroCancion=int(input("Ingrese el numero de la cancion:"));
        #Se le resta un valor ya que suponemos que el usuario va a ingresar valores desde el 1
        #(Basicamente para evitar acceder a datos erroneos )
        numeroCancion-=1;
        buscar_musica(numeroCancion,Musica,Duracion);
    elif (opcion==3):
        #Llamar a la funcion Añadir a favoritos
        agregar_a_favoritos(favoritos,Musica);
    elif (opcion==4):
        #Llamar a la funcion reproducir
        numeroCancion=int(input("Ingrese el numero de la cancion:"))
        reproducir(numeroCancion,Duracion);
    elif (opcion==5):
        #LLamar a la funcion mostrar Biblioteca
        mostrar_biblioteca(favoritos);
    elif (opcion==6):
        #Mensaje despedida;
        print("Adios!");
    else:
        #Mensaje de Advertencia
        print("El valor ingresado no coincide con ninguna opcion!");

    time.sleep(3);

    #Aviso Importante:El uso del time solo es por estetica ,Ya que la salida (output) se muestra super rapido sin posibilidad de observar 
    #el funcionamiento de cada procedimiento , metodo o funcion.No esta hecho con la intención de romper alguna regla.
