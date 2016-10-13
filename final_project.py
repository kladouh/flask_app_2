from flask import Flask, render_template, request
import giphypop

import os

app = Flask(__name__)




@app.route('/')
def index():
	name = request.values.get('name', 'Nobody') #how does this work?? 
	greeting = "Hello {}".format(name)
	return render_template('index.html')  


@app.route("/about")
def about():
	return render_template('about.html')


@app.route('/results')
def results():
	g = giphypop.Giphy()
	results = g.search_list('gif_name')

	for result in results:
		print(result.media_url)
		print(result.url)
	
	return render_template('results.html')



if __name__ == "__main__":  #is this line necessary?  guide on canvas does not mention it
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)





#see the last email for grading scale to receive max points