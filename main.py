#importanto tkinter
from tkinter import *
from tkinter import ttk

#importanto pillow
from PIL import Image, ImageTk

#importando o requests
import requests

url_base = "https://pokeapi.co/api/v2/"

def buscar_poke(nome):
    url = f"{url_base}/pokemon/{nome.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        dado_pokemon = response.json()
        return dado_pokemon
    else:    
        print(f"Pokémon não encontrado! Erro {response.status_code}")
        return None

def abrir_dex():
    nome = entry_pokemon.get().strip()
    if not nome:
        mensagem.config(text="Por favor, digite o nome ou o ID do Pokémon.")
        return

    info_do_poke = buscar_poke(nome)
    if info_do_poke is None:
        mensagem.config(text="Pokémon não encontrado!")
        return 

    janela_inicio.destroy()

    mostrar_pokedex(info_do_poke)

#cores
cores = ["#2f2f44", "#feffff", "#6f9fbd", "#2d485b", "#403d3d", "#ee3c39"]

def mostrar_pokedex(info_do_poke):

    if info_do_poke:
        print(f"Nome: {info_do_poke['name'].capitalize()}")
        print(f"ID: {info_do_poke['id']}")
        print(f"Espécie: {info_do_poke['species']['name'].capitalize()}")
        print(f"Tipo: {info_do_poke['types'][0]['type']['name'].capitalize()}")

    sprite = info_do_poke['sprites']['front_default'] if info_do_poke else None

#separando as habilidades
    habilidades_comuns = []
    habilidade_hidden = None
    if info_do_poke:
        for habilidade in info_do_poke['abilities']:
            nome = habilidade['ability']['name'].capitalize()

            if habilidade['is_hidden']:
                habilidade_hidden = nome
            else:
                habilidades_comuns.append(nome)

#janela
    janela = Tk()
    janela.title("Pokédex")
    janela.geometry("600x540")
    janela.configure(bg=cores[1])

    ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

    style = ttk.Style(janela)
    style.theme_use("clam")

#frame
    frame_poke = Frame(janela, width=600, height=340, relief="flat")
    frame_poke.grid(row=1, column=0)

#nome do pokemon
    nome_poke = Label(frame_poke, text=f"Nome: {info_do_poke['name'].capitalize()}", relief="flat", anchor="center", font=("Fixedsys 30"), bg=cores[1], fg=cores[0])
    nome_poke.place(x=12, y=15)

#categoria do pokemon
    generation_poke = Label(frame_poke, text=f"Geração: {info_do_poke['game_indices'][0]['version']['name'].capitalize()}", relief="flat", anchor="center", font=("Ivy 15 bold"), bg=cores[1], fg=cores[0])
    generation_poke.place(x=12, y=60)

#Tipagem do pokemon
    tipo_poke = Label(frame_poke, text=f"Tipo: {info_do_poke['types'][0]['type']['name'].capitalize()}", relief="flat", anchor="center", font=("Ivy 10 bold"), bg=cores[1], fg=cores[0])
    tipo_poke.place(x=12, y=85)

#id do pokemon
    id_poke = Label(frame_poke, text=f"ID: {info_do_poke['id']}", relief="flat", anchor="center", font=("Ivy 10 bold"), bg=cores[1], fg=cores[0])
    id_poke.place(x=12, y=105)

#imagem do pokemon
    foto_poke = Image.open(requests.get(sprite, stream=True).raw)
    foto_poke = foto_poke.resize((250, 250))
    foto_poke = ImageTk.PhotoImage(foto_poke)

    imagem_poke = Label(frame_poke, image=foto_poke, relief="flat", bg=cores[1], fg=cores[0])
    imagem_poke.place(x=100, y=85)

    id_poke.lift()

#status
    status_poke = Label(janela, text=f"Status", relief="flat", anchor="center", font=("Verdana 20"), bg=cores[1], fg=cores[0])
    status_poke.place(x=15, y=350)

    hp_poke = Label(janela, text=f"HP: {info_do_poke['stats'][0]['base_stat']}", relief="flat", anchor="center", font=("Verdana 10"), bg=cores[1], fg=cores[0])
    hp_poke.place(x=12, y=390)

    atk_poke = Label(janela, text=f"Ataque: {info_do_poke['stats'][1]['base_stat']}", relief="flat", anchor="center", font=("Verdana 10"), bg=cores[1], fg=cores[0])
    atk_poke.place(x=12, y=410)

    def_poke = Label(janela, text=f"Defesa: {info_do_poke['stats'][2]['base_stat']}", relief="flat", anchor="center", font=("Verdana 10"), bg=cores[1], fg=cores[0])
    def_poke.place(x=12, y=430)

    sp_atk_poke = Label(janela, text=f"Ataque Especial: {info_do_poke['stats'][3]['base_stat']}", relief="flat", anchor="center", font=("Verdana 10"), bg=cores[1], fg=cores[0])
    sp_atk_poke.place(x=12, y=450)

    sp_def_poke = Label(janela, text=f"Defesa Especial: {info_do_poke['stats'][4]['base_stat']}", relief="flat", anchor="center", font=("Verdana 10"), bg=cores[1], fg=cores[0])
    sp_def_poke.place(x=12, y=470)

    speed_poke = Label(janela, text=f"Velocidade: {info_do_poke['stats'][5]['base_stat']}", relief="flat", anchor="center", font=("Verdana 10"), bg=cores[1], fg=cores[0])
    speed_poke.place(x=12, y=490)

#habilidades
    habilidade = Label(janela, text=f"Habilidades", relief="flat", anchor="center", font=("Verdana 20"), bg=cores[1], fg=cores[0])
    habilidade.place(x=300, y=350)

#habilidade 1
    if len(habilidades_comuns) > 0:

        habil_poke = Label(janela, text=habilidades_comuns[0], relief="flat", anchor="center", font=("Verdana 10"), bg=cores[1], fg=cores[0])
        habil_poke.place(x=300, y=390)


#habilidade 2
    if len(habilidades_comuns) > 1:

        habil_poke2 = Label(janela, text=habilidades_comuns[1], relief="flat", anchor="center", font=("Verdana 10"), bg=cores[1], fg=cores[0])
        habil_poke2.place(x=300, y=410)


#habilidade escondida
    if habilidade_hidden:

        hidden_habil_poke = Label(janela,text=f"Hidden: {habilidade_hidden}", relief="flat", anchor="center", font=("Verdana 10"), bg=cores[1], fg=cores[0])
        hidden_habil_poke.place(x=300, y=430)

#botôes
    botao_anterior = Button(frame_poke, text="Anterior", relief="raised", overrelief=RIDGE, anchor=NW, font=("Fixedsys 15"), bg=cores[0], fg=cores[1])
    botao_anterior.place(x=380, y=15)

    botao_proximo = Button(frame_poke, text="Próximo", relief="raised", overrelief=RIDGE, anchor=NW, font=("Fixedsys 15"), bg=cores[0], fg=cores[1])
    botao_proximo.place(x=500, y=15)

    janela.mainloop()

#janela inicial
janela_inicio = Tk()
janela_inicio.title("Pokédex")
janela_inicio.geometry("400x250")
janela_inicio.configure(bg=cores[1])

titulo = Label(janela_inicio, text="POKÉDEX", font=("Fixedsys 30"), bg=cores[1], fg=cores[0])
titulo.pack(pady=30)

label_pokemon = Label(janela_inicio, text="Digite o nome ou ID do Pokémon:", font=("Verdana 10"), bg=cores[1], fg=cores[0])
label_pokemon.pack()

entry_pokemon = Entry(janela_inicio, font=("Verdana 12"), width=25)
entry_pokemon.pack(pady=10)

mensagem = Label(janela_inicio, text="", font=("Verdana 9"), bg=cores[1], fg=cores[5])
mensagem.pack()

botao_buscar = Button(janela_inicio, text="BUSCAR", command=abrir_dex, font=("Fixedsys 15"), bg=cores[0], fg=cores[1])
botao_buscar.pack(pady=15)

janela_inicio.mainloop()
