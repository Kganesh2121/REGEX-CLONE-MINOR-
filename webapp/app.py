from flask import Flask, render_template, request
import re

app = Flask(__name__)

def find_matches(regex_pattern, test_string):
    matches = re.findall(regex_pattern, test_string)
    return matches

def validate_email_in_string(test_string):
    email_matches = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', test_string)
    valid_emails = []
    for email in email_matches:
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            valid_emails.append(email)
    return valid_emails

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        regex_pattern = request.form['regex_pattern']
        test_string = request.form['test_string']

        # Find matches for the regular expression pattern in the test string
        matches = find_matches(regex_pattern, test_string)
        
        # Check if the entered email is valid
        email_matches = validate_email_in_string(test_string)

        # Validate email addresses and create a dictionary to hold email validation results
        email_validation_results = {}
        for email in email_matches:
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                email_validation_results[email] = True
            else:
                email_validation_results[email] = False

        return render_template('home.html', regex_pattern=regex_pattern, test_string=test_string, matches=matches, email_matches=email_matches, email_validation_results=email_validation_results)
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
