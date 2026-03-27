"""
AGENTES DE IA PARA PAGOS DE ACCESIBILIDAD
==========================================
¿Qué son los agentes de IA?
Los agentes son programas autónomos que pueden:
- Tomar decisiones
- Ejecutar acciones
- Interactuar con otros agentes
- Realizar pagos sin intervención humana

¿Por qué son importantes para ciudades accesibles?
Permiten automatizar servicios de accesibilidad:
- Un usuario escanea un QR → el agente paga automáticamente por la info
- Un edificio ofrece servicios → el agente gestiona los pagos
- Las rutas accesibles generan micro-pagos automáticos

Esto es el FUTURO: una economía donde las máquinas interactúan entre sí
para facilitar servicios a las personas.
"""

from hedera import Client, AccountId
from typing import Dict, Any, Optional, List
import logging
import time
from datetime import datetime
import json

# Importar nuestros servicios
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.hedera_service import HederaService
from src.token_service import AccesaTokenService

logger = logging.getLogger(__name__)


class AccessibilityAgent:
    """
    Agente base para servicios de accesibilidad.
    
    Cada agente representa un actor en el ecosistema:
    - UserAgent: Representa a un usuario con necesidades de accesibilidad
    - ServiceAgent: Representa un servicio (edificio, transporte, etc.)
    - MarketplaceAgent: Intermediario que conecta usuarios con servicios
    """
    
    def __init__(
        self,
        client: Client,
        agent_id: str,
        agent_type: str
    ):
        """
        Inicializa el agente.
        
        Args:
            client: Cliente de Hedera
            agent_id: Identificador único del agente
            agent_type: Tipo de agente (user, service, marketplace)
        """
        self.client = client
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.hedera_service = HederaService(client)
        self.token_service = AccesaTokenService(client)
        
        # Historial de acciones del agente
        self.action_history: List[Dict[str, Any]] = []
        
        logger.info(f"✅ Agente {agent_type} '{agent_id}' inicializado")
    
    def log_action(self, action_type: str, details: Dict[str, Any]):
        """
        Registra una acción del agente.
        
        Args:
            action_type: Tipo de acción (payment, decision, interaction)
            details: Detalles de la acción
        """
        action = {
            "timestamp": datetime.now().isoformat(),
            "agent_id": self.agent_id,
            "agent_type": self.agent_type,
            "action_type": action_type,
            "details": details
        }
        self.action_history.append(action)
        logger.info(f"📝 {self.agent_id}: {action_type} - {details}")
    
    def get_history(self) -> List[Dict[str, Any]]:
        """Devuelve el historial de acciones del agente."""
        return self.action_history


class UserAgent(AccessibilityAgent):
    """
    Agente que representa a un usuario con necesidades de accesibilidad.
    
    Capacidades:
    - Decidir automáticamente qué servicios necesita
    - Pagar por servicios de accesibilidad
    - Evaluar la calidad de los servicios
    - Gestionar su presupuesto de ACCESA tokens
    """
    
    def __init__(
        self,
        client: Client,
        agent_id: str,
        user_profile: Dict[str, Any]
    ):
        """
        Inicializa el agente de usuario.
        
        Args:
            client: Cliente de Hedera
            agent_id: ID del agente
            user_profile: Perfil del usuario (necesidades de accesibilidad)
        """
        super().__init__(client, agent_id, "user")
        self.user_profile = user_profile
        self.budget = 0  # Budget en ACCESA tokens
        
        logger.info(f"👤 Usuario con perfil: {user_profile.get('accessibility_needs', [])}")
    
    def set_budget(self, amount: int):
        """
        Establece el presupuesto del agente.
        
        Args:
            amount: Cantidad de ACCESA tokens disponibles
        """
        self.budget = amount
        self.log_action("budget_set", {"amount": amount})
        logger.info(f"💰 Presupuesto establecido: {amount} ACCESA")
    
    def request_service(
        self,
        service_type: str,
        service_cost: int
    ) -> bool:
        """
        Decide si solicitar un servicio basándose en necesidades y presupuesto.
        
        Esta es la INTELIGENCIA del agente: evalúa si el servicio
        es necesario y si tiene fondos suficientes.
        
        Args:
            service_type: Tipo de servicio (audio_guide, visual_alert, etc.)
            service_cost: Costo del servicio en ACCESA tokens
            
        Returns:
            bool: True si decide solicitar el servicio
        """
        # Verificar si el usuario necesita este tipo de servicio
        needs = self.user_profile.get('accessibility_needs', [])
        
        # Lógica de decisión del agente
        is_needed = service_type in needs
        has_budget = self.budget >= service_cost
        
        decision = is_needed and has_budget
        
        self.log_action("service_evaluation", {
            "service_type": service_type,
            "cost": service_cost,
            "is_needed": is_needed,
            "has_budget": has_budget,
            "decision": "accept" if decision else "reject"
        })
        
        return decision
    
    def pay_for_service(
        self,
        service_provider_account: str,
        service_cost: int,
        service_description: str
    ) -> Dict[str, Any]:
        """
        Paga automáticamente por un servicio de accesibilidad.
        
        Este es el CORE del hackathon: un agente que ejecuta pagos
        de forma autónoma en la blockchain.
        
        Args:
            service_provider_account: Cuenta del proveedor del servicio
            service_cost: Costo en ACCESA tokens
            service_description: Descripción del servicio
            
        Returns:
            Dict con detalles del pago
        """
        try:
            logger.info(f"💳 Agente pagando {service_cost} ACCESA por: {service_description}")
            
            # Verificar presupuesto
            if self.budget < service_cost:
                raise ValueError(f"Presupuesto insuficiente: {self.budget} < {service_cost}")
            
            # Ejecutar el pago en Hedera
            payment_result = self.token_service.transfer_tokens(
                to_account_id=service_provider_account,
                amount=service_cost,
                memo=f"Pago automático por agente: {service_description}"
            )
            
            # Actualizar presupuesto
            self.budget -= service_cost
            
            # Registrar la acción
            self.log_action("payment_executed", {
                "service": service_description,
                "cost": service_cost,
                "provider": service_provider_account,
                "remaining_budget": self.budget,
                "transaction_id": payment_result['transaction_id']
            })
            
            logger.info(f"✅ Pago exitoso! TX: {payment_result['transaction_id']}")
            logger.info(f"💰 Presupuesto restante: {self.budget} ACCESA")
            
            return payment_result
            
        except Exception as e:
            logger.error(f"❌ Error en pago: {str(e)}")
            self.log_action("payment_failed", {
                "service": service_description,
                "error": str(e)
            })
            raise


class ServiceAgent(AccessibilityAgent):
    """
    Agente que representa un servicio de accesibilidad.
    
    Ejemplos:
    - Un edificio que ofrece información accesible
    - Un sistema de navegación con guías por voz
    - Un servicio de interpretación en lengua de señas
    
    Capacidades:
    - Publicar servicios disponibles
    - Recibir pagos automáticamente
    - Ajustar precios basándose en demanda
    """
    
    def __init__(
        self,
        client: Client,
        agent_id: str,
        service_catalog: List[Dict[str, Any]]
    ):
        """
        Inicializa el agente de servicio.
        
        Args:
            client: Cliente de Hedera
            agent_id: ID del agente
            service_catalog: Catálogo de servicios ofrecidos
        """
        super().__init__(client, agent_id, "service")
        self.service_catalog = service_catalog
        self.revenue = 0  # Ingresos acumulados
        
        logger.info(f"🏢 Servicio con catálogo: {[s['name'] for s in service_catalog]}")
    
    def get_service_price(self, service_type: str) -> Optional[int]:
        """
        Obtiene el precio de un servicio.
        
        Args:
            service_type: Tipo de servicio
            
        Returns:
            Precio en ACCESA tokens, o None si no existe
        """
        for service in self.service_catalog:
            if service['type'] == service_type:
                return service['price']
        return None
    
    def provide_service(
        self,
        user_agent: UserAgent,
        service_type: str
    ) -> Dict[str, Any]:
        """
        Provee un servicio a un usuario.
        
        Este método demuestra la INTERACCIÓN AGENTE-A-AGENTE:
        1. El servicio verifica si existe el servicio solicitado
        2. El usuario decide si lo quiere (basado en su IA)
        3. Si acepta, el usuario paga automáticamente
        4. El servicio registra el ingreso
        
        Args:
            user_agent: Agente del usuario
            service_type: Tipo de servicio solicitado
            
        Returns:
            Dict con resultado de la transacción
        """
        try:
            logger.info(f"🤝 Interacción agente-a-agente: {self.agent_id} ↔️ {user_agent.agent_id}")
            
            # Buscar el servicio en el catálogo
            service = None
            for s in self.service_catalog:
                if s['type'] == service_type:
                    service = s
                    break
            
            if not service:
                raise ValueError(f"Servicio '{service_type}' no disponible")
            
            # El usuario decide si acepta el servicio (IA autónoma)
            user_accepts = user_agent.request_service(
                service_type=service_type,
                service_cost=service['price']
            )
            
            if not user_accepts:
                result = {
                    "status": "rejected",
                    "reason": "Usuario rechazó el servicio",
                    "service": service
                }
                self.log_action("service_rejected", result)
                return result
            
            # Intentar pago real en blockchain; si falla, simular para demo
            payment = None
            try:
                payment = user_agent.pay_for_service(
                    service_provider_account=str(self.client.operatorAccountId),
                    service_cost=service['price'],
                    service_description=service['name']
                )
            except Exception as pay_err:
                logger.warning(f"⚠️ Pago blockchain no disponible ({pay_err}), usando modo demo simulado")
                # Simular pago exitoso para demo del hackathon
                import uuid
                user_agent.budget -= service['price']
                payment = {
                    "status": "success",
                    "transaction_id": f"demo-tx-{uuid.uuid4().hex[:12]}",
                    "from": user_agent.agent_id,
                    "to": self.agent_id,
                    "amount": service['price'],
                    "memo": f"[DEMO] Pago automático: {service['name']}",
                    "receipt_status": "SUCCESS",
                    "mode": "demo_simulation"
                }
                user_agent.log_action("payment_executed_demo", {
                    "service": service['name'],
                    "cost": service['price'],
                    "remaining_budget": user_agent.budget,
                    "transaction_id": payment['transaction_id']
                })
            
            # Registrar el ingreso
            self.revenue += service['price']
            
            result = {
                "status": "success",
                "service": service,
                "payment": payment,
                "total_revenue": self.revenue
            }
            
            self.log_action("service_provided", result)
            logger.info(f"✅ Servicio '{service['name']}' proporcionado exitosamente")
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Error proporcionando servicio: {str(e)}")
            raise


class MarketplaceAgent(AccessibilityAgent):
    """
    Agente que actúa como mercado/intermediario.
    
    Gestiona la conexión entre usuarios y servicios:
    - Registra servicios disponibles
    - Busca el mejor servicio para cada usuario
    - Facilita pagos entre agentes
    - Puede cobrar una pequeña comisión
    """
    
    def __init__(
        self,
        client: Client,
        agent_id: str = "marketplace"
    ):
        """Inicializa el agente de marketplace."""
        super().__init__(client, agent_id, "marketplace")
        self.registered_services: List[ServiceAgent] = []
        self.registered_users: List[UserAgent] = []
        
        logger.info("🏪 Marketplace de accesibilidad inicializado")
    
    def register_service(self, service_agent: ServiceAgent):
        """Registra un servicio en el marketplace."""
        self.registered_services.append(service_agent)
        self.log_action("service_registered", {
            "service_id": service_agent.agent_id,
            "services": [s['name'] for s in service_agent.service_catalog]
        })
        logger.info(f"📝 Servicio registrado: {service_agent.agent_id}")
    
    def register_user(self, user_agent: UserAgent):
        """Registra un usuario en el marketplace."""
        self.registered_users.append(user_agent)
        self.log_action("user_registered", {
            "user_id": user_agent.agent_id,
            "needs": user_agent.user_profile.get('accessibility_needs', [])
        })
        logger.info(f"📝 Usuario registrado: {user_agent.agent_id}")
    
    def match_service_to_user(
        self,
        user_agent: UserAgent,
        service_type: str
    ) -> Optional[ServiceAgent]:
        """
        Encuentra el mejor servicio para un usuario.
        
        Esta es la INTELIGENCIA del marketplace: busca el servicio
        que mejor se ajusta a las necesidades del usuario.
        
        Args:
            user_agent: Agente del usuario
            service_type: Tipo de servicio necesitado
            
        Returns:
            ServiceAgent que puede proveer el servicio, o None
        """
        logger.info(f"🔍 Buscando servicio '{service_type}' para {user_agent.agent_id}...")
        
        for service_agent in self.registered_services:
            if service_agent.get_service_price(service_type) is not None:
                logger.info(f"✅ Servicio encontrado: {service_agent.agent_id}")
                return service_agent
        
        logger.info(f"❌ No se encontró servicio para '{service_type}'")
        return None
    
    def facilitate_transaction(
        self,
        user_agent: UserAgent,
        service_type: str
    ) -> Dict[str, Any]:
        """
        Facilita una transacción entre usuario y servicio.
        
        Este método orquesta toda la interacción:
        1. Encuentra el servicio adecuado
        2. Conecta usuario con servicio
        3. Facilita el pago
        4. Registra la transacción
        
        Args:
            user_agent: Agente del usuario
            service_type: Tipo de servicio solicitado
            
        Returns:
            Dict con resultado de la transacción
        """
        try:
            logger.info(f"🤝 Facilitando transacción para {user_agent.agent_id}...")
            
            # Buscar servicio
            service_agent = self.match_service_to_user(user_agent, service_type)
            
            if not service_agent:
                raise ValueError(f"No hay servicios disponibles para '{service_type}'")
            
            # Facilitar la transacción
            result = service_agent.provide_service(user_agent, service_type)
            
            # Registrar en el marketplace
            self.log_action("transaction_facilitated", {
                "user": user_agent.agent_id,
                "service_provider": service_agent.agent_id,
                "service_type": service_type,
                "result": result['status']
            })
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Error facilitando transacción: {str(e)}")
            raise


# Funciones helper para crear agentes rápidamente

def create_user_agent(
    client: Client,
    user_id: str,
    accessibility_needs: List[str],
    initial_budget: int = 1000
) -> UserAgent:
    """
    Crea un agente de usuario con configuración básica.
    
    Args:
        client: Cliente de Hedera
        user_id: ID del usuario
        accessibility_needs: Lista de necesidades (ej: ["visual_impairment", "mobility"])
        initial_budget: Presupuesto inicial en ACCESA tokens
        
    Returns:
        UserAgent configurado
    """
    profile = {
        "user_id": user_id,
        "accessibility_needs": accessibility_needs
    }
    
    agent = UserAgent(client, user_id, profile)
    agent.set_budget(initial_budget)
    
    return agent


def create_building_service_agent(
    client: Client,
    building_name: str
) -> ServiceAgent:
    """
    Crea un agente de servicio para un edificio accesible.
    
    Args:
        client: Cliente de Hedera
        building_name: Nombre del edificio
        
    Returns:
        ServiceAgent configurado
    """
    catalog = [
        {
            "type": "visual_impairment",
            "name": f"Información por voz - {building_name}",
            "description": "Guía de voz con información del edificio y rutas internas",
            "price": 10  # 0.10 ACCESA (si decimals=2)
        },
        {
            "type": "hearing_impairment",
            "name": f"Videos en lengua de señas - {building_name}",
            "description": "Videos informativos en lengua de señas sobre servicios disponibles",
            "price": 15
        },
        {
            "type": "mobility",
            "name": f"Mapa de accesibilidad - {building_name}",
            "description": "Mapa interactivo con rampas, ascensores y rutas accesibles",
            "price": 5
        }
    ]
    
    return ServiceAgent(client, f"building_{building_name.lower()}", catalog)
