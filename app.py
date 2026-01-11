import streamlit as st
import pandas as pd

st.title("Student Marks Management App")

name = st.text_input("Enter Student Name: ")
m = st.number_input("Enter Python Marks: " , min_value = 0 , max_value = 50 )
n = st.number_input("Enter Statistics Marks: " , min_value = 0 , max_value = 50 )
o = st.number_input("Enter Excel Marks: " , min_value = 0 , max_value = 50 )
p = st.number_input("Enter OTDS Marks: " , min_value = 0 , max_value = 50 )
q = st.number_input("Enter Practical Marks:" , min_value = 0 , max_value = 50 )

if st.button("Calculate Result"):
    percentage = (m+n+o+p+q) / 250 * 100

    st.success(f"Congratulations you got {percentage:.2f} %")

    if percentage >= 90 :
         Grade = "A"
    elif percentage >= 80 :
         Grade = "B"
    elif percentage >= 70 :
         Grade = "C"
    elif percentage >= 60 :
         Grade = "D"
    elif percentage >= 45 :
         Grade = "E"
    else :
        Grade = "Fail"
        
    st.info(f"Congratulations on getting {Grade} Grade")
        
    data = {
        "Student Name" : [name],
        "Python Marks" : [m],
        "Statistics Marks" : [n],
        "Excel Marks" : [o],
        "OTDS Marks" : [p],
        "Practical Marks" : [q],
    }
    
    df = pd.DataFrame(data)
    df.to_csv("Student Marks Data.csv" , mode = "a" , index = False, header = False)
    
    st.success(f"Result Saved Successfully")

st.subheader("Saved Student Records")

try :
    saved_df = pd.read_csv("Student Marks Data.csv")
    st.dataframe(saved_df)
except FileNotFoundError:
    st.warning("No data saved yet")
    
