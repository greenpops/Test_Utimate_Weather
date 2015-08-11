import json
import unirest
import logging
from random import randint

class Utimate_Weather_Forcasts:
    def __init__(self):
        # Set up logging to file
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            filename='DEBUG.log',
                            filemode='w')
        # Set up Console logging
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(console_formatter)
        # Add the handler to the root logger
        logging.getLogger('').addHandler(console)
        
        # Get name of cities from cities.json file
        with open('cities.json') as json_file:
            json_data = json.load(json_file)
        # End with

        self.cities = []
        if (json_data):
            logging.info("Loading the cities from cities.json ... \n")
            for cityObj in json_data['cities']:
                self.cities.append(cityObj["city"])
            # End for
        else: 
            logging.info("Loading the default cities: \n")
            self.cities = ['Los Angeles', 'New York', 'Seoul', 'Buenos Aires']
        # End if
        logging.debug(str(self.cities) + "\n")       
    # End __init__
    
    def http_request(self, city=""):
        service_url = "https://george-vustrey-weather.p.mashape.com/api.php?location=" + city
        logging.info(service_url)
        response = unirest.get(service_url,           
             headers={
                "X-Mashape-Key": "t2IK5ZZV6vmshGFOtdeUMFpUPsJlp1IioAyjsneIQHwKAVWP1Q",
                "Accept": "application/json"
              }
            )
        return response
    # End http_request
    
    def test_cities_correctValues(self, NumOfCities=5):
        #------------------------------------------------
        # NumOfCities: How many cities you want to test?
        #------------------------------------------------
        for counter in range(0,NumOfCities):
            # Generate a random index
            picked_index = randint(0, len(self.cities))
            picked_city = self.cities[picked_index]

            # processing the value of city
            if (picked_city != " "):
                # - Remove spaces at beginning or end of the string
                picked_city.strip()
                # - Replace spaces to +
                picked_city = picked_city.replace(" ", "+")
            else:
                logging.warning("The value of city is empty")
            # End if
            
            http_response = self.http_request(picked_city) 
            unirest.timeout(5)
            logging.debug(http_response.code)
            logging.debug(http_response.headers)
            logging.debug(http_response.body)
            
            if (http_response.code == 200):
                test_result = self.parsing_http_body(http_body=http_response.body)
                if (test_result):
                    logging.info("PositiveTest: Test for " + picked_city + " has PASSED\n")
                else:
                    logging.info("PositiveTest: Test for " + picked_city + " has FAILED\n")
                # End if
            else:
                logging.info("PositiveTest: Test for " + picked_city + " has FAILED\n")
            # End if
        # End for
    # End test_cities_correctValues

    def test_cities_incorrectValues(self):
        cities_with_incorrectValues = ["",  "++$$$", "#$#@$2er"]
        for city in cities_with_incorrectValues:            
            http_response = self.http_request(city) 
            unirest.timeout(5)
            logging.debug(http_response.code)
            logging.debug(http_response.headers)
            logging.debug(http_response.body)
            
            if (http_response.code == 200):
                test_result = self.parsing_http_body(http_body=http_response.body)
                if (not test_result):
                    logging.info("NegativeTest: Test for " + city + " has returned an error.\n"+
                                 "So, Test for " + city + " has PASSED\n")
                else:
                    logging.info("NegativeTest: Test for " + city + " has returned no error.\n"+
                                  "So, Test for " + city + " has FAILED\n")
                # End if
            else:
                logging.info("NegativeTest: Test for " + city + " has FAILED\n")
        # End for
    # End test_cities_incorrectValues

    def parsing_http_body(self, http_body=""):
        result = 0

        if (http_body==""):
            logging.info("No http body info to parse \n")
            return result
        # end if
        
        try:
            if (http_body[0]['day_of_week']):
                logging.info("Weather Forecast info is retrived \n")
                result = 1
        except:
            if (http_body[0]['message']):
                logging.error(http_body[0]['message'] +"\n")
        # End Try

        logging.debug(" parsing_http_body ReturnValue: " + str(result))
        return result
            
# End Test_Utimate_Weather_Forcasts
 
if __name__ == '__main__':
    WeatherService = Utimate_Weather_Forcasts()
    WeatherService.test_cities_correctValues(NumOfCities=10)
    WeatherService.test_cities_incorrectValues()
    
# End __main__
