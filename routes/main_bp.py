from flask import Blueprint, render_template

main_bp = Blueprint("main_bp", __name__)


@main_bp.get("/")
def main_screen():
    return render_template("main-screen.html")
