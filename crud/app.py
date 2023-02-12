from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route("/display",methods=['POST'])
def disp():
    if request.method =='POST':
        n=request.form.get('user_name')
        m=request.form.get('user_mail')
        p=request.form.get('user_pass')
        return render_template('display.html',name=n,mail=m,passw=p)


if __name__=="__main__":
    app.run(debug=True)