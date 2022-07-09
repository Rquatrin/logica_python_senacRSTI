#criar uma lista com 12 elementos onde cada lista é um dicionário e contem a temperatura média daquele mes

meses = [
        {'mês' : 'Janeiro', 'TemperaturaMEDIA' : 29},
        {'mês' : 'Fevereiro', 'TemperaturaMEDIA' : 26},
        {'mês' : 'Março', 'TemperaturaMEDIA' : 25},
        {'mês' : 'Abril', 'TemperaturaMEDIA' : 22},
        {'mês' : 'Maio' , 'TemperaturaMEDIA' : 20},
        {'mês' : 'Junho', 'TemperaturaMEDIA' : 10},
        {'mês' : 'Julho' , 'TemperaturaMEDIA' : 8},
        {'mês' : 'Agosto' , 'TemperaturaMEDIA' : 14},
        {'mês' : 'Setembro' , 'TemperaturaMEDIA' : 20},
        {'mês' : 'Outubro' , 'TemperaturaMEDIA' : 22},
        {'mês' : 'Novembro' , 'TemperaturaMEDIA' : 24},
        {'mês' : 'Dezembro' , 'TemperaturaMEDIA' : 28},
        ]
sensacao = ''
for mes in meses:
    if mes.get('TemperaturaMEDIA') < 15:
        print( mes.get('mês'), mes.get('TemperaturaMEDIA'), sensacao)
        sensacao = 'Frio'
        
    else:
        
        sensacao = 'Quente'
        print(mes.get('mês'), mes.get('TemperaturaMEDIA'), 'Sensação: ' ,sensacao)
   
    
    