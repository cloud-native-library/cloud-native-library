import logging
import azure.functions as func
import mimetypes

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        #return func.HttpResponse(f"Hello {name}!")
        path = 'index-func' # or other paths under `MyFunctionProj`
        filename = f"{path}/{name}"
        with open(filename, 'rb') as f:
            mimetype = mimetypes.guess_type(filename)
            return func.HttpResponse(f.read(), mimetype=mimetype[0])
    else:
        
        path = 'index-func' # or other paths under `MyFunctionProj`
        filename = f"{path}/{'index.html'}"
        with open(filename, 'rb') as f:
            mimetype = mimetypes.guess_type(filename)
            return func.HttpResponse(f.read(), mimetype=mimetype[0])
            "Please pass a name on the query string or in the request body",
            status_code=400
