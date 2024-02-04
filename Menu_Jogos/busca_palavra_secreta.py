import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

def remover_acentos(word):
    return unidecode(word)

def palavra():
    base_url = "https://api.dicionario-aberto.net/random"
    try:
        # Faz a requisição à API
        response = requests.get(base_url)
        response.raise_for_status()  # Gera uma exceção para respostas HTTP ruins
        data = response.json()

        # Extrai a palavra e a definição
        word = data["word"]

        return word
    except Exception as e:
        print(f"Erro ao obter palavra: {e}")
        return None

def obter_significado(word):
    word = remover_acentos(word)
    url = f'https://www.dicio.com.br/{word}'
    try:
        # Faz a requisição à API
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida (código 200)
        response.raise_for_status()

        # Faz o parsing do HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Verifica se a palavra existe na API
        if not soup.find('div', {'class': 'title-header'}):
            return "Palavra não encontrada"

        # Extrai o significado usando a classe 'significado'
        significado_element = soup.find('p', {'class': 'significado textonovo'})

        if significado_element:
            # Extrai as duas primeiras <span> dentro do <p>
            spans = significado_element.find_all('span')[:2]

            # Constrói a string com o conteúdo das <span>
            significado = ' '.join(span.text.strip() for span in spans)
            return significado
        else:
            return None

    except requests.exceptions.RequestException as e:
        return None

def obter_sinonimos(word):
    word = remover_acentos(word)
    url = f'https://www.sinonimos.com.br/busca.php?q={word}'
    try:
        # Faz a requisição à API
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida (código 200)
        response.raise_for_status()

        # Faz o parsing do HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrai os sinônimos usando a classe 'sinonimo'
        sinonimos_elements = soup.find_all('a', {'class': 'search-result--link'})
        sinonimos = [element.text.strip() for element in sinonimos_elements]

        if sinonimos:
            return sinonimos
        else:
            return None

    except requests.exceptions.RequestException as e:
        return None

if __name__ == "__main__":
    palavra()
