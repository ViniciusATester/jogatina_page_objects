import os
import time

import pytest
from selenium import webdriver
from pages.cadastro_usuario_page import CadastroPage


@pytest.fixture
def cadastro(request):
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')

    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome(_chromedriver)
    else:
        driver_ = webdriver.Chrome()
    cadastroPage = CadastroPage(driver_)

    driver_.maximize_window()
    driver_.implicitly_wait(30)

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return cadastroPage


def test_cadastro_usuario(cadastro, logo_re='Jogatina.com', buraco_re='Buraco', domino_re="Dominó", bingo_re='Bingo',
                          tranca_re='Tranca', truco_re='Truco', paciencia_re='Paciência', poker_re='Poker',
                          email_re='viniciustester04@tester', senha_re='123123'):
    assert cadastro.localiza_logo() == logo_re
    cadastro.rolar_abaixo()
    time.sleep(3)
    assert cadastro.localiza_buraco() == buraco_re
    assert cadastro.localiza_domino() == domino_re
    assert cadastro.localiza_bingo() == bingo_re
    assert cadastro.localiza_tranca() == tranca_re
    assert cadastro.localiza_truco() == truco_re
    assert cadastro.localiza_paciencia() == paciencia_re
    assert cadastro.localiza_poker() == poker_re
    cadastro.rolar_acima()
    cadastro.clicar_botao_cadastrar()
    time.sleep(3)
    cadastro.preencher_email_senha(email_re, senha_re)
    time.sleep(3)
    cadastro.clicar_botao_criacao_de_conta()

    assert cadastro.validar_email_perfil() == email_re
    cadastro.deslogar_da_conta()

