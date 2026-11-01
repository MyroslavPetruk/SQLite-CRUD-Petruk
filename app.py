from flask import Flask, render_template, request, redirect, url_for
import database_connector as db

app = Flask(__name__)

# Ініціалізація бази даних при першому запуску
db.create_db_table()

@app.route('/')
def index():
    students = db.get_all_items()
    return render_template('index.html', students=students)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        student_group = request.form['student_group']
        gpa = float(request.form['gpa'])
        
        db.insert_item(first_name, last_name, student_group, gpa)
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    student = db.get_item_by_id(id)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        student_group = request.form['student_group']
        gpa = float(request.form['gpa'])
        
        db.update_item(id, first_name, last_name, student_group, gpa)
        return redirect(url_for('index'))
    return render_template('update.html', student=student)

@app.route('/delete/<int:id>')
def delete(id):
    db.delete_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)