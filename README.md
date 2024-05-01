# Quiz-Generator
Generate multiple-choice quizzes from the content of pdf file(s) through a web application developed with Streamlit, Langchain, ChromaDB, and Google Cloud Platform. 

When we learn something new, how do we not forget but instead retain that information? Testing with multiple-choice questions can be an effective study strategy for recall and long-term retention (Bae et al., 2019). However, acquiring the necessary practice quizzes may not be readily accessible. The following repository includes the code to build a streamlit application that can process multiple pdfs, such as journal articles and lecture notes, and generate a quiz within minutes.

## Set-Up
### Google Cloud
1) Create a Google Cloud Platform account.
2) Create new project. The associated project ID number will be used to build the application.
3) Enable Vertex AI API.
4) Create service account and download corresponding service account key to be saved with directory which can be add to .gitignore file.

### Running in VS Code terminal
1) Clone GitHub Repository
   ```python 
   git clone https://github.com/remomcc/Quiz-Generator.git
   ```
2) Create virtual environment
   ```python
   python -m venv env
   ```
3) Activate virtual environment
   ```python
   source env/bin/activate
   ```
4) Install requirements
   ```python
   pip install -r requirements.txt
   ```
5) Make sure service account key (named as 'authentication.json' in this case) is in the same directory as the cloned respository.
   ```python
   export GOOGLE_APPLICATION_CREDENTIALS='authentication.json'
   ```   
6) Run application
   ```python
   streamlit run main.py
   ```
## Web quiz application overview
Ingesting pdf(s) with LangChain --> Vertex AI text embeddings --> Persistent ChromaDB --> Gemini Pro Large Language Model --> Streamlit session states --> Generated Quiz

## Loom presentation
https://www.loom.com/share/33eb7b4804354b59b39947a851f54598?sid=0e74616d-8681-464e-8db2-4f0b280e3ce0

https://pitch.com/v/quiz-generator-mp2t7g

## Time allocated for this project
40+ hours.  This was my first project using the aforementioned technologies. I invested one week in reading the respective documentation, watching videos and fixing bugs (specifically the class developed in task 5 and optimization in task 10); putting together the presentation took longer than fixing the technical bugs.  

## Special thanks 
Thank you to Radical AI's ReX, Dmitri, Mikhail, Neil, and Nirbhay.

## References
Bae, C. L., Therriault, D. J., & Redifer, J. L. (2019). Investigating the testing effect: Retrieval as a characteristic of
effective study strategies.  Learning and Instruction, 60, 206–214. https://doi.org/10.1016/j.learninstruc.2017.12.008

Documentation. (n.d.). Google Cloud. https://cloud.google.com/docs

langchain 0.1.12 — 🦜🔗 LangChain 0.1.12. (n.d.). Api.python.langchain.com. 
https://api.python.langchain.com/en/latest/langchain_api_reference.html

‌Streamlit. (n.d.). Streamlit Docs. Docs.streamlit.io. https://docs.streamlit.io/
