from datetime import datetime

antiga = datetime(2000,5,2,15,32)

agora = datetime.now()
print(agora)
print(antiga)
print((agora-antiga).days)