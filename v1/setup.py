# Importe tudo que está usando no seu código py aqui
import sys
import os
import requests
from cx_Freeze import setup, Executable

base = None
# DESCOMENTE A DUAS LINHAS ABAIXO CASO SUA APLICAÇÃO USE INTERFACE!
# if sys.platform == "win32":
#     base = "Win32GUI"

executables = [
    # Nome do seu arquivo .py que quer converter para .exe
    Executable("steag_menu.py", base=base)
]

buildOptions = dict(
    packages=["idna"],
    includes=[],
    include_files=[],
    excludes=[]
)

setup(
    name="Steag",
    version="1.6",
    description="Steag solutions",
    options=dict(build_exe=buildOptions),
    executables=executables
)

# PARA UTILIZAR ESSE CÓDIGO COLOQUE ESSE ARQUIVO NA MESMA PASTA DO .PY
#                   QUE VOCÊ DESEJA CONVERTE PARA .EXE
# ABRA O CMD EM MODO ADM
# INSTALE O CX FREEZE COM O SEGUITE COMANDO:
# pip install cx_freeze
# ACESSE VIA CMD A PASTA ONDE SE ENCONTRA O AQUIVO .PY QUE DESEJA CONVERTER
#                   QUE DEVE CONTER ESSE ARQUIVO SETUP.PY TAMBÉM.
# EXECUTE O SEGUINTE COMANDO:
# python setup.by build
# QUANDO O PROCESSO TERMINAR, VOCÊ VERÁ UMA PASTA NOVA DENTRO DA PASTA QUE ESTÃO
#  OS ARQUIVOS, DENTRO DESSA PASTA ESTÁ SEU .EXE JUNTO COM TODAS AS DLLS E TUDO
#                         QUE É NECESSÁRIO PARA ELE RODAR.

# Comentários adicionados por @SmithUup  www.tismith.com.br
