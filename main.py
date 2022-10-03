
from __init__ import app  # Definitions initialization
from flask import render_template

def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

# @app.route('/stub/')  # connects /stub/ URL to stub() function
# def stub():
#     return render_template("stub.html")

# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
