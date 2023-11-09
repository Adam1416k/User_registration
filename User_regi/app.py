from flask import Flask, request, render_template, redirect, url_for, flash
import csv

app = Flask(__name__)
app.secret_key = 'en_riktigt_säker_nyckel'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']  # Igen, kom ihåg att aldrig spara lösenord i klartext i en riktig applikation!

        # Kontrollera om användaren redan finns
        user_exists = False
        with open('users.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and (username == row[0] or email == row[1]):
                    user_exists = True
                    break

        if user_exists:
            flash(f"Användaren {username} eller e-postadressen {email} är redan registrerad.")
        else:
            # Om användaren inte finns, registrera den
            with open('users.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, email, password])
            flash(f"Användare {username} har registrerats!")

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)