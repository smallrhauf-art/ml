# -*- coding: utf-8 -*-

import os
import shutil

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

DESTINO = r"C:\Users\RHAUF\Desktop\get\pastaimage\ml"

PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))

RELATORIO = "RELATORIO_COPIA_IMAGENS.txt"

TOTAL = 0
ERROS = 0

LOG = []

# ==========================================================
# CRIA DESTINO SE NÃO EXISTIR
# ==========================================================

os.makedirs(DESTINO, exist_ok=True)

# ==========================================================
# COPIA AS IMAGENS
# ==========================================================

for arquivo in os.listdir(PASTA_ATUAL):

    caminho = os.path.join(PASTA_ATUAL, arquivo)

    if not os.path.isfile(caminho):
        continue

    if not arquivo.lower().endswith(".png"):
        continue

    destino = os.path.join(DESTINO, arquivo)

    try:

        shutil.copy2(caminho, destino)

        TOTAL += 1

        LOG.append(f"OK  - {arquivo}")

    except Exception as erro:

        ERROS += 1

        LOG.append(f"ERRO - {arquivo} -> {erro}")

# ==========================================================
# RELATÓRIO
# ==========================================================

with open(RELATORIO, "w", encoding="utf-8") as f:

    f.write("RELATÓRIO DE CÓPIA DE IMAGENS\n\n")

    f.write("=" * 70 + "\n\n")

    for linha in LOG:

        f.write(linha + "\n")

    f.write("\n")

    f.write("=" * 70 + "\n")

    f.write(f"Imagens copiadas : {TOTAL}\n")

    f.write(f"Erros            : {ERROS}\n")

# ==========================================================
# RESUMO
# ==========================================================

print()

print("=" * 60)

print("FINALIZADO")

print(f"IMAGENS COPIADAS : {TOTAL}")

print(f"ERROS            : {ERROS}")

print(f"RELATÓRIO        : {RELATORIO}")

print("=" * 60)

input("\nPressione ENTER para finalizar...")