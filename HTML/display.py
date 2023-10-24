from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user information (for demonstration)
user_info = {
    'name': "John",
    'password': "newpassword"
}

@app.route('/')
def finance_application():
    # Pass the user information to the finance_application template
    return render_template('finance_application.html', user_info=user_info)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        new_name = request.form['new_name']
        new_password = request.form['new_password']

        # Update user information
        user_info['name'] = new_name
        user_info['password'] = new_password

        return redirect(url_for('finance_application'))

    return render_template('edit_profile.html')

@app.route('/settings')
def settings():
    # Add logic to handle settings page
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
