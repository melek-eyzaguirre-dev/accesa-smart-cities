"""
API REST PARA ACCESA SMART CITIES
==================================
¿Qué es esto?
Una API (Application Programming Interface) es como un mesero en un restaurante:
tú pides algo, el mesero lo lleva a la cocina, y te trae lo que pediste.

Esta API permite:
- Crear tokens ACCESA
- Gestionar agentes de IA
- Ejecutar transacciones
- Consultar balances

Todo desde una interfaz web simple (HTTP requests).
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import logging
import sys
import os

# Agregar el directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import get_client, get_config
from src.hedera_service import HederaService
from src.token_service import AccesaTokenService
from agents.accessibility_agents import (
    UserAgent,
    ServiceAgent,
    MarketplaceAgent,
    create_user_agent,
    create_building_service_agent
)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Crear la app Flask
# Configurar para servir frontend desde la carpeta /frontend
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend')
app = Flask(__name__, static_folder=frontend_dir, static_url_path='/static')
CORS(app)  # Permitir requests desde cualquier origen (para desarrollo)

# Variables globales para mantener estado
client = None
hedera_service = None
token_service = None
marketplace = None


def initialize_services():
    """Inicializa los servicios de Hedera."""
    global client, hedera_service, token_service, marketplace
    
    try:
        logger.info("🚀 Inicializando servicios de Hedera...")
        client = get_client()
        hedera_service = HederaService(client)
        token_service = AccesaTokenService(client)
        marketplace = MarketplaceAgent(client)
        logger.info("✅ Servicios inicializados correctamente")
        return True
    except Exception as e:
        logger.error(f"❌ Error inicializando servicios: {str(e)}")
        return False


# Rutas de la API

@app.route('/')
def home():
    """Ruta principal - Dashboard frontend."""
    return send_from_directory(frontend_dir, 'index.html')


@app.route('/api/info')
def api_info():
    """Información de la API (JSON)."""
    return jsonify({
        "name": "ACCESA Smart Cities API",
        "version": "1.0.0",
        "description": "API para pagos de accesibilidad con agentes de IA en Hedera",
        "endpoints": {
            "GET /": "Dashboard frontend",
            "GET /api/info": "Información de la API",
            "GET /health": "Estado del sistema",
            "GET /account/balance": "Consultar balance de cuenta",
            "POST /token/create": "Crear token ACCESA",
            "POST /token/transfer": "Transferir tokens",
            "POST /agent/user/create": "Crear agente de usuario",
            "POST /agent/service/create": "Crear agente de servicio",
            "POST /agent/transaction": "Ejecutar transacción entre agentes",
            "GET /agent/history/:agent_id": "Ver historial de agente"
        },
        "documentation": "Ver README.md para más información"
    })


@app.route('/health')
def health():
    """Verifica que todos los servicios estén funcionando."""
    try:
        config = get_config()
        account_info = config.get_account_info()
        
        return jsonify({
            "status": "healthy",
            "network": account_info['network'],
            "account_id": account_info['account_id'],
            "services": {
                "hedera": hedera_service is not None,
                "tokens": token_service is not None,
                "marketplace": marketplace is not None
            }
        })
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500


@app.route('/account/balance', methods=['GET'])
def get_balance():
    """Consulta el balance de una cuenta."""
    try:
        account_id = request.args.get('account_id')
        if not account_id:
            # Usar la cuenta del operador por defecto
            try:
                account_id = client.operatorAccountId.toString()
            except Exception:
                account_id = str(client.operatorAccountId)
        
        balance = hedera_service.get_account_balance(account_id)
        return jsonify(balance)
    
    except Exception as e:
        logger.error(f"❌ Error consultando balance: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/token/create', methods=['POST'])
def create_token():
    """
    Crea el token ACCESA.
    
    Body JSON:
    {
        "initial_supply": 1000000,
        "decimals": 2
    }
    """
    try:
        data = request.get_json() or {}
        initial_supply = data.get('initial_supply', 1000000)
        decimals = data.get('decimals', 2)
        
        logger.info(f"🪙 Creando token ACCESA...")
        result = token_service.create_accesa_token(initial_supply, decimals)
        
        return jsonify(result)
    
    except Exception as e:
        logger.error(f"❌ Error creando token: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/token/transfer', methods=['POST'])
def transfer_tokens():
    """
    Transfiere tokens ACCESA.
    
    Body JSON:
    {
        "to_account_id": "0.0.12345",
        "amount": 100,
        "memo": "Pago por servicio"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'to_account_id' not in data or 'amount' not in data:
            return jsonify({"error": "Faltan campos requeridos"}), 400
        
        result = token_service.transfer_tokens(
            to_account_id=data['to_account_id'],
            amount=data['amount'],
            memo=data.get('memo', '')
        )
        
        return jsonify(result)
    
    except Exception as e:
        logger.error(f"❌ Error transfiriendo tokens: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/agent/user/create', methods=['POST'])
def create_user_agent_endpoint():
    """
    Crea un agente de usuario.
    
    Body JSON:
    {
        "user_id": "maria_lopez",
        "accessibility_needs": ["visual_impairment"],
        "initial_budget": 1000
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'user_id' not in data:
            return jsonify({"error": "user_id es requerido"}), 400
        
        agent = create_user_agent(
            client=client,
            user_id=data['user_id'],
            accessibility_needs=data.get('accessibility_needs', []),
            initial_budget=data.get('initial_budget', 1000)
        )
        
        # Registrar en el marketplace
        marketplace.register_user(agent)
        
        return jsonify({
            "status": "success",
            "agent_id": agent.agent_id,
            "agent_type": agent.agent_type,
            "budget": agent.budget,
            "needs": agent.user_profile['accessibility_needs']
        })
    
    except Exception as e:
        logger.error(f"❌ Error creando agente de usuario: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/agent/service/create', methods=['POST'])
def create_service_agent_endpoint():
    """
    Crea un agente de servicio.
    
    Body JSON:
    {
        "building_name": "Municipalidad de Mendoza"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'building_name' not in data:
            return jsonify({"error": "building_name es requerido"}), 400
        
        agent = create_building_service_agent(
            client=client,
            building_name=data['building_name']
        )
        
        # Registrar en el marketplace
        marketplace.register_service(agent)
        
        return jsonify({
            "status": "success",
            "agent_id": agent.agent_id,
            "agent_type": agent.agent_type,
            "services": agent.service_catalog
        })
    
    except Exception as e:
        logger.error(f"❌ Error creando agente de servicio: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/agent/transaction', methods=['POST'])
def execute_agent_transaction():
    """
    Ejecuta una transacción entre agentes.
    
    Body JSON:
    {
        "user_id": "maria_lopez",
        "service_type": "visual_impairment"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'user_id' not in data or 'service_type' not in data:
            return jsonify({"error": "Faltan campos requeridos"}), 400
        
        # Buscar el agente de usuario en el marketplace
        user_agent = None
        for agent in marketplace.registered_users:
            if agent.agent_id == data['user_id']:
                user_agent = agent
                break
        
        if not user_agent:
            return jsonify({"error": "Usuario no encontrado"}), 404
        
        # Facilitar la transacción
        result = marketplace.facilitate_transaction(
            user_agent=user_agent,
            service_type=data['service_type']
        )
        
        return jsonify(result)
    
    except Exception as e:
        logger.error(f"❌ Error en transacción: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/marketplace/stats', methods=['GET'])
def marketplace_stats():
    """Obtiene estadísticas del marketplace."""
    return jsonify({
        "users_registered": len(marketplace.registered_users),
        "services_registered": len(marketplace.registered_services),
        "total_transactions": len(marketplace.action_history)
    })


if __name__ == '__main__':
    # Inicializar servicios al arrancar
    if not initialize_services():
        logger.error("❌ No se pudieron inicializar los servicios. Verifica tu configuración.")
        exit(1)
    
    # Obtener puerto desde env o usar 5000
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    logger.info(f"""
✅ API de ACCESA Smart Cities iniciada
🌐 Servidor: http://localhost:{port}
📚 Documentación: http://localhost:{port}/
    """)
    
    app.run(host='0.0.0.0', port=port, debug=debug)
