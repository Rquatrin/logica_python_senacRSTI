from datetime import datetime

d1_str = '31/05/2022 14:58'

dt = datetime.strptime(d1_str,'%d/%m/%Y %H:%M')


print(dt)