import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import os
from datetime import datetime
import numpy as np

class DashboardVentas:
    def __init__(self, archivo_datos='Reporte_Consolidado.xlsx'):
        self.archivo_datos = archivo_datos
        self.df = None
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.cargar_datos()
        self.configurar_layout()
        self.configurar_callbacks()
    
    def cargar_datos(self):
        """Cargar y procesar los datos del archivo Excel"""
        try:
            if os.path.exists(self.archivo_datos):
                self.df = pd.read_excel(self.archivo_datos)
                print(f"✅ Datos cargados: {len(self.df)} registros")
                
                # Procesar fechas si existen
                if 'FECHA' in self.df.columns:
                    self.df['FECHA'] = pd.to_datetime(self.df['FECHA'], errors='coerce')
                
                # Asegurar que las columnas numéricas estén en formato correcto
                columnas_numericas = ['CANTIDAD', 'PRECIO_UNITARIO', 'TOTAL_VENTA']
                for col in columnas_numericas:
                    if col in self.df.columns:
                        self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
            else:
                print(f"❌ No se encontró el archivo {self.archivo_datos}")
                # Crear datos de ejemplo si no existe el archivo
                self.crear_datos_ejemplo()
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            self.crear_datos_ejemplo()
    
    def crear_datos_ejemplo(self):
        """Crear datos de ejemplo para demostración"""
        datos_ejemplo = {
            'PRODUCTO': ['Smartphone Samsung', 'Laptop Dell', 'Auriculares Sony', 'Tablet iPad', 'Monitor LG'] * 10,
            'CANTIDAD': np.random.randint(1, 20, 50),
            'PRECIO_UNITARIO': np.random.uniform(100, 2000, 50),
            'FECHA': pd.date_range('2025-01-01', periods=50, freq='D'),
            'CATEGORIA': np.random.choice(['Electrónicos', 'Computadoras', 'Accesorios'], 50),
            'VENDEDOR': np.random.choice(['María González', 'Carlos Rodríguez', 'Ana Martínez', 'Luis García'], 50)
        }
        self.df = pd.DataFrame(datos_ejemplo)
        self.df['TOTAL_VENTA'] = self.df['CANTIDAD'] * self.df['PRECIO_UNITARIO']
        print("📊 Usando datos de ejemplo para demostración")
    
    def configurar_layout(self):
        """Configurar el diseño del dashboard"""
        self.app.layout = dbc.Container([
            # Header
            dbc.Row([
                dbc.Col([
                    html.H1("📊 Dashboard de Ventas", className="text-center mb-4", 
                           style={'color': '#2c3e50', 'font-weight': 'bold'}),
                    html.Hr()
                ])
            ]),
            
            # Métricas principales
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("💰 Ventas Totales", className="card-title"),
                            html.H2(id="total-ventas", className="text-primary")
                        ])
                    ], color="light")
                ], width=3),
                
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("📦 Productos Vendidos", className="card-title"),
                            html.H2(id="total-productos", className="text-success")
                        ])
                    ], color="light")
                ], width=3),
                
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("🛍️ Ventas Promedio", className="card-title"),
                            html.H2(id="venta-promedio", className="text-info")
                        ])
                    ], color="light")
                ], width=3),
                
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("📈 Mejor Vendedor", className="card-title"),
                            html.H2(id="mejor-vendedor", className="text-warning")
                        ])
                    ], color="light")
                ], width=3)
            ], className="mb-4"),
            
            # Filtros
            dbc.Row([
                dbc.Col([
                    html.Label("Filtrar por Categoría:", style={'font-weight': 'bold'}),
                    dcc.Dropdown(
                        id='filtro-categoria',
                        options=[{'label': 'Todas', 'value': 'todas'}],
                        value='todas',
                        className="mb-3"
                    )
                ], width=4),
                
                dbc.Col([
                    html.Label("Filtrar por Vendedor:", style={'font-weight': 'bold'}),
                    dcc.Dropdown(
                        id='filtro-vendedor',
                        options=[{'label': 'Todos', 'value': 'todos'}],
                        value='todos',
                        className="mb-3"
                    )
                ], width=4),
                
                dbc.Col([
                    html.Label("Período:", style={'font-weight': 'bold'}),
                    dcc.DatePickerRange(
                        id='filtro-fecha',
                        start_date=None,
                        end_date=None,
                        display_format='DD/MM/YYYY',
                        className="mb-3"
                    )
                ], width=4)
            ]),
            
            # Gráficos principales
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="grafico-ventas-tiempo")
                ], width=8),
                
                dbc.Col([
                    dcc.Graph(id="grafico-top-productos")
                ], width=4)
            ], className="mb-4"),
            
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="grafico-ventas-categoria")
                ], width=6),
                
                dbc.Col([
                    dcc.Graph(id="grafico-vendedores")
                ], width=6)
            ], className="mb-4"),
            
            # Tabla de datos
            dbc.Row([
                dbc.Col([
                    html.H3("📋 Datos Detallados", style={'color': '#2c3e50'}),
                    dash_table.DataTable(
                        id='tabla-datos',
                        columns=[],
                        data=[],
                        sort_action="native",
                        filter_action="native",
                        page_action="native",
                        page_current=0,
                        page_size=10,
                        style_cell={'textAlign': 'left', 'padding': '10px'},
                        style_header={'backgroundColor': '#3498db', 'color': 'white', 'fontWeight': 'bold'},
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'odd'},
                                'backgroundColor': '#f8f9fa'
                            }
                        ]
                    )
                ])
            ])
        ], fluid=True)
    
    def configurar_callbacks(self):
        """Configurar los callbacks para interactividad"""
        
        @self.app.callback(
            [Output('filtro-categoria', 'options'),
             Output('filtro-vendedor', 'options'),
             Output('filtro-fecha', 'start_date'),
             Output('filtro-fecha', 'end_date')],
            [Input('filtro-categoria', 'id')]
        )
        def actualizar_filtros(_):
            if self.df is None or self.df.empty:
                return [], [], None, None
            
            # Opciones de categoría
            categorias = [{'label': 'Todas', 'value': 'todas'}]
            if 'CATEGORIA' in self.df.columns:
                categorias.extend([{'label': cat, 'value': cat} 
                                 for cat in self.df['CATEGORIA'].unique() if pd.notna(cat)])
            
            # Opciones de vendedor
            vendedores = [{'label': 'Todos', 'value': 'todos'}]
            if 'VENDEDOR' in self.df.columns:
                vendedores.extend([{'label': vend, 'value': vend} 
                                 for vend in self.df['VENDEDOR'].unique() if pd.notna(vend)])
            
            # Fechas
            start_date = self.df['FECHA'].min() if 'FECHA' in self.df.columns else None
            end_date = self.df['FECHA'].max() if 'FECHA' in self.df.columns else None
            
            return categorias, vendedores, start_date, end_date
        
        @self.app.callback(
            [Output('total-ventas', 'children'),
             Output('total-productos', 'children'),
             Output('venta-promedio', 'children'),
             Output('mejor-vendedor', 'children'),
             Output('grafico-ventas-tiempo', 'figure'),
             Output('grafico-top-productos', 'figure'),
             Output('grafico-ventas-categoria', 'figure'),
             Output('grafico-vendedores', 'figure'),
             Output('tabla-datos', 'columns'),
             Output('tabla-datos', 'data')],
            [Input('filtro-categoria', 'value'),
             Input('filtro-vendedor', 'value'),
             Input('filtro-fecha', 'start_date'),
             Input('filtro-fecha', 'end_date')]
        )
        def actualizar_dashboard(categoria, vendedor, fecha_inicio, fecha_fin):
            if self.df is None or self.df.empty:
                return "0", "0", "0", "N/A", {}, {}, {}, {}, [], []
            
            # Filtrar datos
            df_filtrado = self.df.copy()
            
            if categoria != 'todas' and 'CATEGORIA' in df_filtrado.columns:
                df_filtrado = df_filtrado[df_filtrado['CATEGORIA'] == categoria]
            
            if vendedor != 'todos' and 'VENDEDOR' in df_filtrado.columns:
                df_filtrado = df_filtrado[df_filtrado['VENDEDOR'] == vendedor]
            
            if fecha_inicio and fecha_fin and 'FECHA' in df_filtrado.columns:
                df_filtrado = df_filtrado[
                    (df_filtrado['FECHA'] >= fecha_inicio) & 
                    (df_filtrado['FECHA'] <= fecha_fin)
                ]
            
            # Calcular métricas
            total_ventas = f"${df_filtrado['TOTAL_VENTA'].sum():,.0f}" if 'TOTAL_VENTA' in df_filtrado.columns else "0"
            total_productos = f"{df_filtrado['CANTIDAD'].sum():,}" if 'CANTIDAD' in df_filtrado.columns else "0"
            venta_promedio = f"${df_filtrado['TOTAL_VENTA'].mean():,.0f}" if 'TOTAL_VENTA' in df_filtrado.columns else "0"
            
            mejor_vendedor = "N/A"
            if 'VENDEDOR' in df_filtrado.columns and 'TOTAL_VENTA' in df_filtrado.columns:
                ventas_por_vendedor = df_filtrado.groupby('VENDEDOR')['TOTAL_VENTA'].sum()
                if not ventas_por_vendedor.empty:
                    mejor_vendedor = ventas_por_vendedor.idxmax()
            
            # Crear gráficos
            graficos = self.crear_graficos(df_filtrado)
            
            # Preparar tabla
            columnas = [{"name": col, "id": col} for col in df_filtrado.columns]
            datos = df_filtrado.round(2).to_dict('records')
            
            return (total_ventas, total_productos, venta_promedio, mejor_vendedor,
                   *graficos, columnas, datos)
    
    def crear_graficos(self, df):
        """Crear todos los gráficos del dashboard"""
        
        # Gráfico de ventas en el tiempo
        if 'FECHA' in df.columns and 'TOTAL_VENTA' in df.columns:
            ventas_tiempo = df.groupby('FECHA')['TOTAL_VENTA'].sum().reset_index()
            fig_tiempo = px.line(ventas_tiempo, x='FECHA', y='TOTAL_VENTA',
                               title='📈 Evolución de Ventas en el Tiempo',
                               labels={'TOTAL_VENTA': 'Ventas ($)', 'FECHA': 'Fecha'})
            fig_tiempo.update_layout(title_x=0.5)
        else:
            fig_tiempo = {}
        
        # Top productos
        if 'PRODUCTO' in df.columns and 'TOTAL_VENTA' in df.columns:
            top_productos = df.groupby('PRODUCTO')['TOTAL_VENTA'].sum().nlargest(10).reset_index()
            fig_productos = px.bar(top_productos, x='TOTAL_VENTA', y='PRODUCTO',
                                 orientation='h', title='🏆 Top 10 Productos',
                                 labels={'TOTAL_VENTA': 'Ventas ($)', 'PRODUCTO': 'Producto'})
            fig_productos.update_layout(title_x=0.5, height=400)
        else:
            fig_productos = {}
        
        # Ventas por categoría
        if 'CATEGORIA' in df.columns and 'TOTAL_VENTA' in df.columns:
            ventas_categoria = df.groupby('CATEGORIA')['TOTAL_VENTA'].sum().reset_index()
            fig_categoria = px.pie(ventas_categoria, values='TOTAL_VENTA', names='CATEGORIA',
                                 title='🎯 Ventas por Categoría')
            fig_categoria.update_layout(title_x=0.5)
        else:
            fig_categoria = {}
        
        # Ventas por vendedor
        if 'VENDEDOR' in df.columns and 'TOTAL_VENTA' in df.columns:
            ventas_vendedor = df.groupby('VENDEDOR')['TOTAL_VENTA'].sum().reset_index()
            fig_vendedor = px.bar(ventas_vendedor, x='VENDEDOR', y='TOTAL_VENTA',
                                title='👥 Ventas por Vendedor',
                                labels={'TOTAL_VENTA': 'Ventas ($)', 'VENDEDOR': 'Vendedor'})
            fig_vendedor.update_layout(title_x=0.5)
        else:
            fig_vendedor = {}
        
        return fig_tiempo, fig_productos, fig_categoria, fig_vendedor
    
    def ejecutar(self, debug=True, port=8050):
        """Ejecutar el dashboard"""
        print(f"🚀 Iniciando dashboard en http://localhost:{port}")
        self.app.run(debug=debug, port=port, host='127.0.0.1')

# Función principal
def main():
    dashboard = DashboardVentas()
    dashboard.ejecutar()

if __name__ == "__main__":
    main()
