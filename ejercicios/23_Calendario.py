#Reto: Importar la librería calendar. Imprimir el calendario del mes actual.


#metodo1
import datetime
import calendar
x = datetime.datetime.now().year
y = datetime.datetime.now().month

print(calendar.month(x,y))


#metodo 2
# from datetime import datetime
# import calendar
# x= datetime.today().year
# y= datetime.today().month
# c = calendar.TextCalendar(calendar.SUNDAY)
# c.prmonth(x, y)