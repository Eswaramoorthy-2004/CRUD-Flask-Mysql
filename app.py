from flask import Flask ,render_template,url_for,request,redirect
from flask_mysqldb import MySQL
app=Flask(__name__)
#Sql Connection
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="@Eswar143"
app.config["MYSQL_DB"]="crud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)
#Home page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="Select * from users"
    con.execute(sql)
    res=con.fetchall()
    return render_template("index.html",datas=res)
#Insert value
@app.route("/insert",methods=['GET','POST'])
def insert():
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        con=mysql.connection.cursor()
        sql="insert into users (name,age,city) value (%s,%s,%s)"
        con.execute(sql,[name,age,city])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("insert.html")
#Update value
@app.route("/update/<string:id>",methods=['GET','POST'])
def update(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        city=request.form['city']
        sql="update users set name=%s,age=%s,city=%s where id=%s"
        con.execute(sql,[name,age,city,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
        con=mysql.connection.cursor()
        
    sql="select * from users where id=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("update.html",datas=res)
#Delete Value
@app.route("/delete/<string:id>",methods=['GET','POST'])
def delete(id):
    con=mysql.connection.cursor()
    sql="delete from users where id=%s "
    con.execute(sql,(id,))
    mysql.connection.commit()
    con.close()
    return redirect(url_for("home"))






  
if(__name__=='__main__'):
    app.run()
