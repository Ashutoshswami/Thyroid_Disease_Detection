import streamlit as st
import pickle
from sklearn import svm
from sklearn.svm import SVC

model_dt=pickle.load(open('model_dt.pkl','rb'))



def main():
    st.title("Tyroid Disease Detection App")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Thyroid Disease Type Classification</h2>
    <h3 style="color:white;text-align:center;">0='Normal',1='Hypo',2='Hyper'</h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Decision Tree']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    var_1=st.slider('T3 resin uptake test', 65.0, 144.0)
    var_2=st.slider('Total Serum thyroxin', 0.5, 25.0)
    var_3=st.slider('Total serum triiodothyronine', 0.20, 10.0)
    var_4=st.slider('basal thyroid-stimulating hormone (TSH)', 0.1, 6.0)
    var_5=st.slider('Maximal absolute difference of TSH value after injection of 200 micro grams of thyrotropin releasing hormone as compared to the basal', -0.7,6.0)
    inputs=[[var_1,var_2,var_3,var_4,var_5]]
  
    predict_dt=model_dt.predict(inputs)
    
    if st.button('Classify'):
            st.success(predict_dt)


if __name__=='__main__':
    main()