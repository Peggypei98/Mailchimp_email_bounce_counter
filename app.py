import streamlit as st
import pandas as pd

def load_data(files):
    """Load and concatenate multiple CSV files into a single DataFrame."""
    dataframes = [pd.read_csv(file) for file in files]
    return pd.concat(dataframes, ignore_index=True)

def calculate_bounce_summary(df):
    """Group the DataFrame by email and aggregate the total bounce count."""
    df['Bounce_Count'] = 1  # Add a column to count occurrences
    return df.groupby(['Email Address', 'First Name', 'Last Name'])['Bounce_Count'].sum().reset_index()

def filter_by_bounce_count(df, selected_counts):
    """Filter the DataFrame based on selected bounce counts."""
    return df[df['Bounce_Count'].isin(selected_counts)]

def display_statistics(df):
    """Display statistics on bounce counts and provide recommendations."""
    st.subheader("Bounce Count Statistics")

    bounce_counts = df['Bounce_Count'].value_counts().sort_index()
    st.write("Number of recipients with specific bounce counts:")
    st.write(bounce_counts)

    recommendation_threshold = 3
    st.markdown("""
        ### Recommendations:
        - **Recipients with more than 3 bounces** should be removed from Mailchimp.
        - Review email addresses with multiple bounces to maintain list quality.
        - Use double opt-in or confirm email formats to reduce bounce rates.
    """)

    if (bounce_counts.index >= recommendation_threshold).any():
        st.warning(
            f"There are recipients with bounce counts exceeding {recommendation_threshold}. "
            "Consider removing them from Mailchimp."
        )

def main():
    """The main function to run the Streamlit app."""
    st.title("Email Bounce Counter App")

    uploaded_files = st.file_uploader(
        "Upload at least two CSV files", 
        accept_multiple_files=True, 
        type=["csv"]
    )

    if len(uploaded_files) >= 2:
        try:
            merged_df = load_data(uploaded_files)
            bounce_summary = calculate_bounce_summary(merged_df)
            unique_counts = sorted(bounce_summary['Bounce_Count'].unique())

            selected_counts = st.multiselect(
                "Select Bounce Counts to Include", 
                unique_counts, 
                default=unique_counts
            )

            filtered_summary = filter_by_bounce_count(bounce_summary, selected_counts)
            st.write("Filtered Email Bounce Summary:", filtered_summary)

            csv = filtered_summary.to_csv(index=False).encode('utf-8')

            st.download_button(
                label="Download Filtered Summary as CSV",
                data=csv,
                file_name='filtered_email_bounce_summary.csv',
                mime='text/csv',
            )

            display_statistics(filtered_summary)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload at least two CSV files.")

if __name__ == "__main__":
    main()
