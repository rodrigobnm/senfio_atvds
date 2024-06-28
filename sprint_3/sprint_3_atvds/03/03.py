# ->> Ex 03) Crie um app que realize um request através da biblioteca 'requests' para o endereço 'http://api.github.com' e exiba o código de retorno.
#    * Utilize ambiente virtual
#    * Guarde os dados do ambiente virtual num arquivo 'requirements.txt'

import requests

response = requests.get('http://api.github.com')
print(response)

