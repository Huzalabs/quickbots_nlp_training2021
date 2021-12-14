
# Written in Training NLP
#________________________
from flask_cors import CORS
from flask import Flask, request, jsonify
from qna import QuestionAnswer
from processing.nida import nida_context_answers
from processing.mtn import mtn_context_answers
from processing.visitrwanda import visitrwanda_context_answers

# create flask app
app = Flask(__name__)
CORS(app)

context, answers = nida_context_answers()
expanded_context = context # [i+","+j for i,j in zip(context, answers)]
question_answer = QuestionAnswer(context=expanded_context, answers=answers)

    
@app.route('/nida', methods=['GET'])
def main(): 
    question = request.args.get('question')   
    return {"answer":question_answer.get_answer_percontext([question])}

if __name__ == '__main__':
   app.run()
