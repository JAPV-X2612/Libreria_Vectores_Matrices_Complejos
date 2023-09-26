# Librería de Operaciones con Vectores y Matrices Complejos
 
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
18. Producto tensor de dos vectores/matrices

## Requisitos 🧾
---
Para poder implementar la librería en su máquina local, se recomienda tener las siguientes ***especificaciones mínimas***:

- **Sistema Operativo:** Windows 8.1 / macOS 10.8 Mountain Lion / Linux Ubuntu 18.04 LTS Bionic Beaver
- **Procesador:** Intel Celeron / AMD Athlon
- **Almacenamiento:** 128 Gb (2 Gb libres)
- **Memoria RAM:** 4 Gb
- [IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado) con soporte para Python [IDLE](https://docs.python.org/es/3/library/idle.html), [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/?section=windows), [VSC](https://code.visualstudio.com/), [PyDev](https://www.pydev.org/), [Spyder](https://www.spyder-ide.org/), [Atom](https://github.com/atom))

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
7. En otro caso, si la respuesta fue `OK`, entonces la librería está lista para su uso personal. 💻😎👍

## Ejecutando Pruebas ⚙️
---
A continuación se muestra un ejemplo de ejecución de cada función en [IDLE](https://docs.python.org/es/3/library/idle.html):

#### 1. Suma de vectores
```
>>> cplx_vect_sum([1+2j, 5-2j], [4+4j, -1+7j])
    array([5.+6.j, 4.+5.j])
```

#### 2. Inverso aditivo de un vector
```
>>> cplx_vect_add_inver([2-5.7j, 7+4j])
    array([-2.+5.7j, -7.-4.j ])
```

#### 3. Multiplicación de un escalar por un vector
```
>>> cplx_vect_scal_mult(2-1j, [17, 9.3j, 2.5-3j])
    array([34. -17.j, 9.3+18.6j, 2. -8.5j])
```

#### 4. Adición de matrices
```
>>> cplx_mtx_sum([[-33+2j, 6-74j], [14-8j, 18-4j]], [[-4+1j, 11-1j], [21+7j, -1+2j]])
    array([[-37. +3.j, 17.-75.j],
        [35. -1.j, 17. -2.j]])
```

#### 5. Inversa aditiva de una matriz
```
>>> cplx_mtx_add_inver([[-4+1j, 11-1j], [21+7j, -1+2j]])
    array([[4.-1.j, -11.+1.j],
        [-21.-7.j, 1.-2.j]])
```

#### 6. Multiplicación de un escalar por una matriz
```
>>> cplx_mtx_scal_mult(2+3j,[[1+3j, -5-7j], [4-1j, 8+4j]])
    array([[-7. +9.j, 11.-29.j],
        [11.+10.j, 4.+32.j]])
```

#### 7. Transpuesta de un vector/matriz
```
>>> cplx_vct_mtx_trans([[-4.6+3j, 1.1-1j, 2j], [21+7j, 4, -1+2j], [-15.2+9j, -1-4.4j, -100+2.2j]])
    array([[-4.6+3.j , 21. +7.j, -15.2+9.j ],
        [1.1-1.j, 4. +0.j, -1. -4.4j],
        [0. +2.j, -1. +2.j, -100. +2.2j]])
```

#### 8. Conjugado de un vector/matriz
```
>>> cplx_vct_mtx_conj([1+3j, -5-7j, 4-1j, 8+4j])
    array([ 1.-3.j, -5.+7.j,  4.+1.j,  8.-4.j])
```

#### 9. Adjunta (daga) de un vector/matriz
```
>>> cplx_vct_mtx_adj([[-4.6+3j, 1.1-1j], [21+7j,-1+2j]])
    array([[-4.6-3.j, 21. -7.j],
        [ 1.1+1.j, -1. -2.j]])
```

#### 10. Producto matricial
```
>>> cplx_mtx_prod([[-1+2j, 6-7j], [1-8j, 5]], [[1j, 1-1j], [1+7j, 0]])
    array([[53.+34.j, 1. +3.j],
        [13.+36.j, -7. -9.j]])
```

#### 11. Acción de una matriz sobre un vector
```
>>> cplx_vct_mtx_act([1+3j, -5+1j], [[1-1j, 2-6j], [3+9j, -4+2j]])
    array([-20.-40.j, 38.-14.j])
```

#### 12. Producto interno de dos vectores/matrices
```
>>> cplx_vct_mtx_inter_prod([[-1+2j, 1], [1-3j, 5]], [[1j, 1-1j], [1+7j, 0]])
    (-17+8j)
```

#### 13. Norma de un vector/matriz
```
>>> cplx_vct_mtx_norm([1+7j, 4-1j, 2-6j])                 
    10.344080432788601
>>> cplx_vct_mtx_norm([[-1+2j, -3j,1+7j], [1-3j, 5, 1j], [1j, 1-1j, 2+3j]])             
    10.770329614269007
```

#### 14. Distancia entre dos vectores/matrices
```
>>> cplx_vct_mtx_dist([-1+2j, 6-7j, 1-8j], [4+1j, -12, 1-1j])
    21.166010488516726
```

#### 15. Valores y vectores propios de una matriz
```
>>> cplx_mtx_val_vect([[-1j, 1], [0, 1j]])               
    (array([-0.-1.j, 0.+1.j]), array([[1. +0.j, 0. -0.4472136j], [0. +0.j, 0.89442719+0.j]]))
```

#### 16. Validación de una matriz Unitaria
```
>>> cplx_unt_mtx([[1j, 0, 0], [0, 1j, 0], [0, 0, 1j]])
    True
>>> cplx_unt_mtx([[-1+2j, 1], [1-3j, 0]])                
    False
```

#### 17. Validación de una matriz Hermitiana
```
>>> cplx_herm_mtx([[3, 3-8j, -1-1j], [3+8j, 1, -5-6j], [-1+1j, -5+6j, -2]])            
    True
>>> cplx_herm_mtx([[-1+2j, 1], [1-3j, 0]])          
    False
```

#### 18. Producto tensor de dos vectores/matrices
```
>>> cplx_vct_mtx_tens_prod([[2j, 1+6j], [1j, 0]], [[-5j, 3+4j], [2, -1j]])         
    array([[ 10. -0.j,  -8. +6.j,  30. -5.j, -21.+22.j],
        [0. +4.j, 2. -0.j, 2.+12.j, 6. -1.j],
        [5. -0.j, -4. +3.j, 0. -0.j, 0. +0.j],
        [0. +2.j, 1. -0.j, 0. +0.j, 0. -0.j]])
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
Este proyecto es de la autoría de ***Jesús Alfonso Pinzón Vega***, Ingeniero de Sistemas de la Escuela Colombiana de Ingeniería Julio Garavito ([ECIJG](https://www.escuelaing.edu.co/es/)). 
**Correo:** jesus.pinzon-v@mail.escuelaing.edu.co

## Licencia 📄
---
Este proyecto tiene licencia de código abierto, por lo cual puede ser usado por cualquier persona u organización con fines educativos y de investigación. No obstante, está **PROHIBIDA SU DISTRIBUCIÓN** parcial o completa con fines lucrativos sin expreso consentimiento del autor.  
Se recomienda revisar el archivo [LICENSE](https://github.com/JAPV-X2612/Libreria_Numeros_Complejos/blob/main/LICENSE.md) adjunto al repositorio para mayor información.

## Información Adicional 💡
--- 
Próximamente se agregarán más funciones a la librería para ampliar sus capacidades de cálculo con números complejos.