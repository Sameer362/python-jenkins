import requests

def fetch_data():
    url = "https://api.github.com"
    response = requests.get(url)
    if response.status_code == 200:
        print("Response from GitHub API:", response.json())
    else:
        print("Failed to fetch data. Status code:", response.status_code)

if __name__ == "__main__":
    fetch_data()

