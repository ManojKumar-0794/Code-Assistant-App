import streamlit as st

# Title
st.title("Code Assistant App")

# Input
query = st.text_input("Enter your query (e.g. 'merge two Excel files in Python')")

# Simulated code lookup
if query:
    st.write("Searching open-source code repositories...")
    
    # Example response
    if "excel" in query.lower():
        st.code("import pandas as pd\n\nfile1 = pd.read_excel('file1.xlsx')\nfile2 = pd.read_excel('file2.xlsx')\nmerged = pd.concat([file1, file2])")
    elif "vba" in query.lower():
        st.code('Sub AutoRun()\n  MsgBox "Hello from VBA!"\nEnd Sub')
    elif "formula" in query.lower():
        st.code('=IF(A1>10, "High", "Low")')
    else:
        st.write("No example yet. More functionality coming soon!")

st.markdown("---")
st.caption("This is just a demo. You’ll later connect this to real open-source sources.")
