# FIWARE Orion – Integração com MQTT e Node-RED

## 📌 Descrição

Este projeto demonstra a integração entre tecnologias IoT utilizando o ecossistema FIWARE.

A solução realiza a coleta de dados simulados de sensores ambientais, transmissão via MQTT, processamento no Node-RED, armazenamento no FIWARE Orion Context Broker e visualização em um Dashboard em tempo real.

## 🚀 Tecnologias Utilizadas

* Docker
* Docker Compose
* Python
* MQTT (Mosquitto)
* Node-RED
* FIWARE Orion Context Broker
* MongoDB

---

## 🏗️ Arquitetura da Solução

```text
Python Publisher
       ↓ MQTT
Mosquitto Broker
       ↓
Node-RED
       ↓
FIWARE Orion Context Broker
       ↓
MongoDB
       ↓
Dashboard
```

---

## 📡 Sensores Simulados

### Sensor001 – Monitoramento Ambiental

Atributos:

* Temperatura (°C)
* Umidade (%)

Exemplo:

```json
{
  "temperature": 28.39,
  "humidity": 50.15
}
```

---

### Sensor002 – Qualidade do Ar

Atributos:

* CO₂ (ppm)
* PM2.5 (μg/m³)

Exemplo:

```json
{
  "co2": 770,
  "pm25": 24.10
}
```

---

## 📂 Tópicos MQTT

### Sensor001

```text
/iot/sensor001
```

### Sensor002

```text
/iot/sensor002
```

---

## 📦 Serviços Docker

O projeto utiliza os seguintes containers:

| Serviço   | Descrição               |
| --------- | ----------------------- |
| Mosquitto | Broker MQTT             |
| Node-RED  | Processamento dos dados |
| Orion     | Context Broker FIWARE   |
| MongoDB   | Persistência dos dados  |

Verificar containers:

```bash
docker ps
```

---

## ▶️ Executando o Projeto

Subir os containers:

```bash
docker-compose up -d
```

Verificar status:

```bash
docker ps
```

---

## 📊 Dashboard

O Dashboard apresenta os seguintes indicadores em tempo real:

* 🌡️ Temperatura
* 💧 Umidade do Ar
* 🌿 Nível de CO₂
* 🌫️ Qualidade do Ar

Acessar:

```text
http://localhost:1880/ui
```

---

## 🔍 Testando MQTT

Entrar no container Mosquitto:

```bash
docker exec -it trabalho-fiware-iot-mosquitto-1 sh
```

Monitorar mensagens:

```bash
mosquitto_sub -h localhost -t "/iot/#" -v
```

Saída esperada:

```text
/iot/sensor001 {"temperature":28.39,"humidity":50.15}
/iot/sensor002 {"co2":770,"pm25":24.10}
```

---

## 🔎 Consultando Entidades no Orion

### Sensor001

```bash
curl -s http://localhost:1026/v2/entities/Sensor:001 | jq
```

### Sensor002

```bash
curl -s http://localhost:1026/v2/entities/Sensor:002 | jq
```

---

## 📸 Evidências

### Arquitetura do Projeto

![Arquitetura](docs/arquitetura.png)

### Fluxo Node-RED

![Node-RED](docs/nodered-flow.png)

### Dashboard

![Dashboard](docs/dashboard.png)

### MQTT em Execução

![MQTT](docs/mqtt-monitoramento.png)

---

## 📚 Objetivo Acadêmico

Este projeto foi desenvolvido com fins acadêmicos para demonstrar a integração entre dispositivos IoT, protocolos de comunicação e componentes da plataforma FIWARE.

---

## 👨‍💻 Autor

**Moisés**




