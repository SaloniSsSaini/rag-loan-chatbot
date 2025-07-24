import pandas as pd

def load_and_prepare_data(csv_path):
    df = pd.read_csv(csv_path)
    df.fillna("Unknown", inplace=True)
    docs = []

    for _, row in df.iterrows():
        doc = f"""
        Applicant {row['Loan_ID']} is a {row['Education']} with an income of {row['ApplicantIncome']}, 
        a coapplicant income of {row['CoapplicantIncome']}, applying for a loan of amount {row['LoanAmount']}. 
        They have a credit history of {row['Credit_History']} and the loan was {'approved' if row['Loan_Status']=='Y' else 'not approved'}.
        """
        docs.append(doc.replace("\n", " ").strip())

    return docs