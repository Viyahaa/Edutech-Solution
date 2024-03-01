from flask import Flask, render_template, request

app = Flask(__name__)

# Mock data for courses and mentors
courses = [
    {"title": "Introduction to Programming", "description": "Learn the basics of programming languages like Python and Java.", "image": "programming.jpg"},
    {"title": "Financial Literacy", "description": "Gain knowledge about managing personal finances and investments.", "image": "finance.jpg"},
    # Add more courses as needed
]

mentors = [
    {"name": "Jane Doe", "expertise": "Software Development", "bio": "Experienced software engineer passionate about empowering women in tech.", "image": "jane.jpg"},
    {"name": "Alice Smith", "expertise": "Financial Advisor", "bio": "Certified financial planner dedicated to helping women achieve financial independence.", "image": "alice.jpg"},
    # Add more mentors as needed
]

# Routes for homepage and course pages
@app.route('/')
def index():
    return render_template('index.html', courses=courses, mentors=mentors)

@app.route('/course/<int:course_id>')
def course(course_id):
    course = courses[course_id]
    return render_template('course.html', course=course)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
