from flask import Flask, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)

model = GPT4All(model_name='orca-mini-3b.ggmlv3.q4_0.bin')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        prompt = request.json.get('prompt')
        temp = request.json.get('temp', 0)
        with model.chat_session():
            response = model.generate(prompt=prompt, temp=temp)
            return jsonify({
                'response': response,
                'chat_session': model.current_chat_session
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
