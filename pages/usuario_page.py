from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UsuarioPage(BasePage):

    _logo = {'by': By.CSS_SELECTOR, 'value': 'a.header__logo-jogatina'}
    _jogo_buraco = {'by': By.CSS_SELECTOR, 'value':
        'li.box-jogo.buraco-aberto.box-esquerda:nth-child(1) a:nth-child(1) > h3.titulo-jogo'}
    _jogo_domino = {'by': By.CSS_SELECTOR, 'value':
        'li.box-jogo.domino:nth-child(2) a:nth-child(1) > h3.titulo-jogo'}
    _jogo_bingo = {'by': By.CSS_SELECTOR, 'value':
        'li.box-jogo.bingo:nth-child(3) a:nth-child(1) > h3.titulo-jogo'}
    _jogo_tranca = {'by': By.CSS_SELECTOR, 'value':
        'li.box-jogo.tranca:nth-child(4) a:nth-child(1) > h3.titulo-jogo'}
    _jogo_truco = {'by': By.CSS_SELECTOR, 'value':
        'li.box-jogo.truco-paulista.box-esquerda:nth-child(5) a:nth-child(1) > h3.titulo-jogo'}
    _jogo_paciencia = {'by': By.CSS_SELECTOR, 'value':
        'li.box-jogo.paciencia:nth-child(6) > h3.titulo-jogo:nth-child(2)'}
    _jogo_poker = {'by': By.CSS_SELECTOR, 'value':
        'li.box-jogo.poker:nth-child(7) a:nth-child(1) > h3.titulo-jogo'}

    # botoes / icones / / cliques/ imagem
    _botao_cadastrar = {'by': By.CSS_SELECTOR, 'value': 'a.btn.btn-laranja.js-btn-cadastro'}
    _botao_criar_conta = {'by': By.CSS_SELECTOR, 'value': 'input.btn.btn-laranja.js-event-track'}
    _perfil_seta_baixo = {'by': By.CSS_SELECTOR, 'value': 'a.header__nav-profile-wrapper > i.caret'}
    _imagem = {'by': By.CSS_SELECTOR, 'value': 'div.footer__logo-reclame-aqui.fright > img:nth-child(1)'}
    _botao_entrar = {'by': By.CSS_SELECTOR, 'value': 'a.btn.btn-verde.header__btn-login.js-login-btn'}
    _botao_logar = {'by': By.CSS_SELECTOR, 'value': 'input.btn.btn-verde.btn-entrar.fright:nth-child(5)'}
    _clicar_ver_perfil = {'by': By.XPATH, 'value': "//a[contains(text(),'Ver meu Perfil')]"}
    _clicar_sair = {'by': By.XPATH, 'value': "//a[contains(text(),'Sair')]"}

    # email / senha / usuario
    _email = {'by': By.ID, 'value': 'emailIn'}
    _senha = {'by': By.ID, 'value': 'password-field'}
    _email_usuario = {'by': By.CSS_SELECTOR, 'value': 'div.header__subnav-info-email'}
    _email_login = {'by': By.ID, 'value': '#email-login'}
    _senha_login = {'by': By.ID, 'value': '#senha-login'}



    _localiza_perfil = {'by': By.CSS_SELECTOR, 'value': 'li.nav-secondary__item.active:nth-child(1)'}
    _clicar_editar_informacoes = {'by': By.XPATH, 'value': '/html[1]/body[1]/div[1]/div[2]/p[1]/a[1]'}

    _localiza_gerenciamento = {'by': By.CSS_SELECTOR, 'value': 'h1.titulo.titulo--pagina:nth-child(1)'}
    _botao_editar = {'by': By.CSS_SELECTOR, 'value': '#perfil .btn'}
    _muda_tela = {'by': By.CSS_SELECTOR, 'value': 'div:nth-child(1) > iframe.cboxIframe'}

    _cidade = {'by': By.ID, 'value': 'campo-new-city'}
    _estado = {'by': By.ID, 'value': 'campo-new-state'}
    _pais = {'by': By.ID, 'value': 'country'}
    _dia = {'by': By.ID, 'value': 'birthday'}
    _mes = {'by': By.ID, 'value': 'birthmonth'}
    _ano = {'by': By.ID, 'value': 'birthyear'}
    _genero = {'by': By.ID, 'value': 'mascGender'}

    _drop_pais = {'by': By.XPATH, 'value': "//option[. = 'Brasil']"}
    _drop_dia = {'by': By.XPATH, 'value': "//option[. = '2']"}
    _drop_mes = {'by': By.XPATH, 'value': "//option[. = 'Abril']"}
    _drop_ano = {'by': By.XPATH, 'value': "//option[. = '1988']"}

    _botao_alterar_perfil = {'by': By.CSS_SELECTOR, 'value': 'input.md-btn.md-btn--primary'}
    _mensagem_confirma_alteracao = {'by': By.TAG_NAME, 'value': 'span'}
    _clicar_fechar = {'by': By.CSS_SELECTOR, 'value': '"#cboxClose"'}

    _confirma_cidade = {'by': By.CSS_SELECTOR, 'value': 'div.opcoes--cadastro__descricao > label:nth-child(2)'}
    _confirma_pais = {'by': By.CSS_SELECTOR, 'value': 'div.opcoes--cadastro__descricao > label:nth-child(6)'}
    _confirma_genero = {'by': By.CSS_SELECTOR, 'value': 'div.opcoes--cadastro__descricao > label:nth-child(9)'}
    _confirma_nascimento = {'by': By.CSS_SELECTOR, 'value': 'div.opcoes--cadastro__descricao > label:nth-child(11)'}



    # Ações gerais

    def __init__(self, driver):
        self.driver = driver
        self._acessar('https://www.jogatina.com/')


    ##############

    def rolar_abaixo(self):
        self._rolar_abaixo()

    def rolar_acima(self):
        self._rolar_acima()

    ###### Asserts

    def localiza_logo(self):
        return self._encontrar(self._logo).text

    def localiza_buraco(self):
        return self._encontrar(self._jogo_buraco).text

    def localiza_domino(self):
        return self._encontrar(self._jogo_domino).text

    def localiza_bingo(self):
        return self._encontrar(self._jogo_bingo).text

    def localiza_tranca(self):
        return self._encontrar(self._jogo_tranca).text

    def localiza_truco(self):
        return self._encontrar(self._jogo_truco).text

    def localiza_paciencia(self):
        return self._encontrar(self._jogo_paciencia).text

    def localiza_poker(self):
        return self._encontrar(self._jogo_poker).text

    def clicar_botao_cadastrar(self):
        self._clicar(self._botao_cadastrar)

    def preencher_email_senha(self, email_campo, senha_campo):
        self._escrever(self._email, email_campo)
        self._escrever(self._senha, senha_campo)

    def clicar_botao_criacao_de_conta(self):
        self._clicar(self._botao_criar_conta)


    def validar_email_perfil(self):
        self._encontrar(self._imagem).is_displayed()
        self._clicar(self._perfil_seta_baixo)
        return self._encontrar(self._email_usuario).text

    def deslogar_da_conta(self):
        self._clicar(self._clicar_sair)


#########Dados perfil

    def clicar_botao_entrar(self, email_campo, senha_campo):
        self._clicar(self._botao_entrar)
        self._escrever(self._email_login, email_campo)
        self._escrever(self._senha_login, senha_campo)
        self._clicar(self._botao_logar)

    def clicar_em_ver_perfil(self):
        self._clicar(self._clicar_ver_perfil)

    def valida_perfil(self):
        return self._encontrar(self._localiza_perfil).text


    def validar_gerenciamento_de_conta(self):
        self._clicar(self._clicar_editar_informacoes)
        return self._encontrar(self._localiza_gerenciamento).text

    def clicar_editar_no_perfil(self):
        self._clicar(self._botao_editar)

    def muda_tela(self):
        self._encontrar(self._muda_tela)

    def localiza_formulario_e_preenche(self, cicade, estado):
        self._escrever(self._cidade, cicade)
        self._escrever(self._estado, estado)
        self._encontrar(self._pais)
        self._clicar(self._genero)
        self._encontrar(self._drop_pais)
        self._encontrar(self._dia)
        self._encontrar(self._drop_dia)
        self._encontrar(self._mes)
        self._encontrar(self._drop_mes)
        self._encontrar(self._ano)
        self._encontrar(self._drop_ano)

    def clico_no_botao_alterar(self):
        self._clicar(self._botao_alterar_perfil)
        return self._encontrar(self._mensagem_confirma_alteracao).text

    def clicar_fechar(self):
        self._clicar(self._clicar_fechar)

    def localiza_cidade(self):
        return self._encontrar(self._confirma_cidade).text

    def localiza_pais(self):
        return self._encontrar(self._confirma_pais).text

    def localiza_genero(self):
        return self._encontrar(self._confirma_genero).text

    def localiza_nascimento(self):
        return self._encontrar(self._confirma_nascimento).text

    def sair_da_conta(self):
        self._clicar(self._perfil_seta_baixo)
        return self._encontrar(self._email_usuario).text



