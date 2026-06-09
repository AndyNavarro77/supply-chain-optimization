# 📦 Optimización de Supply Chain — DataCo Global

> **Sistema de análisis de supply chain end-to-end construido sobre 180K+ órdenes reales en 5 mercados globales — combinando Predicción de Riesgo de Entrega, Análisis de Rentabilidad y Forecasting de Demanda para identificar $13.7M en oportunidades de optimización.**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-red)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-blue?logo=tableau)
![Status](https://img.shields.io/badge/Estado-Completo-brightgreen)

---

## 🧠 El Problema de Negocio

Una empresa de retail global que opera en 5 mercados — Europa, LATAM, Pacific Asia, USCA y África — con $36.8M en revenue anual y 10.8% de margen general enfrenta tres desafíos críticos de supply chain:

- **El 54.8% de las órdenes llegan tarde** — más de 98.000 entregas por año no cumplen la fecha programada, sin ningún mecanismo predictivo para detectar envíos en riesgo antes de que salgan del depósito
- **El 18.7% de las órdenes generan pérdidas** — casi 1 de cada 5 órdenes destruye margen, con $3.9M en pérdidas totales en el período analizado
- **Sin visibilidad de demanda** — las decisiones de inventario son reactivas, creando un riesgo de stockout estimado en $51.610/mes en las categorías principales

> *Con un margen del 10.8%, cada punto porcentual de ineficiencia operativa tiene un impacto desproporcionado en la rentabilidad.*

---

## ✅ La Solución

Un sistema analítico de tres componentes que transforma datos transaccionales brutos en inteligencia operativa accionable:

- **Predicción de Riesgo de Entrega** — modelo Random Forest que detecta envíos en riesgo antes de su salida, habilitando intervención proactiva
- **Análisis de Rentabilidad y Pérdidas** — inteligencia de margen por categoría con clasificación estratégica y recomendaciones de optimización
- **Forecasting de Demanda y Optimización de Inventario** — forecasting de series de tiempo con Prophet, safety stock y reorder point por categoría

---

## 📐 Arquitectura

```
┌─────────────────────────┐    ┌────────────────────────┐    ┌─────────────────────┐
│   Dataset DataCo        │───▶│   Pipeline Python      │───▶│     MySQL DB        │
│   180K+ órdenes         │    │   EDA · ML · Forecast  │    │   12 tablas         │
│   5 mercados globales   │    │   RF · XGBoost         │    │   resultados        │
│   53 variables          │    │   Prophet · Stats      │    │   métricas          │
└─────────────────────────┘    └────────────────────────┘    └──────────┬──────────┘
                                                                         │
                                              ┌──────────────────────────▼──────────────────────┐
                                              │            Dashboard Tableau                     │
                                              │   KPIs · Entregas · Rentabilidad · Forecast      │
                                              └─────────────────────────────────────────────────┘
```

---

## 📊 Dashboard Interactivo

> Construido en Tableau Public — KPIs, análisis de entregas tardías, rentabilidad por categoría y mercado, y forecast de demanda en una vista ejecutiva unificada.

![Dashboard](img/dashboard_supply_chain.png)

**[→ Ver en Tableau Public](https://public.tableau.com/app/profile/andres.navarro77)**

---

## 🔄 Pipeline — Paso a Paso

| Paso | Acción | Tecnología | Valor de Negocio |
|---|---|---|---|
| 1 | Carga, limpieza y feature engineering de 180K órdenes | Python · pandas | Vista operativa unificada |
| 2 | EDA: patrones de entrega tardía, performance por mercado, shipping modes | Python · seaborn | Identificar el problema del 54.8% de tardías |
| 3 | Análisis de rentabilidad por categoría, mercado y nivel de descuento | Python · pandas | Localizar $3.9M en pérdidas |
| 4 | Predicción de riesgo de entrega — LR · RF · XGBoost | scikit-learn · XGBoost | AUC-ROC 0.743 · $9.2M net benefit |
| 5 | Optimización de threshold — maximizar recall | scikit-learn | 69.6% recall · 69% precisión |
| 6 | Matriz de rentabilidad por categoría — clasificación estratégica | Python · pandas | Segmentación Star · Solid · Underperformer |
| 7 | Forecasting de demanda — Prophet (10 categorías, 6 meses) | Prophet | MAPE 3.2% · señales de inventario accionables |
| 8 | Safety stock y reorder point por categoría | Python · numpy | $51.610/mes de riesgo de stockout cuantificado |
| 9 | ETL a MySQL — 12 tablas de producción | MySQL · SQLAlchemy | Modelo de datos estructurado para capa BI |

---

## 📊 Resultados Clave

| Métrica | Valor |
|---|---|
| Órdenes analizadas | 180.511 |
| Mercados cubiertos | 5 (Europa · LATAM · Pacific Asia · USCA · África) |
| Tasa de entrega tardía | **54.8%** |
| AUC-ROC del modelo de riesgo | **0.743** |
| Recall (tardías detectadas) | **69.6%** |
| Tasa de órdenes con pérdida | **18.7%** |
| MAPE del forecast | **3.2%** (benchmark <10%) |
| **Valor total identificado** | **$13.723.427** |

---

## 🤖 Modelo de Predicción de Riesgo

| Modelo | AUC-ROC | Notas |
|---|---|---|
| Logistic Regression | 0.727 | Baseline |
| XGBoost | 0.740 | Alto rendimiento |
| **Random Forest** | **0.743** | **Seleccionado — mejor AUC** |

**Hallazgo clave:** `Days for shipment (scheduled)` y `Shipping Mode` representan ~85% de la importancia de features — el problema de entregas tardías es sistémico, no específico de categoría o mercado. First Class tiene 95.3% de tasa de entrega tardía a pesar de ser el servicio premium.

**Optimización de threshold:** threshold por defecto 0.5 → optimizado a 0.40, mejorando el recall de 57% a 69.6% con reducción aceptable de precisión (82% → 69%).

---

## 💡 Impacto de Negocio

| Oportunidad | Impacto |
|---|---|
| Modelo de riesgo de entrega — net benefit | **$9.220.624 / año** |
| Recuperación de órdenes con pérdida | **$3.883.483** |
| Riesgo de stockout evitado | **$619.320 / año** |
| **Valor total identificado** | **$13.723.427** |

*Supuestos del modelo: $25 costo por entrega tardía no detectada · $15 ahorro por entrega flaggeada · $3 costo por falsa alerta*

---

## 🔍 Hallazgos Clave

| Hallazgo | Implicancia de Negocio |
|---|---|
| First Class shipping: 95.3% de tardías | El servicio premium falla casi siempre — desalineación precio/SLA |
| Late delivery uniforme en todos los mercados y categorías | Problema sistémico de scheduling, no logístico |
| Delay promedio: 0.57 días | Los días programados están mal calibrados — corrección pequeña, impacto grande |
| 18.7% de órdenes con pérdida en todos los estados | Problema estructural de margen, no operativo |
| El descuento no correlaciona con pérdidas de margen | Las pérdidas las genera el mix de productos y costos logísticos |
| Fishing: MAPE 2.0%, tendencia creciente | Mayor confianza de forecast — aumentar inventario |
| Electronics: MAPE más alto (4.6%), tendencia decreciente | Reducir stock, monitorear de cerca |
| $51.610/mes de riesgo de stockout en top 10 categorías | La optimización de inventario reduce directamente la pérdida de revenue |

---

## 📊 Visualizaciones

**Overview del Negocio**
![EDA Overview](img/eda_overview.png)

**Análisis de Entregas Tardías**
![Late Delivery](img/late_delivery_analysis.png)

**Análisis de Rentabilidad**
![Profitability](img/profitability_analysis.png)

**Matriz de Rentabilidad por Categoría**
![Category Matrix](img/category_matrix.png)

**Modelo de Riesgo — Evaluación**
![Model Evaluation](img/model_evaluation.png)

**Optimización de Threshold**
![Threshold](img/threshold_optimization.png)

**Riesgo de Entrega — Impacto de Negocio**
![Business Impact](img/business_impact_model.png)

**Impacto de Descuentos**
![Discount Impact](img/discount_impact.png)

**Análisis de Órdenes con Pérdida**
![Loss Analysis](img/loss_analysis.png)

**Forecast de Demanda — 10 Categorías**
![Demand Forecast](img/demand_forecast.png)

**Optimización de Inventario**
![Inventory](img/inventory_optimization.png)

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología | Propósito |
|---|---|---|
| Ingeniería de Datos | Python · pandas · numpy | ETL, feature engineering, limpieza |
| Machine Learning | scikit-learn · XGBoost | Clasificación de riesgo de entrega |
| Series de Tiempo | Prophet | Forecasting de demanda |
| Análisis Estadístico | scipy · numpy | Cálculos de optimización de inventario |
| Base de Datos | MySQL · SQLAlchemy | Modelo de datos de producción (12 tablas) |
| Visualización | matplotlib · seaborn | Gráficos de análisis · evaluación del modelo |
| Dashboard | Tableau Public | Dashboard ejecutivo interactivo |

---

## 📁 Estructura del Repositorio

```
supply-chain-optimization/
│
├── notebooks/
│   ├── 01_eda_and_business_intelligence.ipynb   # EDA · mercado · entregas tardías · rentabilidad
│   ├── 02_delivery_risk_prediction.ipynb         # RF · XGBoost · optimización de threshold
│   ├── 03_profitability_analysis.ipynb           # Margen · pérdidas · matriz de categorías
│   └── 04_demand_forecasting.ipynb               # Prophet · safety stock · reorder point
├── dashboard/
│   └── supply_chain_dashboard.twb                # Workbook Tableau
├── scripts/
│   └── load_to_mysql.py                          # ETL: resultados → MySQL (12 tablas)
├── data/
│   └── processed/                                # Artefactos del pipeline (no trackeados)
├── img/                                          # Exportaciones de visualizaciones (11 gráficos + dashboard)
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

**DataCo Smart Supply Chain for Big Data Analysis** — disponible en [Kaggle](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis).

Datos reales de supply chain con 180K+ órdenes, 53 variables cubriendo órdenes, productos, clientes, envíos y finanzas en 5 mercados globales (2015–2018).

---

## 🔗 Proyectos Relacionados

- [fraud-detection](https://github.com/AndyNavarro77/fraud-detection) — Detección de fraude con XGBoost · 97% recall · $55K net benefit
- [customer-analytics](https://github.com/AndyNavarro77/customer-analytics) — RFM · CLV · Análisis de Cohortes · $1.1M en oportunidades
- [next-best-offer](https://github.com/AndyNavarro77/next-best-offer) — Motor de recomendación híbrido · 88% Precision@3 · $1.6M revenue uplift

---

## 👤 Autor

**Andrés Navarro** — Analista de Datos · BI · Machine Learning

[![GitHub](https://img.shields.io/badge/GitHub-AndyNavarro77-black?logo=github)](https://github.com/AndyNavarro77)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue?logo=linkedin)](https://www.linkedin.com/in/andrés-navarro77/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visitar-orange?logo=netlify)](https://andres-navarro-portfolio.netlify.app)

---

*Construido para demostrar análisis de supply chain end-to-end — desde datos transaccionales brutos hasta un sistema de optimización production-ready con $13.7M en valor de negocio cuantificado. Alineado con proyectos reales de consultoría en Supply Chain & Operations.*
