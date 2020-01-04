from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', mode='a') as database:
        database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', mode='a', newline='\n') as database:
        csvwriter = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email, subject, message])

@app.route('/submit-page', methods=['POST'])
def submit_msg():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return render_template('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong, Try again'

# @app.route('/about.html')
# def about_page():
#     return render_template('about.html')

# @app.route('/components.html')
# def components_page():
#     return render_template('components.html')

# @app.route('/work.html')
# def work_page():
#     return render_template('work.html')

# @app.route('/contact.html')
# def contact_page():
#     return render_template('contact.html')