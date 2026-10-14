import streamlit as st
import math

st.set_page_config(page_title="Mechanical Engineering Calculator", layout="wide")

def calculate_force():
    st.subheader("Force (F = m * a)")
    m = st.number_input("Enter mass (m) in kg:", value=0.0)
    a = st.number_input("Enter acceleration (a) in m/s^2:", value=0.0)
    if st.button("Calculate Force"):
        force = m * a
        st.success(f"Result: Force (F) = {force:.4f} N")

def calculate_work():
    st.subheader("Work (W = F * d * cos(theta))")
    f = st.number_input("Enter force (F) in N:", value=0.0)
    d = st.number_input("Enter displacement (d) in m:", value=0.0)
    angle_deg = st.number_input("Enter angle theta in degrees:", value=0.0)
    if st.button("Calculate Work"):
        angle_rad = math.radians(angle_deg)
        work = f * d * math.cos(angle_rad)
        st.success(f"Result: Work Done (W) = {work:.4f} J")

def calculate_power():
    st.subheader("Power (P = W / t)")
    w = st.number_input("Enter work done (W) in J:", value=0.0)
    t = st.number_input("Enter time (t) in seconds:", value=1.0, min_value=0.0001)
    if st.button("Calculate Power"):
        power = w / t
        st.success(f"Result: Power (P) = {power:.4f} W")

def calculate_kinetic_energy():
    st.subheader("Kinetic Energy (KE = 0.5 * m * v^2)")
    m = st.number_input("Enter mass (m) in kg:", value=0.0)
    v = st.number_input("Enter velocity (v) in m/s:", value=0.0)
    if st.button("Calculate Kinetic Energy"):
        ke = 0.5 * m * (v ** 2)
        st.success(f"Result: Kinetic Energy (KE) = {ke:.4f} J")


def calculate_stress():
    st.subheader("Stress (sigma = F / A)")
    f = st.number_input("Enter force (F) in N:", value=0.0, key="stress_f")
    a = st.number_input("Enter cross-sectional area (A) in m^2:", value=1.0, min_value=0.0001)
    if st.button("Calculate Stress"):
        stress = f / a
        st.success(f"Result: Stress (sigma) = {stress:.4f} Pa (N/m^2)")

def calculate_strain():
    st.subheader("Strain (epsilon = delta_L / L0)")
    delta_l = st.number_input("Enter change in length (delta L) in m:", value=0.0)
    l0 = st.number_input("Enter original length (L0) in m:", value=1.0, min_value=0.0001)
    if st.button("Calculate Strain"):
        strain = delta_l / l0
        st.success(f"Result: Strain (epsilon) = {strain:.6f} (dimensionless)")

def calculate_youngs_modulus():
    st.subheader("Young's Modulus (E = stress / strain)")
    stress = st.number_input("Enter stress (sigma) in Pa:", value=0.0)
    strain = st.number_input("Enter strain (epsilon):", value=1.0, min_value=0.000001)
    if st.button("Calculate Young's Modulus"):
        e = stress / strain
        st.success(f"Result: Young's Modulus (E) = {e:.4e} Pa")


def calculate_heat_transfer():
    st.subheader("Heat Transfer (Q = m * c * delta_T)")
    m = st.number_input("Enter mass (m) in kg:", value=0.0, key="ht_m")
    c = st.number_input("Enter specific heat capacity (c) in J/(kg*K):", value=0.0)
    delta_t = st.number_input("Enter temperature change (delta T) in K or °C:", value=0.0)
    if st.button("Calculate Heat Transfer"):
        q = m * c * delta_t
        st.success(f"Result: Heat Transfer (Q) = {q:.4f} J")

def calculate_thermo_work():
    st.subheader("Boundary Work Done (W = P * delta_V)")
    p = st.number_input("Enter pressure (P) in Pa:", value=0.0, key="tw_p")
    v1 = st.number_input("Enter initial volume (V1) in m^3:", value=0.0)
    v2 = st.number_input("Enter final volume (V2) in m^3:", value=0.0)
    if st.button("Calculate Work Done"):
        w = p * (v2 - v1)
        st.success(f"Result: Boundary Work Done (W) = {w:.4f} J")

def calculate_thermal_efficiency():
    st.subheader("Thermal Efficiency (eta = W_net / Q_in * 100)")
    w_net = st.number_input("Enter net work output (W_net) in J:", value=0.0)
    q_in = st.number_input("Enter total heat input (Q_in) in J:", value=1.0, min_value=0.0001)
    if st.button("Calculate Thermal Efficiency"):
        eta = (w_net / q_in) * 100
        st.success(f"Result: Thermal Efficiency (eta) = {eta:.2f}%")


def calculate_fluid_pressure():
    st.subheader("Hydrostatic Pressure (P = rho * g * h)")
    rho = st.number_input("Enter fluid density (rho) in kg/m^3:", value=1000.0)
    g = st.number_input("Enter gravitational acceleration (g) in m/s^2:", value=9.81)
    h = st.number_input("Enter fluid depth/height (h) in m:", value=0.0)
    if st.button("Calculate Pressure"):
        p = rho * g * h
        st.success(f"Result: Hydrostatic Pressure (P) = {p:.4f} Pa")

def calculate_reynolds_number():
    st.subheader("Reynolds Number (Re = rho * v * D / mu)")
    rho = st.number_input("Enter fluid density (rho) in kg/m^3:", value=1000.0, key="re_rho")
    v = st.number_input("Enter flow velocity (v) in m/s:", value=0.0, key="re_v")
    d = st.number_input("Enter characteristic length/diameter (D) in m:", value=0.0)
    mu = st.number_input("Enter dynamic viscosity (mu) in Pa*s:", value=0.001, min_value=0.000001)
    if st.button("Calculate Reynolds Number"):
        re = (rho * v * d) / mu
        regime = "Laminar" if re < 2300 else ("Transitional" if re <= 4000 else "Turbulent")
        st.success(f"Result: Reynolds Number (Re) = {re:.2f} ({regime} Flow)")

def calculate_flow_velocity():
    st.subheader("Flow Velocity (v = Q / A)")
    q = st.number_input("Enter discharge / flow rate (Q) in m^3/s:", value=0.0)
    a = st.number_input("Enter cross-sectional area (A) in m^2:", value=1.0, min_value=0.0001, key="fv_a")
    if st.button("Calculate Velocity"):
        v = q / a
        st.success(f"Result: Flow Velocity (v) = {v:.4f} m/s")

def calculate_discharge():
    st.subheader("Discharge (Q = A * v)")
    a = st.number_input("Enter cross-sectional area (A) in m^2:", value=0.0, key="dis_a")
    v = st.number_input("Enter flow velocity (v) in m/s:", value=0.0, key="dis_v")
    if st.button("Calculate Discharge"):
        q = a * v
        st.success(f"Result: Discharge (Q) = {q:.4f} m^3/s")


def calculate_heat_conduction():
    st.subheader("Heat Conduction (Fourier's Law)")
    k = st.number_input("Enter thermal conductivity (k) in W/(m*K):", value=0.0)
    a = st.number_input("Enter surface area (A) in m^2:", value=0.0, key="hc_a")
    th = st.number_input("Enter hot temperature (Th) in K or °C:", value=0.0)
    tc = st.number_input("Enter cold temperature (Tc) in K or °C:", value=0.0)
    dx = st.number_input("Enter material thickness (dx) in m:", value=1.0, min_value=0.0001)
    if st.button("Calculate Heat Conduction"):
        q_cond = k * a * (th - tc) / dx
        st.success(f"Result: Heat Conduction Rate (Q_cond) = {q_cond:.4f} W")

def calculate_cop():
    st.subheader("Coefficient of Performance (COP)")
    mode = st.radio("Select mode:", ("Refrigerator", "Heat Pump"))
    w_in = st.number_input("Enter work input (W_in) in J or W:", value=1.0, min_value=0.0001)
    
    if mode == "Refrigerator":
        q_cool = st.number_input("Enter heat absorbed from cold reservoir (Q_L) in J or W:", value=0.0)
        if st.button("Calculate COP"):
            cop = q_cool / w_in
            st.success(f"Result: COP (Refrigerator) = {cop:.4f}")
    else:
        q_hot = st.number_input("Enter heat rejected to hot reservoir (Q_H) in J or W:", value=0.0)
        if st.button("Calculate COP"):
            cop = q_hot / w_in
            st.success(f"Result: COP (Heat Pump) = {cop:.4f}")

def calculate_heat_engine_efficiency():
    st.subheader("Heat-Engine Efficiency (Carnot)")
    th = st.number_input("Enter hot reservoir temperature (T_H) in Kelvin:", value=300.0, min_value=0.01)
    tc = st.number_input("Enter cold reservoir temperature (T_C) in Kelvin:", value=290.0, min_value=0.01)
    if st.button("Calculate Carnot Efficiency"):
        if tc >= th:
            st.error("Error: T_H must be strictly greater than T_C.")
        else:
            eta_max = (1 - (tc / th)) * 100
            st.success(f"Result: Carnot Heat-Engine Efficiency = {eta_max:.2f}%")


def calculate_torque():
    st.subheader("Torque (T = 60 * P / (2 * pi * N))")
    p = st.number_input("Enter power (P) in Watts:", value=0.0, key="tq_p")
    n = st.number_input("Enter rotational speed (N) in RPM:", value=1.0, min_value=0.0001, key="tq_n")
    if st.button("Calculate Torque"):
        omega = (2 * math.pi * n) / 60
        torque = p / omega
        st.success(f"Result: Torque (T) = {torque:.4f} N*m")

def calculate_shaft_power():
    st.subheader("Shaft Power (P = 2 * pi * N * T / 60)")
    t = st.number_input("Enter torque (T) in N*m:", value=0.0, key="sp_t")
    n = st.number_input("Enter rotational speed (N) in RPM:", value=0.0, key="sp_n")
    if st.button("Calculate Shaft Power"):
        power = (2 * math.pi * n * t) / 60
        st.success(f"Result: Shaft Power (P) = {power:.4f} W ({power / 1000:.4f} kW)")

def calculate_shaft_diameter():
    st.subheader("Shaft Diameter (d = [(16 * T) / (pi * tau)]^(1/3))")
    t = st.number_input("Enter transmitted torque (T) in N*m:", value=0.0, key="sd_t")
    tau_allowable = st.number_input("Enter allowable shear stress (tau) in Pa:", value=1.0, min_value=0.0001)
    if st.button("Calculate Shaft Diameter"):
        d = ((16 * t) / (math.pi * tau_allowable)) ** (1/3)
        st.success(f"Result: Minimum Shaft Diameter (d) = {d:.6f} m ({d * 1000:.2f} mm)")


def main():
    st.title("⚙️ Complete Mechanical Engineering Calculator")
    
    # Sidebar navigation
    st.sidebar.header("Select Module")
    modules = {
        "1. Mechanics": ["Force", "Work", "Power", "Kinetic Energy"],
        "2. Strength of Materials": ["Stress", "Strain", "Young's Modulus"],
        "3. Thermodynamics": ["Heat Transfer", "Work Done", "Thermal Efficiency"],
        "4. Fluid Mechanics": ["Pressure", "Reynolds Number", "Flow Velocity", "Discharge"],
        "5. Thermal Engineering": ["Heat Conduction", "COP", "Heat-Engine Efficiency"],
        "6. Machine Design": ["Torque", "Shaft Power", "Shaft Diameter"]
    }
    
    selected_module = st.sidebar.selectbox("Choose a category:", list(modules.keys()))
    selected_topic = st.sidebar.selectbox("Choose a calculation:", modules[selected_module])
    
    st.markdown("---")
    
    # Route to the correct calculation based on user choice
    if selected_module == "1. Mechanics":
        if selected_topic == "Force": calculate_force()
        elif selected_topic == "Work": calculate_work()
        elif selected_topic == "Power": calculate_power()
        elif selected_topic == "Kinetic Energy": calculate_kinetic_energy()
            
    elif selected_module == "2. Strength of Materials":
        if selected_topic == "Stress": calculate_stress()
        elif selected_topic == "Strain": calculate_strain()
        elif selected_topic == "Young's Modulus": calculate_youngs_modulus()
            
    elif selected_module == "3. Thermodynamics":
        if selected_topic == "Heat Transfer": calculate_heat_transfer()
        elif selected_topic == "Work Done": calculate_thermo_work()
        elif selected_topic == "Thermal Efficiency": calculate_thermal_efficiency()
            
    elif selected_module == "4. Fluid Mechanics":
        if selected_topic == "Pressure": calculate_fluid_pressure()
        elif selected_topic == "Reynolds Number": calculate_reynolds_number()
        elif selected_topic == "Flow Velocity": calculate_flow_velocity()
        elif selected_topic == "Discharge": calculate_discharge()
            
    elif selected_module == "5. Thermal Engineering":
        if selected_topic == "Heat Conduction": calculate_heat_conduction()
        elif selected_topic == "COP": calculate_cop()
        elif selected_topic == "Heat-Engine Efficiency": calculate_heat_engine_efficiency()
            
    elif selected_module == "6. Machine Design":
        if selected_topic == "Torque": calculate_torque()
        elif selected_topic == "Shaft Power": calculate_shaft_power()
        elif selected_topic == "Shaft Diameter": calculate_shaft_diameter()

if __name__ == "__main__":
    main()
