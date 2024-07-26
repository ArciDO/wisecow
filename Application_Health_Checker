import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException as e:
        return 'down'

if __name__ == "__main__":
    url = "http://www.simmons.edu"
    status = check_application_health(url)
    print(f"The application is {status}.")
