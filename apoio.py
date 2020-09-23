


#sofreu melhoria steag_app
selected = input('Digite o nome do arquivo (.xlsx):')
caminho = r'D:\OneDrive\Área de Trabalho\steag\atual\{}.xlsx'.format(selected)
destino = r'c:\steag_plantas'
steagsupports.createsheets(destino)
steagsupports.createsubsheets(destino)
period = steagsupports.option()
choose = steagsupports.option1()
equipment = steagsupports.option2()
steagsupports.sheetperiod(choose, destino, period)
if choose != 0:
    print('Processando.......\n')
    v0 = time()
    if equipment == 1:
        steagframes.calcinverter(caminho, period, choose, destino)
    elif equipment == 2:
        steagframes.calcstringsbox(caminho, period, choose, destino)
    elif equipment == 3:
        steagframes.calcstrings(caminho, period, choose, destino)
    elif equipment == 4:
        steagframes.calcweather(caminho, period, choose, destino)
#até aqui



#sofreu melhoria steagsupports
def option2():
    flag = True
    while flag:
        opt2 = [0, 1, 2, 3, 4]
        plant2 = int(input('################################################'
                           '\nSelecione um tipo de equipamento disponível:'
                           '\nDigite 1 --> Inversores'
                           '\nDigite 2 --> Strings Box'
                           '\nDigite 3 --> Strings'
                           '\nDigite 4 --> Weather Station'
                           '\nDigite 0 --> Sair.'
                           '\n################################################'
                           '\nPrezado usuário, escolha uma opção?'))
        if plant2 in opt2:
            return plant2
        else:
            print('Opção incorreta, tente novamente.')
            time.sleep(3)



#sofreu melhoria steagframes
def calcweather(*args):
    df_fin = pd.read_excel(args[0])
    df_fin = df_fin.fillna(0.00)
    df_fin.rename(columns={'Date': 'timestamp'}, inplace=True)
    df_fin['timestamp'] = pd.to_datetime(df_fin['timestamp'])
    df_fin['timestamp'] = df_fin['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    print(df_fin)
