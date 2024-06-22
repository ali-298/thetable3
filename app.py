from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initial content
content = {
    "header": "الجدول الدراسي",
    "table": {
        "الأحد": ["الحصة 1", "الحصة 2", "الحصة 3", "الحصة 4", "الحصة 5", "الحصة 6", "الحصة 7", "الحصة 8"],
        "الإثنين": ["الحصة 1", "الحصة 2", "الحصة 3", "الحصة 4", "الحصة 5", "الحصة 6", "الحصة 7", "الحصة 8"],
        "الثلاثاء": ["الحصة 1", "الحصة 2", "الحصة 3", "الحصة 4", "الحصة 5", "الحصة 6", "الحصة 7", "الحصة 8"],
        "الأربعاء": ["الحصة 1", "الحصة 2", "الحصة 3", "الحصة 4", "الحصة 5", "الحصة 6", "الحصة 7", "الحصة 8"],
        "الخميس": ["الحصة 1", "الحصة 2", "الحصة 3", "الحصة 4", "الحصة 5", "الحصة 6", "الحصة 7", "الحصة 8"]
    },
    "footer": "أ.سلطان الوائلي"
}

@app.route('/')
def index():
    return render_template('index.html', content=content)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', content=content)

@app.route('/update', methods=['POST'])
def update_content():
    global content
    content['header'] = request.form['h1_content']
    day = request.form['day']
    for i in range(1, 9):
        class_name = request.form[f'class{i}']
        class_link = request.form[f'link{i}']
        content['table'][day][i-1] = {"name": class_name, "link": class_link}
    content['footer'] = request.form['footer']
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
