from flask import Flask, render_template, request
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os
from flask import jsonify

from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
HF_TOKEN= os.getenv('HF_TOKEN')

app = Flask(__name__)

# promp for llm model 

# load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# load FAISS + data
index = pickle.load(open("faiss_index.pkl", "rb"))
chunks = pickle.load(open("chunks.pkl", "rb"))


def get_relevnet_text(question):
    q_vec = model.encode([question])

    D, I = index.search(q_vec, k=10)

    relevent_text = "\n".join([chunks[i] for i in I[0]])

    return relevent_text


def get_answer(question):

    relevent_text= get_relevnet_text(question)

    prompt = PromptTemplate(
    template=f"you are answering to a computer engineer student, generate a response from these informations  at the begging of the answer write this is your answer: {relevent_text}",
    input_variables=['relevent_text']
    )

    llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    temperature=0,
    huggingfacehub_api_token=HF_TOKEN,
    task="text-generation", 
    )

    model = ChatHuggingFace(llm=llm)

    parser = StrOutputParser()
    chain = prompt | model | parser
    answer = chain.invoke({'relevent_text' : relevent_text})
    return answer



@app.route("/ask", methods=["GET", "POST"])
def ask():
    answer = ""
    if request.method == "POST":
        data = request.get_json()
        question = data["question"]
        answer = get_answer(question)
    return jsonify({"answer": answer})




@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)