import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Border, Side, PatternFill
from datetime import datetime
import os


# Pesquisa e coleta todos os dados
def buscar_clima():
    navegador = webdriver.Chrome()

    # Acessa o site
    navegador.get('https://www.google.com')

    # Pesquisa pela temperatura em São Paulo
    navegador.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('Temperatura em São Paulo')

    # Envia a pesquisa
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)

    # Captura os dados
    temperatura = navegador.find_element(By.XPATH, '//*[@id="wob_tm"]').text
    umidade = navegador.find_element(By.XPATH, '//*[@id="wob_hm"]').text
    ceu = navegador.find_element(By.XPATH, '//*[@id="wob_dc"]').text
    alertas = navegador.find_element(By.XPATH, '//*[@id="wob_wc"]/div[4]/div[1]').text

    # Exibe os dados no console (opcional)
    print(f'Temperatura: {temperatura}°C\nUmidade do ar: {umidade}\nCéu: {ceu}\nAlertas: {alertas}')

    # Chama a função para salvar os dados na planilha
    salvar_dados(temperatura, umidade, ceu, alertas)

    # Fecha o navegador após coletar os dados
    navegador.quit()


# Salva os dados coletados em uma planilha
def salvar_dados(temperatura, umidade, ceu, alertas):
    arquivo_nome = 'dados_climaticos.xlsx'

    # Verifica se o arquivo já existe
    if not os.path.exists(arquivo_nome):
        # Cria um novo arquivo e uma planilha
        arquivo = Workbook()
        planilha = arquivo.active
        planilha.title = 'Sheet1'

        # Cabeçalhos
        cabecalhos = ['Data e Hora', 'Temperatura', 'Umidade', 'Céu', 'Alertas']
        for col_num, cabecalho in enumerate(cabecalhos, start=1):
            cell = planilha.cell(row=1, column=col_num)
            cell.value = cabecalho
            cell.border = Border(left=Side(style='thin'),
                                 right=Side(style='thin'),
                                 top=Side(style='thin'),
                                 bottom=Side(style='thin'))
            cell.fill = PatternFill(start_color='FFD700', end_color='FFD700', fill_type='solid')

    else:
        # Abre o arquivo existente
        arquivo = load_workbook(arquivo_nome)
        planilha = arquivo['Sheet1']

    # Data e hora atual
    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Encontra a próxima linha vazia
    linha_vazia = planilha.max_row + 1

    # Adiciona os dados na próxima linha
    valores = [data_hora, f"{temperatura}°C", umidade, ceu, alertas]
    for col_num, valor in enumerate(valores, start=1):
        cell = planilha.cell(row=linha_vazia, column=col_num)
        cell.value = valor
        cell.border = Border(left=Side(style='thin'),
                             right=Side(style='thin'),
                             top=Side(style='thin'),
                             bottom=Side(style='thin'))

    # Ajusta a largura das colunas
    for col in planilha.columns:
        max_length = max(len(str(cell.value)) for cell in col if cell.value)
        planilha.column_dimensions[col[0].column_letter].width = max_length + 2

    # Salva a planilha
    arquivo.save('dados_climaticos.xlsx')

    print("Planilha atualizada com sucesso!!!")


# Interface gráfica com tkinter
root = tk.Tk()
root.title("Captador de temperatura em São Paulo")
root.geometry("400x100")

# Texto de instrução
label_instrucoes = tk.Label(root, text="Clique no botão para buscar o clima de São Paulo.")
label_instrucoes.pack(pady=10)

# Botão para buscar o clima
botao_buscar = tk.Button(root, text="Buscar Clima", command=buscar_clima)
botao_buscar.pack(pady=10)

# Executa o loop da interface gráfica
root.mainloop()
