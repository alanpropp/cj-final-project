from flask import Flask, render_template, request
#from foo import just_do_it
import helpers
from collections import OrderedDict
app = Flask(__name__)

@app.route("/")
def homepage():
    #First, get a list of countries to help format the homepage
    countries = sorted(helpers.get_countries(), key = str.lower)
    html = render_template('index.html', nations = countries)
    return html

@app.route("/results")
def results():
    reqargs = request.args
    #First, we need to know what counry we are talking about
    country = reqargs.get('country')
    #Throw an error if there's no country entered
    if not country:
        return """
            <h1>Error</h1>
            <p>Please enter in a country or a region!</p>
        """


    #Next, what metric are they requesting
    metric = reqargs.get('metric')

    information = []
    #Fill 'electricity' with this specific country's info
    if reqargs.get('metric') == 'coal':
        information = helpers.coal()
    
    argument = []
    for i in information:
        if i[''] == country:
            for y in helpers.years():
                argument.append(i[y])


    return render_template('results.html', nation = country, argument = argument, years = helpers.years())


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


