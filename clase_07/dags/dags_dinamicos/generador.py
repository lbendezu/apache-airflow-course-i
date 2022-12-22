#jinja2 es una libreria externa de python, para instalarla correr ---> "pip install jinja2"
from jinja2 import Environment, FileSystemLoader
#yaml es una clase de la libreria externa PyYaml de python, para instalarla correr ---> "pip install pyyaml"
import yaml
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(file_dir))
template = env.get_template('template_dag.j2')

for filename in os.listdir(file_dir):
    if filename.endswith(".yaml"):
        with open(f"{file_dir}/{filename}", "r") as configfile:
            config = yaml.safe_load(configfile)
            with open(f"dags/get_info_{config['dag_id']}.py", "w") as f:
                f.write(template.render(config))