import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

# Set Streamlit page config
st.set_page_config(
    page_title='Understand Data',
    page_icon='📊'
)

# Function to generate and display profile report
def generate_report(data):
    if data.empty:
        st.warning("Uploaded file is empty! Please check the data.")
        return

    profile = ProfileReport(data, explorative=True)
    
    # Generate and display the HTML report
    report_html = profile.to_html()
    html(report_html, height=800, scrolling=True)

# Main function
def main():
    st.title("📈 Understand Your Data")

    # File uploader
    file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if file is not None:
        try:
            if file.name.endswith(".csv"):
                data = pd.read_csv(file)
            elif file.name.endswith(".xlsx"):
                data = pd.read_excel(file)
            else:
                st.error("Unsupported file format. Please upload a CSV or Excel file.")
                return
            
            # Display first few rows of the data
            st.write("### Data Preview:")
            st.dataframe(data.head())

            # Generate the profiling report
            generate_report(data)

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Ensure script runs as main
if __name__ == "__main__":
    main()
