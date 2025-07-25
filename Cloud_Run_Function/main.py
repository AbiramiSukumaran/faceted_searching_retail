import functions_framework
from toolbox_langchain import ToolboxClient
import json

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    
    if name == 'FILTERS':
        filters = toolboxcall();
    else:
        filters = toolboxcallformatches(name);
    return filters

def toolboxcall():
    print("*++++++++++++++++++++++++++++++++++++++*")
    toolbox = ToolboxClient("<<YOUR_TOOLBOX_SERVER>>")
    print("****************************************")
    tool = toolbox.load_tool("get-retail-facet-filters")
    result = tool.invoke({})
    #print(result)
    return result

def toolboxcallformatches(name):
    
    toolbox = ToolboxClient("YOUR_TOOLBOX_SERVER")
    tool = toolbox.load_tool("filtered-vector-search-quality")
    print("*++++++++++++++++++++++++++++++++++++++*")
    print(name)
    parsed_name = json.loads(name)
    print("****************************************")
    print(parsed_name)
    result = tool.invoke(parsed_name)
    print(result)
    return result
