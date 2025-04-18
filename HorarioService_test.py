import unittest
from HorarioService import HorarioService
import json


class TestHorarioServiceInstanciamento(unittest.TestCase):
    #@patch('json.loads')
    #def test_consctructor(self,mock_json_loads):
    #Vi na aula do Vitor, mas não precisa, já que o método json.loads não é o que está sendo testado, mas sim a instancia.
    def test_consctructor_fulano(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }''' # ainda é uma string
        mock_instance = HorarioService(json_resposta)

        self.assertEqual(mock_instance.nomeDoProfessor,"Prof. Fulano")
        self.assertEqual(mock_instance.horarioDeAtendimento,"10:00-12:00")
        self.assertEqual(mock_instance.periodo, "matutino")
        self.assertEqual(mock_instance.predio,"1")
        

    def test_consctructor_sucesso_instanciacao(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        mock_instance = HorarioService(json_resposta)
        self.assertIsInstance(mock_instance,HorarioService)
    
    def test_consctructor_sala_int(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        mock_instance = HorarioService(json_resposta)
        self.assertIsInstance(mock_instance.sala,int)
        self.assertEqual(mock_instance.sala,3)
        self.assertNotEqual(mock_instance.sala,"3") #sala não pode ser uma string

    def test_consctructor_Chris(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Chris",
            "horarioDeAtendimento": "18:00-20:00",
            "periodo": "noturno",
            "sala": "15",
            "predio": "3"
        }''' 
        mock_instance = HorarioService(json_resposta)

        self.assertIsInstance(mock_instance,HorarioService)
        self.assertEqual(mock_instance.nomeDoProfessor,"Chris")
        self.assertEqual(mock_instance.horarioDeAtendimento,"18:00-20:00")
        self.assertEqual(mock_instance.periodo, "noturno")
        self.assertEqual(mock_instance.sala,15)
        self.assertNotEqual(mock_instance.sala,"15")
        self.assertEqual(mock_instance.predio,"3")

        self.assertEqual(mock_instance.selecionarPredio(),int(mock_instance.predio))

    def test_multiplas_instancias(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Chris",
            "horarioDeAtendimento": "11:00-13:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }''' 
        mock_instance = HorarioService(json_resposta)
        json_resposta2 = '''{ 
            "nomeDoProfessor": "Maria Santos",
            "horarioDeAtendimento": "14:00-16:00",
            "periodo": "integral",
            "sala": "7",
            "predio": 2
        }''' 
        mock_instance2 = HorarioService(json_resposta2)

        self.assertNotEqual(mock_instance.nomeDoProfessor,mock_instance2.nomeDoProfessor)
        self.assertNotEqual(mock_instance.horarioDeAtendimento,mock_instance2.horarioDeAtendimento)
        self.assertNotEqual(mock_instance.periodo, mock_instance2.periodo)
        self.assertNotEqual(mock_instance.sala,mock_instance2.sala)
        self.assertNotEqual(mock_instance.predio,mock_instance2.predio)
        self.assertNotEqual(mock_instance.selecionarPredio(),mock_instance2.selecionarPredio())

    def test_consctructor_selecionarPredio(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        mock_instance = HorarioService(json_resposta)

        self.assertEqual(mock_instance.selecionarPredio(),int(mock_instance.predio))

    def test_sala_limite_inferior(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "1",
            "predio": "1"
        }'''
        mock_instance = HorarioService(json_resposta)
        self.assertEqual(mock_instance.sala,1)
        self.assertEqual(mock_instance.predio,'1')
        self.assertEqual(mock_instance.predioEscolhido,1)
    
    def test_sala_limite_superior(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "30",
            "predio": "6"
        }'''
        mock_instance = HorarioService(json_resposta)
        self.assertEqual(mock_instance.sala,30)
        self.assertEqual(mock_instance.predio,'6')
        self.assertEqual(mock_instance.predioEscolhido,6)
        self.assertNotEqual(mock_instance.sala,"30") #sala não pode ser uma string

    ######## Testes de erro

    def test_sala_negativa(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "-3",
            "predio": "1"
        }'''
        with self.assertRaises(ValueError):
            mock_instance = HorarioService(json_resposta) 

    def test_sala_excedente(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "33",
            "predio": "6"
        }'''
        with self.assertRaises(ValueError):
            mock_instance = HorarioService(json_resposta)

    def test_dado_faltante_horario(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "periodo": "matutino",
            "sala": "29",
            "predio": "6"
        }'''
        
        with self.assertRaises(KeyError):
            mock_instance = HorarioService(json_resposta)

    def test_dado_faltante_nome(self):
        json_resposta = '''{ 
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "29",
            "predio": "6"
        }'''
        with self.assertRaises(KeyError):
            mock_instance = HorarioService(json_resposta)

    def test_dado_faltante_periodo(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "sala": "29",
            "predio": "6"
        }'''
        with self.assertRaises(KeyError):
            mock_instance = HorarioService(json_resposta)

    def test_dado_faltante_sala(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "predio": "6"
        }'''
        with self.assertRaises(KeyError):
            mock_instance = HorarioService(json_resposta)

    def test_dado_faltante_predio(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3"
        }'''
        with self.assertRaises(KeyError):
            mock_instance = HorarioService(json_resposta)
    
    
            
    
    def test_nome_invalido(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "a",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        with self.assertRaises(ValueError):
            mock_instance = HorarioService(json_resposta)

    def test_multi_professores(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        },
            "nomeDoProfessor": "Prof. Fsulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
            }'''
        with self.assertRaises(json.decoder.JSONDecodeError):
            mock_instance = HorarioService(json_resposta)

    def test_horario_invalido_excedente(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "101:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        with self.assertRaises(ValueError):
            mock_instance = HorarioService(json_resposta)
    
    def test_horario_invalido_insuficiente(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "1:0-12:0",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        with self.assertRaises(ValueError):
            mock_instance = HorarioService(json_resposta)

    def test_horario_invalido_mal_formatado(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "11:00 12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        with self.assertRaises(ValueError):
            mock_instance = HorarioService(json_resposta)

    def test_horario_invalido_mal_formatado(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "11:a0-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        with self.assertRaises(ValueError):
            mock_instance = HorarioService(json_resposta)

class TestMarcarHorario(unittest.TestCase):


    def test_marcar_horario_valido(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "08:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        mock_instance = HorarioService(json_resposta)
        self.assertEqual(mock_instance.marcarHorario("11:00"), print("Horário 11:00 marcado com sucesso!"))
    def test_marcar_horario_invalido(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        mock_instance = HorarioService(json_resposta)
        with self.assertRaises(ValueError):
            mock_instance.marcarHorario("10:00-12:00")

    def test_marcar_horario_invalido2(self):
        json_resposta = '''{ 
            "nomeDoProfessor": "Prof. Fulano",
            "horarioDeAtendimento": "10:00-12:00",
            "periodo": "matutino",
            "sala": "3",
            "predio": "1"
        }'''
        mock_instance = HorarioService(json_resposta)
        with self.assertRaises(ValueError):
            mock_instance.marcarHorario("10-12")

if __name__ == "__main__":
    unittest.main()