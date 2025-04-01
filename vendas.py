import pyodbc

import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import plotly.express as px

def conectar_ao_banco():
    dados_empresa = (
        'DRIVER={SQL Server Native Client 11.0};'
        'SERVER=aquidaba.infonet.com.br;'
        'DATABASE=dbproinfo;'
        'UID=leituraVendas;'
        'PWD=***********;'
    )

    conexao = pyodbc.connect(dados_empresa)
    cursor = conexao.cursor()

    return conexao, cursor

conexao, cursor = conectar_ao_banco()

consulta = cursor.execute("SELECT * FROM tbVendasDashboard where nmFilial ='FILIAL 0001';").fetchall()
#print(consulta)





