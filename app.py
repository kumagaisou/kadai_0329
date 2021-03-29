from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def top():
    return render_template('index.html')

@app.route('/kyuryo')
def kyuryo():
    return render_template('kyuryo.html')

@app.route('/salary', methods=['POST'])
def salary():
    s = request.form.get('sal')
    t = request.form.get('time')
    n = int(s) * int(t)
    return render_template('salary.html', n = n)

if __name__ == '__main__':
    app.run(debug=True)