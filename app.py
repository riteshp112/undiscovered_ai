from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)
client = Client()

@app.route('/generate', methods=['POST'])
def generate_response():
    # Get the JSON data from the request
    data = request.get_json()

    # Check if 'prompt' is in the JSON data
    if 'prompt' not in data:
        return jsonify({"error": "No prompt provided"}), 400

    prompt = data['prompt']

    # Create the chat completion
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """
                You are an expert traveller and backpacker who has seen the world and know every destination's ins and outs.
            """},
            {"role": "user", "content": prompt}
        ],
        max_tokens=30000
    )

    # Get the response content
    response_content = chat_completion.choices[0].message.content or ""

    # Return the response as JSON
    return jsonify({"response": response_content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # This allows the app to be accessible on all interfaces
