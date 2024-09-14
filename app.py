from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/StringRespnse')
def StringRespnse():
    return "This is my 1st project in flask"

@FAI.route('/str2')
def str2():
    return "2nd Response"

@FAI.route('/wish')
def wish():
    return render_template('wish.html')

@FAI.route('/greet')
def greet():
    return render_template('greet.html')


#url navigation...........
@FAI.route('/staticfiles')
def static_files():
    return render_template('staticfiles.html')

if __name__=='__main__':
    FAI.run(debug=True)
