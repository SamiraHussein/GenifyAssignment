import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


GenifyCustomers = [
    {
    'id': 1,
    'name':'Ivan Alex',
    'age': 26,
     'seniority': 214,
     'segment': 'Individual',
     'gender': 'Male',
     'relationchip': '',
     'annualincome': 9374,
     'nationality': 'Russian',
     'activelevel': 'Active',
     'region': 'Moscow'
     
     }
     ,
    {
     'id': 2,
    'name':'Ana Baloma',
    'age': 35,
     'seniority': 214,
     'segment': 'Student',
     'gender': 'Female',
     'relationchip': '',
     'annualincome': 50155,
     'nationality': 'Argentinian',
     'activelevel': 'Active',
     'region': 'Buenos Aires'
     },

    {
        'id': 3,
    'name':'Ivan Alex',
     'age': 26,
     'seniority': 214,
     'segment': 'Individual',
     'gender': 'Male',
     'relationchip': '',
     'annualincome': 50155,
     'nationality': 'Argentinian',
     'activelevel': 'Active',
     'region': 'Buenos Aires'
     
     }
     ,
     
    {

    'id': 4,
    'name':'Emilano Lopez',
     'age': 34,
     'seniority': 171,
     'segment': 'Individual',
     'gender': 'Male',
     'relationchip': '',
     'annualincome': 55005,
     'nationality': 'Mexican',
     'activelevel': 'Inactive',
     'region': 'Mexico'
     
     }
      ,
      
    {

     'id': 5,
    'name':'Fatima Aziz',
     'age': 34,
     'seniority': 6,
     'segment': 'Individual',
     'gender': 'Male',
     'relationchip': '',
     'annualincome': 55005,
     'nationality': 'Egytian',
     'activelevel': 'Inactive',
     'region': 'Cairo'
     
     }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Recommend banking products</h1>
<p>Banking product recommender system
Give a try to Genify's machine learning-powered banking product recommender 
system and let us know what you think!</p>'''

@app.route('/service-apis/v1/GenifyCustomers/all', methods=['GET'])
def api_all():
    return jsonify(GenifyCustomers)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/service-apis/v1/GenifyCustomers', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:    
         return page_not_found(404)

    # Create an empty list for our results
    results = []

    for customer in GenifyCustomers:
        if customer['id'] == id:
            results.append(customer)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()