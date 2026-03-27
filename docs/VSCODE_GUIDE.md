# 💻 Guía de VS Code para ACCESA Smart Cities

## Extensiones Recomendadas

Cuando abras el proyecto por primera vez, VS Code te sugerirá instalar extensiones. ¡Acéptalas!

### Esenciales para Python

1. **Python** (Microsoft)
   - Soporte completo para Python
   - Debugging
   - IntelliSense

2. **Pylance** (Microsoft)
   - Type checking
   - Auto-completado inteligente

### Útiles para el Proyecto

3. **GitLens**
   - Ver historial de Git inline
   - Comparar cambios

4. **REST Client**
   - Probar la API sin salir de VS Code

5. **Better Comments**
   - Resalta comentarios importantes
   - Útil para entender el código educativo

6. **Error Lens**
   - Muestra errores inline
   - Detecta problemas rápidamente

## Atajos de Teclado Útiles

### Generales

| Atajo | Acción |
|-------|--------|
| `Ctrl+P` (Win/Linux) o `Cmd+P` (Mac) | Buscar archivo rápidamente |
| `Ctrl+Shift+P` | Command Palette (ejecutar comandos) |
| `Ctrl+` | Abrir terminal integrada |
| `Ctrl+B` | Toggle sidebar |

### Python

| Atajo | Acción |
|-------|--------|
| `F5` | Iniciar debugging |
| `F9` | Toggle breakpoint |
| `F10` | Step over (debugging) |
| `F11` | Step into (debugging) |
| `Shift+F5` | Detener debugging |

### Edición

| Atajo | Acción |
|-------|--------|
| `Ctrl+D` | Seleccionar siguiente ocurrencia |
| `Ctrl+Shift+L` | Seleccionar todas las ocurrencias |
| `Alt+Up/Down` | Mover línea arriba/abajo |
| `Ctrl+/` | Comentar/descomentar línea |
| `Ctrl+Space` | Trigger IntelliSense |

## Configuraciones de Debugging

### 1. Demo Completa

Ejecuta la demo completa del hackathon:

1. Abre el panel de debugging (`Ctrl+Shift+D`)
2. Selecciona "Demo Completa"
3. Presiona `F5`

### 2. API Flask

Inicia el servidor API:

1. Panel de debugging
2. Selecciona "API Flask"
3. `F5`
4. Visita http://localhost:5000

### 3. Quick Test

Verifica tu configuración:

1. Panel de debugging
2. Selecciona "Quick Test"
3. `F5`

## Tareas Automatizadas

Accede con `Ctrl+Shift+P` > "Tasks: Run Task"

### Tareas Disponibles

1. **Instalar Dependencias**
   - Ejecuta `pip install -r requirements.txt`

2. **Ejecutar Demo Completa**
   - Corre la demo del hackathon

3. **Test de Configuración**
   - Verifica que todo esté bien configurado

4. **Iniciar API**
   - Levanta el servidor Flask

5. **Limpiar Cache Python**
   - Elimina `__pycache__` y `.pyc`

## IntelliSense y Auto-Completado

### Usar IntelliSense

1. Empieza a escribir el nombre de una función o variable
2. VS Code mostrará sugerencias
3. Usa las flechas para navegar
4. `Enter` o `Tab` para aceptar

### Ver Documentación

- Coloca el cursor sobre una función
- Presiona `Ctrl+K Ctrl+I`
- Verás la documentación (nuestros comentarios educativos)

### Go to Definition

- `Ctrl+Click` en cualquier función o clase
- O `F12`
- Te lleva a la definición del código

## Terminal Integrada

### Abrir Terminal

- `` Ctrl+` `` (tecla backtick)
- O desde menú: Terminal > New Terminal

### Múltiples Terminales

1. Terminal 1: Servidor API
   ```bash
   python api/app.py
   ```

2. Terminal 2: Ejecutar demos
   ```bash
   python examples/demo_complete.py
   ```

3. Terminal 3: Testing
   ```bash
   python examples/quick_test.py
   ```

## Snippets Útiles

### Crear un Snippet Personalizado

1. `Ctrl+Shift+P` > "Preferences: Configure User Snippets"
2. Selecciona "python.json"
3. Agrega:

```json
{
    "Hedera Client": {
        "prefix": "hclient",
        "body": [
            "from src.config import get_client",
            "client = get_client()"
        ],
        "description": "Importar y crear cliente de Hedera"
    },
    "User Agent": {
        "prefix": "uagent",
        "body": [
            "from agents.accessibility_agents import create_user_agent",
            "user = create_user_agent(",
            "    client=client,",
            "    user_id='$1',",
            "    accessibility_needs=['$2'],",
            "    initial_budget=$3",
            ")"
        ],
        "description": "Crear agente de usuario"
    }
}
```

Ahora escribe `hclient` y presiona `Tab` para expandir.

## Debugging Tips

### Poner Breakpoints

1. Click en el margen izquierdo (al lado del número de línea)
2. Aparecerá un punto rojo
3. Ejecuta con `F5`
4. El programa se detendrá en ese punto

### Inspeccionar Variables

Cuando estés en un breakpoint:
- Panel izquierdo muestra todas las variables
- Hover sobre cualquier variable para ver su valor
- Panel "Watch" para observar variables específicas

### Debug Console

En modo debugging, la consola te permite:
```python
# Evaluar expresiones
print(user.budget)

# Llamar funciones
hedera_service.get_account_balance("0.0.12345")

# Ver objetos
user.__dict__
```

## Trabajar con Git

### Source Control Panel

1. `Ctrl+Shift+G` para abrir
2. Ver cambios
3. Stage files (botón +)
4. Commit (botón ✓)
5. Push

### GitLens

- Ver quién cambió cada línea
- Ver historial de un archivo
- Comparar versiones

## Comandos Útiles en Command Palette

`Ctrl+Shift+P` y escribe:

- `Python: Select Interpreter` - Elegir el intérprete (venv)
- `Format Document` - Formatear código
- `Organize Imports` - Ordenar imports
- `Reload Window` - Reiniciar VS Code
- `Clear Editor History` - Limpiar historial

## Configuración del Entorno Virtual

### Activar Automáticamente

1. Abre el proyecto
2. `Ctrl+Shift+P` > "Python: Select Interpreter"
3. Elige el intérprete de `./venv/bin/python`
4. VS Code activará el venv automáticamente en nuevas terminales

## Personalizar VS Code

### Cambiar Tema

1. `Ctrl+K Ctrl+T`
2. Elige un tema
3. Recomendados:
   - Dark+ (default)
   - Monokai
   - One Dark Pro

### Cambiar Íconos de Archivos

1. `Ctrl+Shift+P` > "Preferences: File Icon Theme"
2. Selecciona "Material Icon Theme" (si lo instalaste)

## Tips para el Hackathon

### Preparar la Demo

1. Abre `examples/demo_complete.py`
2. Lee el código con calma
3. Pon breakpoints en partes clave
4. Ejecuta con `F5` y observa el flujo
5. Practica explicar cada paso

### Grabar el Video

1. Cierra paneles innecesarios (`Ctrl+B` para sidebar)
2. Aumenta el zoom del editor (`Ctrl++`)
3. Usa un tema con buen contraste
4. Terminal a pantalla completa: `Ctrl+Shift+5`

### Presentar Código

- Usa `Ctrl+\` para split editor
- Muestra código y terminal simultáneamente
- Usa `Alt+Z` para word wrap
- Colapsa secciones con `Ctrl+Shift+[`

## Atajos para la Demo

### Navegación Rápida

```
Ctrl+P > demo      # Abre demo_complete.py
Ctrl+P > agent     # Abre accessibility_agents.py
Ctrl+P > config    # Abre config.py
```

### Mostrar Estructura

- `Ctrl+Shift+O` - Outline del archivo actual
- Ver todas las funciones y clases
- Saltar rápidamente a cada sección

## Troubleshooting en VS Code

### "Import could not be resolved"

**Solución**:
1. `Ctrl+Shift+P` > "Python: Select Interpreter"
2. Elige el intérprete de tu venv
3. Reload Window

### Linter Errors

**Deshabilitar temporalmente**:
```json
"python.linting.enabled": false
```

### Terminal no Activa Venv

**Solución**:
1. Cierra todas las terminales
2. Selecciona intérprete correcto
3. Abre nueva terminal

## Recursos

- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Debugging Python in VS Code](https://code.visualstudio.com/docs/python/debugging)
- [VS Code Tips & Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

---

**¡Domina VS Code y serás mucho más productivo en el hackathon!** 🚀
