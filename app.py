"""
Portfolio Web Application (Python + Flask)
==========================================
Main application server for the personal portfolio website.
Runs a local development server, serves dynamic templates, and handles
interactive API endpoints such as contact form submissions and project details.
"""

import os
import sys
import json
import socket
import logging
import webbrowser
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory

# Import portfolio data
import data

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger("PortfolioApp")

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)
app.config['SECRET_KEY'] = 'dark-purple-portfolio-secret-key-2026'

# Submissions log file
MESSAGES_FILE = os.path.join(os.path.dirname(__file__), "contact_messages.json")


def save_contact_message(message_data):
    """Save contact form messages to a local JSON file."""
    messages = []
    if os.path.exists(MESSAGES_FILE):
        try:
            with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
                messages = json.load(f)
        except Exception as e:
            logger.warning(f"Could not read existing messages: {e}")
            messages = []

    message_data["timestamp"] = datetime.now().isoformat()
    messages.append(message_data)

    try:
        with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=2)
        logger.info(f"Saved message from {message_data.get('email')}")
    except Exception as e:
        logger.error(f"Failed to write message to file: {e}")


@app.context_processor
def inject_global_data():
    """Inject common portfolio data into all templates."""
    return {
        "profile": data.PROFILE,
        "current_year": datetime.now().year
    }


@app.route("/")
def index():
    """Render the main portfolio page."""
    return render_template(
        "index.html",
        profile=data.PROFILE,
        about=data.ABOUT,
        skill_categories=data.SKILL_CATEGORIES,
        tech_tags=data.TECH_TAGS,
        projects=data.PROJECTS,
        education=data.EDUCATION,
        experience=data.EXPERIENCE,
        contact_info=data.CONTACT_INFO,
        is_static=False
    )


@app.route("/resume")
def download_resume():
    """Download the PDF resume."""
    assets_dir = os.path.join(os.path.dirname(__file__), "static", "assets")
    filename = data.PROFILE.get("resume_filename", "Priyanshu_Kumar_Srivastav_Resume.pdf")
    return send_from_directory(assets_dir, filename, as_attachment=True)


@app.route("/api/projects")
def get_projects():
    """Return projects as JSON."""
    category = request.args.get("category")
    if category and category != "all":
        filtered = [p for p in data.PROJECTS if p.get("category") == category]
        return jsonify({"projects": filtered, "total": len(filtered)})
    return jsonify({"projects": data.PROJECTS, "total": len(data.PROJECTS)})


@app.route("/api/projects/<project_id>")
def get_project_detail(project_id):
    """Return single project details by ID."""
    for p in data.PROJECTS:
        if p["id"] == project_id:
            return jsonify({"success": True, "project": p})
    return jsonify({"success": False, "error": "Project not found"}), 404


@app.route("/api/contact", methods=["POST"])
def submit_contact():
    """Handle interactive contact form submissions."""
    data_in = request.get_json(silent=True) or request.form.to_dict()

    name = data_in.get("name", "").strip()
    email = data_in.get("email", "").strip()
    subject = data_in.get("subject", "").strip() or "General Inquiry"
    message = data_in.get("message", "").strip()

    # Basic server-side validation
    if not name or not email or not message:
        return jsonify({
            "success": False,
            "error": "Please provide your name, a valid email address, and a message."
        }), 400

    if "@" not in email or "." not in email:
        return jsonify({
            "success": False,
            "error": "Please provide a valid email address."
        }), 400

    # Save to storage
    record = {
        "name": name,
        "email": email,
        "subject": subject,
        "message": message
    }
    save_contact_message(record)

    return jsonify({
        "success": True,
        "message": f"Thank you, {name}! Your message has been received. I'll get back to you within 24 hours.",
        "received_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def find_free_port(start_port=5000, max_tries=20):
    """Find an available TCP port starting from start_port."""
    for port in range(start_port, start_port + max_tries):
        with socket.socket(socket.AF_SOCKET if hasattr(socket, 'AF_SOCKET') else socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                return port
            except OSError:
                continue
    return start_port


def print_banner(port):
    """Print a sleek ASCII terminal banner."""
    banner = f"""
========================================================================
   ____  __  __ _____ _   _  ___  _   _   ____   ___  ____ _____ 
  |  _ \\ \\ \\/ /|_   _| | | |/ _ \\| \\ | | |  _ \\ / _ \\|  _ \\_   _|
  | |_) | \\  /   | | | |_| | | | |  \\| | | |_) | | | | |_) || |  
  |  __/  /  \\   | | |  _  | |_| | |\\  | |  __/| |_| |  _ < | |  
  |_|    /_/\\_\\  |_| |_| |_|\\___/|_| \\_| |_|    \\___/|_| \\_\\|_|  
========================================================================
 >> Luxury Black & Purple Theme Loaded
 >> Server running at: http://127.0.0.1:{port}
 >> API Endpoints active: /api/projects, /api/contact
 >> Press Ctrl+C in this terminal to stop the server
========================================================================
"""
    print(banner)


if __name__ == "__main__":
    port = find_free_port(5000)
    print_banner(port)
    url = f"http://127.0.0.1:{port}"

    # Auto-open browser unless flag --no-browser is passed
    if "--no-browser" not in sys.argv:
        try:
            webbrowser.open_new_tab(url)
        except Exception as e:
            logger.warning(f"Could not open browser automatically: {e}")

    app.run(host="127.0.0.1", port=port, debug=False)
