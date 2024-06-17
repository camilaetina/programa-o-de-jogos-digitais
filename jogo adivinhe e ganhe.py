import random
import tkinter as tk
from tkinter import messagebox

# Lista de palavras para o jogo
palavras = [
    "Cachorro",
    "Gato",
    "Computador",
    "Avião",
    "Bola",
    "Dança",
    "Telefone",
    "Chuva",
    "Cinema",
    "Livro",
    "Surpresa",
    "Brinquedo"
]


# Função para escolher uma palavra aleatória da lista
def escolher_palavra():
    return random.choice(palavras)


# Função para mostrar uma dica com base na tentativa atual
def mostrar_dica(palavra, tentativa):
    dicas = {
        "Cachorro": ["É um animal.", "Tem quatro patas."],
        "Gato": ["É um animal.", "Faz 'miau'."],
        "Computador": ["É um objeto.", "Usado para processamento de dados."],
        "Avião": ["É um objeto.", "Transporte aéreo."],
        "Bola": ["É um objeto.", "Usado em vários esportes."],
        "Dança": ["É uma ação.", "Praticada ao ritmo de música."],
        "Telefone": ["É um objeto.", "Usado para comunicação à distância."],
        "Chuva": ["É um fenômeno natural.", "Cai do céu em forma de gotas."],
        "Cinema": ["É um lugar.", "Onde são exibidos filmes."],
        "Livro": ["É um objeto.", "Contém páginas com texto."],
        "Surpresa": ["É uma emoção.", "Causa choque ou admiração."],
        "Brinquedo": ["É um objeto.", "Usado para entretenimento."]
    }

    if tentativa == 1:
        return dicas[palavra][0]
    elif tentativa == 2:
        return dicas[palavra][1]


# Função para verificar o palpite do jogador
def verificar_palpite(palpite, palavra, tentativa):
    if palpite == palavra:
        messagebox.showinfo("Resultado", f"Parabéns! Você acertou a palavra: {palavra}")
        return True
    elif palpite == "Desistir":
        messagebox.showinfo("Resultado", f"Você desistiu. A palavra correta era: {palavra}")
        return True
    else:
        if tentativa == 3:
            messagebox.showinfo("Resultado", f"Suas tentativas acabaram. A palavra correta era: {palavra}")
            return True
        else:
            return False


# Função principal para jogar o jogo de mímica
def jogar_mimica():
    # Configurando a janela principal
    root = tk.Tk()
    root.title("ADIVINHE E GANHE")

    # Definindo cor de fundo rosa
    root.configure(bg='pink')

    # Título principal do jogo
    titulo = tk.Label(root, text="ADIVINHE E GANHE", font=("Arial", 46))
    titulo.pack()

    # Escolhendo uma palavra aleatória
    palavra = escolher_palavra()

    # Exibindo a duração da palavra
    label_palavra = tk.Label(root, text=f"A palavra escolhida é uma: {len(palavra)} letras")
    label_palavra.pack()

    tentativa = 1

    # Lista para armazenar as labels das dicas
    labels_dicas = []

    # Função para mostrar a próxima dica
    def proxima_dica():
        nonlocal tentativa
        if tentativa <= 2:
            # Exibir a dica correspondente à tentativa atual
            dica_texto = mostrar_dica(palavra, tentativa)
            label_dica = tk.Label(root, text=f"Dica {tentativa}: {dica_texto}")
            label_dica.pack()
            labels_dicas.append(label_dica)
            tentativa += 1
        else:
            messagebox.showinfo("Resultado", f"Suas tentativas acabaram. A palavra correta era: {palavra}")
            root.destroy()

    # Função para verificar o palpite do jogador
    def verificar():
        palpite = entry_palpite.get().capitalize()
        if verificar_palpite(palpite, palavra, tentativa):
            root.destroy()
        else:
            entry_palpite.delete(0, tk.END)
            proxima_dica()

    # Campo de entrada para o palpite do jogador
    entry_palpite = tk.Entry(root)
    entry_palpite.pack()

    # Botão para verificar o palpite
    button_verificar = tk.Button(root, text="Verificar", command=verificar)
    button_verificar.pack()

    # Exibir a primeira dica ao iniciar o jogo
    proxima_dica()

    # Iniciar a interface gráfica
    root.mainloop()


# Verificando se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    jogar_mimica()

import random
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

# Lista de palavras para o jogo
palavras = [
    "Cachorro",
    "Gato",
    "Computador",
    "Avião",
    "Bola",
    "Dança",
    "Telefone",
    "Chuva",
    "Cinema",
    "Livro",
    "Surpresa",
    "Brinquedo"
]


# Função para escolher uma palavra aleatória da lista
def escolher_palavra():
    return random.choice(palavras)


# Função para mostrar uma dica com base na tentativa atual
def mostrar_dica(palavra, tentativa):
    dicas = {
        "Cachorro": ["É um animal.", "Tem quatro patas."],
        "Gato": ["É um animal.", "Faz 'miau'."],
        "Computador": ["É um objeto.", "Usado para processamento de dados."],
        "Avião": ["É um objeto.", "Transporte aéreo."],
        "Bola": ["É um objeto.", "Usado em vários esportes."],
        "Dança": ["É uma ação.", "Praticada ao ritmo de música."],
        "Telefone": ["É um objeto.", "Usado para comunicação à distância."],
        "Chuva": ["É um fenômeno natural.", "Cai do céu em forma de gotas."],
        "Cinema": ["É um lugar.", "Onde são exibidos filmes."],
        "Livro": ["É um objeto.", "Contém páginas com texto."],
        "Surpresa": ["É uma emoção.", "Causa choque ou admiração."],
        "Brinquedo": ["É um objeto.", "Usado para entretenimento."]
    }

    if tentativa == 1:
        return dicas[palavra][0]
    elif tentativa == 2:
        return dicas[palavra][1]


# Função para verificar o palpite do jogador
def verificar_palpite(palpite, palavra, tentativa):
    if palpite == palavra:
        messagebox.showinfo("Resultado", f"Parabéns! Você acertou a palavra: {palavra}")
        return True
    elif palpite == "Desistir":
        messagebox.showinfo("Resultado", f"Você desistiu. A palavra correta era: {palavra}")
        return True
    else:
        if tentativa == 3:
            messagebox.showinfo("Resultado", f"Suas tentativas acabaram. A palavra correta era: {palavra}")
            return True
        else:
            return False


# Função principal para jogar o jogo de mímica
def jogar_mimica():
    # Configurando a janela principal
    root = tk.Tk()
    root.title("ADIVINHE E GANHE")

    # Carregar a imagem para o fundo
    imagem_fundo = PhotoImage(file="seu_fundo.png")

    # Definir a imagem como fundo usando um label
    fundo = tk.Label(root, image=imagem_fundo)
    fundo.place(x=0, y=0, relwidth=1, relheight=1)

    # Título principal do jogo
    titulo = tk.Label(root, text="ADIVINHE E GANHE", font=("Arial", 46))
    titulo.pack()

    # Escolhendo uma palavra aleatória
    palavra = escolher_palavra()

    # Exibindo a duração da palavra
    label_palavra = tk.Label(root, text=f"A palavra escolhida é uma: {len(palavra)} letras")
    label_palavra.pack()

    tentativa = 1

    # Lista para armazenar as labels das dicas
    labels_dicas = []

    # Função para mostrar a próxima dica
    def proxima_dica():
        nonlocal tentativa
        if tentativa <= 2:
            # Exibir a dica correspondente à tentativa atual
            dica_texto = mostrar_dica(palavra, tentativa)
            label_dica = tk.Label(root, text=f"Dica {tentativa}: {dica_texto}")
            label_dica.pack()
            labels_dicas.append(label_dica)
            tentativa += 1
        else:
            messagebox.showinfo("Resultado", f"Suas tentativas acabaram. A palavra correta era: {palavra}")
            root.destroy()

    # Função para verificar o palpite do jogador
    def verificar():
        palpite = e

