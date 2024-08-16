import streamlit as st
import joblib
import sklearn

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:10px;">
    <h2 style="text-align:center;">Insurance Prediction</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    model = joblib.load('health_model')

    p1 = st.slider("Enter Your Age", 18, 100)
    s1 = st.selectbox("Sex", ("Male", "Female"))
    p2 = 1 if s1 == "Male" else 0
    p3 = st.number_input("Enter Your BMI Value")
    p4 = st.slider("Enter Number of Children", 0, 4)
    s2 = st.selectbox("Smoker", ("Yes", "No"))
    p5 = 1 if s2 == "Yes" else 0
    p6 = st.slider("Enter Your Region [1-4]", 1, 4)

    if st.button('Predict'):
        prediction = model.predict([[p1, p2, p3, p4, p5, p6]])
        st.balloons()
        st.success('Insurance Amount is {} '.format(round(prediction[0], 2)))

if __name__ == '__main__':
    main()  