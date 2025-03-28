import json
from math import ceil as mathCeil

class HorarioService:

    def __init__(self, string_json):
        data = json.loads(string_json)

        try:
            if 'nomeDoProfessor' not in data:
                raise KeyError("Nome do professor não encontrado.")
            self.nomeDoProfessor = data['nomeDoProfessor']
            if not isinstance(self.nomeDoProfessor, str) or len(self.nomeDoProfessor) < 3:
                raise ValueError("Nome do professor deve ser uma string com mais de 2 caracteres.")
        except ValueError as e:
            raise ValueError(f"nome de professor invalido {e}")
        
        try:
            if 'horarioDeAtendimento' not in data:
                raise KeyError("Horário de atendimento não encontrado.")
            self.validateHorarioDuplo(data['horarioDeAtendimento'])
            self.horarioDeAtendimento = data['horarioDeAtendimento']
        except ValueError as e:
            raise ValueError(f"Erro ao processar o horário: {e}")
        
        try:
            if 'periodo' not in data:
                raise KeyError("Período não encontrado.")
            self.periodo = data.get('periodo')
        except ValueError as e:
            raise ValueError(f"Erro ao processar o período: {e}")
        

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
    
    
    def validateHorarioDuplo(self, horario):
        if not isinstance(horario, str) or len(horario) < 11:
            raise ValueError("Horário inválido. Deve ser uma string com pelo menos 11 caracteres.")
        if not (isinstance(horario, str) and ':' in horario):
            raise ValueError("Horário inválido. Deve conter dois pontos.")
        if not (horario[2] == ':' and horario[5] == '-' and horario[8] == ':'):
            raise ValueError("Horário inválido. Deve ter o formato HH:MM-HH:MM.")
        if not (horario[0:2].isdigit() and horario[3:5].isdigit() and horario[6:8].isdigit() and horario[9:11].isdigit()):
            raise ValueError("Horário inválido. Deve conter apenas números.")


        if int(horario[0:2]) > 24 or int(horario[3:5]) > 59 or int(horario[6:8]) > 24 or int(horario[9:11]) > 59:
            raise ValueError("Horário inválido. Horas devem ser menores que 24 e minutos menores que 60.")
        return True
    
    def validateHorario(self, horario):
        if not isinstance(horario, str) or len(horario) > 5:
            raise ValueError("Horário inválido. Deve ser uma string com menos de 5 caracteres.")
        if not (isinstance(horario, str) and ':' in horario):
            raise ValueError("Horário inválido. Deve conter dois pontos.")
        if not (horario[2] == ':'):
            raise ValueError("Horário inválido. Deve ter o formato HH:MM.")
        if int(horario[0:2]) > 24 or int(horario[3:5]) > 59:
            raise ValueError("Horário inválido. Horas devem ser menores que 24 e minutos menores que 60.")
        return True

    def marcarHorario(self, horario):
        self.validateHorario(horario)
        return print(f"Horário marcado: {horario} com sucesso!")
                

    
