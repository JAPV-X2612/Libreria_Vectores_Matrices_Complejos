# Librería de Números Complejos
 
## Descripción 📑
---
Esta es una librería que contiene múltiples funciones y operaciones entre números, vectores y matrices complejos, los cuales forman parte de las bases para cálculos más avanzados de un curso de [Computación Cuántica](https://es.wikipedia.org/wiki/Computaci%C3%B3n_cu%C3%A1ntica).

## Tabla de Contenidos 🗂️
---
Operaciones con números, vectores y matrices complejos:

1. Suma de vectores
2. Inverso aditivo de un vector
3. Multiplicación de un escalar por un vector
4. Adición de matrices
5. Inversa aditiva de una matriz
6. Multiplicación de un escalar por una matriz
7. Transpuesta de un vector/matriz
8. Conjugado de un vector/matriz
9. Adjunta (daga) de un vector/matriz
10. Producto matricial 
11. Acción de una matriz sobre un vector
12. Producto interno de dos vectores/matrices
13. Norma de un vector/matriz
14. Distancia entre dos vectores/matrices
15. Valores y vectores propios de una matriz
16. Validación de una matriz Unitaria
17. Validación de una matriz Hermitiana
18. Producto tensor de dos vectores/matrices (Próximamente)

## Requisitos 🧾
---
Para poder implementar la librería en su máquina local, se recomienda tener las siguientes ***especificaciones mínimas***:

- **Sistema Operativo:** Windows 8.1 / macOS 10.8 Mountain Lion / Linux Ubuntu 18.04 LTS Bionic Beaver
- **Procesador:** Intel Celeron / AMD Athlon
- **Almacenamiento:** 128 Gb (2 Gb libres)
- **Memoria RAM:** 4 Gb
- [IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado) con soporte para Python ([IDLE](https://docs.python.org/es/3/library/idle.html), [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/?section=windows), [VSC](https://code.visualstudio.com/), [PyDev](https://www.pydev.org/), [Spyder](https://www.spyder-ide.org/), [Atom](https://github.com/atom))

Para una óptima implementación de la librería, se sugieren las siguientes ***especificaciones recomendadas***:

- **Sistema Operativo:** Windows 10 / macOS 13.0 Ventura / Linux Ubuntu 22.04 LTS Jammy Jellyfish
- **Procesador:** Intel Core i3 o i5 10ma Gen. / AMD Ryzen 3 o 5 Serie 3000 / Apple M1
- **Almacenamiento:** 256 Gb (4 Gb libres)- 
- **Memoria RAM:** 8 Gb
- [IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado) con soporte para Python ([IDLE](https://docs.python.org/es/3/library/idle.html), [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/?section=windows), [VSC](https://code.visualstudio.com/), [PyDev](https://www.pydev.org/), [Spyder](https://www.spyder-ide.org/), [Atom](https://github.com/atom))

## Comenzando 🚀
---
Para usar esta proyecto se recomienda seguir los siguientes pasos:

1. Crear una nueva carpeta en su máquina local
2. Dar clic derecho en el interior de la carpeta y abrir "Open Git Bush here"
3. Clonar el repositorio:
     ```sh
     $ git clone https://github.com/JAPV-X2612/Libreria_Numeros_Complejos.git
     ```
4. Verificar que se hallan descargado 5 archivos
5. Salir de la terminal de Git:
     ```sh
     $ git exit
     ```

## Instalación 🔧
---
Una vez descargada una copia del repositorio en su máquina local, se recomienda:

1. Abrir el entorno de desarrollo integrado ([IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado)) de su preferencia
2. Abrir el archivo `Pruebas Libreria_Vectores_Matrices_Complejos`
3. Instalar la librería `Numpy` en el IDE en caso de no tenerla
4. Ejecutar el intérprete de Python predeterminado
5. Verificar que no haya problemas de ejecución o errores
6. Si la respuesta fue `FAILED (failures=#)`, absténgase de usar la librería y reporte el error a jesus.pinzon-v@mail.escuelaing.edu.co
7. En otro caso, si la respuesta fue `OK`, entonces la librería está lista para su uso personal. 💻😎👍 (Revisar ***LICENSE.md***)

## Ejecutando las Pruebas ⚙️
---
A continuación se muestran algunos ejemplos de ejecución de 5 funciones en IDLE:

```
>>> cplx_vect_sum([1+2j, 5-2j], [4+4j, -1+7j])
    array([5.+6.j, 4.+5.j])
```
```
>>> cplx_mtx_sum([[-33+2j, 6-74j], [14-8j, 18-4j]], [[-4+1j, 11-1j], [21+7j, -1+2j]])
    array([[-37. +3.j,  17.-75.j],
           [ 35. -1.j,  17. -2.j]])
```
```
>>> cplx_vct_mtx_adj([[-4.6+3j, 1.1-1j], [21+7j,-1+2j]])
    array([[-4.6-3.j, 21. -7.j],
        [ 1.1+1.j, -1. -2.j]])
```
```
>>> cplx_vct_mtx_dist([-1+2j, 6-7j, 1-8j], [4+1j, -12, 1-1j])
    21.166010488516726
```
```
>>> cplx_unt_mtx([[1j, 0, 0], [0, 1j, 0], [0, 0, 1j]])
    True
```

## Textos y Wikis 📖
---
Para mayor información sobre los temas descritos en este proyecto se recomienda revisar los siguientes enlaces:

* [Números Complejos](https://es.wikipedia.org/wiki/N%C3%BAmero_complejo)
* [Qubit](https://es.wikipedia.org/wiki/C%C3%BAbit)
* [Computación Cuántica](https://es.wikipedia.org/wiki/Computaci%C3%B3n_cu%C3%A1ntica)
* [Quantum Computing for Computer Scientists](https://www.cambridge.org/core/books/quantum-computing-for-computer-scientists/8AEA723BEE5CC9F5C03FDD4BA850C711)

## Autor ✒️
---
Este proyecto es de la autoría de ***Jesús Alfonso Pinzón Vega***, Ingeniero de Sistemas de la Escuela Colombiana de Ingeniería Julio Garavito (ECIJG).  
**Correo:** jesus.pinzon-v@mail.escuelaing.edu.co

## Licencia 📄
---
Este proyecto tiene licencia de código abierto, por lo cual puede ser usado por cualquier persona u organización con fines educativos y de investigación. No obstante, está **PROHIBIDA SU DISTRIBUCIÓN** parcial o completa con fines lucrativos sin expreso consentimiento del autor.  
Se recomienda revisar el archivo **LICENSE** adjunto al repositorio para mayor información.

## Información Adicional 💡
--- 
Próximamente se agregarán más funciones a la librería para ampliar sus capacidades de cálculo con los números complejos.