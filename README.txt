Implementación del sistema en PC

Esta carpeta contiene los archivos necesarios para ejecutar el sistema de supervisión y adquisición de datos sobre una computadora con sistema operativo Windows, configuración utilizada durante las etapas de desarrollo, pruebas y validación del proyecto.

Requisitos
Sistema operativo Windows 10/11.
Node.js.
Node-RED.
XAMPP con MariaDB.
Acceso a la red donde se encuentra el PLC Siemens S7-1200.
Estructura
pc/
├── node-red/
│   └── .node-red/
├── database/
│   └── base_de_datos_backup.sql
└── README.md
Restauración de la base de datos
Instalar XAMPP y ejecutar los servicios Apache (opcional) y MariaDB.
Crear una nueva base de datos denominada:
base_de_datos
Importar el archivo:
database/base_de_datos_backup.sql

Puede realizarse mediante phpMyAdmin o desde la consola:

mysql -u root -p base_de_datos < base_de_datos_backup.sql
Configuración de Node-RED
Instalar Node.js.
Instalar Node-RED.
Reemplazar la carpeta .node-red del usuario por la incluida en este repositorio o importar el flujo correspondiente.
Instalar las dependencias indicadas en package.json, en caso de ser necesario.
Configuración de la comunicación con el PLC

Modificar el nodo de conexión S7 con la dirección IP correspondiente al PLC Siemens S7-1200 utilizado.

Verificar los siguientes parámetros:

- **Dirección IP del PLC:** 192.168.0.2.
- **Puerto:** 102.
- **Rack:** 0.
- **Slot:** 1.
- **Protocolo:** ISO-on-TCP (S7).
- **Modo de lectura:** Todas las variables (All Variables).
- **Tiempo de actualización:** 5 segundos para variables dinámicas.


Las variables de proceso se encuentran almacenadas en los bloques de datos (DB) del PLC y son leídas mediante el nodo S7 de Node-RED. Entre las principales variables configuradas se encuentran:

- Temperatura.
- Nivel.
- Caudal.
- Presión de agua.
- Presión de aire.
- Estados de actuadores.
- Alarmas.
- Setpoints de nivel y temperatura.
- Parámetros de los controladores PID (Kp, Ki y Kd).
- Modos de operación automático y manual.

## Base de datos

El proyecto utiliza MariaDB como gestor de base de datos.

Configuración utilizada:

- **Motor:** MariaDB.
- **Puerto:** 3306.
- **Base de datos:** `base_de_datos`.
- **Usuario:** `nodered`.
- **Contraseña: definida por el usuario durante la instalación

La base de datos está compuesta por dos tablas principales:

- **historico_dinamico:** almacena las variables de proceso cada 5 segundos.
- **historico_estatico:** registra únicamente cambios en parámetros de configuración y estados del sistema.



Funcionamiento

Una vez iniciado Node-RED y establecida la comunicación con el PLC:

Se adquieren las variables de proceso mediante protocolo S7.
Los datos son procesados por el middleware.
La información se almacena en MariaDB.
El Dashboard y la interfaz SCADA se actualizan en tiempo real.
Las consultas históricas se realizan directamente sobre la base de datos.

Esta implementación corresponde al entorno de desarrollo utilizado durante la construcción y validación del proyecto. Posteriormente, el sistema completo fue migrado a una Raspberry Pi 3 Model B para obtener una solución embebida, autónoma y de bajo consumo energético.