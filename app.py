from flask import Flask, render_template, request, jsonify
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load FAQ data
with open("faq.json", "r") as file:
    faqs = json.load(file)

questions = [faq["question"] for faq in faqs]
answers = [faq["answer"] for faq in faqs]

# Load Deep Learning model (BERT-based)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert questions into embeddings (DL step)
question_embeddings = model.encode(questions)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    # Convert user input into embedding
    user_embedding = model.encode([user_message])

    # Compute similarity
    similarity = cosine_similarity(user_embedding, question_embeddings)

    best_match_index = similarity.argmax()
    score = similarity[0][best_match_index]

    if score > 0.5:
        response = answers[best_match_index]
    else:
        response = "Sorry, I don't understand your question."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)