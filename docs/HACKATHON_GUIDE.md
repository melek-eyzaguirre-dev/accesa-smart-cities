# 🏆 Guía del Hackathon VendimiaTech 2026

## Checklist Completo

### 📋 Antes del Viernes 27 (17:00 hs)

#### 1. Configuración Técnica

- [ ] Crear cuenta en Hedera Portal
- [ ] Obtener Account ID y Private Key
- [ ] Configurar archivo `.env`
- [ ] Obtener HBAR gratis del faucet
- [ ] Ejecutar `python examples/quick_test.py` exitosamente

#### 2. Crear Token ACCESA

- [ ] Ejecutar creación del token
- [ ] Guardar Token ID en `.env`
- [ ] Verificar en HashScan: https://hashscan.io/testnet
- [ ] Tomar screenshot del token en HashScan

#### 3. Ejecutar Demo

- [ ] Correr `python examples/demo_complete.py`
- [ ] Verificar que se crean agentes
- [ ] Confirmar que se ejecutan 3 transacciones
- [ ] Ver transacciones en HashScan
- [ ] Tomar screenshots de cada transacción

#### 4. Repositorio GitHub

- [ ] Crear repositorio público
- [ ] Inicializar Git: `git init`
- [ ] Agregar archivos: `git add .`
- [ ] Commit inicial: `git commit -m "Initial commit - ACCESA Smart Cities"`
- [ ] Vincular con GitHub: `git remote add origin <tu-url>`
- [ ] Push: `git push -u origin main`
- [ ] Verificar que se vea bien en GitHub
- [ ] **¡NO SUBIR EL ARCHIVO .env CON TUS CLAVES!**

#### 5. Video Demo (Máximo 5 minutos)

- [ ] Grabar intro (30 seg): Problema + Solución
- [ ] Mostrar código clave (1 min):
  - Agentes de IA
  - Lógica de pagos
- [ ] Ejecutar demo en vivo (2 min)
- [ ] Mostrar transacciones en HashScan (30 seg)
- [ ] Conclusión + impacto (1 min)
- [ ] Subir a YouTube (unlisted o public)
- [ ] Copiar enlace del video

#### 6. Pitch Deck (PDF)

- [ ] Portada con nombre del proyecto
- [ ] El problema (accesibilidad en ciudades)
- [ ] La solución (agentes + blockchain)
- [ ] Arquitectura técnica
- [ ] Demo/Screenshots
- [ ] Tecnologías usadas
- [ ] Impacto social
- [ ] Roadmap futuro
- [ ] Equipo
- [ ] Exportar a PDF

#### 7. Validación de Mercado

- [ ] Investigar estadísticas de discapacidad en Chile/LATAM
- [ ] Buscar datos de accesibilidad urbana
- [ ] Opcional: Encuesta rápida (Google Forms)
- [ ] Incluir fuentes en el pitch deck

#### 8. Subir a DoraHacks (ANTES de las 17:00)

- [ ] Crear cuenta en DoraHacks
- [ ] Encontrar VendimiaTech Hackathon 2026
- [ ] Seleccionar Track: Hedera Hackathon
- [ ] Subir:
  - [ ] Enlace al repositorio GitHub
  - [ ] Enlace al video demo
  - [ ] Pitch deck (PDF)
  - [ ] Enlace a la API (si está desplegada)
- [ ] **SUBIR CON 30-40 MINUTOS DE ANTICIPACIÓN**
- [ ] Confirmar que todo se subió correctamente

---

## 🎯 Requisitos Mínimos de Hedera

### ✅ Obligatorios

1. **Agente(s) de IA ejecutan pagos**
   - Ver: `agents/accessibility_agents.py`
   - Método: `UserAgent.pay_for_service()`

2. **Al menos una transacción en Hedera Testnet**
   - La demo ejecuta 3 transacciones
   - Todas visibles en HashScan

3. **Uso de Hedera SDK**
   - hedera-sdk-py >= 2.30.0
   - Ver: `requirements.txt`

4. **Repositorio público con README**
   - ✅ Ya está listo
   - README.md completo

5. **Video de 5 minutos o menos**
   - Mostrar agentes operando
   - Evidencia de pagos en blockchain

6. **Enlace público accesible**
   - API REST en puerto 5000
   - Endpoints documentados

7. **Pitch deck en PDF**
   - Ver sección "Contenido del Pitch Deck"

### ⭐ Puntos Extra

- [x] **Hedera Token Service (HTS)**: Token ACCESA
- [x] **Múltiples agentes**: User, Service, Marketplace
- [x] **Interacción agente-a-agente**: Sí
- [x] **Caso de uso real**: Accesibilidad urbana
- [ ] **Hedera CLI**: Opcional
- [ ] **Scheduled Transactions**: Opcional
- [ ] **HCS (Consensus Service)**: Opcional

---

## 📊 Criterios de Evaluación

### Distribución de Puntos

| Criterio | Peso | Cómo Maximizar |
|----------|------|------------------|
| **Integración con Hedera** | 25% | Usa HTS, muestra transacciones reales, explica por qué Hedera |
| **Ejecución (MVP funcional)** | 20% | Demo que funciona sin errores, código limpio |
| **Impacto** | 20% | Problema real, solución escalable, datos de mercado |
| **Validación** | 15% | Estadísticas, encuestas, entrevistas |
| **Innovación** | 10% | Agentes autónomos, economía agéntica |
| **Pitch** | 10% | Presentación clara, entusiasmo, responde bien preguntas |

### Tips para Cada Criterio

#### Integración con Hedera (25%)

**Qué mostrar:**
- Token ACCESA creado con HTS
- Transacciones exitosas en HashScan
- Código usando hedera-sdk-py

**Qué explicar:**
- Por qué Hedera (velocidad, costo, sostenibilidad)
- Cómo HTS simplifica la creación de tokens
- Ventajas sobre otras blockchains

#### Ejecución (20%)

**Qué demostrar:**
- Demo funcionando sin errores
- Código bien estructurado
- Comentarios educativos
- README completo

**Qué evitar:**
- Errores en vivo
- Código desorganizado
- Falta de documentación

#### Impacto (20%)

**Qué incluir:**
- Datos de personas con discapacidad en LATAM
- Problema actual de accesibilidad
- Cómo tu solución ayuda
- Potencial de escalabilidad

**Fuentes de datos:**
- INE (Chile)
- OMS (Organización Mundial de la Salud)
- SENADIS
- Estudios académicos

#### Validación (15%)

**Opciones:**
- Encuesta rápida (Google Forms)
- Estadísticas oficiales
- Entrevistas con personas con discapacidad
- Análisis de apps similares

#### Innovación (10%)

**Qué destacar:**
- Agentes que toman decisiones autónomas
- Pagos automáticos sin intervención humana
- Economía agéntica aplicada a accesibilidad
- Marketplace descentralizado

#### Pitch (10%)

**Estructura de 5 minutos:**
1. Problema (30 seg)
2. Solución (30 seg)
3. Demo (2 min)
4. Tecnología (1 min)
5. Impacto + Roadmap (1 min)

---

## 📦 Contenido del Pitch Deck

### Slide 1: Portada
- Logo/nombre: ACCESA SMART CITIES
- Tagline: "Pagos Automatizados para Accesibilidad en Ciudades Inteligentes"
- Tu nombre
- VendimiaTech Hackathon 2026

### Slide 2: El Problema
- Millones de personas con discapacidad en LATAM
- Barreras de accesibilidad diarias
- Servicios fragmentados y costosos
- Falta de automatización
- **Incluir estadísticas**

### Slide 3: La Solución
- Agentes de IA + Blockchain
- Pagos automáticos
- Marketplace descentralizado
- Token ACCESA

### Slide 4: Casos de Uso
- María: Persona con baja visión
- Carlos: Discapacidad auditiva
- Ana: Movilidad reducida
- **Con diagramas visuales**

### Slide 5: Arquitectura Técnica
- Diagrama de componentes
- User Agents
- Service Agents
- Marketplace Agent
- Hedera Blockchain

### Slide 6: Tecnologías
- Hedera Token Service (HTS)
- hedera-sdk-py
- Python
- Flask API
- Agentes de IA

### Slide 7: Demo / Screenshots
- Screenshots de:
  - Código de agentes
  - Terminal ejecutando demo
  - Transacciones en HashScan
  - Token ACCESA en HashScan

### Slide 8: Por qué Hedera?
- Transacciones en 3-5 segundos
- $0.0001 USD por transacción
- 10,000+ TPS
- Sostenible (huella de carbono negativa)
- HTS nativo (no necesita smart contracts)

### Slide 9: Impacto Social
- Mayor autonomía para personas con discapacidad
- Economía descentralizada de accesibilidad
- Escalable a toda LATAM
- Datos para políticas públicas

### Slide 10: Validación
- Estadísticas de mercado
- Resultados de encuesta (si la hiciste)
- Entrevistas
- Potencial de adopción

### Slide 11: Roadmap
- **Fase 1**: Piloto en Mendoza (10 edificios)
- **Fase 2**: Expansión regional (100+ edificios)
- **Fase 3**: Integración con gobierno
- **Fase 4**: LATAM

### Slide 12: Equipo
- Tu nombre
- Background (Ingeniera Informática + Educadora)
- Por qué te apasiona este proyecto

### Slide 13: Llamado a la Acción
- Repositorio GitHub
- Video demo
- Contacto
- **¡Gracias!**

---

## 🎥 Guion del Video Demo

### Segundo 0-30: Intro

```
"Hola, soy Julieta Eyzaguirre. Millones de personas con discapacidad
enfrentan barreras diarias en ciudades. Presento ACCESA Smart Cities:
agentes de IA que pagan automáticamente por servicios de accesibilidad
en la blockchain de Hedera."
```

### Segundo 30-60: El Problema

```
"El problema no es la falta de infraestructura, sino la falta de
automatización y descentralización en servicios de accesibilidad."
```

*Mostrar diapositiva con estadísticas*

### Segundo 60-120: Demo del Código

```
"Aquí tenemos tres tipos de agentes: usuarios, servicios y marketplace.
Cada agente puede tomar decisiones y ejecutar pagos autónomamente."
```

*Mostrar `accessibility_agents.py` con scroll lento*

### Segundo 120-240: Demo en Vivo

```
"Ahora ejecutemos la demo. Creamos el token ACCESA en Hedera Token Service,
registramos agentes, y... observen cómo interactúan."
```

*Ejecutar `python examples/demo_complete.py`*

```
"María necesita información por voz. Su agente evalúa, decide pagar
10 ACCESA tokens, y ejecuta la transacción. Todo en segundos."
```

### Segundo 240-270: Transacciones en HashScan

```
"Aquí en HashScan podemos ver las transacciones reales en la blockchain.
Tres pagos ejecutados con costos mínimos y confirmados en segundos."
```

*Mostrar HashScan con las transacciones*

### Segundo 270-300: Cierre

```
"Esta es la economía agéntica aplicada a un problema real: accesibilidad.
Con Hedera, creamos una solución escalable, económica y sostenible.
¡Transformemos nuestras ciudades!"
```

---

## ❓ Preguntas del Jurado (Prepara Respuestas)

### Técnicas

**P: ¿Por qué Hedera y no Ethereum u otra blockchain?**

R: "Tres razones clave:
1. Velocidad: Transacciones en 3-5 seg vs 15+ min en Ethereum
2. Costo: $0.0001 vs $5-50 en Ethereum
3. HTS: Token nativo sin smart contracts complejos
Para micropagos de accesibilidad, la velocidad y bajo costo son críticos."

**P: ¿Cómo funcionan los agentes de IA?**

R: "Los agentes evalúan:
1. Necesidades del usuario (perfil de accesibilidad)
2. Presupuesto disponible
3. Costo del servicio
Si coincide con sus necesidades y tiene fondos, ejecutan el pago
automáticamente. Es lógica de decisión programada."

**P: ¿Es escalable?**

R: "Sí. Hedera soporta 10,000+ TPS. Nuestra arquitectura de marketplace
permite agregar usuarios y servicios dinámicamente. El costo por
transacción permite millones de micropagos diarios."

### Negocio

**P: ¿Cómo se monetiza?**

R: "Modelo freemium:
- Básico: Información gratuita
- Premium: Servicios avanzados (10-50 ACCESA)
- Marketplace: Comisión del 5% en transacciones
- Licencias a gobiernos municipales"

**P: ¿Quién es tu usuario objetivo?**

R: "Tres segmentos:
1. Personas con discapacidad (usuarios finales)
2. Edificios y servicios (proveedores)
3. Gobiernos municipales (compradores B2G)"

**P: ¿Qué pasa con personas que no saben usar tecnología?**

R: "El sistema es autónomo: una vez configurado, los agentes trabajan
solos. Interfaces simples: QR codes, comandos de voz, app intuitiva.
Además, capacitación en comunidades."

### Impacto

**P: ¿Cómo validaste que este problema existe?**

R: "[Incluir tus fuentes]:
- X millones de personas con discapacidad en Chile
- Estudios de SENADIS sobre barreras urbanas
- [Si hiciste encuesta] Encuesta a N personas que confirmó..."

**P: ¿Qué te diferencia de otras soluciones?**

R: "Tres diferenciadores:
1. Automatización con agentes de IA
2. Blockchain para descentralización
3. Enfoque en economía agéntica (futuro de internet)
No hay soluciones que combinen estos tres elementos para accesibilidad."

---

## 🚀 Próximos Pasos Después del Hackathon

### Si Ganas

1. **🎯 Aprovechar la visibilidad**
   - Publicar en redes sociales
   - Conectar con embajadores de Hedera
   - Buscar mentores en el ecosistema

2. **🔧 Mejorar el prototipo**
   - Integrar con APIs reales de edificios
   - Crear app móvil
   - Dashboard de administración

3. **🤝 Buscar usuarios pilotos**
   - Contactar municipalidades
   - Organizaciones de personas con discapacidad
   - Edificios públicos en Mendoza

4. **💰 Buscar financiamiento**
   - Grants de Hedera
   - Fondos de innovación social
   - Competir en más hackathons

### Si No Ganas

**¡También ganaste experiencia valiosa!**

1. Aprendiste blockchain
2. Tienes un proyecto completo en tu portfolio
3. Conociste la comunidad
4. Puedes seguir desarrollando

**El proyecto sigue siendo valioso:**
- Publcalo en tu LinkedIn
- Usa el código en otros hackathons
- Aplicá lo aprendido en futuros proyectos

---

## 📌 Enlaces Útiles

### Hedera
- Portal: https://portal.hedera.com/
- Faucet: https://portal.hedera.com/faucet
- HashScan: https://hashscan.io/testnet
- Docs: https://docs.hedera.com/
- Discord: https://hedera.com/discord

### Hackathon
- DoraHacks: [URL del evento]
- Discord VendimiaTech: [URL]
- Horarios de mentoría: Ver guía principal

### Recursos
- Este proyecto en GitHub: [tu-repo]
- Video demo: [tu-video]
- Pitch deck: [tu-link]

---

## ✨ Mensaje Final

**Respira hondo. Estás preparado.**

Tienes:
- ✅ Código funcional
- ✅ Documentación completa
- ✅ Demo lista
- ✅ Conocimiento de blockchain
- ✅ Un proyecto con propósito

**Tu proyecto no es solo tecnológico. Es inclusivo.**

Estás construyendo un futuro donde la tecnología sirve a todos.
Eso vale más que cualquier premio.

**¡Éxito en el hackathon!** 🎯🏆

---

*Cualquier pregunta: usa los mentores del evento o Discord de Hedera.*
