import urllib.request,json
from .models import Quote


def get_quotes():
    """
    :return: quotes results
    """

    get_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = get_quotes_response

        # if get_quotes_response['quote']:
        #     quotes_results = get_quotes_response['quote']

    return quotes_results
