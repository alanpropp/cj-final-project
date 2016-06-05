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
    percentage_energy = helpers.percentage_energy(information, years_list, argument)
    percentage_pop = helpers.percentage_population(country)
    population_rank = helpers.population_rank(country)
    usage_rank = helpers.usage_rank(country, information)
    usage_rank_per_capita = helpers.usage_rank_per_capita(country, information)
    fun_facts_url = helpers.get_fun_facts(country)
    return render_template('results.html', nation = country, argument = argument, years = years_list,
        metric = metric, metric_units = metric_units, similar = similar_countries,
        percentage_energy = percentage_energy, population = population, per_capita = per_capita,
        percentage_pop = percentage_pop, population_curr = population[len(population)-1],
        population_rank = population_rank, usage_rank = usage_rank, usage_rank_per_capita = usage_rank_per_capita,
        funfacts = fun_facts_url)

@app.route("/rank")
def rank():
    reqargs = request.args
    metric = reqargs.get('metric')
    metric_units = helpers.get_units(metric)
    information = helpers.get_correct_metric(metric)
    ranked_list = helpers.ranked_list(information)
    return render_template('rank.html', metric = metric, ranked_list = ranked_list, metric_units = metric_units)

@app.route("/compare")
def compare():
    reqargs = request.args
    country1 = reqargs.get('country1')
    country2 = reqargs.get('country2')
    if not country1 and not country2:
        return """
                <h1>Error</h1>
                <p>Please enter in 2 countries/regions!</p>
        """

    metric = reqargs.get('metric')
    information = helpers.get_correct_metric(metric)
    metric_units = helpers.get_units(metric)
    country1_data = helpers.get_country_data(country1, information)
    country2_data = helpers.get_country_data(country2, information)
    years = helpers.get_years_list(information)
    country1_per_capita = helpers.compare_per_capita(country1, country1_data, years)
    country2_per_capita = helpers.compare_per_capita(country2, country2_data, years)
    return render_template('compare.html', metric = metric, country1 = country1, country2 = country2, years = years,
        country1_data = country1_data, country2_data = country2_data, country1_per_capita = country1_per_capita,
        country2_per_capita = country2_per_capita, metric_units = metric_units)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


