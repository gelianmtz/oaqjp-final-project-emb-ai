import json
import requests

def emotion_detection(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = {'raw_document': {'text': text_to_analyze}}
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    response = requests.post(url, json=input_json, headers=headers)

    result = json.loads(response.text)
    emotions = result['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions
