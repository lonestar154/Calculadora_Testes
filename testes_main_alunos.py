import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

class TestCalculadora(unittest.TestCase):

    def teste_operacoes_basicas(self):
        # Teste operações básicas de cada operador + - * / % ^
        self.assertEqual(calculadora(2, 3, '+'), 5)
        self.assertEqual(calculadora(5, 3, '-'), 2)
        self.assertEqual(calculadora(2, 4, '*'), 8)
        self.assertEqual(calculadora(10, 2, '/'), 5)
        self.assertEqual(calculadora(10, 3, '%'), 1)
        self.assertEqual(calculadora(2, 3, '^'), 8)

    def teste_v2_operacoes(self):
        self.assertEqual(calculadora_v2(2, 3, '+'), 5)
        self.assertEqual(calculadora_v2(5, 3, '-'), 2)
        self.assertEqual(calculadora_v2(2, 4, '*'), 8)
        self.assertEqual(calculadora_v2(10, 2, '/'), 5)
        self.assertEqual(calculadora_v2(10, 3, '%'), 1)
        self.assertEqual(calculadora_v2(2, 3, '^'), 8)
        self.assertTrue(math.isnan(calculadora_v2(10, 0, '/')))
        self.assertTrue(math.isnan(calculadora_v2(10, 0, '%')))
        self.assertTrue(math.isnan(calculadora_v2(2, 3, '$')))

    def teste_v3_operacoes(self):
        self.assertEqual(calculadora_v3(2, 3, '+'), 5)
        self.assertEqual(calculadora_v3(5, 3, '-'), 2)
        self.assertEqual(calculadora_v3(2, 4, '*'), 8)
        self.assertEqual(calculadora_v3(10, 2, '/'), 5)
        self.assertEqual(calculadora_v3(10, 3, '%'), 1)
        self.assertEqual(calculadora_v3(2, 3, '^'), 8)
        self.assertTrue(math.isnan(calculadora_v3(10, 0, '/')))
        self.assertTrue(math.isnan(calculadora_v3(10, 0, '%')))
        self.assertTrue(math.isnan(calculadora_v3(2, 3, '$')))

    def teste_v4_operacoes(self):
        self.assertEqual(calculadora_v4(2, 3, '+'), 5)
        self.assertEqual(calculadora_v4(5, 3, '-'), 2)
        self.assertEqual(calculadora_v4(2, 4, '*'), 8)
        self.assertEqual(calculadora_v4(10, 2, '/'), 5)
        self.assertEqual(calculadora_v4(10, 3, '%'), 1)
        self.assertEqual(calculadora_v4(2, 3, '^'), 8)
        self.assertTrue(math.isnan(calculadora_v4(10, 0, '/')))
        self.assertTrue(math.isnan(calculadora_v4(10, 0, '%')))
        self.assertTrue(math.isnan(calculadora_v4(2, 3, '$')))

if __name__ == '__main__':
    unittest.main()

# para correr os testes: python -m unittest -v testes_main_alunos.py