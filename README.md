# 📈 Cotações em Tempo Real

Aplicação simples em **Python + Tkinter** para exibir as cotações
atualizadas de **Dólar**, **Euro** e **Bitcoin** utilizando a API
pública da **AwesomeAPI**.

------------------------------------------------------------------------

## 🧰 Funcionalidades

-   Consulta em tempo real das moedas:
    -   🇺🇸 **Dólar (USD → BRL)**
    -   🇪🇺 **Euro (EUR → BRL)**
    -   ₿ **Bitcoin (BTC → BRL)**
-   Interface gráfica com **Tkinter**
-   Botão para atualizar manualmente as cotações
-   Exibição da hora da última atualização

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    .
    ├── app.py      # Interface gráfica (Tkinter)
    └── get.py      # Funções responsáveis pelas requisições HTTP

------------------------------------------------------------------------

## 🚀 Como Executar

### 1. Instale as dependências

``` bash
pip install requests
```

### 2. Execute o programa

``` bash
python app.py
```

------------------------------------------------------------------------

## 🧠 Como Funciona

### 🔹 Arquivo `get.py`

Contém três funções responsáveis por realizar chamadas HTTP e retornar
as cotações:

-   `Dolar()` → Retorna o valor atual do **USD-BRL**
-   `Euro()` → Retorna o valor atual do **EUR-BRL**
-   `BTC()` → Retorna o valor atual do **BTC-BRL**

As funções utilizam: - `requests.get()` para acessar a API\
- `.json()` para interpretar a resposta\
- `round()` para formatar os valores

### 🔹 Arquivo `app.py`

É responsável por criar a interface gráfica com Tkinter:

-   Cria a janela principal
-   Exibe os valores das moedas
-   Botão **ATUALIZAR** chama `atualizar()`, que:
    -   Busca novas cotações
    -   Atualiza os textos exibidos
    -   Mostra a hora da atualização

------------------------------------------------------------------------

## 📡 API Utilizada

Os dados são fornecidos pela AwesomeAPI:

-   **USD-BRL**
-   **EUR-BRL**
-   **BTC-BRL**

------------------------------------------------------------------------

## 🛠 Possíveis Melhorias Futuras

-   Atualização automática por intervalo de tempo (timer)
-   Tema escuro
-   Gráficos históricos
-   Tratamento de erros ao consumir a API
-   Suporte para mais moedas

------------------------------------------------------------------------

## 📜 Licença

Este projeto é livre para uso e modificação.
