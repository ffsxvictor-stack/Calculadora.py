import tkinter as tk
from tkinter import simpledialog, messagebox


# Criar a janela principal
janela = tk.Tk()
janela.title("calculadora")
janela.geometry("350x150")

def clicar_botao(valor):
    visor.insert(tk.END, valor)
    
def limpar():
    texto_visor = visor.get()
    
    if len(texto_visor) > 0:
        visor.delete(len(texto_visor) - 1, tk.END)

def limpar_tudo():
    visor.delete(0, tk.END)

def calcular():
    texto_visor = visor.get()

    if "+" in texto_visor:
        partes = texto_visor.split("+")
        resultado = sum(float(p) for p in partes)


    elif "-" in texto_visor:
        partes = texto_visor.split("-")
        resultado = float(partes[0])
        for parte in partes[1:]:
            resultado -= float(parte)
    
    elif "*" in texto_visor:
        partes = texto_visor.split("*")
        resultado = float(partes[0])
        for parte in partes[1:]:
            resultado *= float(parte)

    elif "/" in texto_visor:
        partes = texto_visor.split("/")
        resultado = float(partes[0])
        for parte in partes[1:]:
            divisor = float(parte)

            if divisor == 0:
                    messagebox.showerror("Erro", "Não é possível dividir por zero!")
                    return
            resultado /= divisor

    elif "%" in texto_visor:
        partes = texto_visor.split("%")
        num1 = float(partes[0])
        num2 = float(partes[1])
        resultado = num2 * (num1 / 100)

    else:
        return

    visor.delete(0, tk.END)
    visor.insert(tk.END, str(resultado))

visor = tk.Entry(janela, font=("Arial", 16), justify="right", bd=5, relief=tk.SUNSET if hasattr(tk, 'SUNSET') else tk.GROOVE)
visor.place(relx=0.5, rely=0.37, anchor=tk.CENTER, width=200, height=40)

# agrupar os botoes
quadro_botoes = tk.Frame(janela)
#centralizar janela 
quadro_botoes.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

botao0 = tk.Button(quadro_botoes, text="0", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("0"))
botao0.grid(row = 4,columnspan=2, sticky="we", column = 0, pady=0, padx = 0)

botao1 = tk.Button(quadro_botoes, text="1", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("1"))
botao1.grid(row = 1, column = 0, pady=0, padx = 0)

botao2 = tk.Button(quadro_botoes, text="2", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("2"))
botao2.grid(row = 1, column = 1, pady=0, padx = 0)

botao3 = tk.Button(quadro_botoes, text="3", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("3"))
botao3.grid(row = 1, column = 2, pady=0, padx = 0)

botao4 = tk.Button(quadro_botoes, text="4", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("4"))
botao4.grid(row = 2, column = 0, pady=0, padx = 0)

botao5 = tk.Button(quadro_botoes, text="5", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("5"))
botao5.grid(row = 2, column = 1, pady=0, padx = 0)

botao6 = tk.Button(quadro_botoes, text="6", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("6"))
botao6.grid(row = 2, column = 2, pady=0, padx = 0)

botao7 = tk.Button(quadro_botoes, text="7", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("7"))
botao7.grid(row = 3, column = 0, pady=0, padx = 0)

botao8 = tk.Button(quadro_botoes, text="8", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("8"))
botao8.grid(row = 3, column = 1, pady=0, padx = 0)

botao9 = tk.Button(quadro_botoes, text="9", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("9"))
botao9.grid(row = 3, column = 2, pady=0, padx = 0)

botaosoma = tk.Button(quadro_botoes, text="+", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("+"))
botaosoma.grid(row = 1, column = 3, pady=0, padx = 0)

botaomenos = tk.Button(quadro_botoes, text="-", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("-"))
botaomenos.grid(row = 2, column = 3, pady=0, padx = 0)

botaomultiplicacao = tk.Button(quadro_botoes, text="*", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("*"))
botaomultiplicacao.grid(row = 3, column = 3, pady=0, padx = 0)

botaodivisao = tk.Button(quadro_botoes, text="/", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("/"))
botaodivisao.grid(row = 0, column = 3, pady=0, padx = 0)

botaolimpar = tk.Button(quadro_botoes, text="C", width=5, height=1, font=("Arial", 10),command=limpar_tudo)
botaolimpar.grid(row = 0, column = 1, pady=0, padx = 0)

botaoporcentagem = tk.Button(quadro_botoes, text="%", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("%"))
botaoporcentagem.grid(row = 0, column = 2, pady=0, padx = 0)

botaoresultado= tk.Button(quadro_botoes, text="=", width=5, height=1, font=("Arial", 10),command=calcular)
botaoresultado.grid(row = 4, column = 3, pady=0, padx = 0)

botaoapagarum= tk.Button(quadro_botoes, text="CE", width=5, height=1, font=("Arial", 10),command=limpar)
botaoapagarum.grid(row = 0, column = 0, pady=0, padx = 0)

botaoponto = tk.Button(quadro_botoes, text=".", width=5, height=1, font=("Arial", 10),command=lambda: clicar_botao("."))
botaoponto.grid(row = 4, column = 2, pady=0, padx = 0)

# Loop principal da janela
janela.mainloop()
