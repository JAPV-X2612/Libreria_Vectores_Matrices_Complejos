# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/08/31

# Librería de Operaciones con Vectores y Matrices Complejos

from math import *
from numpy import *

def cplx_vect_sum(v1,v2):
    """Calcula y devuelve la suma de dos vectores complejos
    (1D array, 1D array) -> 1D array"""
    v1,v2 = array(v1),array(v2),
    vr = v1 + v2
    return vr


def cplx_vect_add_inver(v):
    """Calcula y devuelve el inverso aditivo de un vector complejo
    (1D array) -> 1D array"""
    v = array(v)
    vr = -1*v
    return vr


def cplx_vect_scal_mult(c,v):
    """Calcula y devuelve la multiplicación de un escalar por un vector complejo
    (complex or int ot float, 1D array) -> 1D array"""
    v = array(v)
    vr = c*v
    return vr


def cplx_mtx_sum(m1,m2):
    """Calcula y devuelve la suma de matrices complejas
    (2D array, 2D array) -> 2D array"""
    m1,m2 = array(m1),array(m2)
    mr = m1 + m2
    return mr


def cplx_mtx_add_inver(m):
    """Calcula y devuelve la inversa aditiva de una matriz compleja
    (2D array) -> 2D array"""
    m = array(m)
    mr = -1*m
    return mr


def cplx_mtx_scal_mult(c,m):
    """Calcula y devuelve la multiplicación de un escalar por una matriz compleja
    (complex or int ot float, 1D array) -> 1D array"""
    m = array(m)
    mr = c*m
    return mr


def cplx_vct_mtx_trans(vm):
    """Calcula y devuelve la transpuesta de un vector o matriz complejos
    (1D array or 2D array) -> 1D array or 2D array"""
    vmt = transpose(vm)
    return vmt


def cplx_vct_mtx_conj(vm):
    """Calcula y devuelve el conjugado de un vector o matriz complejos
    (1D array or 2D array) -> 1D array or 2D array"""
    vm = array(vm)
    vmc = vm.conjugate()
    return vmc


def cplx_vct_mtx_adj(vm):
    """Calcula y devuelve la adjunta (daga) de un vector o matriz complejos
    (1D array or 2D array) -> 1D array or 2D array"""
    vm = array(vm)
    vma = transpose(vm.conjugate())
    return vma