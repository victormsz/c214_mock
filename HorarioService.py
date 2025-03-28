import json

#classe a ser mockada, pois não existe o arquivo json
class HorarioAtendimento:

    json_data = {
  "nomeDoProfessor": "<nome_do_professor>",
  "horarioDeAtendimento": "<horario_de_atendimento>",
  "periodo": "<integral_ou_noturno>",
  "sala": "<sala_de_atendimento>",
  "predio": [
    "1",
    "2",
    "3",
    "4",
    "6"
  ]
}

    def __init__(self):
        self.data = json.loads(json_data)

    def get_predio(self):
        sala = self.data['sala']
        if (sala / 5) <= 1:
            return "Predio 1"
        elif (sala / 5) <= 2:
            return "Predio 2"
        elif (sala / 5) <= 3:
            return "Predio 3"
        elif (sala / 5) <= 4:
            return "Predio 4"
        elif (sala / 5) <= 5:
            return "Predio 5"
        elif (sala / 5) <= 6:
            return "Predio 6"
        pass


    def __str__(self):
        return f"{self.dia} - {self.inicio} até {self.fim}"