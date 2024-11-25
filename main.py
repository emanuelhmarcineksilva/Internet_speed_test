# Importando Tkinter
from tkinter import*

# Importando pillow
from PIL import Image, ImageTk

# Cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#fc766d"  # vermelha / red
co4 = "#403d3d"   # preta / black
co5 = "#4a88e8"  # Azul / Bblue

# Criando janela

# O Tk() é uma classe do módulo Tkinter, que é a biblioteca padrão de interface gráfica (GUI) para o Python. Isso significa que está sendo criada uma janela principal de uma aplicação gráfica utilizando o Tkinter.
janela = Tk()
# O 'title' é o titulo da janela
janela.title("")
# O 'geometry' é as dimenções da janela, ('largura x altura')
janela.geometry('350x200')
# O 'configure' muda a configuração da janela, 'bg' é background
janela.configure(bg=co1)
# O código abaixo bloqueia que o tamanho da janela seja alterado, ela não fica em tela cheia
janela.resizable(width=False, height=False)

# Dividindo a janela em 2 frames

frame_logo = Frame(janela, width=350, height=60, bg=co1)
# O 'grid' permite escolher onde vai ficar o frame, qual coluna e qual linha. O método .grid() no Tkinter é utilizado para posicionar os widgets dentro de um layout de grid (tabela) em uma janela.
# O 'pady' espaço no eixo y e o 'padx' um espaço no eixo x
# O 'sticky' alinha como sera o frame na janela. Você pode usá-lo para fazer o widget se alinhar à esquerda, direita, cima, baixo ou em todas as direções dentro da janela. sticky='nsew': Faz o widget se expandir para preencher toda a janela, ocupando todo o espaço.
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=138, bg=co1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando frame_logo
# Lembrar de colocar letra maiuscula em 'Image' antes do 'open()'
imagem = Image.open('speed.png')
# O método resize() é usado para redimensionar uma imagem no Python, quando você trabalha com a biblioteca Pillow (a versão atualizada da PIL). Ele altera as dimensões da imagem (largura e altura) para um novo tamanho especificado.
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)
# O 'image' adiciona uma imagem ao Label.
# O 'compound'controla a posição do texto em relação à imagem (se houver). O valor LEFT significa que a imagem será à esquerda do texto (se houver texto).
# O 'anchor' controla o alinhamento do conteúdo dentro do Label, ou seja, como o conteúdo (imagem ou texto) é posicionado em relação à área do Label. 'nw' significa "norte-oeste" (ou seja, canto superior esquerdo).
# O 'fg' define a cor do texto na label
l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold '), bg=co1, fg=co3)
# o 'place' é como cordenadas de onde ficará o que escolheu colocar o place, aqui no caso é a logo
l_logo_imagem.place(x=20, y=0)

# Fazendo o título
l_logo_nome = Label(frame_logo, text='internet speed test', padx=10, anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
l_logo_nome.place(x=75, y=10)

# Fazendo a linha
l_logo_linha = Label(frame_logo, width=350, anchor=NW, font=('Ivy 1'), bg=co2)
l_logo_linha.place(x=0, y=57)

# Configurando o frame_corpo

l_download = Label(frame_corpo, text='65.7', anchor=NW, font=('arial 28'), bg=co1, fg=co4)
l_download.place(x=44, y=25)

l_download = Label(frame_corpo, text='Mbps download', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_download.place(x=32, y=70)


# l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold '), bg=co1, fg=co3)
# l_logo_imagem.place(x=20, y=0)

# l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold '), bg=co1, fg=co3)
# l_logo_imagem.place(x=20, y=0)


down = Image.open('down.png')
down = down.resize((55,55))
down = ImageTk.PhotoImage(down)

up = Image.open('up.png')
up = up.resize((55,55))
up = ImageTk.PhotoImage(up)


# Esse 'mainloop()' fala ao programa para entrar no loop de eventos da interface gráfica do tkinter. O app começa a rodar e a perceber eventos.
janela.mainloop()
