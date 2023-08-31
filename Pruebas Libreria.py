# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/08/31

# Pruebas de la Librería de Operaciones con Vectores y Números Complejos

from Libreria_Vectores_Matrices_Complejos import *
import unittest as ut

class Test_Libreria_Nombre(ut.TestCase):
    
    def test_cplx_vect_sum(self):
        """Prueba del cálculo de la suma de dos vectores complejos
        None -> OK or FAILED (failures=#)"""
        vr = list(cplx_vect_sum([1+2j, 5-2j], [4+4j, -1+7j]))
        self.assertEqual(vr, [5+6j, 4+5j])
        vr = list(cplx_vect_sum([1.5j, 3, -1-1.2j], [7, 4.7+9.2j, 3j]))
        self.assertEqual(vr, [7+1.5j, 7.7+9.2j, -1+1.8j])
    
    
    def test_cplx_vect_add_inver(self):
        """Prueba del cálculo del inverso aditivo de un vector complejo
        None -> OK or FAILED (failures=#)"""
        vr = list(cplx_vect_add_inver([2-5.7j, 7+4j]))
        self.assertEqual(vr, [-2+5.7j, -7-4j])
        vr = list(cplx_vect_add_inver([-1-5j, 1j, -1j]))
        self.assertEqual(vr, [1+5j, -1j, +1j])
        
        
    def test_cplx_vect_scal_mult(self):
        """Prueba del cálculo de la suma de dos vectores complejos
        None -> OK or FAILED (failures=#)"""
        vr = list(cplx_vect_scal_mult(9, [1+2j, 5-2j]))
        self.assertEqual(vr, [9+18j, 45-18j])
        vr = list(cplx_vect_scal_mult(2-3j, [7, 4.7+9.2j, 2.5-3j]))
        self.assertEqual(vr, [14-21j, 37+4.299999999999997j, -4-13.5j])
    
      
    def test_cplx_mtx_sum(self):
        """Prueba del cálculo de la suma de dos matrices complejas
        None -> OK or FAILED (failures=#)"""
        mr = [list(m) for m in cplx_mtx_sum([[1+3j, -5-7j], [4-1j, 8+4j]], [[1+1j, 2-6j], [9+9j, -10+20j]])]
        self.assertEqual(mr, [[2+4j, -3-13j], [13+8j, -2+24j]])
        mr = [list(m) for m in cplx_mtx_sum([[-33+2j, 6-74j], [14-8j, 18-4j]], [[-4+1j, 11-1j], [21+7j, -1+2j]])]
        self.assertEqual(mr, [[-37+3j, 17-75j], [35-1j, 17-2j]])
        
    
    def test_cplx_mtx_add_inver(self):
        """Prueba del cálculo de la inversa aditiva de una matriz compleja
        None -> OK or FAILED (failures=#)"""
        mr = [list(m) for m in cplx_mtx_add_inver([[1+3j, -5-7j], [4-1j, 8+4j]])]
        self.assertEqual(mr, [[-1-3j, 5+7j], [-4+1j, -8-4j]])
        mr = [list(m) for m in cplx_mtx_add_inver([[-4+1j, 11-1j], [21+7j, -1+2j]])]
        self.assertEqual(mr, [[4-1j, -11+1j], [-21-7j, 1-2j]])
        
    
    def test_cplx_mtx_scal_mult(self):
        """Prueba del cálculo de la multiplicación de un escalar por una matriz compleja
        None -> OK or FAILED (failures=#)"""
        vmt = [list(m) for m in cplx_mtx_scal_mult(2+3j,[[1+3j, -5-7j], [4-1j, 8+4j]])]
        self.assertEqual(vmt, [[-7+9j, 11-29j], [11+10j, 4+32j]])
        vmt = [list(m) for m in cplx_mtx_scal_mult(5,[[-4+1j, 11-1j], [21+7j, -1+2j]])]
        self.assertEqual(vmt, [[-20+5j, 55-5j], [105+35j, -5+10j]])
     
        
    def test_cplx_vct_mtx_trans(self):
        """Prueba del cálculo de la transpuesta de un vector o matriz complejos
        None -> OK or FAILED (failures=#)"""
        mr = list(cplx_vct_mtx_trans([1+3j, -5-7j, 4-1j, 8+4j]))
        self.assertEqual(mr, [1+3j, -5-7j, 4-1j, 8+4j])
        mr = [list(m) for m in cplx_vct_mtx_trans([[-4.6+3j, 1.1-1j, 2j], [21+7j, 4, -1+2j], [-15.2+9j, -1-4.4j, -100+2.2j]])]
        self.assertEqual(mr, [[-4.6+3j, 21+7j, -15.2+9j], [1.1-1j, 4+0j, -1-4.4j], [2j, -1+2j, -100+2.2j]])
    
    
    def test_cplx_vct_mtx_conj(self):
        """Prueba del cálculo del conjugado de un vector o matriz complejos
        None -> OK or FAILED (failures=#)"""
        vmc = list(cplx_vct_mtx_conj([1+3j, -5-7j, 4-1j, 8+4j]))
        self.assertEqual(vmc, [1-3j, -5+7j, 4+1j, 8-4j])
        vmc = [list(m) for m in cplx_vct_mtx_conj([[-4.6+3j, 1.1-1j, 2j], [21+7j, 4, -1+2j], [-15.2+9j, -1-4.4j, -100+2.2j]])]
        self.assertEqual(vmc, [[-4.6-3j, 1.1+1j, -2j], [21-7j, 4, -1-2j], [-15.2-9j, -1+4.4j, -100-2.2j]])


if __name__ == '__main__':
    ut.main()