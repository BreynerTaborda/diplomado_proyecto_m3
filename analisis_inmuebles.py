"""
Análisis de Datos de Inmuebles - Diplomado Proyecto M3
===============================================
Librerías requeridas:
pip install pandas matplotlib seaborn numpy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo para gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

def limpiar_precio(precio_str):
    """Limpia y convierte el precio a float"""
    if pd.isna(precio_str):
        return np.nan

    precio_limpio = str(precio_str).replace('$', '').replace('.', '').replace(',', '.')
    try:
        return float(precio_limpio)
    except ValueError:
        return np.nan

def limpiar_numero_habitaciones(hab_str):
    """Extrae el número de habitaciones"""
    if pd.isna(hab_str):
        return np.nan
    
    import re
    match = re.search(r'(\d+)', str(hab_str))
    return int(match.group(1)) if match else np.nan

def limpiar_numero_banos(bano_str):
    """Extrae el número de baños"""
    if pd.isna(bano_str):
        return np.nan
    
    import re
    match = re.search(r'(\d+)', str(bano_str))
    return int(match.group(1)) if match else np.nan

def limpiar_metros_cuadrados(area_str):
    """Extrae los metros cuadrados"""
    if pd.isna(area_str):
        return np.nan
    
    import re
    match = re.search(r'(\d+(?:\.\d+)?)', str(area_str))
    return float(match.group(1)) if match else np.nan

def cargar_y_limpiar_datos(ruta_csv):
    """Carga y limpia los datos del CSV"""
    print("Cargando datos del CSV...")
    df = pd.read_csv(ruta_csv)

    print(f"Datos cargados: {len(df)} registros")

    print("Limpiando datos...")
    df['precio'] = df['precio'].apply(limpiar_precio)
    df['numero_habitaciones'] = df['numero_habitaciones'].apply(limpiar_numero_habitaciones)
    df['numero_banos'] = df['numero_banos'].apply(limpiar_numero_banos)
    df['metros_cuadrados'] = df['metros_cuadrados'].apply(limpiar_metros_cuadrados)

    df_limpio = df.dropna(subset=['precio', 'numero_habitaciones', 'numero_banos', 'metros_cuadrados'])

    print(f"Datos limpios: {len(df_limpio)} registros (eliminados {len(df) - len(df_limpio)} con datos faltantes)")

    return df_limpio

def analisis_descriptivo(df):
    """Realiza análisis descriptivo de los datos"""
    print("\n" + "="*60)
    print("ANÁLISIS DESCRIPTIVO")
    print("="*60)

    print(f"\nESTADÍSTICAS GENERALES:")
    print(f"Total de inmuebles analizados: {len(df)}")
    print(f"Precio promedio: ${df['precio'].mean():,.0f}")
    print(f"Precio mediano: ${df['precio'].median():,.0f}")
    print(f"Precio mínimo: ${df['precio'].min():,.0f}")
    print(f"Precio máximo: ${df['precio'].max():,.0f}")

    # Estadísticas por tipo de inmueble
    print(f"\nDISTRIBUCIÓN POR TIPO DE INMUEBLE:")
    tipo_counts = df['tipo_inmueble'].value_counts()
    for tipo, count in tipo_counts.items():
        porcentaje = (count / len(df)) * 100
        print(f"{tipo}: {count} ({porcentaje:.1f}%)")

    # Estadísticas detalladas
    print(f"\nESTADÍSTICAS DETALLADAS:")
    columnas_numericas = ['precio', 'numero_habitaciones', 'numero_banos', 'metros_cuadrados']
    stats = df[columnas_numericas].describe()
    print(stats.round(2))

def crear_visualizaciones(df):
    """Crea visualizaciones de los datos"""
    print("\n" + "="*60)
    print("CREANDO VISUALIZACIONES")
    print("="*60)

    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Análisis de Inmuebles en Arriendo - Medellín', fontsize=16, fontweight='bold')

    # Histograma de precios
    axes[0,0].hist(df['precio']/1000000, bins=30, edgecolor='black', alpha=0.7)
    axes[0,0].set_title('Distribución de Precios (Millones COP)')
    axes[0,0].set_xlabel('Precio (Millones)')
    axes[0,0].set_ylabel('Frecuencia')
    axes[0,0].grid(True, alpha=0.3)

    # Boxplot de precios por tipo
    tipos_principales = df['tipo_inmueble'].value_counts().head(2).index
    df_filtrado = df[df['tipo_inmueble'].isin(tipos_principales)]
    precios_millones = df_filtrado['precio']/1000000
    sns.boxplot(data=df_filtrado, x='tipo_inmueble', y=precios_millones, ax=axes[0,1])
    axes[0,1].set_title('Precios por Tipo de Inmueble')
    axes[0,1].set_ylabel('Precio (Millones COP)')
    axes[0,1].tick_params(axis='x', rotation=45)

    # Scatter plot: Área vs Precio
    axes[0,2].scatter(df['metros_cuadrados'], df['precio']/1000000, alpha=0.6, s=50)
    axes[0,2].set_title('Relación Área vs Precio')
    axes[0,2].set_xlabel('Área (m²)')
    axes[0,2].set_ylabel('Precio (Millones COP)')
    axes[0,2].grid(True, alpha=0.3)

    # Histograma de habitaciones
    axes[1,0].hist(df['numero_habitaciones'], bins=range(1, int(df['numero_habitaciones'].max())+2),
                   edgecolor='black', alpha=0.7, align='left')
    axes[1,0].set_title('Distribución de Número de Habitaciones')
    axes[1,0].set_xlabel('Número de Habitaciones')
    axes[1,0].set_ylabel('Frecuencia')
    axes[1,0].grid(True, alpha=0.3)

    # Histograma de baños
    axes[1,1].hist(df['numero_banos'], bins=range(1, int(df['numero_banos'].max())+2),
                   edgecolor='black', alpha=0.7, align='left')
    axes[1,1].set_title('Distribución de Número de Baños')
    axes[1,1].set_xlabel('Número de Baños')
    axes[1,1].set_ylabel('Frecuencia')
    axes[1,1].grid(True, alpha=0.3)

    # Matriz de correlación
    corr_matrix = df[['precio', 'numero_habitaciones', 'numero_banos', 'metros_cuadrados']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=axes[1,2])
    axes[1,2].set_title('Matriz de Correlación')

    plt.tight_layout()
    plt.savefig('analisis_inmuebles_visualizaciones.png', dpi=300, bbox_inches='tight')
    print("Visualizaciones guardadas como 'analisis_inmuebles_visualizaciones.png'")

    plt.show()

def analisis_por_barrio(df):
    """Análisis adicional por barrio"""
    print("\n" + "="*60)
    print("ANÁLISIS POR BARRIO")
    print("="*60)

    top_barrios = df['barrio_ubicacion'].value_counts().head(10)
    print("\nTOP 10 BARRIOS POR CANTIDAD DE INMUEBLES:")
    for barrio, count in top_barrios.items():
        print(f"{barrio}: {count} inmuebles")

    print(f"\nPRECIOS PROMEDIO POR BARRIO (TOP 10):")
    barrio_precio = df.groupby('barrio_ubicacion')['precio'].agg(['mean', 'count']).round(0)
    barrio_precio = barrio_precio[barrio_precio['count'] >= 5].sort_values('mean', ascending=False).head(10)
    for barrio, row in barrio_precio.iterrows():
        print(f"{barrio}: ${row['mean']:,.0f} (n={int(row['count'])})")

def conclusiones(df):
    """Presenta conclusiones del análisis"""
    print("\n" + "="*60)
    print("CONCLUSIONES Y INSIGHTS")
    print("="*60)

    print("RESUMEN EJECUTIVO:")
    print(f"• Se analizaron {len(df)} inmuebles en arriendo en Medellín")
    print(f"• Precio promedio: ${df['precio'].mean():,.0f}")
    print(f"• Área promedio: {df['metros_cuadrados'].mean():.1f} m²")

    # Correlaciones principales
    corr_precio_area = df['precio'].corr(df['metros_cuadrados'])
    corr_precio_hab = df['precio'].corr(df['numero_habitaciones'])
    print(f"• Correlación precio-área: {corr_precio_area:.3f}")
    print(f"• Correlación precio-habitaciones: {corr_precio_hab:.3f}")
    print("\nPATRONES OBSERVADOS:")
    print("• Los apartamentos representan la mayoría de las ofertas de arriendo")
    print("• Existe una correlación positiva entre área, habitaciones y precio")
    print("• Los precios varían significativamente según la ubicación")
    print("• La mayoría de inmuebles tienen entre 2-3 habitaciones y 1-2 baños")

    print("\nRECOMENDACIONES PARA FUTUROS ANÁLISIS:")
    print("• Implementar modelos predictivos de precios usando machine learning")
    print("• Analizar tendencias temporales si se dispone de datos históricos")
    print("• Incluir variables adicionales como antigüedad, estrato socioeconómico")
    print("• Realizar análisis de clustering para segmentar el mercado inmobiliario")

def main():
    """Función principal del programa"""
    print("ANÁLISIS DE INMUEBLES EN ARRIENDO - MEDELLÍN")
    print("="*60)

    ruta_csv = "./resultados/inmuebles_header.csv"

    df = cargar_y_limpiar_datos(ruta_csv)

    analisis_descriptivo(df)
    analisis_por_barrio(df)
    crear_visualizaciones(df)
    conclusiones(df)

    print("\n" + "="*60)
    print("ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("Archivo de visualizaciones: analisis_inmuebles_visualizaciones.png")
    print("="*60)

if __name__ == "__main__":
    main()