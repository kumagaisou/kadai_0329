from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def top():
    return render_template('index.html')

@app.route('/maru')
def cir():
    return render_template('en.html')

@app.route('/batu', methods=['POST'])
    r=int(request.form.get['hankei'])
    p=3.14

    a = 2*r*p
    b = r**2*p

    return render_template('maru2.html', a = a, b = b)
    
if __name__ == '__main__':
    app.run(debug=True)