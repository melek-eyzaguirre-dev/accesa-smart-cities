# 🏙️ ACCESA SMART CITIES - Hedera Blockchain

> **Sistema de Pagos Automatizados para Accesibilidad en Ciudades Inteligentes**  
> Proyecto para VendimiaTech Hackathon 2026 - Track Hedera

[![Hedera](https://img.shields.io/badge/Hedera-Testnet-blue)](https://hedera.com)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📋 Tabla de Contenidos

- [¿Qué es ACCESA Smart Cities?](#-qué-es-accesa-smart-cities)
- [¿Por qué Blockchain?](#-por-qué-blockchain)
- [Conceptos de Blockchain (para principiantes)](#-conceptos-de-blockchain-para-principiantes)
- [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Cómo Usar](#-cómo-usar)
- [API REST](#-api-rest)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Demo para el Hackathon](#-demo-para-el-hackathon)
- [Recursos de Aprendizaje](#-recursos-de-aprendizaje)

---

## 🎯 ¿Qué es ACCESA Smart Cities?

**ACCESA Smart Cities** es una plataforma que utiliza **agentes de IA** y **blockchain** para facilitar el acceso a servicios de accesibilidad en ciudades inteligentes.

### El Problema

Millones de personas con discapacidad enfrentan barreras diarias:
- ❌ Falta de información accesible en edificios públicos
- ❌ Sistemas de navegación que no consideran necesidades especiales
- ❌ Servicios de accesibilidad costosos y centralizados
- ❌ Datos de accesibilidad fragmentados

### La Solución

Una economía descentralizada donde:
- ✅ **Usuarios** pagan automáticamente por servicios de accesibilidad
- ✅ **Edificios y servicios** reciben pagos instantáneos
- ✅ **Agentes de IA** toman decisiones y ejecutan pagos sin intervención humana
- ✅ **Blockchain** garantiza transparencia y seguridad

### Casos de Uso

1. **María** (baja visión) escanea un QR en un edificio:
   - Su agente de IA evalúa si necesita información por voz
   - Decide automáticamente pagar 10 ACCESA tokens
   - Recibe guía de voz personalizada
   - Todo en segundos, sin fricciones

2. **Carlos** (discapacidad auditiva) entra a un hospital:
   - Su agente detecta videos en lengua de señas disponibles
   - Paga automáticamente 15 ACCESA tokens
   - Accede a información médica adaptada

3. **Ana** (movilidad reducida) busca una ruta accesible:
   - Su agente consulta el marketplace de accesibilidad
   - Encuentra y paga por un mapa con rampas y ascensores
   - Navega de forma independiente

---

## 🔗 ¿Por qué Blockchain?

### Beneficios de Usar Hedera

| Característica | Beneficio para ACCESA |
|---------------|---------------------|
| **Transacciones instantáneas** | Pagos confirmados en 3-5 segundos |
| **Costos bajísimos** | $0.0001 USD por transacción |
| **Tokens nativos (HTS)** | Crear ACCESA token sin smart contracts complejos |
| **Escalabilidad** | 10,000+ transacciones por segundo |
| **Seguridad** | Consenso aBFT (más seguro que PoW) |
| **Sostenibilidad** | Huella de carbono negativa |

### ¿Por qué no una base de datos tradicional?

- 🔒 **Descentralización**: No depende de una sola empresa
- 💎 **Transparencia**: Todas las transacciones son auditables
- 🤖 **Pagos automatizados**: Los agentes pueden pagar sin intermediarios
- 🌍 **Interoperabilidad**: Funciona globalmente sin fronteras
- 📊 **Datos inmutables**: Historial de accesibilidad que no se puede alterar

---

## 📚 Conceptos de Blockchain (para principiantes)

### 1. ¿Qué es Blockchain?

Imagina un **libro de contabilidad compartido** que:
- ✅ Todos pueden ver
- ✅ Nadie puede alterar el pasado
- ✅ No necesita un banco o gobierno central

### 2. Conceptos Clave

#### 🪙 Criptomoneda
**Dinero digital** que funciona sin bancos.
- **Bitcoin** es la más famosa
- **HBAR** es la criptomoneda de Hedera
- **ACCESA** es nuestro token personalizado

#### 🆔 Account ID (ID de Cuenta)
Tu "número de cuenta" en blockchain.
- Formato en Hedera: `0.0.12345`
- Es público (como tu email)
- Todos pueden ver tu balance (pero no quién eres)

#### 🔑 Private Key (Clave Privada)
Tu "contraseña ultra secreta" para firmar transacciones.
- **¡NUNCA la compartas!**
- Si la pierdes, pierdes acceso a tu cuenta
- Es como la combinación de una caja fuerte

#### 📝 Transacción
Cualquier operación en blockchain:
- Transferir dinero
- Crear un token
- Ejecutar un smart contract
- Todas quedan registradas para siempre

#### 🎟️ Token
Una "moneda personalizada" creada sobre una blockchain.
- **USDT** (Tether) representa dólares
- **ACCESA** representa créditos de accesibilidad
- Puedes crear tokens para lo que quieras

#### 💰 Gas Fee
El "costo de operación" en blockchain.
- Como la comisión de un banco, pero MUCHO más barata
- En Hedera: ~$0.0001 USD por transacción
- Compensa a los nodos que mantienen la red

#### 🤖 Agente de IA
Un programa que:
- Toma decisiones automáticas
- Puede pagar y recibir pagos
- Interactúa con otros agentes
- **Funciona sin intervención humana**

### 3. ¿Cómo Funciona una Transacción?

```
1. María necesita información accesible
   ↓
2. Su agente de IA detecta un servicio disponible
   ↓
3. El agente decide automáticamente si pagarlo
   ↓
4. Firma la transacción con su clave privada
   ↓
5. La envía a la red Hedera
   ↓
6. Los nodos validan y registran la transacción
   ↓
7. En 3-5 segundos: ¡Pago confirmado!
   ↓
8. María recibe el servicio
```

---

## 🏗️ Arquitectura del Proyecto

### Componentes Principales

```
┌─────────────────────────────────────────────────────┐
│                  MARKETPLACE AGENT                   │
│         (Conecta usuarios con servicios)             │
└──────────────────┬──────────────────────────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
┌──────────────┐      ┌──────────────┐
│ USER AGENTS  │      │SERVICE AGENTS│
│              │      │              │
│ • María      │◄────►│• Municipalidad│
│ • Carlos     │      │• Hospital    │
│ • Ana        │      │• Transporte  │
└──────┬───────┘      └──────┬───────┘
       │                     │
       │  PAGOS AUTOMÁTICOS  │
       │                     │
       └─────────┬───────────┘
                 ▼
      ┌──────────────────────┐
      │   HEDERA BLOCKCHAIN   │
      │                       │
      │  • Token ACCESA (HTS) │
      │  • Transacciones      │
      │  • Consenso aBFT      │
      └──────────────────────┘
```

### Flujo de Datos

1. **Usuario** → Agente de usuario detecta necesidad
2. **Agente** → Busca servicio en marketplace
3. **Marketplace** → Conecta con servicio apropiado
4. **Agente** → Decide si pagar (IA)
5. **Blockchain** → Ejecuta pago en Hedera
6. **Servicio** → Proporciona acceso
7. **Usuario** → Recibe servicio accesible

---

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Cuenta de Hedera Testnet (¡gratis!)

### Paso 1: Clonar el Repositorio

```bash
# Si estás en el hackathon, ya lo tienes
cd accesa_smart_cities_hedera

# Si lo clonas de GitHub
git clone <tu-repo-url>
cd accesa_smart_cities_hedera
```

### Paso 2: Crear Entorno Virtual (Recomendado)

```bash
# En Linux/Mac
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Esto instalará:
- `hedera-sdk-py` - SDK oficial de Hedera
- `Flask` - Para la API REST
- `openai` / `anthropic` - Para agentes de IA (opcional)
- Y más...

---

## ⚙️ Configuración

### 1. Obtener Credenciales de Hedera

#### Opción A: Hedera Portal (Recomendado)

1. Ve a https://portal.hedera.com/
2. Crea una cuenta gratuita
3. Crea un nuevo proyecto
4. Selecciona **Testnet**
5. Copia tu **Account ID** y **Private Key**

#### Opción B: Hedera Faucet

1. Ve a https://portal.hedera.com/register
2. Completa el proceso de registro
3. Recibirás credenciales por email

### 2. Configurar Variables de Entorno

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar con tus credenciales
nano .env  # o usa VS Code
```

Completa estos campos:

```env
# Tu cuenta de Hedera
HEDERA_ACCOUNT_ID=0.0.TU_NUMERO_AQUI
HEDERA_PRIVATE_KEY=302e...TU_CLAVE_AQUI

# Red (testnet para desarrollo)
HEDERA_NETWORK=testnet
```

### 3. Obtener HBAR de Prueba (Gratis)

Para crear tokens y hacer transacciones necesitas un poco de HBAR:

1. Ve a https://portal.hedera.com/faucet
2. Ingresa tu Account ID
3. Solicita HBAR gratis
4. ¡Listo para probar!

### 4. Verificar Configuración

```bash
python examples/quick_test.py
```

Deberías ver:

```
✅ Configuración cargada
✅ Conectado a Hedera TESTNET
✅ Balance consultado
✅ ¡TODOS LOS TESTS PASARON!
```

---

## 🎮 Cómo Usar

### Opción 1: Demo Completa (Recomendado para el Hackathon)

```bash
python examples/demo_complete.py
```

Esta demo ejecutará:
1. ✅ Conexión a Hedera
2. ✅ Creación del token ACCESA
3. ✅ Creación de agentes de usuario y servicio
4. ✅ 3 transacciones automáticas agente-a-agente
5. ✅ Visualización de resultados

**¡Perfecto para grabar el video del hackathon!** 🎥

### Opción 2: API REST

#### Iniciar el servidor

```bash
python api/app.py
```

El servidor estará en: http://localhost:5000

#### Ejemplos de uso

##### 1. Crear el token ACCESA

```bash
curl -X POST http://localhost:5000/token/create \
  -H "Content-Type: application/json" \
  -d '{
    "initial_supply": 1000000,
    "decimals": 2
  }'
```

##### 2. Crear un agente de usuario

```bash
curl -X POST http://localhost:5000/agent/user/create \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "maria_lopez",
    "accessibility_needs": ["visual_impairment"],
    "initial_budget": 500
  }'
```

##### 3. Crear un agente de servicio

```bash
curl -X POST http://localhost:5000/agent/service/create \
  -H "Content-Type: application/json" \
  -d '{
    "building_name": "Municipalidad de Mendoza"
  }'
```

##### 4. Ejecutar transacción automática

```bash
curl -X POST http://localhost:5000/agent/transaction \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "maria_lopez",
    "service_type": "visual_impairment"
  }'
```

##### 5. Ver estadísticas

```bash
curl http://localhost:5000/marketplace/stats
```

### Opción 3: Usar en tu Código Python

```python
from src.config import get_client
from agents.accessibility_agents import create_user_agent, create_building_service_agent, MarketplaceAgent

# Conectar a Hedera
client = get_client()

# Crear marketplace
marketplace = MarketplaceAgent(client)

# Crear un usuario
user = create_user_agent(
    client=client,
    user_id="maria",
    accessibility_needs=["visual_impairment"],
    initial_budget=500
)

# Crear un servicio
service = create_building_service_agent(
    client=client,
    building_name="Hospital_Central"
)

# Registrarlos
marketplace.register_user(user)
marketplace.register_service(service)

# Ejecutar transacción automática
result = marketplace.facilitate_transaction(
    user_agent=user,
    service_type="visual_impairment"
)

print(f"✅ Transacción: {result['status']}")
print(f"💰 Costo: {result['service']['price']} ACCESA")
```

---

## 🌐 API REST

### Endpoints Disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información de la API |
| GET | `/health` | Estado del sistema |
| GET | `/account/balance` | Consultar balance |
| POST | `/token/create` | Crear token ACCESA |
| POST | `/token/transfer` | Transferir tokens |
| POST | `/agent/user/create` | Crear agente de usuario |
| POST | `/agent/service/create` | Crear agente de servicio |
| POST | `/agent/transaction` | Ejecutar transacción |
| GET | `/marketplace/stats` | Estadísticas del marketplace |

Ver documentación completa en: http://localhost:5000 (cuando el servidor esté corriendo)

---

## 📁 Estructura del Proyecto

```
accesa_smart_cities_hedera/
│
├── src/                          # Código fuente principal
│   ├── config.py                 # Configuración de Hedera
│   ├── hedera_service.py         # Servicios básicos de Hedera
│   └── token_service.py          # Gestión del token ACCESA (HTS)
│
├── agents/                       # Agentes de IA
│   └── accessibility_agents.py   # Agentes de usuario, servicio y marketplace
│
├── api/                          # API REST
│   └── app.py                    # Servidor Flask
│
├── examples/                     # Ejemplos y demos
│   ├── quick_test.py             # Test rápido de configuración
│   └── demo_complete.py          # Demo completa para el hackathon
│
├── docs/                         # Documentación adicional
│   ├── BLOCKCHAIN_101.md         # Guía de blockchain para principiantes
│   ├── HEDERA_GUIDE.md           # Guía específica de Hedera
│   └── HACKATHON_CHECKLIST.md    # Checklist para el hackathon
│
├── .vscode/                      # Configuración de VS Code
│   ├── settings.json             # Settings recomendados
│   ├── launch.json               # Configuración de debugging
│   └── extensions.json           # Extensiones recomendadas
│
├── .env.example                  # Plantilla de variables de entorno
├── .gitignore                    # Archivos ignorados por Git
├── requirements.txt              # Dependencias de Python
├── README.md                     # Este archivo
└── LICENSE                       # Licencia MIT
```

---

## 🎥 Demo para el Hackathon

### Guion de la Demo (5 minutos)

#### Minuto 1: Introducción (30 seg)
```
"Hola, soy [tu nombre] y presento ACCESA Smart Cities.
Millones de personas enfrentan barreras de accesibilidad todos los días.
Nuestra solución usa agentes de IA que pagan automáticamente por servicios
de accesibilidad en la blockchain de Hedera."
```

#### Minuto 1-2: El Problema (30 seg)
```
"El problema no es la falta de servicios, sino:
- Información fragmentada
- Pagos complicados
- Falta de automatización
- Sistemas centralizados"
```

#### Minuto 2-4: La Demo en Vivo (2 min)
```bash
# Ejecutar la demo
python examples/demo_complete.py
```

Mientras corre, explica:
1. "Creamos tokens ACCESA en Hedera Token Service"
2. "Estos son agentes de IA que representan usuarios con diferentes necesidades"
3. "Y estos son servicios de edificios inteligentes"
4. "Ahora los agentes interactúan y pagan automáticamente..."
5. "¡Vean! 3 transacciones ejecutadas en segundos"

#### Minuto 4-5: Tecnología e Impacto (1 min)
```
"Tecnología usada:
- Hedera Token Service para tokens nativos
- Agentes de IA autónomos
- Python con hedera-sdk-py

Impacto:
- Pagos instantáneos ($0.0001 por transacción)
- Economía descentralizada de accesibilidad
- Escalable a toda Latinoamérica
- Auténtica economía agéntica"
```

### Grabando el Video

1. **Prepara el entorno**
   ```bash
   python examples/quick_test.py  # Verificar que todo funciona
   ```

2. **Graba la pantalla**
   - Usa OBS Studio (gratis) o Zoom
   - Muestra VS Code con el código
   - Ejecuta la demo
   - Muestra HashScan con las transacciones

3. **Puntos clave para mostrar**
   - ✅ El código de los agentes (con comentarios educativos)
   - ✅ La ejecución de la demo en tiempo real
   - ✅ Las transacciones en HashScan (https://hashscan.io/testnet)
   - ✅ Los logs mostrando las interacciones agente-a-agente

---

## 📚 Recursos de Aprendizaje

### Blockchain en General

- [Blockchain en 7 minutos](https://www.youtube.com/watch?v=yubzJw0uiE4) (YouTube)
- [¿Qué es blockchain?](https://www.blockchain.com/learning-portal/how-does-blockchain-work) (Blockchain.com)

### Hedera

- [Documentación oficial](https://docs.hedera.com/)
- [Hedera Portal](https://portal.hedera.com/) - Obtén credenciales
- [HashScan](https://hashscan.io/testnet) - Explorador de transacciones
- [Hedera Token Service](https://docs.hedera.com/hedera/sdks-and-apis/sdks/token-service)

### Python & Hedera

- [hedera-sdk-py en GitHub](https://github.com/hashgraph/hedera-sdk-python)
- [Ejemplos de código](https://docs.hedera.com/hedera/sdks-and-apis/sdks/token-service/define-a-token)

### Videos del Hackathon

- Workshop Hedera 1: Introducción para builders
- Workshop Hedera 2: Hedera Agent Kit
- Keynote Henry Tong: Economía Agéntica

---

## 🏆 Cumplimiento de Requisitos del Hackathon

### ✅ Requisitos Mínimos

- [x] **Agente de IA que ejecuta pagos**: Ver `agents/accessibility_agents.py`
- [x] **Operación en Hedera Testnet**: Configurado en `src/config.py`
- [x] **Uso de Hedera SDK**: hedera-sdk-py>=2.30.0
- [x] **Repositorio público en GitHub**: Este repositorio
- [x] **README con documentación**: Este archivo
- [x] **Video demo de 5 minutos**: Ejecutar `examples/demo_complete.py`
- [x] **Enlace público**: API REST en puerto 5000
- [x] **Pitch deck**: Ver `docs/PITCH_DECK.md`

### ⭐ Puntos Extra

- [x] **Hedera Token Service (HTS)**: Creación del token ACCESA
- [x] **Múltiples agentes interactuando**: UserAgent, ServiceAgent, MarketplaceAgent
- [x] **Casos de uso reales**: Accesibilidad en ciudades
- [x] **Arquitectura escalable**: Marketplace que soporta múltiples usuarios y servicios
- [x] **Comentarios educativos**: Todo el código está documentado para principiantes

---

## 🤝 Contribuir

Este proyecto fue desarrollado para el VendimiaTech Hackathon 2026.

Si quieres mejorarlo:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -m 'Agrego nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 👤 Autora

**Julieta Eyzaguirre Arenas**  
Ingeniera Informática y Educadora

- VendimiaTech Hackathon 2026
- Track: Hedera - Pagos a través de Agentes de IA
- Proyecto: ACCESA Smart Cities

---

## 🙏 Agradecimientos

- **Hedera** por proporcionar la infraestructura blockchain
- **VendimiaTech** por organizar este increíble hackathon
- **Henry Tong** y **Martin Gutter** por su mentoría
- Comunidad de **desarrolladores de Hedera** en Discord

---

## ❓ Preguntas Frecuentes

### ¿Necesito saber blockchain para usar esto?

**No**. Este proyecto está diseñado para principiantes. Lee la sección de "Conceptos de Blockchain" arriba.

### ¿Cuánto cuesta usar Hedera?

En **testnet** (pruebas): **Gratis**. Obtienes HBAR gratis para probar.  
En **mainnet** (producción): Centavos por miles de transacciones.

### ¿Puedo usar esto en producción?

Sí, solo cambia `HEDERA_NETWORK=mainnet` en `.env` y usa credenciales de mainnet.

### ¿Funciona en Windows/Mac/Linux?

Sí, Python funciona en todos los sistemas operativos.

### ¿Dónde veo mis transacciones?

En [HashScan](https://hashscan.io/testnet) - El explorador de bloques de Hedera.

---

## 🚨 Solución de Problemas

### Error: "HEDERA_ACCOUNT_ID no encontrado"

**Solución**: Crea el archivo `.env` copiando `.env.example` y completa tus credenciales.

### Error: "Insufficient balance"

**Solución**: Obtén HBAR gratis en https://portal.hedera.com/faucet

### Error: "Failed to connect"

**Solución**: Verifica tu conexión a internet y que `HEDERA_NETWORK=testnet`

### Error en imports

**Solución**: 
```bash
pip install -r requirements.txt --upgrade
```

---

## 📞 Soporte

Si tienes problemas durante el hackathon:

1. Revisa esta documentación
2. Consulta los archivos en `docs/`
3. Pregunta a los mentores en el evento
4. Discord de Hedera: https://hedera.com/discord

---

<div align="center">

**🏆 ¡Buena suerte en el hackathon! 🏆**

*La verdadera innovación no es solo tecnológica. Es inclusiva.*

---

[![Hedera](https://img.shields.io/badge/Built%20with-Hedera-blue)](https://hedera.com)
[![Python](https://img.shields.io/badge/Made%20with-Python-green)](https://python.org)
[![VendimiaTech](https://img.shields.io/badge/VendimiaTech-2026-purple)](https://vendimiahackathon.org)

</div>
