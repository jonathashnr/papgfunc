import unittest
from unittest.mock import patch

import script
from script import prog_function, validade_function, whatprog, main

class TestProgressionApp(unittest.TestCase):
    # Testa prog_function e as funções retornadas
    def test_prog_function_pa(self):
        pa_func = prog_function('pa')
        result = pa_func(2, 4, 5) # r: 2, e1: 4, n:5
        self.assertEqual(result, [4, 6, 8, 10, 12])
    def test_prog_function_pg(self):
        pg_func = prog_function('pg')
        result = pg_func(3, 1, 4) # r: 3, e1: 1, n:4
        self.assertEqual(result, [1, 3, 9, 27])

    # Testa validate_func para valor correto
    @patch('builtins.input', side_effect=['10'])
    def test_validate_func(self, mock_input):
        validate_test = validade_function('Testando', float)
        result = validate_test()
        self.assertEqual(result, 10.0)
    
    #Testa mensagem de erro para validade_func
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['Mah oi aqui é o Silvio Santos', '10'])
    def test_validate_func_invalid_input(self, mock_input, mock_print):
        validate_test = validade_function('Testando', float)
        validate_test()
        mock_print.assert_any_call('Tipo de entrada inválido, a entrada deve ser do tipo: ' + str(float))
    
    # Testa whatprog para valor correto
    @patch('builtins.input', side_effect=['PA'])
    def test_whatprog_pa(self, mock_input):
        result = whatprog()
        self.assertEqual(result, 'pa')
    @patch('builtins.input', side_effect=['PG'])
    def test_whatprog_pg(self, mock_input):
        result = whatprog()
        self.assertEqual(result, 'pg')

    #Testa mensagem de erro para whatprog
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['Mah oi aqui é o Silvio Santos', 'PA'])
    def test_whatprog_invalid_input(self, mock_input, mock_print):
        whatprog()
        mock_print.assert_any_call('Entrada inválida, as únicas entradas válidas são PA e PG.')
    
    #Testa o flow inteiro do app
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['PG','3','5','6'])
    def test_main_flow(self, mock_input, mock_print):
        main()
        mock_print.assert_any_call('[5.0, 15.0, 45.0, 135.0, 405.0, 1215.0]')


if __name__ == '__main__':
    unittest.main()