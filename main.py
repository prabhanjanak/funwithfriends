import streamlit as st

# Set up the Streamlit app
st.title("Favorite Rapper Selector")

# Input for name
name = st.text_input("Enter your name:")

# Dropdown for favorite rapper selection
rapper = st.selectbox("Select your favorite rapper:", ["Rahul Dito", "All-ok"])

# Show submit button if "Rahul Dito" is selected
if rapper == "Rahul Dito":
    if st.button("Submit"):
        st.image("tarun.png")  # Display the photo from the given path
else:
    st.write("You have selected All-ok. No additional action required.")

# Display a message with the user's name
st.write(f"Hello, {name}!")
