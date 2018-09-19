from flask import Flask,render_template,request
import pandas as pd
app = Flask(__name__)
df=pd.DataFrame(columns=['Name'])
@app.route('/',methods=['GET','POST'])
def homepage():	
	
	if request.method =='POST':
		writer = pd.ExcelWriter('pandas_simple11.xlsx', engine='openpyxl')
		first_name=request.form['first_name']
		last_name=request.form['last_name']
		print ('Hello' + " " + first_name + " " + last_name )
		global df
		df1=pd.DataFrame([first_name],columns=['Name'])
		print (df1)
		df=df.append(df1)
		print (df)
		df.to_excel(writer, sheet_name='Sheet1')
	#	df.to_excel(writer, startrow=len(df)+1, index=False)
		writer.save()
	return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

