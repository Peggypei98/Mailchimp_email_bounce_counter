# 📧 Mailchimp Email Bounce Counter App

A simple and effective Email Bounce Counter App built using Streamlit and Python. This tool allows users to upload CSV files with email campaign bounce times data, analyze bounce counts, filter results, and download them for further action in Mailchimp.

I created this quick app with the help of GPT to make my colleagues' lives easier by helping them manage email campaigns more effectively, improve email list quality, and save on Mailchimp costs.



## 🛠️ Features
- **File Upload & Merging:** 

    Upload multiple CSV files and merge them into a single dataset.
- **Bounce Summary Calculation:**
    
    Automatically counts the number of bounces for each email address.
- **Filtering by Bounce Count:** 
    
    Easily filter email recipients by specific bounce counts.
- **Statistical Summary:**
    
    Displays how many recipients have 1, 2, 3, etc., bounce counts.
- **Recommendations:** 
    
    Provides actionable insights to remove recipients with high bounce counts.
- **CSV Download:** 
    
    Download filtered results as a CSV file.
- **Mailchimp Removal Guide:** 
    
    A step-by-step guide on how to remove high bounce rate emails from Mailchimp.

## 📋 Prerequisites
Use the deployed version withoue prerequistes: 

or 

Make sure you have Python 3.8+ installed.

Install the required Python packages:
```
pip install streamlit pandas
```

 use the deployed version withoue prerequistes.

## 🚀 How to Run

Access the deployed version of this app, visit:

or

Clone this repository:
```
git clone https://github.com/Peggypei98/Mailchimp_email_bounce_counter.git
cd Mailchimp_email_bounce_counter.git
```

Run the app:
```
streamlit run app.py
```

Open the app:

The app will open in your browser at http://localhost:8501.


## 📄 Usage Instructions
- **Upload CSV Files:**

    Upload at least two CSV files containing your Mailchimp email campaign data. Make sure your files contain columns for Email Address, First Name, Last Name, and Bounce Type.
    
- **Filter Bounce Counts:**
    
    Use the multiselect widget to filter results by bounce counts (e.g., recipients with 1, 2, or more bounces).

- **View Statistics & Recommendations:**
    
    Get an overview of recipients with specific bounce counts and follow recommendations to improve your email list.
    
- **Download Filtered Results:**
    
    Download the filtered results as a CSV file for further use.

## 📊 Sample Output
```
Recipients with Bounce Count = 1: 5
Recipients with Bounce Count = 2: 3
Recommendations:
Remove recipients with more than 3 bounces from Mailchimp.
Use double opt-in to improve list quality.
```
With an attached csv result for download. 

## 📝 Example CSV File Structure

| Email Address  | First Name | Last Name | Bounce Type |
| ------------- | ------------- | ------------- | ------------- |
| example1@mail.com  | Abby  | Doe | Soft  |
| example1@mail.com  |  Jane  | Smith | Hard |

## 📥 Guide: How to Remove High Bounce Rate Emails from Mailchimp
After filtering out the high bounce rate data and downloading it as a CSV file, follow these steps to remove those emails from Mailchimp:

1. **Log in to Mailchimp:**

    Go to Mailchimp's website and log in to your account.
    
    Navigate to Your Audience List:

    In the left-hand menu, click on Audience.

    Select the Audience Dashboard where your email list is located.

2. **Import the Filtered CSV:**

    Click on Manage Contacts > Import Contacts.

    Choose Upload a CSV or TXT file and upload the filtered CSV file with high bounce rate emails.

3. **Tag the Imported Emails:**

    During the import process, assign a tag like “High Bounce Rate” to the imported emails for easier identification.

4. **Filter Contacts by Tag:**

    After importing, go back to your Audience.
    
    Click Tags in the Audience menu, and select the “High Bounce Rate” tag to view the filtered contacts.

5. **Remove the Contacts:**

    Select all the tagged contacts by clicking the checkbox.
    
    Click Actions > Permanently Delete or Unsubscribe to remove them from your list.

6.**Confirm Deletion or Unsubscribe:**

    Follow the on-screen confirmation to remove the contacts from your list.

7. **Verify Removal:**

    Go back to your Audience Dashboard to ensure the high bounce rate contacts have been removed.

## 🏗️ Project Structure
```
email-bounce-counter/
│
├── app.py            # Main Streamlit app code
├── README.md         # Project README file
└── requirements.txt  # List of dependencies 
```

## ❤️ Acknowledgments
- GPT: For assisting in the development of this app.
- Streamlit: For making it easy to create web apps with Python.
- Mailchimp: For providing an excellent platform for email marketing.

🤖 Created Using GPT
This app was built quickly using GPT to streamline my colleagues' workflow and make email list management easier. The app simplifies bounce analysis, saving time and effort.



