# 📊 Dashboard Ejecutivo - Panel de Control de Ventas y Conversión

Una aplicación interactiva construida con **Streamlit**, **Pandas** y **Plotly** para el análisis de ventas, tasas de conversión, comportamiento de usuarios por dispositivo y uso de cupones de descuento.

---

## 🚀 Características Principales

- **Filtros Dinámicos en Barra Lateral**:
  - **Período**: Filtra transacciones por *Últimos 30 días*, *Últimos 3 meses* o *Último año*.
  - **Uso de Cupones**: Clasifica usuarios en *Frecuente*, *Ocasional* o *Nunca*.
  - **Dispositivo**: Analiza el comportamiento desde *Teléfono*, *Laptop* o *Tablet*.
  - **Monto del Carrito**: Filtra por compras *Menores a 100* o *Mayores/iguales a 100*.

- **Métricas Clave (KPIs)**:
  - **Ventas Totales ($)**: Suma acumulada de carritos completados.
  - **Total Transacciones**: Cantidad total de registros bajo los filtros activos.
  - **Completadas (%)**: Porcentaje y recuento de compras exitosas.
  - **Canceladas (%)**: Porcentaje y recuento de transacciones no finalizadas.

- **Visualizaciones Interactivas (Plotly Dark Theme)**:
  - **Estado de Compra por Dispositivo**: Histograma agrupado por tipo de dispositivo y estado de compra (Completada vs. Cancelada).
  - **Tendencia de Ventas por Período**: Gráfico de líneas que muestra la evolución del monto acumulado de ventas.
  - **Distribución del Monto del Carrito**: Histograma de frecuencias para identificar los rangos de valor de compra más habituales.

- **Explorador de Datos**:
  - Tabla interactiva con opción expandible para inspeccionar los registros filtrados en tiempo real.

---

## 🛠️ Tecnologías Utilizadas

- **[Python 3.8+](https://www.python.org/)**
- **[Streamlit](https://streamlit.io/)**: Framework para la creación de la interfaz web.
- **[Pandas](https://pandas.pydata.org/)**: Procesamiento y manipulación de datos.
- **[NumPy](https://numpy.org/)**: Generación de datos simulados/sintéticos.
- **[Plotly Express](https://plotly.com/python/plotly-express/)**: Gráficos interactivos de alta calidad.

---

## 📋 Requisitos Previos

Asegúrate de tener instalado Python en tu sistema. Se recomienda crear un entorno virtual:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Activar entorno virtual (macOS / Linux)
source venv/bin/activate
```

---

## 📦 Instalación

1. **Clona o descarga este repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_DIRECTORIO>
   ```

2. **Instala las dependencias necesarias**:
   ```bash
   pip install streamlit pandas numpy plotly
   ```

   *(Opcional) Si cuentas con un archivo `requirements.txt`:*
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Ejecución de la Aplicación

Para iniciar el dashboard en tu navegador local, ejecuta el siguiente comando:

```bash
streamlit run app.py
```

*(Reemplaza `app.py` por el nombre de tu archivo principal si es diferente).*

La aplicación se abrirá automáticamente en tu navegador predeterminado en `http://localhost:8501`.

---

## 📁 Estructura del Proyecto

```text
.
├── main.py              # Código principal de la aplicación Streamlit
└── README.md           # Documentación del proyecto
```

---

## 📄 Licencia

Este proyecto está disponible bajo la licencia [MIT](LICENSE).