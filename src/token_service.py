"""
SERVICIO DE TOKENS ACCESA (HTS)
================================
¿Qué es esto?
Aquí creamos y manejamos el token ACCESA usando Hedera Token Service (HTS).

¿Qué es un token?
Un token es como una moneda digital personalizada. Bitcoin y HBAR son
criptomonedas nativas de sus redes. Los tokens son criptomonedas creadas
SOBRE esas redes. Ejemplos:
- USDT (Tether) es un token que representa dólares
- ACCESA es un token que representa créditos de accesibilidad

¿Qué es HTS (Hedera Token Service)?
Es un servicio NATIVO de Hedera para crear tokens de forma fácil, segura y
económica. No necesitas escribir smart contracts complicados.

Ventajas de HTS:
- Tokens nativos = más rápidos y baratos que ERC-20
- Configuración flexible (supply, decimales, reglas)
- Cumplimiento regulatorio integrado
"""

from hedera import (
    TokenCreateTransaction,
    TokenType,
    TokenSupplyType,
    TokenAssociateTransaction,
    TransferTransaction,
    AccountId,
    Client,
    PrivateKey
)
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


def java_to_str(obj):
    """Convierte un objeto Java del SDK de Hedera a string Python."""
    try:
        return obj.toString()
    except Exception:
        return str(obj)


class AccesaTokenService:
    """
    Servicio para manejar el token ACCESA.
    
    El token ACCESA representa créditos que los usuarios pueden usar
    para pagar por servicios de accesibilidad en la ciudad:
    - Información de edificios accesibles
    - Guías por voz
    - Alertas personalizadas
    - Servicios premium de navegación
    """
    
    def __init__(self, client: Client):
        """
        Inicializa el servicio de tokens.
        
        Args:
            client: Cliente configurado de Hedera
        """
        self.client = client
        self.token_id: Optional[AccountId] = None
        logger.info("✅ AccesaTokenService inicializado")
    
    def create_accesa_token(
        self,
        initial_supply: int = 1000000,
        decimals: int = 2
    ) -> Dict[str, Any]:
        """
        Crea el token ACCESA en la red Hedera.
        
        ¿Cómo funciona la creación de un token?
        1. Defines las propiedades: nombre, símbolo, cantidad inicial
        2. Estableces reglas: ¿quién puede crear más? ¿se puede quemar?
        3. Pagas una pequeña tarifa (aprox $1 USD en HBAR)
        4. Recibes un Token ID único
        
        Args:
            initial_supply: Cantidad inicial de tokens (1,000,000 por defecto)
            decimals: Decimales del token (2 = permite 0.01 ACCESA)
            
        Returns:
            Dict con información del token creado
        """
        try:
            logger.info("🪙 Creando token ACCESA...")
            
            # Crear la transacción de creación de token
            transaction = (
                TokenCreateTransaction()
                # Nombre del token (aparece en exploradores y wallets)
                .setTokenName("ACCESA Smart Cities Token")
                
                # Símbolo (abreviatura, como BTC para Bitcoin)
                .setTokenSymbol("ACCESA")
                
                # Tipo: FUNGIBLE_COMMON significa que todos los tokens son iguales
                # (como billetes de dinero). Alternativa: NON_FUNGIBLE_UNIQUE (NFTs)
                .setTokenType(TokenType.FUNGIBLE_COMMON)
                
                # Decimales: 2 significa que puedes tener 0.01 ACCESA
                .setDecimals(decimals)
                
                # Supply inicial
                .setInitialSupply(initial_supply)
                
                # Tipo de supply: FINITE = hay un máximo, INFINITE = se puede crear más
                .setSupplyType(TokenSupplyType.INFINITE)
                
                # Max supply (si es FINITE)
                # .setMaxSupply(10000000)
                
                # Cuenta del tesoro (treasury): donde se guardan los tokens iniciales
                .setTreasuryAccountId(self.client.operatorAccountId)
                
                # Supply key: quien puede crear (mint) o destruir (burn) tokens
                .setSupplyKey(self.client.operatorPublicKey)
                
                # Admin key: quien puede modificar propiedades del token
                .setAdminKey(self.client.operatorPublicKey)
                
                # Memo descriptivo
                .setTokenMemo("Token para servicios de accesibilidad en ciudades inteligentes")
            )
            
            # Ejecutar la transacción
            logger.info("🔄 Enviando transacción a la red...")
            response = transaction.execute(self.client)
            
            # Obtener el receipt (comprobante)
            logger.info("⏳ Esperando confirmación...")
            receipt = response.getReceipt(self.client)
            
            # Obtener el Token ID del receipt
            self.token_id = receipt.tokenId
            
            # Convertir Java objects a strings legibles
            try:
                token_id_str = self.token_id.toString()
            except Exception:
                token_id_str = str(self.token_id)
            
            try:
                treasury_str = self.client.operatorAccountId.toString()
            except Exception:
                treasury_str = str(self.client.operatorAccountId)
            
            try:
                tx_id_str = response.transactionId.toString()
            except Exception:
                tx_id_str = str(response.transactionId)
            
            result = {
                "status": "success",
                "token_id": token_id_str,
                "token_name": "ACCESA Smart Cities Token",
                "token_symbol": "ACCESA",
                "initial_supply": initial_supply,
                "decimals": decimals,
                "treasury_account": treasury_str,
                "transaction_id": tx_id_str
            }
            
            logger.info(f"""
✅ ¡Token ACCESA creado exitosamente!
🎯 Token ID: {self.token_id}
💰 Supply inicial: {initial_supply} ACCESA
🔗 Puedes verlo en: https://hashscan.io/testnet/token/{self.token_id}
            """)
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Error creando token: {str(e)}")
            raise
    
    def associate_token(
        self,
        account_id: str,
        token_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Asocia el token ACCESA a una cuenta.
        
        ¿Qué es la asociación de tokens?
        En Hedera, antes de que una cuenta pueda recibir un token,
        debe "asociarse" con él. Es como decir "acepto recibir este token".
        Esto previene spam de tokens no deseados.
        
        Args:
            account_id: Cuenta que se asociará al token
            token_id: ID del token (usa el de ACCESA por defecto)
            
        Returns:
            Dict con el resultado de la asociación
        """
        try:
            # Usar el token ID de ACCESA si no se especifica otro
            token_id_obj = (
                AccountId.fromString(token_id) if token_id
                else self.token_id
            )
            
            if not token_id_obj:
                raise ValueError("No hay token ID configurado")
            
            logger.info(f"🔗 Asociando token {token_id_obj} a cuenta {account_id}...")
            
            # Crear transacción de asociación
            transaction = (
                TokenAssociateTransaction()
                .setAccountId(AccountId.fromString(account_id))
                .setTokenIds([token_id_obj])
            )
            
            # Ejecutar
            response = transaction.execute(self.client)
            receipt = response.getReceipt(self.client)
            
            result = {
                "status": "success",
                "account_id": account_id,
                "token_id": java_to_str(token_id_obj),
                "transaction_id": java_to_str(response.transactionId)
            }
            
            logger.info(f"✅ Cuenta {account_id} asociada exitosamente")
            return result
            
        except Exception as e:
            logger.error(f"❌ Error en asociación: {str(e)}")
            raise
    
    def transfer_tokens(
        self,
        to_account_id: str,
        amount: int,
        token_id: Optional[str] = None,
        memo: str = ""
    ) -> Dict[str, Any]:
        """
        Transfiere tokens ACCESA a otra cuenta.
        
        Args:
            to_account_id: Cuenta destino
            amount: Cantidad de tokens (en unidades mínimas, ej: 100 = 1.00 ACCESA si decimals=2)
            token_id: ID del token (usa ACCESA por defecto)
            memo: Nota opcional
            
        Returns:
            Dict con detalles de la transferencia
        """
        try:
            token_id_obj = (
                AccountId.fromString(token_id) if token_id
                else self.token_id
            )
            
            if not token_id_obj:
                raise ValueError("No hay token ID configurado")
            
            logger.info(f"💸 Transfiriendo {amount} ACCESA tokens a {to_account_id}...")
            
            # Crear transacción de transferencia
            transaction = TransferTransaction()
            
            # Restar tokens de tu cuenta
            transaction.addTokenTransfer(
                token_id_obj,
                self.client.operatorAccountId,
                -amount
            )
            
            # Sumar tokens a la cuenta destino
            transaction.addTokenTransfer(
                token_id_obj,
                AccountId.fromString(to_account_id),
                amount
            )
            
            if memo:
                transaction.setTransactionMemo(memo)
            
            # Ejecutar
            response = transaction.execute(self.client)
            receipt = response.getReceipt(self.client)
            
            result = {
                "status": "success",
                "transaction_id": java_to_str(response.transactionId),
                "from": java_to_str(self.client.operatorAccountId),
                "to": to_account_id,
                "amount": amount,
                "token_id": java_to_str(token_id_obj),
                "memo": memo
            }
            
            logger.info(f"✅ Transferencia exitosa! TX ID: {response.transactionId}")
            return result
            
        except Exception as e:
            logger.error(f"❌ Error en transferencia de tokens: {str(e)}")
            raise
