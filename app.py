from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landing-pages')
def landing_pages():
    return render_template('landing-pages.html')

@app.route('/about-me')
def about_me():
    return render_template('about-me.html')

@app.route('/tools')
def tools_used():
    return render_template('tools.html')

@app.route('/graphic-designs')
def graphic_designs():
    return render_template('graphic-designs.html')

@app.route('/workflows')
def workflows():
    return render_template('workflows.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/client-testimonials')
def testimonials():
    return render_template('testimonials.html')

if __name__ == '__main__':
    app.run(debug=True)