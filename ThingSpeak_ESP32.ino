#include <ThingSpeak.h>
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
}