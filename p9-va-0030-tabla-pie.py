# Cepeda Miramontes Darrell Ramsés NC = 0030  Fecha 3/11/2026

# used to show part-to-whole relationships/data

import matplotlib.pyplot as plt

materias= ["MA", "CN", "LN", "ESP", "FC", "HM"]
califas= [9,8,7,5,10,6]

plt.pie(califas, labels=materias, autopct = '%1.1f%%', startangle=90)
plt.title("Darrell Ramsés 0030")
plt.show()

print("Programa ejecutado por Cepeda Darrell NC = 0030")