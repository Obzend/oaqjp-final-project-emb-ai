import requests
import json


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    print(formatted_response)

    if response.status_code == 200:
        emotion = formatted_response["emotionPredictions"][0]["emotion"]

        for i in emotion:
            if emotion[i] == max(emotion.values()):
                dominant = i

        anger = (emotion["anger"],)
        disgust = (emotion["disgust"],)
        fear = (emotion["fear"],)
        joy = (emotion["joy"],)
        sadness = (emotion["sadness"],)
        dominant_emotion = dominant

    if response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }


emotion_detector("I hate working long hours")
