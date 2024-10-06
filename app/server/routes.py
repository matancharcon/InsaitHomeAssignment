from flask import Blueprint, request, jsonify, render_template
from openai import OpenAI
import os
from .repositories import QuestionRepository
from dotenv import load_dotenv

load_dotenv()

main = Blueprint('main', __name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@main.route("/")
def index():
    return render_template("index.html")

@main.route('/ask', methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get('question')

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        answer = response.choices[0].message.content

        QuestionRepository.add_question(question, answer)

        return jsonify({'question': question, 'answer': answer}), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred. Please try again later.', 'details': str(e)}), 500
