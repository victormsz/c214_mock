import json
from unittest.mock import patch, MagicMock, Mock
from math import ceil as mathCeil

class HorarioService:

    def __init__(self, string_json):
        data = json.loads(string_json)

        try:
            self.nomeDoProfessor = data['nomeDoProfessor']
            if not isinstance(self.nomeDoProfessor, str) or len(self.nomeDoProfessor) < 3:
                raise ValueError("Nome do professor deve ser uma string com mais de 2 caracteres.")
        except ValueError as e:
            raise ValueError(f"nome de professor invalido {e}")
        self.horarioDeAtendimento = data['horarioDeAtendimento'] 
        self.periodo = data.get('periodo')
        try:
            self.sala = int(data['sala'])
            if self.sala < 1 or self.sala > 30:
                raise ValueError("Sala deve ser um número entre 1 e 30.")
        except (ValueError) as e:
            raise ValueError(f"Erro ao processar a sala: {e}")
        self.predio = data['predio']

        self.predioEscolhido = self.selecionarPredio()


    def selecionarPredio(self):
        PredioEscolhido = mathCeil(int(self.sala) / 5)
        
        return PredioEscolhido
    

                

    # def get_predio(self):
    #     sala = int(self.data['sala'])
        
    #     if (sala / 5) <= 1:
    #         return "Predio 1"
    #     elif (sala / 5) <= 2:
    #         return "Predio 2"
    #     elif (sala / 5) <= 3:
    #         return "Predio 3"
    #     elif (sala / 5) <= 4:
    #         return "Predio 4"
    #     elif (sala / 5) <= 5:
    #         return "Predio 5"
    #     elif (sala / 5) <= 6:
    #         return "Predio 6"
    #     pass
    #chatgpt recomendou essa forma para simplificar o código, requer biblioteca math
    
