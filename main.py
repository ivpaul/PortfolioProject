from flask import Blueprint, render_template, send_from_directory
import os

main_bp = Blueprint(__name__, "main")

common = {
    'first_name': 'Ivan',
    'last_name': 'Paul',
    'alias': 'Becca\'s boy'
}
@main_bp.route("/")
def home():
    return render_template("home.html", common=common)

@main_bp.route('/about')
def resume():
    return render_template("about.html")

@main_bp.route('/projects')
def projects():
    return render_template("projects.html")

@main_bp.route('/blog')
def blog():
    return render_template("blog.html")

@main_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Route for serving static files
@main_bp.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

