from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add-form")
def get_student_add_form():
    """Show form for adding a student."""

    return render_template("new_student.html")    

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first = request.form['firstname']  
    last = request.form['lastname']
    github = request.form['github']  
    hackbright.make_new_student(first, last, github)

    return render_template("new_student.html", 
                            first=first,
                            last=last,
                            github=github)

@app.route("/student_grade_title")
def student_grade_title():
    """Lists project title with grade"""

    title = request.args.get('title', 'blockly')
    # student_github, grade, title < parts from unpacking hackbright.get_grades_by_title
    results = hackbright.get_grades_by_title(title)

    #do not unpack the results from hackbright.get_grades_by_title here
    #save tuples as a variable (ex: 'results') to loop through in student_info.html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
