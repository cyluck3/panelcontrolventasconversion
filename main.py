import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

np.random.seed(42)

# 1. Carga de datos
@st.cache_data
def load_data():
    total_users = 189
    return pd.DataFrame({
        "user_id": np.arange(1000, 1000 + total_users),
        "dates": np.random.choice(["Último año", "Últimos 3 meses", "Últimos 30 días"], size=total_users),
        "device_type": np.random.choice(["Teléfono", "Laptop", "Tablet"], size=total_users),
        "car_amount": np.random.randint(10, 201, size=total_users),
        "completed_purchase": np.random.choice(["Sí", "No"], size=total_users),
        "coupon_usage": np.random.choice(["Frecuente", "Ocasional", "Nunca"], size=total_users)
    })

df_raw = load_data()

st.set_page_config(page_title="Dashboard Ejecutivo", layout="wide")
st.title("📊 Panel de Control de Ventas y Conversión")

# 2. Filtros Laterales
st.sidebar.header("Filtros")
period = st.sidebar.selectbox("Período:", ["Todo", "Últimos 30 días", "Últimos 3 meses", "Último año"])
coupon = st.sidebar.selectbox("Uso de Cupones:", ["Todo", "Frecuente", "Ocasional", "Nunca"])
device = st.sidebar.selectbox("Dispositivo:", ["Todo", "Teléfono", "Laptop", "Tablet"])
amount_range = st.sidebar.selectbox("Monto del Carrito:", ["Todo", "Menor a 100", "Mayor o igual a 100"])

# 3. Filtrado de datos
df_filtered = df_raw.copy()

if period != "Todo":
    df_filtered = df_filtered[df_filtered["dates"] == period]
if coupon != "Todo":
    df_filtered = df_filtered[df_filtered["coupon_usage"] == coupon]
if device != "Todo":
    df_filtered = df_filtered[df_filtered["device_type"] == device]
if amount_range == "Menor a 100":
    df_filtered = df_filtered[df_filtered["car_amount"] < 100]
elif amount_range == "Mayor o igual a 100":
    df_filtered = df_filtered[df_filtered["car_amount"] >= 100]

# 4. Métricas Clave (KPIs)
total_records = len(df_filtered)
completed = (df_filtered["completed_purchase"] == "Sí").sum()
canceled = (df_filtered["completed_purchase"] == "No").sum()

perc_completed = round((completed / total_records * 100), 1) if total_records > 0 else 0
perc_canceled = round((canceled / total_records * 100), 1) if total_records > 0 else 0
total_sales = df_filtered[df_filtered["completed_purchase"] == "Sí"]["car_amount"].sum()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Ventas Totales", f"${total_sales:,.2f}")
kpi2.metric("Total Transacciones", f"{total_records}")
kpi3.metric("Completadas", f"{completed}", f"{perc_completed}%")
kpi4.metric("Canceladas", f"{canceled}", f"-{perc_canceled}%")

st.markdown("---")

# 5. Gráficos
col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("Estado de Compra por Dispositivo")
    if total_records > 0:
        fig_bar = px.histogram(
            df_filtered, 
            x="device_type", 
            color="completed_purchase",
            barmode="group",
            color_discrete_map={"Sí": "#2ECC71", "No": "#E74C3C"},
            labels={"device_type": "Dispositivo", "completed_purchase": "Completada"},
            title="Comparativo de compras por tipo de dispositivo"
        )
        fig_bar.update_layout(template="plotly_dark", yaxis_title="Cantidad")
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("Sin datos disponibles para los filtros seleccionados.")

with col_g2:
    st.subheader("Tendencia de Ventas por Período")
    if total_records > 0:
        period_order = ["Último año",  "Últimos 3 meses", "Últimos 30 días"]
        sales_by_period = df_filtered[df_filtered["completed_purchase"] == "Sí"].groupby("dates")["car_amount"].sum().reset_index()
        sales_by_period['dates'] = pd.Categorical(sales_by_period['dates'], categories=period_order, ordered=True)
        sales_by_period = sales_by_period.sort_values('dates')

        fig_line = px.line(
            sales_by_period, 
            x="dates", 
            y="car_amount", 
            markers=True,
            title="Evolución del monto acumulado de ventas ($)"
        )
        fig_line.update_traces(line_color="#4A90E2", line_width=3, marker_size=8)
        fig_line.update_layout(template="plotly_dark", xaxis_title="Período", yaxis_title="Ventas ($)")
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.info("Sin datos disponibles para los filtros seleccionados.")

# Fila Inferior - Histograma
st.subheader("Distribución del Monto del Carrito")
if total_records > 0:
    fig_hist = px.histogram(
        df_filtered, 
        x="car_amount", 
        nbins=10,
        color_discrete_sequence=["#F39C12"],
        title="Frecuencia de montos en carritos de compra"
    )
    fig_hist.update_layout(template="plotly_dark", xaxis_title="Monto ($)", yaxis_title="Frecuencia")
    st.plotly_chart(fig_hist, use_container_width=True)
else:
    st.info("Sin datos disponibles para los filtros seleccionados.")

# Tabla interactiva
with st.expander("🔍 Ver Tabla de Datos"):
    st.dataframe(df_filtered, use_container_width=True)
