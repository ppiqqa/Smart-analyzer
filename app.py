import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Smart Facility Energy Analyzer",
    layout="wide"
)

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(
        135deg,
        #06131f,
        #0b1f35,
        #102b45
    );
}

/* Main Title */
.main-title{
    text-align:center;
    color:#00e5ff;
    font-size:48px;
    font-weight:bold;
    text-shadow:0px 0px 20px #00e5ff;
}

/* Subtitle */
.sub-title{
    text-align:center;
    color:white;
    font-size:20px;
}

/* Cards */
div[data-testid="metric-container"]{
    background:rgba(255,255,255,0.05);
    border:1px solid #00e5ff;
    border-radius:15px;
    padding:15px;
    box-shadow:0 0 15px rgba(0,229,255,0.4);
}

/* Text */
h1,h2,h3,h4,h5,h6,p,label,span{
    color:white !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background-color:#07111c;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='main-title'>
⚡ Smart Facility Energy Analyzer
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
Developed By Engineer Mohammed
</div>
""", unsafe_allow_html=True)




# =====================================
# FACILITY INFORMATION
# =====================================

st.sidebar.header("🏢 Facility Information")

facility_type = st.sidebar.selectbox(
    "Facility Type",
    [
        "School",
        "Hospital",
        "Factory",
        "Office",
        "Mall"
    ]
)

area = st.sidebar.number_input(
    "Area (m²)",
    min_value=100,
    value=1000
)

operating_hours = st.sidebar.slider(
    "Operating Hours / Day",
    1,
    24,
    8
)

tariff = st.sidebar.number_input(
    "Electricity Tariff (SAR/kWh)",
    min_value=0.01,
    value=0.18,
    step=0.01
)

# =====================================
# LOAD INPUTS
# =====================================

st.header("⚡ Load Configuration")

c1, c2 = st.columns(2)

with c1:

    st.subheader("❄ HVAC")

    ac_count = st.number_input(
        "Number of AC Units",
        min_value=0,
        value=10
    )

    ac_power = st.number_input(
        "AC Power (kW)",
        min_value=0.0,
        value=2.0
    )

    st.subheader("💡 Lighting")

    light_count = st.number_input(
        "Number of Lights",
        min_value=0,
        value=100
    )

    light_power = st.number_input(
        "Light Power (W)",
        min_value=0.0,
        value=20.0
    )

with c2:

    st.subheader("💻 Computers")

    pc_count = st.number_input(
        "Number of Computers",
        min_value=0,
        value=50
    )

    pc_power = st.number_input(
        "Computer Power (W)",
        min_value=0.0,
        value=300.0
    )

    st.subheader("⚙ Motors")

    motor_count = st.number_input(
        "Number of Motors",
        min_value=0,
        value=3
    )

    motor_power = st.number_input(
        "Motor Power (kW)",
        min_value=0.0,
        value=5.0
    )

# =====================================
# CALCULATIONS
# =====================================

hvac_kw = ac_count * ac_power

lighting_kw = (
    light_count * light_power
) / 1000

computers_kw = (
    pc_count * pc_power
) / 1000

motors_kw = (
    motor_count * motor_power
)

total_kw = (
    hvac_kw +
    lighting_kw +
    computers_kw +
    motors_kw
)

daily_energy = (
    total_kw *
    operating_hours
)

monthly_energy = (
    daily_energy *
    30
)

annual_energy = (
    daily_energy *
    365
)

monthly_cost = (
    monthly_energy *
    tariff
)

annual_cost = (
    annual_energy *
    tariff
)

# =====================================
# DASHBOARD
# =====================================

st.header("📊 Executive Dashboard")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Total Load",
        f"{total_kw:.1f} kW"
    )

with m2:
    st.metric(
        "Monthly Energy",
        f"{monthly_energy:.0f} kWh"
    )

with m3:
    st.metric(
        "Monthly Cost",
        f"{monthly_cost:.0f} SAR"
    )

m4, m5, m6 = st.columns(3)

with m4:
    st.metric(
        "Annual Energy",
        f"{annual_energy:.0f} kWh"
    )

with m5:
    st.metric(
        "Annual Cost",
        f"{annual_cost:.0f} SAR"
    )

with m6:
    st.metric(
        "Operating Hours",
        f"{operating_hours} h/day"
    )
    # =====================================
# 3D ELECTRICITY FLOW
# =====================================

st.header("⚡ 3D Electricity Flow")

fig = go.Figure()

# Main path
fig.add_trace(
    go.Scatter3d(
        x=[0,1,2,3,4,5,6],
        y=[0,0,0,0,0,0,0],
        z=[7,6,5,4,3,2,1],
        mode="markers+text+lines",
        text=[
            "⚡ Utility Grid",
            "🏭 Power Plant",
            "⚡ Transmission",
            "🔌 Substation",
            "🔄 Transformer",
            "🛡 Main Breaker",
            "🏢 Facility"
        ],
        textposition="top center",
        marker=dict(
            size=12,
            color=[
                "red",
                "orange",
                "yellow",
                "green",
                "cyan",
                "blue",
                "purple"
            ]
        ),
        line=dict(
            color="cyan",
            width=10
        )
    )
)

# HVAC branch
fig.add_trace(
    go.Scatter3d(
        x=[6,8],
        y=[0,2],
        z=[1,0],
        mode="markers+text+lines",
        text=["","❄ HVAC"],
        textposition="top center",
        marker=dict(size=10,color="deepskyblue"),
        line=dict(width=6,color="deepskyblue")
    )
)

# Lighting branch
fig.add_trace(
    go.Scatter3d(
        x=[6,8],
        y=[0,0],
        z=[1,-1],
        mode="markers+text+lines",
        text=["","💡 Lighting"],
        textposition="top center",
        marker=dict(size=10,color="gold"),
        line=dict(width=6,color="gold")
    )
)

# Motors branch
fig.add_trace(
    go.Scatter3d(
        x=[6,8],
        y=[0,-2],
        z=[1,0],
        mode="markers+text+lines",
        text=["","⚙ Motors"],
        textposition="top center",
        marker=dict(size=10,color="lime"),
        line=dict(width=6,color="lime")
    )
)

# Computers branch
fig.add_trace(
    go.Scatter3d(
        x=[6,9],
        y=[0,3],
        z=[1,2],
        mode="markers+text+lines",
        text=["","💻 Computers"],
        textposition="top center",
        marker=dict(size=10,color="violet"),
        line=dict(width=6,color="violet")
    )
)

fig.update_layout(
    height=800,
    title="Electricity Flow From Utility Grid To Facility Loads",
    scene=dict(
        bgcolor="black",
        xaxis_visible=False,
        yaxis_visible=False,
        zaxis_visible=False
    ),
    paper_bgcolor="black",
    font=dict(color="white")
)

st.plotly_chart(
    fig,
    use_container_width=True
)# =====================================
# PREMIUM CONTROL CENTER
# =====================================

st.header("🚀 Smart Facility Control Center")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "⚡ Grid Status",
        "ONLINE",
        "Stable"
    )
score = 85
with c2:
    st.metric(
        "🏢 Facility Health",
        f"{score}%",
        "+2%"
    )

with c3:
    st.metric(
        "💰 Savings Potential",
        "674 SAR",
        "Monthly"
    )

with c4:
    st.metric(
        "🌍 Carbon Score",
        "GREEN",
        "Good"
    )

st.markdown("---")
    # =====================================
# LOAD DISTRIBUTION
# =====================================
# =====================================
# LIVE LOAD MONITOR
# =====================================

st.header("📡 Live Load Monitoring")

live_fig = go.Figure()

live_fig.add_trace(
    go.Bar(
        x=["HVAC","Lighting","Computers","Motors"],
        y=[
            hvac_kw,
            lighting_kw,
            computers_kw,
            motors_kw
        ]
    )
)

live_fig.update_layout(
    title="Real-Time Load Consumption",
    height=500
)

st.plotly_chart(
    live_fig,
    use_container_width=True
)
st.header("📈 Load Distribution")

labels = [
    "HVAC",
    "Lighting",
    "Computers",
    "Motors"
]

values = [
    hvac_kw,
    lighting_kw,
    computers_kw,
    motors_kw
]

fig_pie = go.Figure(
    data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=0.45
        )
    ]
)

# =====================================
# LARGEST CONSUMER
# =====================================

loads = {
    "HVAC": hvac_kw,
    "Lighting": lighting_kw,
    "Computers": computers_kw,
    "Motors": motors_kw
}

largest_load = max(
    loads,
    key=loads.get
)

largest_value = loads[
    largest_load
]

st.subheader("🔥 Largest Energy Consumer")

st.success(
    f"{largest_load} consumes "
    f"{largest_value:.1f} kW"
)

# =====================================
# FACILITY SCORE
# =====================================

score = 100

if operating_hours > 12:
    score -= 10

if monthly_cost > 5000:
    score -= 15

if hvac_kw > total_kw * 0.6:
    score -= 10

score = max(score, 0)

st.subheader("🏆 Facility Score")

st.progress(score / 100)

st.metric(
    "Facility Health Score",
    f"{score}/100"
)

# =====================================
# ENERGY CLASS
# =====================================

if score >= 90:
    rating = "A+ Excellent"

elif score >= 80:
    rating = "A Good"

elif score >= 70:
    rating = "B Average"

elif score >= 60:
    rating = "C Needs Improvement"

else:
    rating = "D Poor"

st.info(
    f"Energy Rating: {rating}"
)

# =====================================
# SAVINGS CENTER
# =====================================

st.header("💰 Savings Center")

saving1 = monthly_cost * 0.10
saving2 = monthly_cost * 0.15
saving3 = monthly_cost * 0.05

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "LED Upgrade Saving",
        f"{saving1:.0f} SAR/month"
    )

with c2:
    st.metric(
        "HVAC Optimization",
        f"{saving2:.0f} SAR/month"
    )

with c3:
    st.metric(
        "Smart Scheduling",
        f"{saving3:.0f} SAR/month"
    )

st.success(
    f"Potential Total Saving: "
    f"{saving1+saving2+saving3:.0f} SAR/month"
)
# =====================================
# FORECAST CENTER
# =====================================

st.header("📈 Energy Forecast")

future_1_month = monthly_cost * 1.03
future_6_months = monthly_cost * 1.10
future_12_months = monthly_cost * 1.20

forecast_x = [
    "Current",
    "1 Month",
    "6 Months",
    "12 Months"
]

forecast_y = [
    monthly_cost,
    future_1_month,
    future_6_months,
    future_12_months
]

forecast_fig = go.Figure()

forecast_fig.add_trace(
    go.Scatter(
        x=forecast_x,
        y=forecast_y,
        mode="lines+markers"
    )
)

forecast_fig.update_layout(
    title="Cost Forecast",
    height=450
)

st.plotly_chart(
    forecast_fig,
    use_container_width=True
)

# =====================================
# CARBON IMPACT
# =====================================

st.header("🌍 Carbon Impact")

co2_monthly = monthly_energy * 0.43
co2_annual = annual_energy * 0.43

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Monthly CO₂",
        f"{co2_monthly:.0f} kg"
    )

with c2:
    st.metric(
        "Annual CO₂",
        f"{co2_annual:.0f} kg"
    )

if co2_annual < 10000:
    carbon_status = "🟢 Low"

elif co2_annual < 30000:
    carbon_status = "🟡 Medium"

else:
    carbon_status = "🔴 High"

st.info(
    f"Environmental Impact: {carbon_status}"
)

# =====================================
# EXECUTIVE REPORT
# =====================================

st.header("📋 Executive Report")

report_text = f'''
Facility Type: {facility_type}

Area: {area} m²

Total Connected Load: {total_kw:.1f} kW

Daily Energy Consumption: {daily_energy:.1f} kWh

Monthly Energy Consumption: {monthly_energy:.1f} kWh

Annual Energy Consumption: {annual_energy:.1f} kWh

Monthly Cost: {monthly_cost:.0f} SAR

Annual Cost: {annual_cost:.0f} SAR

Largest Energy Consumer: {largest_load}

Facility Score: {score}/100

Energy Rating: {rating}

Carbon Impact: {carbon_status}
'''

st.text_area(
    "Facility Summary",
    report_text,
    height=350
)

# =====================================
# QUICK RECOMMENDATIONS
# =====================================

st.header("🧠 Smart Recommendations")

if hvac_kw > total_kw * 0.5:
    st.warning(
        "HVAC is the dominant load. Consider high-efficiency units."
    )

if operating_hours > 12:
    st.warning(
        "Long operating hours detected. Consider load scheduling."
    )

if monthly_cost > 3000:
    st.warning(
        "Monthly cost is high. Energy optimization is recommended."
    )

if score >= 90:
    st.success(
        "Facility performance is excellent."
    )
    # =====================================
# 3D BUILDING DIGITAL TWIN
# =====================================

st.header("🏢 3D Building Digital Twin")

building_fig = go.Figure()

building_fig.add_trace(
    go.Scatter3d(
        x=[0, 0, 0, 0],
        y=[0, 0, 0, 0],
        z=[0, 1, 2, 3],
        mode="markers+text+lines",
        text=[
            "🚰 Pumps",
            "💡 Lighting",
            "❄ HVAC",
            "💻 Computers"
        ],
        textposition="top center",
        marker=dict(
            size=18,
            color=[
                motors_kw,
                lighting_kw,
                hvac_kw,
                computers_kw
            ],
            colorscale="Turbo",
            showscale=True,
            colorbar=dict(
                title="Load (kW)"
            )
        ),
        line=dict(
            width=10
        )
    )
)

building_fig.update_layout(
    height=700,
    scene=dict(
        xaxis_visible=False,
        yaxis_visible=False,
        zaxis_title="Building Floors"
    )
)

st.plotly_chart(
    building_fig,
    use_container_width=True
)

# =====================================
# ENERGY FLOW
# =====================================

st.header("⚡ Energy Flow")

flow_fig = go.Figure()

flow_fig.add_trace(
    go.Scatter(
        x=[0, 1, 2, 3, 4, 5],
        y=[0, 0, 0, 0, 0, 0],
        mode="markers+text+lines",
        text=[
            "⚡ Grid",
            "🔲 Main Panel",
            "🏢 Building",
            "❄ HVAC",
            "💡 Lighting",
            "💻 Loads"
        ],
        textposition="top center",
        marker=dict(
            size=35
        ),
        line=dict(
            width=6
        )
    )
)

flow_fig.update_layout(
    height=350,
    xaxis_visible=False,
    yaxis_visible=False
)

st.plotly_chart(
    flow_fig,
    use_container_width=True
)

# =====================================
# PERFORMANCE DASHBOARD
# =====================================

st.header("🚀 Performance Dashboard")

performance = score

cost_index = max(
    0,
    min(
        100,
        100 - (monthly_cost / 100)
    )
)

efficiency_index = max(
    0,
    min(
        100,
        score + 5
    )
)

g1, g2, g3 = st.columns(3)

with g1:

    gauge1 = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=performance,
            title={"text": "Facility Score"},
            gauge={
                "axis": {"range": [0, 100]}
            }
        )
    )

    st.plotly_chart(
        gauge1,
        use_container_width=True
    )

with g2:

    gauge2 = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=cost_index,
            title={"text": "Cost Index"},
            gauge={
                "axis": {"range": [0, 100]}
            }
        )
    )

    st.plotly_chart(
        gauge2,
        use_container_width=True
    )

with g3:

    gauge3 = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=efficiency_index,
            title={"text": "Efficiency Index"},
            gauge={
                "axis": {"range": [0, 100]}
            }
        )
    )

    st.plotly_chart(
        gauge3,
        use_container_width=True
    )# =====================================
# RISK ANALYSIS
# =====================================

st.header("🚨 Risk Analysis")

if monthly_cost < 2000:
    risk = "🟢 Low Risk"

elif monthly_cost < 5000:
    risk = "🟡 Medium Risk"

else:
    risk = "🔴 High Risk"

st.warning(
    f"Current Facility Risk Level: {risk}"
)

if hvac_kw > total_kw * 0.5:
    st.error(
        "HVAC system dominates consumption."
    )

if operating_hours > 12:
    st.error(
        "Long operating schedule detected."
    )

# =====================================
# FINAL STATUS
# =====================================

st.header("🏆 Facility Final Assessment")

if score >= 90:

    st.success(
        "Excellent Facility Performance"
    )

elif score >= 80:

    st.info(
        "Good Facility Performance"
    )

elif score >= 70:

    st.warning(
        "Average Facility Performance"
    )

else:

    st.error(
        "Facility Needs Improvement"
    )

st.markdown("---")

st.subheader("📌 Final Conclusion")

st.write(
    f"""
    This {facility_type} consumes approximately
    {monthly_energy:.0f} kWh per month with an
    estimated monthly cost of {monthly_cost:.0f} SAR.

    The largest consumer is {largest_load}.

    The facility score is {score}/100 and the
    potential savings opportunity exceeds
    {(saving1+saving2+saving3):.0f} SAR per month.
    """
)# =====================================
# EXECUTIVE SUMMARY CARD
# =====================================

st.markdown("---")

st.header("🏆 Executive Summary")

st.success(
    f"""
    Facility Type: {facility_type}

    Total Connected Load: {total_kw:.1f} kW

    Monthly Energy Consumption: {monthly_energy:.0f} kWh

    Monthly Cost: {monthly_cost:.0f} SAR

    Largest Consumer: {largest_load}

    Facility Score: {score}/100

    Potential Savings: {(saving1+saving2+saving3):.0f} SAR/month

    Environmental Impact: {carbon_status}
    """
)