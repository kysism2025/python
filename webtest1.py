from flask import Flask
from flask.templating import render_template
 
from dbtest1 import StudentDao
 
app = Flask(__name__)
 
@app.route('/')
def emp():
    empList = StudentDao().getList()
    print(empList)
    return render_template("emp01.html", empList=empList)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


