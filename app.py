from flask import Flask, render_template
from markdown_it import MarkdownIt
from livereload import Server
import os


app = Flask(__name__)

@app.route(rule='/')
def index():
    return render_template(template_name_or_list='index.html', site_data=site_data)

def get_site_data():
    site_layout = {'Home': ['Welcome', 'CV'],
                   'Data Analysis': ['ML Football Analysis', 'Covid-19 Time Series', 'Power BI Analysis', 'Excel Analysis', 'Tableau Analysis', 'SQL Analysis'],
                   'Software Automation': ['Finance Data Automation'],
                   'Game Development': ['Step I Must', 'Maze Generator and Solver', 'Snake', 'Particle Test Chamber'],
                   'Web Apps': ['Portfolio', 'Task Manager'],
                   'Image Maniplulation': ['Brush Paintify', 'Seam Carving', 'Kernels and Convolutions']}
    projects_path = os.path.join(os.path.abspath(os.curdir), 'static', 'projects')
    md = MarkdownIt()
    for project_topic, project_names in site_layout.items():
        projects = {}
        for project_name in project_names:
            project_path = os.path.join(projects_path, project_name)
            if project_name in os.listdir(path=projects_path) and os.path.isdir(project_path):
                if 'README.md' in os.listdir(path=project_path):
                    with open(os.path.join(project_path, 'README.md'), 'r') as f:
                        if project_name == 'CV':
                            projects[project_name] = f.read()
                        else:
                            projects[project_name] = md.render(f.read())
                else:
                    print(f"Warning: README.md file not found for '{project_name}'")
            else:
                print(f"Warning: Project folder not found for '{project_name}'")
        site_layout[project_topic] = projects
    return site_layout

site_data = get_site_data()

if __name__ == '__main__':
    app.debug = True
    host, port = '127.0.0.1', 5000
    app.run(host=host, port=port)
    # server = Server(app.wsgi_app)
    # server.serve(host=host, port=port)
