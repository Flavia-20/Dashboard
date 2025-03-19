import pyodbc

dados_empresa = (
    "Driver={SQL Server};"
    "Server=LAPTOP-C6FDP5R6;"
    "Database=dbproinfo;"
)

conexao = pyodbc.connect(dados_empresa)
print("conectado")