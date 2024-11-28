# -*- coding: utf-8 -*-
"""
Clase streamlit - Electrónica digital
Andrea Margarita Camargo Carreño
"""

import streamlit as st 
import pandas as pd
import numpy as np
from PIL import Image

# Título y descripción inicial
st.title("ElectroWagon")
st.markdown("***Circuito entrenador para ESP32***.")
st.markdown('''
    :red[Proyecto] :orange[Electrónica] :green[Digital] :blue[2024] :violet[-II]
    :gray[] :rainbow.''')
st.markdown("Profesora Yuli Alvarez &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# Descripción del proyecto
multi = '''Prototipo realizado por los estudiantes:.
- Andrea Margarita Camargo Carreño
- Andres Felipe Galvis Jimenez
- Mariana Sofía Monsalve
- Dariana Andrea Torrecilla Morales

De Ingeniería Mecatrónica :sunglasses:
    
***---------------------------------------------------------------------------------------------------------------------------------------------***

***:blue[DESCRIPCIÓN DEL PROYECTO]***    
   El prototipo pretende solucionar lo incómodo que es trabajar con una ESP32 en una protoboard debido a su ancho, permitiendo que el usuario pueda conectar elementos a cualquiera de los pines que necesite; el prototipo está pensado para ser implementado en entorno de laboratorio

***:blue[ELEMENTOS Y COMPONENTES]***

**:rose: :red[Microcontrolador ESP32:]**\n
 Este microcontrolador permite detectar las variables detectadas por los sensores, mostrarlas en la pantalla OLED y enviarlas a la web para ser supervisadas en tiempo real visualizadas en la plataforma ThingSpeak.

**:rose: :red[Sensor DTH11:]**\n
 Este sensor detecta las variables de temperatura y humedad.

**:rose: :red[Módulo LDR:]**\n
 Este sensor detecta la variable de intensidad de luz.

**:rose: :red[Regulador de voltaje LM7805:]**\n
 El regulador convierte el voltaje de entrada de las baterías a uno de 5V que cuida de los elementos electrónicos.

**:rose: :red[Regulador de voltaje LM1117:]**\n
 Permite convertir el voltaje de entrada a uno de 3,3v ideal para crear un nodo de alimentación que el usuario puede utilizar para alimentar de forma controlada sus elementos.

**:rose: :red[Portapilas de dos puestos:]**\n
 Permite colocar dos pilas 18650 que entrega un voltaje de alimentación de 7.4v a la PCB.
 
**:rose: :red[Batería 3,7v:]**\n
 Se utilizan dos baterías de 3,7v 18650.

**:rose: :red[Pantalla OLED:]**\n
 Permite visualizar las variables detectadas por los sensores.

**:rose: :red[Pines MACHO-MACHO:]**\n
 Permiten la conexión de elementos a cualquier salida de la ESP32 o a los nodos de 5v o 3,3v.

**:rose: :red[Pines HEMBRA-MACHO:]**\n
 Permite al usuario quitar y poner la ESP32 en la PCB con libertad.

**:rose: :red[JACK DC HEMBRA y MACHO:]**\n
 Permite la conexión entre las baterías y los reguladores de voltaje a la entrada de alimentación en la PCB.



***:blue[ESQUEMAS, PLANOS TÉCNICOS Y DIMENSIONES]***
'''
st.markdown(multi)




# Cargar y redimensionar la imagen
img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\PCB.jpg')
new_size = (900, 900)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption="Esquema del circuito de la PCB entrenadora para ESP32", use_column_width=True)

multi = '''La imagen muestra el diseño que se imprimió para la PBC donde los componentes electrónicos se van a soldar según lo que se muestra en el esquema de conexiones.
\n'''
st.markdown(multi)


img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\conexiones.png')
new_size = (1200, 900)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption="Esquema de conexiones", use_column_width=True)

multi = '''El esquema muestra las conexiones entre los componentes electrónicos que conforman la PCB.
'''
st.markdown(multi)


img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\plano .png')
new_size = (1300, 900)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption="Plano con las dimensiones de la base para la PCB", use_column_width=True)
multi = '''La base para la PCB  cuenta con una caja en la parte frontal que tiene la medida necesaria para que quepa el portabaterias de dos puestos para la alimentación del circuito que va sobre la parte trasera de la camioneta.\n
'''
st.markdown(multi)


multi = '''***:blue[MECANISMOS DE FUNCIONAMIENTO]***

:sunflower: :orange[Encendido de la PCB]\n
Encendemos los switches de encendido que permiten el paso de voltaje a través del Jack de alimentación hacia los reguladores de voltaje, que a su vez transmiten la tensión requerida para energizar los componentes del circuito de manera controlada. 

:sunflower: :orange[Programación de la ESP32]\n

Se carga a la ESP32 un código que permita leer a través de los pines D33 y D13 las variables detectadas por los sensores y a través de los pines SCL y SDA enviarlos a la pantalla OLED para ser visualizados; además, este código debe permitir a través de la conexión Wifi de la ESP32 conectarse a la plataforma ThingSpeak donde permite ver en la web los datos detectados en tiempo real y graficarlos para facilitar su comprensión.

:sunflower: :orange[Detección de variables por los sensores]\n
Los sensores DTH11 y el módulo LDR toman datos de las variables de humedad, temperatura y luz respectivamente y estos son recolectados por el microcontrolador.


:sunflower: :orange[Visualización de variables en pantalla OLED]\n
La pantalla OLED recibe los datos de la ESP32 a través de los pines SCL y SDA los muestra en tiempo real según estos cambien.

:sunflower: :orange[Visualización de variables en ThingSpeak]\n
La ESP32 se conecta a través de su protocolo Wifi a la plataforma web de visualización ThingSpeak para mostrar de manera gráfica los cambios en los datos enviados por los sensores.

:sunflower: :orange[Libertad de uso]\n
La PCB permite a través los pines y los nodos integrados que el usuario utilice las demás salidas de la ESP32 con toda libertad y que pueda alimentar sus elementos agregados a los nodos de 5v o 3.3v según lo que permitan los componentes electrónicos.\n 

***:blue[CONSTRUCCIÓN Y PRUEBAS]***\n

:cherry_blossom: :violet[Prueba en protoboard del circuito]\n

'''
st.markdown(multi)

img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\protoboard1.jpg')
new_size = (1300, 900)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption="Circuito montado en protoboard", use_column_width=True)
multi = '''Es importante probar el funcionamiento de los circuitos en protoboards ya que al hacerlo es posible verificar que el diseño que se realizó si es funcional y puede ahorrar errores al momento de imprimir la PCB que pueden traducirse en gatos extra e incluso en el daño de los elementos electrónicos del circuito.\n
'''
st.markdown(multi)

multi = '''
:cherry_blossom: :violet[Construcción de la base para PCB]\n
'''
st.markdown(multi)

img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\base.jpg')
new_size = (1300, 900)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption="Base para PCB", use_column_width=True)
multi = '''La base se imprimió en material PETG en impresora 3D y los detalles que no se encuentran detallados en el plano de la base son accesorios de decoración.\n
'''
st.markdown(multi)


multi = '''
***:blue[CÓDIGO PARA PROGRAMAR LA ESP32]***\n
'''
st.markdown(multi)

import streamlit as st

code = '''#include <ThingSpeak.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHT.h>
#include <WiFi.h>

// Configuración de la pantalla OLED
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Configuración del sensor DHT11
#define DHTPIN 13
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Configuración del módulo LDR
#define LDR_PIN 33  // Entrada analógica para el LDR

// Configuración para credenciales de acceso a la red WiFi
const char* ssid = "NATALIAYCARMEN";
const char* password = "susy0712";

// Configuración de ThingSpeak
unsigned long channelID = 2; // Reemplaza con tu ID de canal
const char* WriteAPIKey = "IIS2GZV768K04POM"; // Reemplaza con tu clave API de escritura

WiFiClient cliente;

void setup() {
  // Iniciar comunicación serial
  Serial.begin(115200);

  // Conexión WiFi
  WiFi.begin(ssid, password);
  Serial.print("Conectando al WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado al WiFi");

  // Inicializar ThingSpeak
  ThingSpeak.begin(cliente);

  // Inicializar el bus I²C con los pines de ESP32
  Wire.begin(21, 22);  // SDA: GPIO21, SCL: GPIO22

  // Inicializar la pantalla OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("Error al inicializar la pantalla OLED");
    while (true);  // Detener ejecución si no se detecta la pantalla
  }
  display.clearDisplay();
  display.display();

  // Inicializar el sensor DHT11
  dht.begin();
  Serial.println("Inicialización completa");
}

void loop() {
  // Leer datos del DHT11
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Leer datos del módulo LDR
  int ldrValueRaw = analogRead(LDR_PIN);  // Valor de 0 a 4095
  float ldrPercentage = map(ldrValueRaw, 0, 4095, 100, 0);  // Convertir a porcentaje

  // Verificar lecturas válidas del DHT11
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error al leer datos del DHT11");
    humidity = -1;
    temperature = -1;
  }

  // Mostrar datos en el monitor serial
  Serial.print("Humedad: ");
  Serial.print(humidity);
  Serial.print("% | Temp: ");
  Serial.print(temperature);
  Serial.print("°C | Luz: ");
  Serial.print(ldrPercentage);
  Serial.println("%");

  // Mostrar datos en la pantalla OLED
  display.clearDisplay();
  display.setCursor(0, 0);
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  if (humidity == -1 || temperature == -1) {
    display.println("Error: Sensor DHT11");
  } else {
    display.print("Humedad: ");
    display.print(humidity);
    display.println(" %");
    display.print("Temp: ");
    display.print(temperature);
    display.println(" C");
  }
  display.print("Luz: ");
  display.print(ldrPercentage);
  display.println(" %");
  display.display();

  // Enviar datos a ThingSpeak
  if (WiFi.status() == WL_CONNECTED) {
    ThingSpeak.setField(1, temperature);
    ThingSpeak.setField(2, humidity);
    ThingSpeak.setField(3, ldrPercentage);

    int responseCode = ThingSpeak.writeFields(channelID, WriteAPIKey);
    if (responseCode == 200) {
      Serial.println("Datos enviados a ThingSpeak!");
    } else {
      Serial.print("Error al enviar datos. Código: ");
      Serial.println(responseCode);
    }
  } else {
    Serial.println("No conectado a WiFi, reintentando...");
    WiFi.begin(ssid, password);
  }

  delay(2000);  // Esperar 2 segundos antes de la siguiente lectura
}'''
st.code(code, language="python")

multi = '''
***:blue[PROTOTIPO FUNCIONAL]***\n
'''
st.markdown(multi)

img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\prototipo1.jpg')
new_size = (900, 1300)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption="Prototipo funcional encendido", use_column_width=True)
multi = '''En esta imagen se observa como el JACK DC alimenta los reguladores de voltaje que alimentan la ESP32, los sensores y la pantalla OLED evidendenciando el cumplimiento de los objetivos planteados al inicio del proyecto.\n
'''
st.markdown(multi)

img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\oled.jpg')
new_size = (1300, 700)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption=" Pantalla OLED en funcionamento", use_column_width=True)
multi = '''La pantalla OLED muestra las variables que detectan los sensores; y puede ser utilizada por el usuario como monitor serial segín la aplicación que este le quiera dar.\n
'''
st.markdown(multi)

multi = '''
***:blue[VISUALIZACIÓN DE DATOS EN TIEMPO REAL]***\n
Cargando el código que encuentras en arriba, puedes conectar la ESP32 con su protocolo de conexión Wifi a la plataforma de visualización ThingSpeak para visualizar en tiempo real los cambios en las variables que detectan los sensores.
'''
st.markdown(multi)


img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\luz.jpg')
new_size = (1300, 900)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption="Visualización en tiempo real de variable de intensidad lumínica (detectado por el modulo LDR) en ThingSpeak", use_column_width=True)
multi = ''''''
st.markdown(multi)

img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\temp.jpg')
new_size = (1300, 900)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption="Visualización en tiempo real de variable de temperatura (detectado por el sensor DTH11) en ThingSpeak", use_column_width=True)
multi = ''''''
st.markdown(multi)

img = Image.open(r'C:\Users\ANDREA CAMARGO\Downloads\humedad.jpg')
new_size = (1300, 900)
img_resized = img.resize(new_size)

# Mostrar la imagen con un pie de foto
st.image(img_resized, caption="Visualización en tiempo real de variable de humedad (detectado por el modulo LDR) en ThingSpeak", use_column_width=True)
multi = ''''''
st.markdown(multi)

multi = '''¡Ánimate a hacer tu propio proyecto!.\n
'''
st.markdown(multi)

multi = ''':blue[***El mundo es de los que lo toman en sus manos***.]:sunglasses:\n
'''
st.markdown(multi)