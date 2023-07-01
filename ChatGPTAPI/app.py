from flask import Flask, render_template, request
import openai
app = Flask(__name__)
# Set up OpenAI API credentials
openai.api_key = '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'
# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")
# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    augmented_message = f"{message} - recommend 6 jobs for these skills and give only 1 line description for each in a new line"
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": augmented_message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message
    else :
        return 'Failed to Generate response!'
if __name__=='__main__':
    app.run()