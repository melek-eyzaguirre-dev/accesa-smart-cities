"""
CONFIGURACIÓN DE HEDERA
======================
¿Qué es esto?
Este archivo maneja la configuración de tu conexión con la red Hedera.
Es como tener las llaves de tu casa digital en blockchain.

Conceptos importantes:
- Account ID: Tu identificador único en Hedera (como tu número de cuenta bancaria)
- Private Key: Tu clave secreta para firmar transacciones (¡guárdala bien!)
- Network: La red donde operas (testnet = pruebas, mainnet = producción real)
"""

import os
from dotenv import load_dotenv
from hedera import AccountId, PrivateKey, Client
from typing import Optional
import logging

# Configurar logging para ver qué está pasando
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar variables de entorno desde el archivo .env
load_dotenv()


class HederaConfig:
    """
    Clase para manejar la configuración de Hedera de forma segura.
    
    ¿Por qué usar una clase?
    - Mantiene toda la configuración en un solo lugar
    - Valida que tengamos todas las credenciales necesarias
    - Facilita el cambio entre testnet y mainnet
    """
    
    def __init__(self):
        """Inicializa la configuración y valida las credenciales"""
        
        # Obtener el ID de cuenta desde las variables de entorno
        account_id_str = os.getenv("HEDERA_ACCOUNT_ID")
        if not account_id_str:
            raise ValueError(
                "\n\u274c ERROR: HEDERA_ACCOUNT_ID no encontrado.\n"
                "Crea un archivo .env basado en .env.example"
            )
        
        # Obtener la clave privada
        private_key_str = os.getenv("HEDERA_PRIVATE_KEY")
        if not private_key_str:
            raise ValueError(
                "\n\u274c ERROR: HEDERA_PRIVATE_KEY no encontrada.\n"
                "Asegúrate de agregar tu clave privada en el archivo .env"
            )
        
        # Convertir strings a objetos de Hedera
        # AccountId: Representa tu cuenta en la red
        self.account_id = AccountId.fromString(account_id_str)
        
        # PrivateKey: Tu firma digital para autorizar transacciones
        self.private_key = PrivateKey.fromString(private_key_str)
        
        # Obtener la red (testnet por defecto)
        self.network = os.getenv("HEDERA_NETWORK", "testnet").lower()
        
        # Token ID de ACCESA (se configurará después de crear el token)
        accesa_token_id = os.getenv("ACCESA_TOKEN_ID")
        self.accesa_token_id = (
            AccountId.fromString(accesa_token_id) if accesa_token_id else None
        )
        
        logger.info(f"✅ Configuración cargada: Cuenta {self.account_id} en {self.network}")
    
    def get_client(self) -> Client:
        """
        Crea y devuelve un cliente de Hedera.
        
        ¿Qué es un Cliente?
        El Cliente es tu conexión a la red Hedera. Es como abrir tu app bancaria:
        necesitas identificarte para poder hacer transacciones.
        
        Returns:
            Client: Cliente configurado y listo para usar
        """
        
        # Crear cliente según la red
        if self.network == "testnet":
            # Testnet: Red de pruebas, usa HBAR falsos
            client = Client.forTestnet()
            logger.info("🧪 Conectando a Hedera TESTNET (red de pruebas)")
        elif self.network == "mainnet":
            # Mainnet: Red de producción, usa HBAR reales
            client = Client.forMainnet()
            logger.info("🚀 Conectando a Hedera MAINNET (red de producción)")
        else:
            raise ValueError(f"Red no válida: {self.network}. Usa 'testnet' o 'mainnet'")
        
        # Configurar el operador (tu cuenta que paga las transacciones)
        # Todas las transacciones en blockchain tienen un costo (gas fee)
        client.setOperator(self.account_id, self.private_key)
        
        return client
    
    def get_account_info(self) -> dict:
        """Devuelve información sobre la cuenta configurada"""
        return {
            "account_id": str(self.account_id),
            "network": self.network,
            "accesa_token_id": str(self.accesa_token_id) if self.accesa_token_id else None
        }


# Instancia global de configuración (singleton pattern)
# Esto evita crear múltiples conexiones innecesarias
config: Optional[HederaConfig] = None


def get_config() -> HederaConfig:
    """
    Obtiene la configuración global de Hedera.
    Si no existe, la crea.
    
    Returns:
        HederaConfig: Configuración global
    """
    global config
    if config is None:
        config = HederaConfig()
    return config


def get_client() -> Client:
    """
    Atajo para obtener un cliente de Hedera rápidamente.
    
    Returns:
        Client: Cliente configurado
    """
    return get_config().get_client()
