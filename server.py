from flask import Flask, render_template, url_for, request, redirect
import csv 
app = Flask(__name__)
(print(__name__))


@app.route('/')   # <- decorator
def myHome():
    return render_template('index.html')

@app.route('/<string:pageName>')   
def htmlPage(pageName):
    return render_template(pageName)   


@app.route('/submitForm', methods=['POST', 'GET'])
def submitForm():
		if request.method == 'POST':
			try:
				data = request.form.to_dict()  
				writeToFile(data)
				writeToCsv(data)
				return redirect('/thankyou.html')
			except:
				return 'Bummer! did not save to database'	
		else:
			return 'That is not going to fly.... please, try again' 


def writeToFile(data):
	with open('database.txt', mode='a') as database:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{name},{email},{subject},{message}')

def writeToCsv(data):
	with open('database.csv', newline='', mode='a') as database2:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',',
		quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject,message])


# @app.route('/submitForm', methods=['POST', 'GET'])
# def submitForm():
#     if request.method == 'POST':
#     	try:
# 			data = request.form.to_dict()  
# 			writeToFile(data)
# 			writeToCsv(data)
# 			return redirect('/thankyou.html')
# 		except:
# 			return 'Bummer! did not save to database'	
#     else:
#     	return 'that is not going to fly.... please, try again' 

# @app.route('/index.html')   # <- decorator
# def index():
#     return render_template('index.html')  

# @app.route('/about.html')   
# def aboutMe():
#     return render_template('about.html')

# @app.route('/projects.html')   
# def myProjects():
#     return render_template('projects.html')

# @app.route('/contact.html')   
# def myContact():
#     return render_template('contact.html')


#-------- Adding User Login: ------------
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)
















           


