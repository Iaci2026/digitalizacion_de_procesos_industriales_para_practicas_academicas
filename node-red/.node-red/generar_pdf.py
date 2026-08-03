import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from datetime import datetime, timedelta

ruta_json = r"C:\Users\jor_b\.node-red\grafica_temp.json"

with open(ruta_json, encoding="utf-8") as f:
    datos = json.load(f)

temp = datos[0]["data"][0]
sp = datos[0]["data"][1]
pid = datos[0]["data"][2]

fecha = []
temperatura = []
setpoint = []
salida = []

for p in temp:

    print(p["x"])

    dt = datetime.fromisoformat(
        p["x"].replace("Z", "")
    ) - timedelta(hours=3)

    print(dt)

    fecha.append(dt)
    temperatura.append(float(p["y"]))

for p in sp:
    setpoint.append(float(p["y"]))

for p in pid:
    salida.append(float(p["y"]))

plt.figure(figsize=(10,5))

plt.plot(fecha, temperatura, label="Temperatura")
plt.plot(fecha, setpoint, label="SP Temp")
plt.plot(fecha, salida, label="Salida PID")

plt.xlabel("Tiempo")
plt.ylabel("Valor")

plt.ylim(0,100)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(5))

# Formato del eje X
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
plt.xticks(rotation=45)

plt.legend()
plt.grid()

plt.tight_layout()

plt.savefig(
    r"C:\Users\jor_b\.node-red\Graficas_PDF\grafica_temperatura.pdf",
    format="pdf",
    bbox_inches="tight"
)

plt.close()

print("PDF generado correctamente")