from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
notes = []
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        note = request.form["note"]
        notes.append(note)  
        return redirect(url_for('index')) 
    return render_template("home.html", notes=notes)

@app.route("/delete/<int:note_index>", methods=['POST'])
def delete_note(note_index):
    notes.remove(notes[note_index])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
