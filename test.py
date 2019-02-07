
 
from flask import Flask     
app = Flask(__name__)   # Flask constructor 
  
@app.route('/')       
def index(): 
    return 'Hello World!!checking the scalibiltyyyyy and automation......'
init __name__=='__main__': 
   app.run(host='0.0.0.0', port=80)
   
