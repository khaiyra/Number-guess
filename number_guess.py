#import llibraries
import streamlit as st
import random

#set title
st.title("First app test with Streamlit")
"""
#### _Khaiyra
"""
#set header
st.header('*Can you guess the number between 0-20?*')

answer = random.randint(0,20)
guess = st.number_input('Insert a guess number')
guess = int(guess)
st.write('Your guess is ', guess)

if guess == answer:
    result = st.write('Your guess matched')
elif guess < answer:
    result = st.write('Oops! your guess was too low')
elif guess > answer:
    result = st.write('Oops! your guess was too high')
    
st.write('The random number is :', answer)