import streamlit as st

st.title("Password Validtion and Encryption")
password=st.text_input("Enter the password",type="password")

if st.button("Validate and Encrypt"):
    if password=="":
        st.warning("Please Enter Password")
    elif len(password)<=8:
        st.error("Password must be atleast 8 char")
    elif password[4] not in "1234":
        st.error("The fifth char must be in 1-5 range")
    elif not password.isalnum():
        st.error("Must contain alphabet and numeric")

    else:
        has_upper=any(i.isupper() for i in password)
        has_lower=any(i.islower() for i in password)

        if not (has_upper and has_lower):
            st.error("Must contain one upper and one lower")
        else: 
            encrypted_password=password.replace("A","@")
            encrypted_password=password.replace("b","1")
            encrypted_password=password.replace("a","B")

            st.success("Password is valid")
            st.write("The Encrypted ")
            st.code(encrypted_password)

