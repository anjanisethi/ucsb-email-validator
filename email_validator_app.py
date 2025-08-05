import pandas as pd
import streamlit as st

st.title('UCSB Email Validator')

st.markdown(
    '''Upload a CSV file that contains a designated email column. This tool will flag email 
    addresses that don't have the '@ucsb.edu' domain. The app will also create a CSV file containing emails with invalid addresses,
    as well as a CSV containing the fully annotated dataset.
    Created by Anjani Sethi
    Program Management Office, UC Santa Barbara ITS
    Undergraduate in Statistics & Data Science + Communication'''
)
uploaded_file = st.file_uploader('Upload your CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # tries to pre-select a potential email column
    default_col = next((col for col in df.columns if 'email' in col.lower()), df.columns[0])
    
    st.markdown('### Select the column that contains email addresses:')
    st.caption("We've pre-selected the most likely email column for you. Feel free to select another column yourself if needed.")
    
    selected_col = st.selectbox('Select column', df.columns, index=df.columns.get_loc(default_col))

    df['valid'] = df[selected_col].apply(lambda x: str(x).endswith('@ucsb.edu'))
    df['invalid_running_count'] = (~df['valid']).astype(int).cumsum()

    # count invalids
    invalid_count = (~df['valid']).sum()
    st.success(f'Found {invalid_count} invalid email(s).')

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
        st.info('All emails are valid.')

else:
    st.info('Upload a CSV file above to begin.')
