# 🚀 Inicio Rápido - ACCESA Smart Cities

## En 5 Minutos

### Paso 1: Obtener Credenciales de Hedera (2 min)

1. Ve a https://portal.hedera.com/
2. Crea cuenta gratuita
3. Crea un proyecto Testnet
4. Copia tu **Account ID** y **Private Key**
5. Solicita HBAR gratis: https://portal.hedera.com/faucet

### Paso 2: Configurar Proyecto (1 min)

```bash
# Copiar configuración de ejemplo
cp .env.example .env

# Editar con tus credenciales
nano .env  # o abre con VS Code
```

Completa:
```env
HEDERA_ACCOUNT_ID=0.0.TU_NUMERO
HEDERA_PRIVATE_KEY=TU_CLAVE_PRIVADA
HEDERA_NETWORK=testnet
```

### Paso 3: Instalar (1 min)

```bash
# Crear entorno virtual (recomendado)
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 4: Probar (1 min)

```bash
# Verificar configuración
python examples/quick_test.py

# Si ves "✅ ¡TODOS LOS TESTS PASARON!", estás listo
```

### Paso 5: Demo Completa

```bash
# Ejecutar la demo del hackathon
python examples/demo_complete.py
```

¡Listo! Verás:
- Creación del token ACCESA
- Agentes de usuario y servicios
- 3 transacciones automáticas en Hedera
- Resultados bonitos en terminal

---

## Qué Hacer Después

### Ver tus transacciones en blockchain:

1. Ve a https://hashscan.io/testnet
2. Busca tu Account ID
3. ¡Verás todas las transacciones!

### Iniciar la API:

```bash
python api/app.py
```

Visita http://localhost:5000

### Leer documentación:

- **README.md**: Documentación completa del proyecto
- **docs/BLOCKCHAIN_101.md**: ¿Nuevo en blockchain? Empieza aquí
- **docs/HACKATHON_GUIDE.md**: Checklist para el hackathon
- **docs/VSCODE_GUIDE.md**: Consejos para VS Code

---

## Solucionar Problemas

### Error: "HEDERA_ACCOUNT_ID no encontrado"

➡️ Crea el archivo `.env` copiando `.env.example`

### Error: "Insufficient balance"

➡️ Obtén HBAR gratis: https://portal.hedera.com/faucet

### Error en imports

➡️ Instala dependencias: `pip install -r requirements.txt`

### Error: "Failed to connect"

➡️ Verifica tu conexión a internet y que `HEDERA_NETWORK=testnet`

---

## Estructura del Proyecto

```
├── src/              # Código fuente principal
├── agents/           # Agentes de IA
├── api/              # API REST
├── examples/         # Demos y ejemplos
├── docs/             # Documentación
├── README.md         # Documentación completa
└── QUICKSTART.md     # Este archivo
```

---

## Próximos Pasos

1. ✅ Ejecuta la demo
2. ✅ Explora el código en VS Code
3. ✅ Lee la documentación
4. ✅ Personaliza los agentes
5. ✅ Graba tu video para el hackathon
6. ✅ ¡A ganar! 🏆

---

**¿Dudas?** Lee README.md o pregunta a los mentores del hackathon.

**¡Buena suerte!** 🚀
