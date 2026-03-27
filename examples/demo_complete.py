"""
DEMO COMPLETA DE ACCESA SMART CITIES
=====================================
Este script demuestra el flujo completo del sistema:
1. Configuración inicial de Hedera
2. Creación del token ACCESA
3. Creación de agentes (usuarios y servicios)
4. Transacciones automáticas entre agentes
5. Visualización de resultados

Este es el script perfecto para la DEMO del hackathon!
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import get_client, get_config
from src.hedera_service import HederaService
from src.token_service import AccesaTokenService
from agents.accessibility_agents import (
    create_user_agent,
    create_building_service_agent,
    MarketplaceAgent
)
import logging
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

console = Console()


def print_step(step_num: int, title: str, description: str):
    """Imprime un paso de la demo de forma bonita."""
    console.print()
    console.print(Panel(
        f"[bold cyan]{title}[/bold cyan]\n{description}",
        title=f"[bold yellow]Paso {step_num}[/bold yellow]",
        border_style="cyan"
    ))
    console.print()


def main():
    """
    Función principal de la demo.
    """
    
    console.print(Panel.fit(
        "[bold magenta]ACCESA SMART CITIES[/bold magenta]\n"
        "[cyan]Sistema de Pagos para Accesibilidad en Hedera[/cyan]\n"
        "[yellow]VendimiaTech Hackathon 2026[/yellow]",
        border_style="magenta"
    ))
    
    try:
        # ===== PASO 1: Configuración =====
        print_step(
            1,
            "Configuración de Hedera",
            "Conectando con la red Hedera Testnet..."
        )
        
        config = get_config()
        client = get_client()
        
        account_info = config.get_account_info()
        console.print(f"✅ Conectado a: [cyan]{account_info['network']}[/cyan]")
        console.print(f"👤 Cuenta: [green]{account_info['account_id']}[/green]")
        
        time.sleep(1)
        
        # ===== PASO 2: Consultar Balance =====
        print_step(
            2,
            "Consultar Balance Inicial",
            "Verificando cuánto HBAR tenemos para operar..."
        )
        
        hedera_service = HederaService(client)
        balance = hedera_service.get_account_balance(account_info['account_id'])
        
        console.print(f"💰 Balance: [green]{balance['hbar_balance']} HBAR[/green]")
        
        if balance['hbar_balance'] < 5:
            console.print("[red]⚠️  Advertencia: Balance bajo. Obtén HBAR gratis en:[/red]")
            console.print("[yellow]https://portal.hedera.com/faucet[/yellow]")
        
        time.sleep(1)
        
        # ===== PASO 3: Crear Token ACCESA =====
        print_step(
            3,
            "Crear Token ACCESA",
            "Creando el token nativo para pagos de accesibilidad..."
        )
        
        token_service = AccesaTokenService(client)
        
        # Verificar si ya existe el token
        if account_info['accesa_token_id']:
            console.print(f"✅ Token ACCESA ya existe: [cyan]{account_info['accesa_token_id']}[/cyan]")
            token_service.token_id = account_info['accesa_token_id']
        else:
            console.print("🪙 Creando nuevo token ACCESA...")
            token_result = token_service.create_accesa_token(
                initial_supply=1000000,
                decimals=2
            )
            console.print(f"✅ Token creado: [green]{token_result['token_id']}[/green]")
            console.print(f"🔗 Ver en HashScan: https://hashscan.io/testnet/token/{token_result['token_id']}")
        
        time.sleep(2)
        
        # ===== PASO 4: Crear Marketplace =====
        print_step(
            4,
            "Crear Marketplace de Accesibilidad",
            "Inicializando el mercado donde usuarios y servicios interactúan..."
        )
        
        marketplace = MarketplaceAgent(client)
        console.print("✅ Marketplace inicializado")
        
        time.sleep(1)
        
        # ===== PASO 5: Crear Agentes de Usuario =====
        print_step(
            5,
            "Crear Agentes de Usuario",
            "Creando agentes que representan usuarios con diferentes necesidades..."
        )
        
        # Usuario 1: Persona con baja visión
        user1 = create_user_agent(
            client=client,
            user_id="maria_lopez",
            accessibility_needs=["visual_impairment"],
            initial_budget=500
        )
        marketplace.register_user(user1)
        console.print("✅ Usuario 1: María López (baja visión) - Budget: 500 ACCESA")
        
        # Usuario 2: Persona con discapacidad auditiva
        user2 = create_user_agent(
            client=client,
            user_id="carlos_ruiz",
            accessibility_needs=["hearing_impairment"],
            initial_budget=300
        )
        marketplace.register_user(user2)
        console.print("✅ Usuario 2: Carlos Ruiz (discapacidad auditiva) - Budget: 300 ACCESA")
        
        # Usuario 3: Persona con movilidad reducida
        user3 = create_user_agent(
            client=client,
            user_id="ana_martinez",
            accessibility_needs=["mobility"],
            initial_budget=200
        )
        marketplace.register_user(user3)
        console.print("✅ Usuario 3: Ana Martínez (movilidad reducida) - Budget: 200 ACCESA")
        
        time.sleep(1)
        
        # ===== PASO 6: Crear Agentes de Servicio =====
        print_step(
            6,
            "Crear Agentes de Servicio",
            "Creando agentes que representan edificios con servicios accesibles..."
        )
        
        # Servicio 1: Municipalidad
        service1 = create_building_service_agent(
            client=client,
            building_name="Municipalidad_Mendoza"
        )
        marketplace.register_service(service1)
        console.print("✅ Servicio 1: Municipalidad de Mendoza")
        
        # Servicio 2: Hospital
        service2 = create_building_service_agent(
            client=client,
            building_name="Hospital_Central"
        )
        marketplace.register_service(service2)
        console.print("✅ Servicio 2: Hospital Central")
        
        time.sleep(1)
        
        # ===== PASO 7: Transacciones Automáticas =====
        print_step(
            7,
            "Ejecutar Transacciones Automáticas",
            "Los agentes interactúan de forma autónoma y ejecutan pagos en Hedera..."
        )
        
        console.print("[yellow]🤖 Iniciando interacciones agente-a-agente...[/yellow]")
        console.print()
        
        # Transacción 1: María solicita información por voz
        console.print("[cyan]Transacción 1:[/cyan] María solicita guía de voz en Municipalidad...")
        result1 = marketplace.facilitate_transaction(
            user_agent=user1,
            service_type="visual_impairment"
        )
        
        if result1['status'] == 'success':
            console.print(f"✅ Pago ejecutado: {result1['service']['price']} ACCESA")
            console.print(f"🔗 TX ID: {result1['payment']['transaction_id']}")
        
        time.sleep(2)
        
        # Transacción 2: Carlos solicita videos en lengua de señas
        console.print()
        console.print("[cyan]Transacción 2:[/cyan] Carlos solicita videos en lengua de señas...")
        result2 = marketplace.facilitate_transaction(
            user_agent=user2,
            service_type="hearing_impairment"
        )
        
        if result2['status'] == 'success':
            console.print(f"✅ Pago ejecutado: {result2['service']['price']} ACCESA")
            console.print(f"🔗 TX ID: {result2['payment']['transaction_id']}")
        
        time.sleep(2)
        
        # Transacción 3: Ana solicita mapa de accesibilidad
        console.print()
        console.print("[cyan]Transacción 3:[/cyan] Ana solicita mapa de accesibilidad...")
        result3 = marketplace.facilitate_transaction(
            user_agent=user3,
            service_type="mobility"
        )
        
        if result3['status'] == 'success':
            console.print(f"✅ Pago ejecutado: {result3['service']['price']} ACCESA")
            console.print(f"🔗 TX ID: {result3['payment']['transaction_id']}")
        
        time.sleep(1)
        
        # ===== PASO 8: Resultados =====
        print_step(
            8,
            "Resultados de la Demo",
            "Resumen de todas las transacciones ejecutadas..."
        )
        
        # Crear tabla de resultados
        table = Table(title="Resumen de Transacciones")
        table.add_column("Usuario", style="cyan")
        table.add_column("Servicio", style="magenta")
        table.add_column("Costo", style="green")
        table.add_column("Budget Restante", style="yellow")
        
        table.add_row(
            "María (baja visión)",
            "Guía de voz",
            f"{result1['service']['price']} ACCESA",
            f"{user1.budget} ACCESA"
        )
        
        table.add_row(
            "Carlos (disc. auditiva)",
            "Videos en señas",
            f"{result2['service']['price']} ACCESA",
            f"{user2.budget} ACCESA"
        )
        
        table.add_row(
            "Ana (movilidad)",
            "Mapa accesible",
            f"{result3['service']['price']} ACCESA",
            f"{user3.budget} ACCESA"
        )
        
        console.print(table)
        
        # Estadísticas del marketplace
        console.print()
        console.print("[bold]Estadísticas del Marketplace:[/bold]")
        console.print(f"👥 Usuarios registrados: {len(marketplace.registered_users)}")
        console.print(f"🏛️ Servicios registrados: {len(marketplace.registered_services)}")
        console.print(f"💸 Transacciones facilitadas: 3")
        
        # Ingresos de los servicios
        console.print()
        console.print("[bold]Ingresos de Servicios:[/bold]")
        for service in marketplace.registered_services:
            console.print(f"{service.agent_id}: {service.revenue} ACCESA")
        
        # ===== PASO 9: Conclusión =====
        console.print()
        console.print(Panel(
            "[bold green]✅ DEMO COMPLETADA EXITOSAMENTE[/bold green]\n\n"
            "[cyan]Has demostrado:[/cyan]\n"
            "• Creación de tokens nativos en Hedera (HTS)\n"
            "• Agentes de IA que toman decisiones autónomas\n"
            "• Pagos automáticos en blockchain\n"
            "• Interacciones agente-a-agente\n"
            "• Aplicación real: accesibilidad en ciudades\n\n"
            "[yellow]¡Perfecto para el hackathon VendimiaTech 2026![/yellow]",
            border_style="green"
        ))
        
        console.print()
        console.print("[bold]Próximos pasos:[/bold]")
        console.print("1. Verifica las transacciones en: https://hashscan.io/testnet")
        console.print("2. Graba un video mostrando esta demo")
        console.print("3. Prepara tu pitch explicando la arquitectura")
        console.print("4. ¡A ganar el hackathon! 🏆")
        
    except Exception as e:
        console.print(f"\n[bold red]❌ Error: {str(e)}[/bold red]")
        logger.exception("Error en la demo")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
