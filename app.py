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


@app.route('/maru')
def cir():
    return render_template('en.html')

@app.route('/batu', methods=['POST'])
    r=int(request.form.get('hankei'))
    p=3.14

    a = 2*r*p
    b = r**2*p

    return render_template('maru2.html', a = a, b = b)
    

if __name__ == '__main__':
    app.run(debug=True)