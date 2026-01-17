# 🌦️ Captador de Temperatura por Cidade — Python

## 📖 Descrição
Aplicação desenvolvida em **Python** que permite consultar informações climáticas de **qualquer cidade**, utilizando consumo de **API REST**, interface gráfica com **Tkinter** e persistência de dados em **planilha Excel**.

O projeto simula um cenário real de automação, utilizando integração direta com API (em vez de scraping), garantindo **maior confiabilidade, segurança e escalabilidade**, além do uso de variáveis de ambiente para proteção de credenciais sensíveis.

---

## 🎯 Objetivo
- Praticar consumo de APIs REST em Python  
- Desenvolver uma interface gráfica simples e funcional  
- Armazenar dados históricos de forma estruturada  
- Aplicar boas práticas de automação e tratamento de erros
- Evitar vazamento de credenciais sensíveis (API Key) 

---

## ⚙️ Funcionalidades
- 🔍 Busca de clima por **qualquer cidade**
- 🌡️ Exibição de:
  - Temperatura (°C)
  - Umidade (%)
  - Condição do céu
- 🧠 Validação de entrada do usuário
- 💾 Salvamento automático dos dados em Excel
- 🕒 Registro de data e hora da consulta
- 📊 Criação dinâmica de arquivo e planilha, caso não existam
- 🔐 Uso de variáveis de ambiente para proteger a API Key

---

## 🛠️ Tecnologias Utilizadas
- Python 3  
- Tkinter  
- Requests  
- OpenWeatherMap API  
- OpenPyXL
- Python-dotenv

---

## 🧩 Arquitetura do Projeto
- Interface gráfica responsável pela interação com o usuário  
- Função dedicada para consumo da API de clima  
- Função separada para persistência de dados
- Uso de variáveis de ambiente (.env) para credenciais sensíveis  
- Tratamento de erros para cidades inválidas e arquivos inexistentes  

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/Ingridxisto/Captador-de-Temperatura.git
cd Captador-de-Temperatura
```

### 2️⃣ Instale as dependências
```bash
pip install requests openpyxl python-dotenv
```

### 3️⃣ Configure a API Key

Crie uma conta gratuita em:
https://openweathermap.org/api

Crie um arquivo .env na raiz do projeto com o conteúdo:

```bash
OPENWEATHER_API_KEY=SUA_CHAVE_API_AQUI
```

⚠️ O arquivo .env não é versionado e está incluído no .gitignore por segurança.

### 4️⃣ Execute o projeto
```bash
python clima.py
```
---

## 🖼️ Interface

A aplicação possui uma interface simples e intuitiva, permitindo que o usuário informe a cidade desejada e visualize o clima em tempo real.

![Interface do Captador de Temperatura](screenshots/captador-de-temperatura.png)

---

## 📚 Aprendizados

- Consumo de APIs REST

- Integração entre interface gráfica e backend

- Persistência de dados em Excel

- Tratamento de erros e validações

- Organização e modularização de código

- Uso de variáveis de ambiente para segurança

- Organização e modularização de código

---

## 🔮 Possíveis Melhorias Futuras

- Geração de gráficos de histórico climático

- Integração com banco de dados

- Uso de IA para previsões ou insights

- Interface mais personalizada (CustomTkinter ou Web)

- Deploy da aplicação

---

## 👩‍💻 Autora

Ingrid Xisto
Estudante de Análise e Desenvolvimento de Sistemas
Foco em Python, Automação, APIs e Inteligência Artificial

🔗 GitHub: https://github.com/Ingridxisto

🔗 LinkedIn: https://www.linkedin.com/in/ingridxisto/
