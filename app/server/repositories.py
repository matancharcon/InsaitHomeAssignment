from .models import Question
from . import db

class QuestionRepository:
    def add_question(question, answer):
        new_question = Question(question=question, answer=answer)
        db.session.add(new_question)
        db.session.commit()

    def get_all_questions():
        return Question.query.all()

    def get_question_by_id(question_id):
        return Question.query.get(question_id)

    def delete_question(question_id):
        question = Question.query.get(question_id)
        if question:
            db.session.delete(question)
            db.session.commit()

    def update_question(question_id, updated_answer):
        question = Question.query.get(question_id)
        if question:
            question.answer = updated_answer
            db.session.commit()
