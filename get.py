import requests as rq


def Dolar():
    url_dolar = rq.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
        # Cotação dolár real

    dados_dolar = url_dolar.json()
        # Criando o Json do dolár
    cotacao_dolar = round(float(dados_dolar["USDBRL"]["bid"]), 2)
        # Cotação Dolár
    return cotacao_dolar


def Euro():
    url_euro = rq.get("https://economia.awesomeapi.com.br/json/last/EUR-BRL")
        #cotação euro
    dados_euro = url_euro.json()
        # Criando o Json do euro
    cotacao_euro = round(float(dados_euro["EURBRL"]["bid"]), 2)
        # Cotação Euro
    return cotacao_euro

def BTC():
    url_BTC = rq.get("https://economia.awesomeapi.com.br/json/last/BTC-BRL")
        #cotação euro
    dados_BTC = url_BTC.json()
        # Criando o Json do euro
    cotacao_BTC = round(float(dados_BTC["BTCBRL"]["bid"]), 2)
        # Cotação Euro
    return cotacao_BTC