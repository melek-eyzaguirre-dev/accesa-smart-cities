"""
TEST RÁPIDO DE CONFIGURACIÓN
==============================
Usa este script para verificar que tu configuración de Hedera está correcta.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import get_client, get_config
from src.hedera_service import HederaService
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    print("\n" + "="*50)
    print("🛠️  TEST DE CONFIGURACIÓN - ACCESA SMART CITIES")
    print("="*50 + "\n")
    
    try:
        # Test 1: Cargar configuración
        print("Test 1: Cargando configuración...")
        config = get_config()
        account_info = config.get_account_info()
        print(f"✅ Configuración cargada")
        print(f"   - Red: {account_info['network']}")
        print(f"   - Cuenta: {account_info['account_id']}")
        print()
        
        # Test 2: Conectar a Hedera
        print("Test 2: Conectando a Hedera...")
        client = get_client()
        print(f"✅ Conectado a Hedera {account_info['network'].upper()}")
        print()
        
        # Test 3: Consultar balance
        print("Test 3: Consultando balance...")
        hedera_service = HederaService(client)
        balance = hedera_service.get_account_balance(account_info['account_id'])
        print(f"✅ Balance consultado")
        print(f"   - HBAR: {balance['hbar_balance']}")
        print()
        
        # Resumen
        print("="*50)
        print("✅ ¡TODOS LOS TESTS PASARON!")
        print("="*50)
        print()
        print("🚀 Tu configuración está correcta.")
        print("🎯 Próximo paso: ejecuta la demo completa")
        print("   python examples/demo_complete.py")
        print()
        
        return 0
        
    except Exception as e:
        print("\n" + "="*50)
        print("❌ ERROR EN LA CONFIGURACIÓN")
        print("="*50)
        print(f"\n{str(e)}\n")
        print("🛠️  Solución:")
        print("1. Verifica que existe el archivo .env")
        print("2. Asegúrate de tener HEDERA_ACCOUNT_ID y HEDERA_PRIVATE_KEY")
        print("3. Obtén credenciales en: https://portal.hedera.com/")
        print("4. Copia .env.example a .env y completa los datos")
        print()
        return 1


if __name__ == "__main__":
    exit(main())
