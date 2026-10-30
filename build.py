"""
Static Site Generator (Python)
==============================
Builds a standalone static HTML version of the portfolio using Jinja2 and data.py.
This allows the portfolio to be deployed on GitHub Pages, Netlify, Vercel,
or opened directly as a file in any browser without needing a running server.
"""

import os
import shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

import data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")
OUTPUT_FILE = os.path.join(BASE_DIR, "index.html")


def build_static_site():
    print("[*] Generating static portfolio website...")

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template("index.html")

    rendered_html = template.render(
        profile=data.PROFILE,
        about=data.ABOUT,
        skill_categories=data.SKILL_CATEGORIES,
        tech_tags=data.TECH_TAGS,
        projects=data.PROJECTS,
        education=data.EDUCATION,
        experience=data.EXPERIENCE,
        contact_info=data.CONTACT_INFO,
        current_year=datetime.now().year,
        is_static=True
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print(f"[+] Static HTML generated successfully at: {OUTPUT_FILE}")
    print("[+] Assets are linked to ./static/css, ./static/js, and ./static/assets")


if __name__ == "__main__":
    build_static_site()
