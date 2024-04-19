# Libraries
import streamlit as st
import pandas as pd
import joblib


# Streamlit

def main():
    st.title("Heart Failure Prediction Web App")
    st.markdown('<img src="https://fldscc.com/wp-content/uploads/2020/07/shutterstock_30528475.jpg" alt="image" style="width:500px;height:500px;">', unsafe_allow_html=True)

    # st.info("You Are Welcome")

    st.title("Input Your Data")

        # user input
    def user_input():
        Age = st.number_input("Age")
        Sex = st.selectbox("Sex", ['M', 'F'])
        ChestPainType = st.selectbox("Chest Pain Type", ['ATA', 'NAP', 'ASY', 'TA'])
        Cholesterol = st.number_input("Cholesterol")
        FastingBS = st.selectbox("Fasting Blood Sugar", [0, 1])
        MaxHR = st.number_input("Maximum Heart Rate")
        ExerciseAngina = st.selectbox("Exercise-Induced Angina", ['N', 'Y'])
        Oldpeak = st.number_input("Oldpeak")
        ST_Slope = st.selectbox("ST_Slope", ['Up', 'Flat', 'Down'])

        # ----------------------------------
        Sex_labels = ['M', 'F']
        Sex_encode = [1, 0]
        final_sex = dict(zip(Sex_labels, Sex_encode))
        
        #-----------------------------------
        ChestPainType_labels = ['ATA', 'NAP', 'ASY', 'TA']
        ChestPainType_encode = [1, 2, 0, 3]
        final_ChestPainType = dict(zip(ChestPainType_labels, ChestPainType_encode))
        #-----------------------------------
        RestingECG_labels = ['Normal', 'ST', 'LVH']
        RestingECG_encode = [1, 2, 0]
        final_RestingECG = dict(zip(RestingECG_labels, RestingECG_encode))
        
        #---------------------------------
        ExerciseAngina_labels = ['N', 'Y']
        ExerciseAngina_encode = [0, 1]
        final_ExerciseAngina = dict(zip(ExerciseAngina_labels, ExerciseAngina_encode))
        #---------------------------------
        ST_Slope_labels = ['Up', 'Flat', 'Down']
        ST_Slope_encode = [2, 1, 0]
        final_ST_Slope = dict(zip(ST_Slope_labels, ST_Slope_encode))
        
        #------------------- DataFrame ---------------------------
        df = pd.DataFrame({
                        "Age": [Age],
                        "Sex": [final_sex[Sex]],
                        "ChestPainType": [final_ChestPainType[ChestPainType]],
                        "Cholesterol": [Cholesterol],
                        "Fasting Blood Sugar": [FastingBS],
                        "Maximum Heart Rate": [MaxHR],
                        "ExerciseAngina": [final_ExerciseAngina[ExerciseAngina]],
                        'Oldpeak': [Oldpeak],
                        "ST_Slope": [final_ST_Slope[ST_Slope]],
                        })

        # ---------------------------- Return Data ------------------------------
        
        return df
    
    Data = user_input()
    
    # ---------------------- sidebar ----------------------- 
    st.sidebar.header("The Prediction Side")
    st.sidebar.info("Here You Can Show Your Case !")
    st.sidebar.write("_Click On The Button_")
    button = st.sidebar.button("Submit")
    
    # ------------------------ Model ------------------------
    model = joblib.load(r"LogisticRegression.pkl")
    
    if button:
        prediction = model.predict(Data)
        if prediction == 0:
            st.sidebar.write("The Patient Is Good :)")
            st.sidebar.image("https://rachelziv.com.au/wp-content/uploads/2020/01/happy.jpg", width=150)
        else:
            st.sidebar.write("The Patient Is Sick :(") 
            st.sidebar.image("https://www.apa.org/images/sad-title-image_tcm7-179953.jpg", width=150)
    
        

    st.write(" ## _`By: Mohammed Ghannam`_")
    
if __name__ == "__main__":
    main()