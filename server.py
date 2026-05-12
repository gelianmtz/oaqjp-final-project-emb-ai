from EmotionDetection.emotion_detection import emotion_detection
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection(text_to_analyze)
    return f'From the given statement, the system response is {response}'

@app.route('/')
def render_index_page():
    return render_template('index.html')

app.run()
