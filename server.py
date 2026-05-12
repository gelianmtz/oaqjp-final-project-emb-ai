"""Flask server for emotion detection application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detection

app = Flask(__name__)


@app.route('/emotionDetector')
def emotion_detector():
    """Analyze text and return detected emotions."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'

    return f'From the given statement, the system response is {response}'


@app.route('/')
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')


app.run()
