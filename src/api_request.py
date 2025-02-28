import requests  
import json  
  
def get_data():  
    url = "https://api.example.com/data"  
    response = requests.get(url)  
    if response.status_code == 200:  
        return response.json()  
    else:  
        return None  
  
if __name__ == "__main__":  
    data = get_data()  
    print(json.dumps(data, indent=4)) 

import logging  
logging.basicConfig(level=logging.INFO)  
  
def get_data():  
    logging.info("Отправка запроса к API...")  
    # Запрос к API 