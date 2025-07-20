# organizador.py
# Organizador de Arquivos Python
# -*- coding: utf-8 -*-
import os
import shutil
import time

caminho_para_organizar = "C:/Users/Lenovo/Downloads"

mapa_de_pastas = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Musicas": [".mp3", ".wav", ".flac"],
    "Arquivos Compactados": [".zip", ".rar", ".7z", ".tar.gz"],
    "Executaveis": [".exe", ".msi"],
    "Outros": []
}


def organizar_pasta(caminho):

    print(f"Iniciando a organização da pasta: {caminho}")
    print("-" * 30)

    for pasta in mapa_de_pastas.keys():
        caminho_da_pasta = os.path.join(caminho, pasta)
        if not os.path.exists(caminho_da_pasta):
            os.makedirs(caminho_da_pasta)
            print(f"Pasta '{pasta}' criada.")

    try:
        arquivos = [f for f in os.listdir(
            caminho) if os.path.isfile(os.path.join(caminho, f))]
    except FileNotFoundError:
        print(f"ERRO: O caminho '{caminho}' não foi encontrado.")
        print("Por favor, verifique se o caminho está correto na variável 'caminho_para_organizar'.")
        return

    for arquivo in arquivos:
        extensao = os.path.splitext(arquivo)[1].lower()
        movido = False

        for pasta_destino, extensoes in mapa_de_pastas.items():
            if extensao in extensoes:
                caminho_origem = os.path.join(caminho, arquivo)
                caminho_destino = os.path.join(caminho, pasta_destino, arquivo)

                shutil.move(caminho_origem, caminho_destino)
                print(f"Moveu: '{arquivo}' -> para a pasta '{pasta_destino}'")
                movido = True
                break

        if not movido:
            caminho_origem = os.path.join(caminho, arquivo)
            caminho_destino = os.path.join(caminho, "Outros", arquivo)
            shutil.move(caminho_origem, caminho_destino)
            print(f"Moveu: '{arquivo}' -> para a pasta 'Outros'")

    print("-" * 30)
    print("Organização concluída!")

if __name__ == "__main__":
    organizar_pasta(caminho_para_organizar)
