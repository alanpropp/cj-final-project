from flask import Flask, render_template, request
#from foo import just_do_it
import helpers
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

    #Get the information for the metric requseted
    information = helpers.get_correct_metric(metric)
    years_list = []
    argument = []

    #Get a list of the nation's usage over the years, put it in 'arguments' list
    #Arguments is a list of floats that corresponds to each spot in years_list
    for i in information:
        if i[''] == country:
            for y in helpers.years():
                if(i.get(y)):
                    if(i.get(y) != 'NA' and i.get(y) != '--'):
                        argument.append(float(i[y]))
                        years_list.append(y)
                    else:
                        argument.append(None)
                        years_list.append(y)



    population = []

    #Get the units of whatever we are doing
    metric_units = helpers.get_units(metric)
    
    metric_units = metric_units
    population_overall = helpers.population()
    for p in population_overall:
        if p[''] == country:
            for y in years_list:
                if(p[y]):
                    if p[y] != '--' and p[y] != 'NA':
                        population.append(float(p[y]))
                    else:
                        population.append(None)
    per_capita = []
    for a in range(0,len(argument)):
        if population[a] != None and argument[a] != None:
            b = float(argument[a])/float(population[a])
            per_capita.append(b)
        else:
            per_capita.append(None)

    #Time to find similar countries!
    similar_countries = helpers.find_similar_countries(information, years_list, argument, country)
    percentage = helpers.percentage_total(information, years_list, argument)
    return render_template('results.html', nation = country, argument = argument, years = years_list,
        metric = metric, metric_units = metric_units, similar = similar_countries,
        percentage = percentage, population = population, per_capita = per_capita)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


