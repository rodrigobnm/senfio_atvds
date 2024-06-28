import requests

def main():
    response = requests.get('http://api.github.com')
    print(f"Código de retorno: {response.status_code}")

if __name__ == "__main__":
    main()

# venv\Scripts\activate
# pip install requests
# pip freeze > requirements.txt
# python 03.py
