import streamlit as st
#from service import file_uploader
import os
import sys
import json
sys.path.append(os.path.abspath('...')) #Your path

from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
from tasks.task_5.task_5 import ChromaCollectionCreator
from tasks.task_8.task_8 import QuizGenerator
from tasks.task_9.task_9 import QuizManager

def config():
    """
    Google Cloud embedding configuration
    Parameters:
    - model_name: A string for specified model name.
    - project: A string containing user's Google Cloud Project ID
    - location: A string containg user's Google Region. See https://cloud.google.com/compute/docs/regions-zones.
    """

    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "Google Console Project ID", #YOUR PROJECT ID HERE
        "location": "us-east1"
    }

    return embed_config

def main():

    embed_config = config()
    
    # Add Session State
    if 'question_bank' not in st.session_state or len(st.session_state['question_bank']) == 0:
        
        # Initialize the question bank list in st.session_state
        st.session_state["question_bank"] = []

        screen = st.empty()
        with screen.container():
            st.header("Quiz Builder")
            
            # Screen 1: Create a new st.form flow control for Data Ingestion
            with st.form("Load Data to Chroma"):
                st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
                
                processor = DocumentProcessor()
                processor.ingest_documents()
            
                embed_client = EmbeddingClient(**embed_config) 
            
                chroma_creator = ChromaCollectionCreator(processor, embed_client)
                
                # Set topic input and number of questions
                topic_input = st.text_input("Topic for Generative Quiz", placeholder="Enter the topic of the document")
                questions = st.slider("Number of Questions", min_value=1, max_value=10, value=1)
                    
                submitted = st.form_submit_button("Submit")
                
                if submitted:
                    chroma_creator.create_chroma_collection()
                        
                    if len(processor.pages) > 0:
                        st.write(f"Generating {questions} questions for topic: {topic_input}")
                    
                    # Initialize a QuizGenerator class using the topic, number of questrions, and the chroma collection
                    generator = QuizGenerator(topic_input, questions, chroma_creator) 
                    question_bank = generator.generate_quiz()

                    # Initialize the question bank list in st.session_state
                    if len(st.session_state['question_bank']) == 0:
                        st.session_state["question_bank"] = question_bank

                    # Set a display_quiz flag in st.session_state to True
                    if "display_quiz" not in st.session_state:
                        st.session_state["display_quiz"] = True

                    # Set the question_index to 0 in st.session_state
                    if "question_index" not in st.session_state:
                        st.session_state["question_index"] = 0

                    st.rerun()

    elif st.session_state["display_quiz"]:
        st.empty()

        #Screen 2
        with st.container():
            st.header("Generated Quiz Question: ")
            quiz_manager = QuizManager(st.session_state["question_bank"])
            
            # Format the question and display it
            with st.form("MCQ"):
                
                # Set index_question using the Quiz Manager method get_question_at_index passing the st.session_state["question_index"]
                index_question = quiz_manager.get_question_at_index(st.session_state["question_index"])
                
                # Unpack choices for radio button
                choices = []
                for choice in index_question['choices']:
                    key = choice.get('key')
                    value = choice.get('value')
                    choices.append(f"{key}) {value}")
                
                # Display the Question
                st.write(f"{st.session_state['question_index'] + 1}. {index_question['question']}")
                answer = st.radio(
                    "Choose an answer",
                    choices,
                    index = None
                )
                
                answer_choice = st.form_submit_button("Submit")
                
                # Use the example below to navigate to the next and previous questions
                # Here we use the next_question_index method from our quiz_manager class
                st.form_submit_button("Next Question", on_click=lambda: quiz_manager.next_question_index(direction=1))
                st.form_submit_button("Previous Question", on_click=lambda: quiz_manager.next_question_index(direction= -1))
                
                if answer_choice and answer is not None:
                    correct_answer_key = index_question['answer']
                    if answer.startswith(correct_answer_key):
                        st.success("Correct!")
                    else:
                        st.error("Incorrect!")
                    st.write(f"Explanation: {index_question['explanation']}")

if __name__ == "__main__":
    main()