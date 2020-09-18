import pandas as pd
import steagsupports


caminho = r'C:\Users\julio.firmino\Desktop\plantas\SPD - AGOSTO 2020_2020_09_18.xlsx'
destino = r'c:\steag_plantas'
steagsupports.criar_pastas(destino)
steagsupports.criar_sub(destino)
choose = steagsupports.option()
if choose != 0:
    print('Processando.......\n')
    # readarticle(caminho)
    column = steagsupports.organizefiles(caminho)
    lista_plant = steagsupports.organizetupla(column)
    for i in lista_plant:
        df_fin = pd.read_excel(caminho)
        df_fin = df_fin[[column[0], i[0], i[1]]]
        #print(df_fin)
    print('Processo finalizado')
else:
    exit()
