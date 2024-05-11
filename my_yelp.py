import requests, json 

def search_businesses(search_term, search_location):
    
    api_key = "s_OpTZ_NQ-drrRvI4LZMVU6BCRdxj3QjEMHDFKi5FYMFFEFhlVb2UtnEKnA8d5y-61G1b1Be-94a725Ri739UNcq_IYw-jM3X3UoEssWx8RklEJddu8JTVrikUc2ZnYx"

    url = "https://api.yelp.com/v3/businesses/search"

    my_headers = {
        "Authorization": "Bearer %s" % api_key
    }

    my_params = {
        "term": search_term,
        "location": search_location,
        "limit": 3,
    }

    businesses_object = requests.get(url, headers=my_headers, params=my_params)

    businesses_dict = json.loads(businesses_object.text)

    businesses_list = businesses_dict['businesses']
    
    print(businesses_dict)
    list_of_businesses = []
    for each in businesses_list:
        list_of_businesses.append(each)
    return list_of_businesses