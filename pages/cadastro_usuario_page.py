from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CadastroPage(BasePage):
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

    # botoes / icones / imagem
    _botao_cadastrar = {'by': By.CSS_SELECTOR, 'value': 'a.btn.btn-laranja.js-btn-cadastro'}
    _botao_criar_conta = {'by': By.CSS_SELECTOR, 'value': 'input.btn.btn-laranja.js-event-track'}
    _perfil_seta_baixo = {'by': By.CSS_SELECTOR, 'value': 'a.header__nav-profile-wrapper > i.caret'}
    _imagem = {'by': By.CSS_SELECTOR, 'value': 'div.footer__logo-reclame-aqui.fright > img:nth-child(1)'}
    _clicar_sair = {'by': By.XPATH, 'value': "//a[contains(text(),'Sair')]"}

    # email / senha / usuario
    _email = {'by': By.ID, 'value': 'emailIn'}
    _senha = {'by': By.ID, 'value': 'password-field'}
    _email_usuario = {'by': By.CSS_SELECTOR, 'value': 'div.header__subnav-info-email'}

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



