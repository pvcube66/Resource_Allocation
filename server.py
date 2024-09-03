# from flask import Flask, request, jsonify,render_template
# from g4f.client import Client
# from g4f.Provider import You

# app = Flask(__name__)

# # Initialize the client object
# client = Client()

# # Function to get a response from the GPT-3.5-turbo model
# def get_response(user_input):
#     chat_completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": user_input}],
#     )
#     # Access the content directly from the message object
#     return chat_completion.choices[0].message.content

# # Backend API endpoint to handle chat messages
# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json['message']
#     response = get_response(user_input)
#     return jsonify({'reply': response})

# # Serve the HTML file
# @app.route('/')
# def index():
#     return render_template("index.html")

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)