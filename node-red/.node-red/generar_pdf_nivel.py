import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from datetime import datetime, timedelta


ruta_json = r"C:\Users\jor_b\.node-red\grafica_nivel.json"


with open(ruta_json, encoding="utf-8") as f:
    datos = json.load(f)


nivel = datos[0]["data"][0]
sp = datos[0]["data"][1]
pid = datos[0]["data"][2]


fecha = []
niveles = []
setpoint = []
salida = []


for p in nivel:

    dt = datetime.fromisoformat(
        p["x"].replace("Z", "")
    ) - timedelta(hours=3)

    print(dt)

    fecha.append(dt)
    niveles.append(p["y"])


for p in sp:
    setpoint.append(p["y"])


for p in pid:
    salida.append(p["y"])


plt.figure(figsize=(10,5))

plt.plot(fecha, niveles, label="Nivel")
plt.plot(fecha, setpoint, label="SP Nivel")
plt.plot(fecha, salida, label="Salida PID Nivel")

plt.xlabel("Tiempo")
plt.ylabel("Valor")

# Escala del eje Y
plt.ylim(20, 40)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(1))

# Formato del eje X
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %H:%M'))
plt.gcf().autofmt_xdate()

plt.legend()
plt.grid()

plt.savefig(
    r"C:\Users\jor_b\.node-red\Graficas_PDF\grafica_nivel.pdf",
    format="pdf",
    bbox_inches="tight"
)

plt.close()

print("PDF Nivel generado correctamente")