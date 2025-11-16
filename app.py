from flask import Flask, render_template, url_for
from markdown_it import MarkdownIt
import os


def get_projects():
    project_order = ['Welcome', 'CV', 'ML Football Analysis', 'Finance Data Automation', 'Step I Must', 'Covid-19 Time Series', 'Image Paint']
    projects = {}
    md = MarkdownIt()
    projects_path = os.path.join(os.path.abspath(os.curdir), 'static', 'projects')
    for project_name in project_order:
        project_path = os.path.join(projects_path, project_name)
        if project_name in os.listdir(path=projects_path) and os.path.isdir(project_path):
            if 'README.md' in os.listdir(path=project_path):
                with open(os.path.join(project_path, 'README.md'), 'r') as f:
                    if project_name != 'CV':
                        projects[project_name] = md.render(f.read())
                    else:
                        projects[project_name] = f.read()
            else:
                print(f"README.md file not found for '{project_name}'")
        else:
            print(f"Project folder not found for '{project_name}'")
    return projects

app = Flask(__name__)
projects_data = get_projects()

@app.route(rule='/')
def index():
    return render_template(template_name_or_list='index.html', projects_data=projects_data)

if __name__ == '__main__':
    app.run(debug=True)

# add images to finance automation, redacted screenshots of folder/ excel files?
# finish demo for step i must
# add more pictures (larger brush strokes) to image paint
# add more projects

# group tabs by topic/ theme, have group for games, data analysis, automation, image
