import streamlit as st
import pandas as pd

st.title("Mark spliter")
def split_mark(mark):
    weight = [10,20,30,10,10,20]
    total = sum(weight)

    base = [(i*mark)//total for i in weight]

    remainder = mark - sum(base)
    print(remainder)
    for i in range(remainder):
        base[-1-i] += 1
    
    return base

tot = st.number_input("Enter your mark (out of 100)", max_value=100)

labels = ["Pre-Viva", "Preparation", "Program", "Output & Result", "Post-Viva", "Record"]

if st.button("Split"):
    a = split_mark(tot)
    df = pd.DataFrame({"Label":labels, "Total Mark":[10,20,30,10,10,20], "Marks":a})
    st.table(df)
