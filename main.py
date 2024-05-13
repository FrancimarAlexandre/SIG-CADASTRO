import customtkinter as ctk# importando a biblioteca

# class App Principal
class App():
    def __init__(self):
        self.janela = janela
        self.TabViews()
        self.TelaInicial()

        self.janela.mainloop() # loop principal da janela
    
    def TabViews(self):
        # criando e posicionando as telas das abas
        self.tabview = ctk.CTkTabview(self.janela,width=1230,height=710,bg_color="#444444")
        self.tabview.place(x=10,y=35)
        # criando as títulos das abas
        self.inicio_tab = self.tabview.add("Cadastro")
        self.transicoes_tab = self.tabview.add("exibir cadastros")
        self.saldo_tab = self.tabview.add("créditos")


    def TelaInicial(self):
        # Nome usuário
        self.LabelNome = ctk.CTkLabel(self.inicio_tab,text="Nome",font=("moderna",20)).place(relx=0.01,rely=0.01)
        self.EntryNome = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryNome.place(relx=0.01,rely=0.05,relwidth=0.55)
        # Idade usuário
        self.LabelIdade = ctk.CTkLabel(self.inicio_tab,text="Idade",font=("moderna",20)).place(relx=0.58,rely=0.01)
        self.EntryIdade = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryIdade.place(relx=0.58,rely=0.05,relwidth=0.05)
        # Email usuário
        self.LabelNome = ctk.CTkLabel(self.inicio_tab,text="Gmail",font=("moderna",20)).place(relx=0.01,rely=0.1)
        self.EntryNome = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryNome.place(relx=0.01,rely=0.15,relwidth=0.55)
if "__main__":
    janela = ctk.CTk() # criando janela

    janela._set_appearance_mode('dark') # definindo tema da tela

    janela.geometry('1250x750') # definindo tamanho da tela 

    janela.title("SIG - CADASTRO") # definindo titilo na aplicação

    janela.resizable(width=False,height=False) # definindo que a tela vai ter o tamanho fixo
    App()