from flask import Flask, render_template, request, redirect
from time import localtime, strftime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    data_fruit = {
        'apple': request.form['apple'],
        'blackberry': request.form['blackberry'],
        'raspberry': request.form['raspberry'],
        'strawberry': request.form['strawberry'],
        'firstName': request.form['first_name'],
        'lastName': request.form['last_name'],
        'student_id': request.form['student_id']
        
    }
    order = int(request.form['apple'])+ int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['blackberry'])
    loctime =  strftime("%Y-%m-%d %H:%M %p", localtime())
    return render_template("checkout.html", data=data_fruit, order=order, loctime=loctime)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    