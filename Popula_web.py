import HorarioService as hs

horario = hs.HorarioService('{"nomeDoProfessor":"Prof. Fulano","horarioDeAtendimento":"10:00-12:00","periodo":"matutino","sala":"3","predio":"1"}')
print(horario.nomeDoProfessor)
print(horario.horarioDeAtendimento)
print(horario.periodo)
print(horario.sala)
print(horario.predio)
print(horario.predioEscolhido)
print(horario.selecionarPredio())

print(horario.get_predio())
