from flask import Flask, render_template, request
import giphypop
import os

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')  



@app.route("/about")
def about():
	return render_template('about.html')


@app.route('/results')
def results():
	gif_name = request.values.get('gif_name')
	g = giphypop.Giphy()
	results = g.search_list(gif_name)

	return render_template('results.html', gif_name=gif_name, results=results)






if __name__ == "__main__": 
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)





# To do list
#1- Edit your README.md file so that it links to your newly created Heroku app page and push that to Github.
#2- Add comments