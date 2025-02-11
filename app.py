import streamlit as st
import nltk
from transformers import pipeline
# from nltk.corpus import stopwordsfrom
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation", model="distilgpt2")


# def healthcare_chatbot(user_input):
#     if "symptom" in user_input:
#         return "please consult Doctor for accurate advice"
#     elif "appointment" in user_input:
#         return "would you like to schedule appointment with the Doctor?"
#     elif "medication" in user_input:
#         return "It is important to take prescribed medicines regularly. If you have concerns, consult you doctor."
#     else:
#         response = chatbot(user_input,max_length = 500,num_return_sequences=1)
#         return response[0]['generated_text']



        
# def main():
#     st.title("Healthcare Assistant Chatbot")
#     user_input = st.text_input("How can I Assist you today?")
#     if st.button("Submit"):
#         if user_input:
#             st.write("User:",user_input)
#             with st.spinner("Processing your query, please wait..."):
#                 response = healthcare_chatbot(user_input)
           
#             st.write=("Healthcare Assistant:", response)
#             print(response)

#         else:
#             st.write("Please enter a message to get response.")

# main()

# import streamlit as st

# def healthcare_chatbot(user_input):
#     # Placeholder function for the chatbot response
#     return "This is a sample response."

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "would you like to schedule appointment with the Doctor?"
    elif "medication" in user_input:
        return "It is important to take prescribed medicines regularly. If you have concerns, consult you doctor."
    else:
        response = chatbot(user_input,max_length = 500,num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            
            st.write("Healthcare Assistant:", response)
            print(response)

        else:
            st.write("Please enter a message to get a response.")

if __name__ == "__main__":
    main()


# chatgpt code for ai chatbox//
    

# import streamlit as st
# from transformers import pipeline

# # Load AI Model
# chatbot = pipeline("text-generation", model="distilgpt2")

# def healthcare_chatbot(user_input):
#     """Processes user input and returns chatbot response."""
#     if "symptom" in user_input.lower():
#         return "Please consult a doctor for accurate advice."
#     elif "appointment" in user_input.lower():
#         return "Would you like to schedule an appointment with the doctor?"
#     elif "medication" in user_input.lower():
#         return "It is important to take prescribed medicines regularly. If you have concerns, consult your doctor."
#     else:
#         response = chatbot(user_input, max_length=100, num_return_sequences=1)
#         return response[0]['generated_text']

# def main():
#     """Streamlit UI for the chatbot."""
#     st.title("Healthcare Assistant Chatbot")
    
#     user_input = st.text_input("How can I assist you today?")

#     if st.button("Submit"):
#         if user_input.strip():
#             st.write("**User:**", user_input)
#             with st.spinner("Processing your query, please wait..."):
#                 response = healthcare_chatbot(user_input)
#             st.write("**Healthcare Assistant:**", response)
#         else:
#             st.warning("Please enter a message to get a response.")

# if __name__ == "__main__":
#     main()


# //Deepseek code for ai chatbox//
# import streamlit as st
# from transformers import pipeline

# # Load the chatbot model
# chatbot = pipeline("text-generation", model="distilgpt2")

# # Define the healthcare chatbot logic
# def healthcare_chatbot(user_input):
#     if "symptom" in user_input.lower():
#         return "Please consult a doctor for accurate advice."
#     elif "appointment" in user_input.lower():
#         return "Would you like to schedule an appointment with the doctor?"
#     elif "medication" in user_input.lower():
#         return "It is important to take prescribed medicines regularly. If you have concerns, consult your doctor."
#     else:
#         # Generate a response using the chatbot model
#         response = chatbot(user_input, max_length=50, num_return_sequences=1)
#         return response[0]['generated_text']

# # Main function to run the Streamlit app
# def main():
#     st.title("Healthcare Assistant Chatbot")
#     user_input = st.text_input("How can I assist you today?")
    
#     if st.button("Submit"):
#         if user_input:
#             st.write("User:", user_input)
#             with st.spinner("Processing your query, please wait..."):
#                 response = healthcare_chatbot(user_input)
#             st.write("Healthcare Assistant:", response)
#         else:
#             st.write("Please enter a message to get a response.")

# # Run the app
# if __name__ == "__main__":
#     main()