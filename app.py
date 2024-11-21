from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def resume():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        education = request.form['education']
        experience = request.form['experience']
        skills = request.form['skills']
        projects = request.form['projects']
        return render_template('resume.html', 
                               name=name, dob=dob, email=email, phone=phone, 
                               address=address, education=education, 
                               experience=experience, skills=skills, 
                               projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
