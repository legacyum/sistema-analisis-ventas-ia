#!/usr/bin/env python3
"""
🎯 VISTA FACIL - Interfaz Simplificada del Sistema de Análisis de Ventas
=======================================================================

Una interfaz web simple y amigable que hace que el sistema complejo de 
análisis de ventas sea accesible para todos los usuarios.

Características:
- Interfaz web moderna y limpia
- Un solo clic para generar datos demo
- Acceso directo a dashboards principales  
- Estado visual del sistema
- Configuración automática

Autor: GitHub Copilot
Fecha: Julio 2025
"""

import os
import sys
import subprocess
import threading
import time
import webbrowser
from datetime import datetime
import pandas as pd
from pathlib import Path

try:
    import dash
    from dash import dcc, html, Input, Output, callback, clientside_callback
    import dash_bootstrap_components as dbc
    import plotly.express as px
    import plotly.graph_objects as go
except ImportError as e:
    print(f"Error importando dependencias: {e}")
    print("Instala con: pip install dash dash-bootstrap-components plotly")
    sys.exit(1)

class VistaFacil:
    """Clase principal para la Vista Fácil"""
    
    def __init__(self):
        self.app = dash.Dash(
            __name__,
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            title="Vista Fácil - Sistema de Análisis de Ventas",
            suppress_callback_exceptions=True
        )
        self.puerto = 8053
        self.setup_layout()
        self.setup_callbacks()
        
    def verificar_sistema(self):
        """Verificar el estado del sistema"""
        estado = {
            'dependencias': True,
            'datos': False,
            'archivos': True
        }
        
        # Verificar datos
        archivos_datos = [f for f in os.listdir('.') if f.endswith('.xlsx')]
        if archivos_datos:
            estado['datos'] = True
            
        return estado
    
    def obtener_estadisticas_rapidas(self):
        """Obtener estadísticas rápidas si hay datos disponibles"""
        try:
            archivos_excel = [f for f in os.listdir('.') if f.endswith('.xlsx')]
            if not archivos_excel:
                return None
                
            # Intentar leer el primer archivo Excel encontrado
            df = pd.read_excel(archivos_excel[0])
            
            # Estadísticas básicas
            stats = {
                'total_registros': len(df),
                'archivo': archivos_excel[0],
                'columnas': list(df.columns[:5]),  # Primeras 5 columnas
                'fecha_archivo': datetime.fromtimestamp(
                    os.path.getmtime(archivos_excel[0])
                ).strftime('%d/%m/%Y %H:%M')
            }
            
            # Si tiene columnas de ventas, calcular totales
            if 'TOTAL_VENTA' in df.columns:
                stats['total_ventas'] = f"${df['TOTAL_VENTA'].sum():,.2f}"
            elif 'PRECIO' in df.columns and 'CANTIDAD' in df.columns:
                total = (df['PRECIO'] * df['CANTIDAD']).sum()
                stats['total_ventas'] = f"${total:,.2f}"
            else:
                stats['total_ventas'] = "No disponible"
                
            return stats
        except Exception as e:
            print(f"Error leyendo datos: {e}")
            return None
    
    def setup_layout(self):
        """Configurar el layout de la aplicación"""
        
        # Header principal
        header = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H1([
                            "🎯 VISTA FÁCIL", 
                            html.Small(" - Sistema de Análisis de Ventas", 
                                     className="text-muted ms-2")
                        ], className="display-4 fw-bold text-center mb-3"),
                        html.P([
                            "Interfaz simplificada para acceder fácilmente a todas las funciones del sistema de análisis de ventas con IA"
                        ], className="lead text-center text-muted mb-4")
                    ])
                ], width=12)
            ], className="mb-4")
        ], fluid=True, className="bg-light py-4")
        
        # Panel de estado del sistema
        panel_estado = dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([
                            html.H5(["🔍 Estado del Sistema"], className="mb-0")
                        ]),
                        dbc.CardBody([
                            html.Div(id="estado-sistema"),
                            dbc.Button(
                                "🔄 Actualizar Estado",
                                id="btn-actualizar-estado",
                                color="outline-primary",
                                size="sm",
                                className="mt-2"
                            )
                        ])
                    ])
                ], width=4),
                
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([
                            html.H5(["📊 Datos Disponibles"], className="mb-0")
                        ]),
                        dbc.CardBody([
                            html.Div(id="info-datos")
                        ])
                    ])
                ], width=8)
            ], className="mb-4")
        ], fluid=True)
        
        # Acciones rápidas
        acciones_rapidas = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H4("🚀 Acciones Rápidas", className="mb-3"),
                ], width=12)
            ]),
            dbc.Row([
                # Generar datos demo
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.H5("🎲 Datos Demo", className="card-title"),
                                html.P("Genera datos de ejemplo para probar el sistema", 
                                      className="card-text"),
                                dbc.Button(
                                    "Generar Datos Demo",
                                    id="btn-demo",
                                    color="success",
                                    size="lg",
                                    className="w-100"
                                )
                            ])
                        ])
                    ], className="h-100")
                ], width=6, className="mb-3"),
                
                # Dashboard IA Premium
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.H5("🤖 Dashboard IA", className="card-title"),
                                html.P("Análisis avanzado con inteligencia artificial", 
                                      className="card-text"),
                                dbc.Button(
                                    "Abrir Dashboard IA",
                                    id="btn-dashboard-ia",
                                    color="primary",
                                    size="lg",
                                    className="w-100"
                                )
                            ])
                        ])
                    ], className="h-100")
                ], width=6, className="mb-3"),
                
                # Dashboard Streamlit
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.H5("⚡ Dashboard Simple", className="card-title"),
                                html.P("Interfaz limpia y rápida con Streamlit", 
                                      className="card-text"),
                                dbc.Button(
                                    "Abrir Dashboard Simple",
                                    id="btn-dashboard-streamlit",
                                    color="info",
                                    size="lg",
                                    className="w-100"
                                )
                            ])
                        ])
                    ], className="h-100")
                ], width=6, className="mb-3"),
                
                # Análisis completo
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div([
                                html.H5("🧠 Análisis IA", className="card-title"),
                                html.P("Análisis completo con predicciones y recomendaciones", 
                                      className="card-text"),
                                dbc.Button(
                                    "Ejecutar Análisis IA",
                                    id="btn-analisis-ia",
                                    color="warning",
                                    size="lg",
                                    className="w-100"
                                )
                            ])
                        ])
                    ], className="h-100")
                ], width=6, className="mb-3")
            ])
        ], fluid=True, className="mb-4")
        
        # Panel de ayuda
        panel_ayuda = dbc.Container([
            dbc.Accordion([
                dbc.AccordionItem([
                    html.P("1. Si es tu primera vez, haz clic en 'Generar Datos Demo' para crear datos de ejemplo"),
                    html.P("2. Una vez que tengas datos, puedes usar cualquiera de los dashboards"),
                    html.P("3. El Dashboard IA es más avanzado, el Dashboard Simple es más rápido"),
                    html.P("4. El Análisis IA genera reportes con predicciones automáticas"),
                ], title="🆘 ¿Cómo usar este sistema?"),
                
                dbc.AccordionItem([
                    html.P("• Dashboard IA Premium: Interfaz profesional con gradientes y animaciones"),
                    html.P("• Dashboard Simple: Interfaz limpia tipo Streamlit, ideal para análisis rápido"),
                    html.P("• Análisis IA: Genera predicciones, segmentaciones y recomendaciones automáticas"),
                    html.P("• Datos Demo: Crea 1000+ registros de ventas sintéticos para pruebas"),
                ], title="📋 ¿Qué hace cada opción?"),
                
                dbc.AccordionItem([
                    html.P("• Si no tienes datos: Usa 'Generar Datos Demo' primero"),
                    html.P("• Si los dashboards no cargan: Verifica el estado del sistema"),
                    html.P("• Para mejores resultados: Usa archivos Excel con columnas: Producto, Precio, Cantidad, Fecha"),
                    html.P("• Puertos usados: 8051 (Dashboard IA), 8502 (Streamlit), 8053 (Vista Fácil)"),
                ], title="💡 Consejos y solución de problemas")
            ], start_collapsed=True)
        ], fluid=True, className="mb-4")
        
        # Footer
        footer = html.Footer([
            dbc.Container([
                html.Hr(),
                html.P([
                    "🚀 Sistema de Análisis de Ventas con IA | ",
                    html.A("Documentación", href="#", className="text-decoration-none"),
                    " | ",
                    f"Vista Fácil v1.0 - Puerto {self.puerto}"
                ], className="text-center text-muted small")
            ], fluid=True)
        ])
        
        # Layout principal
        self.app.layout = dbc.Container([
            header,
            panel_estado,
            acciones_rapidas,
            panel_ayuda,
            footer,
            
            # Modales y elementos ocultos
            dbc.Modal([
                dbc.ModalHeader("🔄 Procesando..."),
                dbc.ModalBody([
                    dbc.Spinner([
                        html.P(id="modal-mensaje", children="Ejecutando acción...")
                    ])
                ])
            ], id="modal-procesando", is_open=False),
            
            # Interval para actualizaciones
            dcc.Interval(
                id='interval-component',
                interval=30*1000,  # Actualizar cada 30 segundos
                n_intervals=0
            )
        ], fluid=True, className="py-3")
    
    def setup_callbacks(self):
        """Configurar los callbacks de la aplicación"""
        
        @self.app.callback(
            [Output('estado-sistema', 'children'),
             Output('info-datos', 'children')],
            [Input('btn-actualizar-estado', 'n_clicks'),
             Input('interval-component', 'n_intervals')]
        )
        def actualizar_estado(n_clicks, n_intervals):
            estado = self.verificar_sistema()
            stats = self.obtener_estadisticas_rapidas()
            
            # Estado del sistema
            estado_items = []
            for key, value in estado.items():
                if key == 'dependencias':
                    label = "Dependencias Python"
                elif key == 'datos':
                    label = "Archivos de datos"
                elif key == 'archivos':
                    label = "Scripts del sistema"
                else:
                    label = key.title()
                    
                icon = "✅" if value else "❌"
                color = "success" if value else "danger"
                estado_items.append(
                    dbc.ListGroupItem([
                        html.Span(f"{icon} {label}")
                    ], color=color)
                )
            
            estado_component = dbc.ListGroup(estado_items, flush=True)
            
            # Información de datos
            if stats:
                info_datos = dbc.ListGroup([
                    dbc.ListGroupItem([
                        html.Strong("Archivo: "), stats['archivo']
                    ]),
                    dbc.ListGroupItem([
                        html.Strong("Registros: "), f"{stats['total_registros']:,}"
                    ]),
                    dbc.ListGroupItem([
                        html.Strong("Total ventas: "), stats['total_ventas']
                    ]),
                    dbc.ListGroupItem([
                        html.Strong("Última modificación: "), stats['fecha_archivo']
                    ])
                ], flush=True)
            else:
                info_datos = dbc.Alert([
                    html.H6("Sin datos disponibles", className="alert-heading"),
                    html.P("No se encontraron archivos Excel. Usa 'Generar Datos Demo' para crear datos de ejemplo.")
                ], color="warning")
            
            return estado_component, info_datos
        
        @self.app.callback(
            [Output('modal-procesando', 'is_open'),
             Output('modal-mensaje', 'children')],
            [Input('btn-demo', 'n_clicks'),
             Input('btn-dashboard-ia', 'n_clicks'),
             Input('btn-dashboard-streamlit', 'n_clicks'),
             Input('btn-analisis-ia', 'n_clicks')],
            prevent_initial_call=True
        )
        def manejar_acciones(demo_clicks, ia_clicks, streamlit_clicks, analisis_clicks):
            ctx = dash.callback_context
            if not ctx.triggered:
                return False, ""
            
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            
            if button_id == 'btn-demo':
                self.ejecutar_en_background('demo_ia.py', 'Generando datos demo...')
                return True, "🎲 Generando datos de demostración con IA..."
                
            elif button_id == 'btn-dashboard-ia':
                self.ejecutar_dashboard_ia()
                return True, "🤖 Iniciando Dashboard IA Premium..."
                
            elif button_id == 'btn-dashboard-streamlit':
                self.ejecutar_dashboard_streamlit()
                return True, "⚡ Iniciando Dashboard Simple..."
                
            elif button_id == 'btn-analisis-ia':
                self.ejecutar_en_background('analisis_ia.py', 'Ejecutando análisis IA...')
                return True, "🧠 Ejecutando análisis completo con IA..."
            
            return False, ""
    
    def ejecutar_en_background(self, script, mensaje):
        """Ejecutar un script en segundo plano"""
        def ejecutar():
            try:
                result = subprocess.run([sys.executable, script], 
                                      capture_output=True, text=True, cwd=os.getcwd())
                print(f"✅ {mensaje} completado")
                if result.stdout:
                    print("Salida:", result.stdout[:200] + "..." if len(result.stdout) > 200 else result.stdout)
            except Exception as e:
                print(f"❌ Error ejecutando {script}: {e}")
        
        thread = threading.Thread(target=ejecutar)
        thread.daemon = True
        thread.start()
    
    def ejecutar_dashboard_ia(self):
        """Ejecutar dashboard IA en segundo plano"""
        def ejecutar():
            try:
                subprocess.Popen([sys.executable, 'dashboard_ia.py'], cwd=os.getcwd())
                time.sleep(3)  # Esperar a que se inicie
                webbrowser.open('http://localhost:8051')
            except Exception as e:
                print(f"❌ Error ejecutando dashboard IA: {e}")
        
        thread = threading.Thread(target=ejecutar)
        thread.daemon = True
        thread.start()
    
    def ejecutar_dashboard_streamlit(self):
        """Ejecutar dashboard Streamlit en segundo plano"""
        def ejecutar():
            try:
                subprocess.Popen([sys.executable, '-m', 'streamlit', 'run', 'dashboard_streamlit.py'], 
                               cwd=os.getcwd())
                time.sleep(5)  # Streamlit tarda más en iniciar
                webbrowser.open('http://localhost:8502')
            except Exception as e:
                print(f"❌ Error ejecutando dashboard Streamlit: {e}")
        
        thread = threading.Thread(target=ejecutar)
        thread.daemon = True
        thread.start()
    
    def ejecutar(self):
        """Ejecutar la aplicación"""
        print("🎯 INICIANDO VISTA FÁCIL")
        print("=" * 50)
        print(f"🌐 Abriendo en: http://localhost:{self.puerto}")
        print("🎨 Interfaz simplificada del Sistema de Análisis de Ventas")
        print("💡 Presiona Ctrl+C para detener")
        print("=" * 50)
        
        # Abrir navegador automáticamente
        def abrir_navegador():
            time.sleep(2)
            webbrowser.open(f'http://localhost:{self.puerto}')
        
        thread = threading.Thread(target=abrir_navegador)
        thread.daemon = True
        thread.start()
        
        try:
            self.app.run(
                debug=False, 
                host='0.0.0.0', 
                port=self.puerto
            )
        except KeyboardInterrupt:
            print("\n✅ Vista Fácil detenida")

def main():
    """Función principal"""
    if __name__ == "__main__":
        vista = VistaFacil()
        vista.ejecutar()

if __name__ == "__main__":
    main()