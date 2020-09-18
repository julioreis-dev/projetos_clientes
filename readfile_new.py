import pandas as pd
import steagsupports


caminho = r'C:\Users\julio.firmino\Desktop\plantas\Sol do Futuro - AGOSTO 2020_2020_09_18.xlsx'
destino = r'c:\steag_plantas'
steagsupports.criar_pastas(destino)
steagsupports.criar_sub(destino)
choose = steagsupports.option()
if choose != 0:
    print('Processando.......\n')
    column = steagsupports.organizefiles(caminho)
    lista_plant = steagsupports.organizetupla(column)
    for i in lista_plant:
        df_fin = pd.read_excel(caminho)
        df_fin = df_fin[[column[0], i[0], i[1]]]
        df_fin.rename(columns={'Date': 'timestamp', i[0]: 'ACTIVE POWER', i[1]: 'COMS STATUS'}, inplace=True)
        frame = steagsupports.readframe(df_fin)
        #print(frame)
    print('Processo finalizado')
else:
    exit()
