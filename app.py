import streamlit as st
import random

# Set up the title and description
st.title('Number Guessing Game')
st.write('Welcome to the number guessing game! I have picked a number between 1 and 100, and you need to guess it.')

# Generate a random number
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# Take user input
guess = st.number_input('Enter your guess:', min_value=1, max_value=100, step=1)

# Button to check the guess
if st.button('Submit Guess'):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.number = random.randint(1, 100)  # Reset the game with a new number
        st.session_state.attempts = 0  # Reset attempts
