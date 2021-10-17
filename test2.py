import requests
import flask

app = flask.Flask(__name__)
url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"

headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "e8d97b908amsh7b4f0d096ac23c7p1b57fajsn52fb2945ef0e"
    }

def get_current_market_value(quantity, product):
    querystring = {"symbol": product, "region": "US"}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_data = response.json()
        regularMarketPreviousClose = response_data["summaryDetail"]["regularMarketPreviousClose"]["raw"]
        notional = regularMarketPreviousClose * quantity
        return notional
        #print(response.text)
    except requests.exceptions.HTTPError as error:
        print(error)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Notional retrieval logic</h1><p>The logic is first define the server api endpoint where" \
           " we are getting the info from.  Once established the connection, I firstly look at " \
           "the json output from the endpoint, and ctrl-f to find the variable we are " \
           "looking for. Then customize the retrieval code with function parameters." \
           "Inside of the function, I implement the equation mentioned in the function and then " \
           "return the result.</p>"

app.run()