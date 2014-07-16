import uuid
import json
import os

######### Default Values ###########

# Define default widget size
DEF_HEIGHT = 700
DEF_WIDTH = 1160

# Default network
DEF_NODES = [
    { 'data': { 'id': 'Network Data' } },
    { 'data': { 'id': 'Empty' } }
]

DEF_EDGES = [
    { 'data': { 'id': 'is', 'source': 'Network Data', 'target': 'Empty' } }
]

DEF_LAYOUT = 'preset'

HTML_TEMPLATE_FILE = 'template.html'


def render(network, style, layout_algorithm=DEF_LAYOUT, height=DEF_HEIGHT, width=DEF_WIDTH):
    from jinja2 import Template
    from IPython.core.display import display, HTML


    if network==None:
        nodes = DEF_NODES
        edges = DEF_EDGES
    else:
        nodes = network['elements']['nodes']
        edges = network['elements']['edges']


    path = os.path.abspath(os.path.dirname(__file__)) + '/' + HTML_TEMPLATE_FILE
    template = Template(open(path).read())
    cyjs_widget = template.render(nodes = json.dumps(nodes), edges = json.dumps(edges), 
        uuid="cy" + str(uuid.uuid4()), widget_width = str(width), widget_height = str(height), 
        layout=layout_algorithm, style_json=json.dumps(style))

    return display(HTML(cyjs_widget))