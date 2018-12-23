from flask import Flask, request
import xml2tree

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    #Receive xml and response with tree
    xmlfile = request.get_data(as_text=True)
    resp = xml2tree.makeTree(xmlfile)
    return resp

if __name__ == '__main__':
    #Start service if that module is the main program
    app.run(debug=False, host='0.0.0.0', port=80)
