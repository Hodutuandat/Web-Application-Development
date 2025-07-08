from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def math():
    return render_template('math.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        number = float(request.form['number'])
        square = number ** 2
        return render_template('Result.html', message=f"The square of {number} is {square}.")
    except ValueError:
        message = "Please enter a valid number."
    
if __name__ == '__main__':
    app.run(debug=True)    