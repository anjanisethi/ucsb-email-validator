import pandas as pd
import streamlit as st

st.title('UCSB Email Validator')

st.markdown(
    '''Upload a CSV table that contains an 'email' column. This tool will flag email 
    addresses with the '@ucsb.edu' domain, create a CSV file containing emails with invalid addresses,
    and creat a CSV containing the fully annotated dataset.'''
)
uploaded_file = st.file_uploader('Upload your CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    email_col = None
    for col in df.columns:
        if 'email' in col.lower():
            email_col = col
            break
    if not email_col:
        st.error("Could not find an email column. Please make sure it contains 'email' in the column name.")
    else:
        # flags valid emails
        df['valid'] = df[email_col].apply(lambda x: str(x).endswith('@ucsb.edu'))
        df['invalid_running_count'] = (~df['valid']).astype(int).cumsum()

    # show total
    invalid_count = (~df['valid']).sum()
    st.success('Found {invalid_count} invalid email(s).')

    # show preview
    st.dataframe(df)

    # download full results
    full_csv = df.to_csv(index=False).encode('utf-8')
    st.download_button('Download full CSV with validity flag', full_csv, 'full_email_check.csv', 'text/csv')

    # filter and download just invalids
    invalids = df[~df['valid']].copy()
    if not invalids.empty:
        invalid_csv = invalids.to_csv(index=False).encode('utf-8')
        st.download_button('Download invalid emails only', invalid_csv, 'invalid_emails.csv', 'text/csv')
    else:
        st.info('All emails are valid - no invalids to download.')

else:
    st.info('Upload a CSV file above to begin.')
