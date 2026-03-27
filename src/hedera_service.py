"""
SERVICIO DE HEDERA
==================
¿Qué es esto?
Este archivo contiene funciones básicas para interactuar con Hedera:
- Consultar balances (cuánto HBAR tienes)
- Transferir HBAR (la criptomoneda nativa de Hedera)
- Ver historial de transacciones

Conceptos de Blockchain:
- HBAR: La criptomoneda de Hedera (como Bitcoin es a Bitcoin, HBAR es a Hedera)
- Transacción: Cualquier operación en la blockchain (transferir dinero, crear tokens, etc.)
- Receipt: Comprobante de que tu transacción fue exitosa
- Transaction ID: Identificador único de tu transacción (como un número de seguimiento)
"""

from hedera import (
    AccountBalanceQuery,
    TransferTransaction,
    Hbar,
    AccountId,
    Client
)
import logging
from typing import Dict, Any
from decimal import Decimal

logger = logging.getLogger(__name__)


class HederaService:
    """
    Servicio para operaciones básicas en Hedera.
    
    Esta clase encapsula las operaciones más comunes que harás
    con Hedera, como consultar balances y hacer transferencias.
    """
    
    def __init__(self, client: Client):
        """
        Inicializa el servicio con un cliente de Hedera.
        
        Args:
            client: Cliente configurado de Hedera
        """
        self.client = client
        logger.info("✅ HederaService inicializado")
    
    def get_account_balance(self, account_id: str) -> Dict[str, Any]:
        """
        Consulta el balance de una cuenta.
        
        ¿Qué es un balance?
        Es cuánto dinero (HBAR) y tokens tiene una cuenta.
        Es como consultar tu saldo bancario.
        
        Args:
            account_id: ID de la cuenta a consultar (formato: "0.0.12345")
            
        Returns:
            Dict con el balance de HBAR y tokens
        """
        try:
            logger.info(f"🔍 Consultando balance de {account_id}...")
            
            # Crear la consulta (query)
            # En blockchain, leer datos es gratis, escribir datos cuesta
            query = AccountBalanceQuery().setAccountId(
                AccountId.fromString(account_id)
            )
            
            # Ejecutar la consulta
            balance = query.execute(self.client)
            
            # Convertir a formato legible
            result = {
                "account_id": account_id,
                "hbar_balance": float(balance.hbars.toString()),
                "tokens": {}
            }
            
            # Si tiene tokens, agregarlos
            if balance.tokens:
                for token_id, amount in balance.tokens.items():
                    result["tokens"][str(token_id)] = amount
            
            logger.info(f"✅ Balance: {result['hbar_balance']} HBAR")
            return result
            
        except Exception as e:
            logger.error(f"❌ Error consultando balance: {str(e)}")
            raise
    
    def transfer_hbar(
        self,
        to_account_id: str,
        amount: float,
        memo: str = ""
    ) -> Dict[str, Any]:
        """
        Transfiere HBAR de tu cuenta a otra.
        
        ¿Cómo funciona una transferencia en blockchain?
        1. Creas una transacción especificando: de quién, a quién, cuánto
        2. Firmas la transacción con tu clave privada (autorización)
        3. La envías a la red
        4. Los nodos validan y registran la transacción
        5. Recibes un comprobante (receipt)
        
        Args:
            to_account_id: Cuenta destino
            amount: Cantidad de HBAR a transferir
            memo: Nota opcional (ej: "Pago por servicio de accesibilidad")
            
        Returns:
            Dict con detalles de la transacción
        """
        try:
            logger.info(f"💸 Transfiriendo {amount} HBAR a {to_account_id}...")
            
            # Crear la transacción
            # addHbarTransfer con cantidad negativa = sale de tu cuenta
            # addHbarTransfer con cantidad positiva = entra a la otra cuenta
            transaction = TransferTransaction()
            
            # Restar de tu cuenta
            transaction.addHbarTransfer(
                self.client.operatorAccountId,
                Hbar.fromString(f"-{amount}")
            )
            
            # Sumar a la cuenta destino
            transaction.addHbarTransfer(
                AccountId.fromString(to_account_id),
                Hbar.fromString(str(amount))
            )
            
            # Agregar memo si se proporciona
            if memo:
                transaction.setTransactionMemo(memo)
            
            # Ejecutar la transacción
            # freeze(): Finaliza la construcción de la transacción
            # sign(): Firma con tu clave privada
            # execute(): Envía a la red
            # getReceipt(): Espera confirmación
            response = transaction.execute(self.client)
            receipt = response.getReceipt(self.client)
            
            # Obtener el ID de la transacción
            tx_id = str(response.transactionId)
            
            result = {
                "status": "success",
                "transaction_id": tx_id,
                "from": str(self.client.operatorAccountId),
                "to": to_account_id,
                "amount": amount,
                "memo": memo,
                "receipt_status": str(receipt.status)
            }
            
            logger.info(f"✅ Transferencia exitosa! TX ID: {tx_id}")
            return result
            
        except Exception as e:
            logger.error(f"❌ Error en transferencia: {str(e)}")
            raise
    
    def get_transaction_cost(self, transaction_type: str = "transfer") -> float:
        """
        Estima el costo de una transacción.
        
        ¿Por qué cuestan las transacciones?
        En blockchain, cada operación usa recursos de la red (almacenamiento,
        procesamiento). Los "gas fees" compensan a los nodos que mantienen
        la red funcionando. En Hedera, los costos son MUY bajos (centavos).
        
        Args:
            transaction_type: Tipo de transacción
            
        Returns:
            float: Costo estimado en HBAR
        """
        # Costos aproximados en Hedera (muchísimo más baratos que Ethereum)
        costs = {
            "transfer": 0.0001,  # $0.0001 USD aproximadamente
            "token_create": 1.0,  # $1 USD aproximadamente
            "token_transfer": 0.001,  # $0.001 USD
            "smart_contract": 0.05  # Variable según complejidad
        }
        
        return costs.get(transaction_type, 0.001)
