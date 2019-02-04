
 
from flask import Flask     
app = Flask(__name__)   # Flask constructor 
  
@app.route('/')       
def index(): 
    return 'HELLO world! spilting intooo soo many thingss.. .... the ansible testt!'
  
if __name__=='__main__': 
   app.run(host='0.0.0.0', port=5051)
   
