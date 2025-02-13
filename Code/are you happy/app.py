from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def response():
    user_choice = request.form.get('choice')
    if user_choice == 'yes':
        return render_template('yes.html')
    else:
        return render_template('no.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
