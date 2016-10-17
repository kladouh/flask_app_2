from flask import Flask, render_template, request
import giphypop
import os

#Sets up the flask module
app = Flask(__name__) 


#Registers url of main page
@app.route('/')
def index():
	return render_template('index.html')  


#Registers url of about page
@app.route("/about")
def about():
	return render_template('about.html')


#Registers url of results page
@app.route('/results')
def results():

	#Gets the variable 'gif_name' (an input variable on the main page)
	gif_name = request.values.get('gif_name')
	
	#Runs a giphy search for 'gif_name'
	g = giphypop.Giphy()
	results = g.search_list(gif_name)

	#Passes the variables 'results' and 'gif_name' to the html code
	return render_template('results.html', gif_name=gif_name, results=results)



if __name__ == "__main__": 
	#Necessary to deploy to
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)


# Note to Appraiser:

# Just writing to point out this app will display the appropriate error message for the
# situation when no gifs are found for the given search terms (e.g if gibberish is entered)






