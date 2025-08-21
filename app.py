from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')
@app.route('/submit',methods=['POST'])
def submit():
    un=request.form['username']
    return render_template('submit.html',name=un)

if __name__=='__main__':
    app.run(debug=True)