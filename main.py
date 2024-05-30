import customtkinter as ctk# importando a biblioteca
from funcs import DataBase
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
        # Dados Pessoais
        self.LabelInfoDadosPessoais = ctk.CTkLabel(self.inicio_tab,text="DADOS PESSOAIS",font=("moderna",20)).place(relx=0.35,rely=0.01)
        # Nome usuário
        self.LabelNome = ctk.CTkLabel(self.inicio_tab,text="Nome",font=("moderna",20)).place(relx=0.01,rely=0.02)
        self.EntryNome = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryNome.place(relx=0.01,rely=0.06,relwidth=0.55)
        # Idade usuário
        self.LabelIdade = ctk.CTkLabel(self.inicio_tab,text="Idade",font=("moderna",20)).place(relx=0.58,rely=0.02)
        self.EntryIdade = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryIdade.place(relx=0.58,rely=0.06,relwidth=0.05)
        # Email usuário
        self.LabelGmail = ctk.CTkLabel(self.inicio_tab,text="Gmail",font=("moderna",20)).place(relx=0.01,rely=0.11)
        self.EntryGmail = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryGmail.place(relx=0.01,rely=0.16,relwidth=0.55)
        # Telefone usuário
        self.LabelTelefone = ctk.CTkLabel(self.inicio_tab,text="Telefone",font=("moderna",20)).place(relx=0.58,rely=0.11)
        self.EntryTelefone = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryTelefone.place(relx=0.58,rely=0.16,relwidth=0.20)
        
        # Endereço
        self.LabelInfoDadosPessoais = ctk.CTkLabel(self.inicio_tab,text="ENDEREÇO",font=("moderna",20)).place(relx=0.35,rely=0.23)
        # RUA
        self.LabelRua = ctk.CTkLabel(self.inicio_tab,text="Rua",font=("moderna",20)).place(relx=0.01,rely=0.24)
        self.EntryRua = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryRua.place(relx=0.01,rely=0.29,relwidth=0.4)
        # BAIRRO
        self.LabelBairro = ctk.CTkLabel(self.inicio_tab,text="Bairro",font=("moderna",20)).place(relx=0.5,rely=0.24)
        self.EntryBairro = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryBairro.place(relx=0.5,rely=0.29,relwidth=0.4)
        # CIDADE
        self.LabelCidade = ctk.CTkLabel(self.inicio_tab,text="Cidade",font=("moderna",20)).place(relx=0.01,rely=0.34)
        self.EntryCidade = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryCidade.place(relx=0.01,rely=0.39,relwidth=0.4)
        # ESTADO
        self.LabelEstado = ctk.CTkLabel(self.inicio_tab,text="Estado",font=("moderna",20)).place(relx=0.5,rely=0.34)
        self.EntryEstado = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryEstado.place(relx=0.5,rely=0.39,relwidth=0.4)
        # NÙMERO
        self.LabelNumero = ctk.CTkLabel(self.inicio_tab,text="N°",font=("moderna",20)).place(relx=0.01,rely=0.44)
        self.EntryNumero = ctk.CTkEntry(self.inicio_tab,font=("mordena",20))
        self.EntryNumero.place(relx=0.01,rely=0.49,relwidth=0.05)
        self.ButtonCadastro = ctk.CTkButton(self.inicio_tab,text="CADASTRAR",font=("moderna",20),command=self.convert_dados).place(relx = 0.45,rely=0.55,relwidth=0.1)

    def convert_dados(self):
        self.nome = self.EntryNome.get()
        self.email = self.EntryGmail.get()
        self.idade = self.EntryIdade.get()
        self.rua = self.EntryRua.get()
        self.bairro = self.EntryBairro.get()
        self.cidade = self.EntryCidade.get()
        self.estado = self.EntryEstado.get()
        self.numero = self.EntryNumero.get()

        print(self.nome)
        
        a = DataBase()
        return a.insert_dados(self.nome,self.email,self.idade,self.rua,self.bairro,self.cidade,self.estado,self.numero)
if "__main__":
    janela = ctk.CTk() # criando janela

    janela._set_appearance_mode('dark') # definindo tema da tela

    janela.geometry('1250x750') # definindo tamanho da tela 

    janela.title("SIG - CADASTRO") # definindo titilo na aplicação

    janela.resizable(width=False,height=False) # definindo que a tela vai ter o tamanho fixo
    App()