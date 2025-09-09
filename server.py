''' Executing this function initiates the application of emotion detector to be executed
    over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    '''
    This fuction calls the emotion detector and returns the results
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Form emotions string without dominant string and set dominant emotion
    emotions_str = ", ".join(
        [f"'{k}': {v}" for k, v in response.items() if k != "dominant_emotion"]
    )
    dominant_emotion = response["dominant_emotion"]

    # Check if the dominant is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
