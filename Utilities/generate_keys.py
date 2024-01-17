import pickle
from pathlib import Path 

import streamlit_authenticator as stauth 

#Assigning usernames to the Users
names = ["Clark Kent", "Bruce Wayne"]
unames = ["superman","batman"]

#assigning passwords to the users respectively
passw = ["XXX","XXX"]

#genrating hashed passwords for safety
hashed_passwords = stauth.Hasher(passw).generate()

#creating files for storing user records.
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)


