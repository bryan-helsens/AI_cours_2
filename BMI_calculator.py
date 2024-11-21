import streamlit as st

def calculate_bmi(weight, height):
    """
    Calculate BMI using weight in kg and height in meters
    """
    # Ensure height is converted to meters if needed
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    """
    Determine BMI category based on calculated BMI
    """
    if bmi < 18.5:
        return "Ondergewicht"
    elif 18.5 <= bmi < 25:
        return "Normaal gewicht"
    elif 25 <= bmi < 30:
        return "Overgewicht"
    else:
        return "Obesitas"

# Initialize session state variables
if 'weight' not in st.session_state:
    st.session_state.weight = 70.0
if 'height' not in st.session_state:
    st.session_state.height = 1.75
if 'bmi_calculated' not in st.session_state:
    st.session_state.bmi_calculated = False

# Streamlit app title and description
st.title("BMI Calculator")
st.write("Bereken je Body Mass Index (BMI)")

# Input columns for weight and height
col1, col2 = st.columns(2)

with col1:
    st.session_state.weight = st.number_input(
        "Gewicht (kg)", 
        min_value=1.0, 
        max_value=300.0, 
        value=st.session_state.weight, 
        step=0.1
    )

with col2:
    st.session_state.height = st.number_input(
        "Lengte (m)", 
        min_value=0.5, 
        max_value=2.5, 
        value=st.session_state.height, 
        step=0.01
    )

# Columns for Calculate and Reset buttons
col_calc, col_reset = st.columns(2)

with col_calc:
    if st.button("Bereken BMI"):
        # Perform BMI calculation
        bmi = calculate_bmi(st.session_state.weight, st.session_state.height)
        category = get_bmi_category(bmi)
        
        # Store calculation results
        st.session_state.bmi = bmi
        st.session_state.category = category
        st.session_state.bmi_calculated = True

with col_reset:
    if st.button("Reset"):
        # Reset all session state variables
        st.session_state.weight = 70.0
        st.session_state.height = 1.75
        st.session_state.bmi_calculated = False

# Display results if BMI has been calculated
if st.session_state.bmi_calculated:
    st.success(f"Je BMI is: {st.session_state.bmi}")
    st.info(f"BMI Categorie: {st.session_state.category}")
    
    # Additional health advice based on BMI
    if st.session_state.category == "Ondergewicht":
        st.warning("Overweeg om aan te komen met gezonde voeding en training.")
    elif st.session_state.category == "Overgewicht":
        st.warning("Overweeg meer te bewegen en gezonder te eten.")
    elif st.session_state.category == "Obesitas":
        st.warning("Raadpleeg een arts voor gepersonaliseerd advies.")