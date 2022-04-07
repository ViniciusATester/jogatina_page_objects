import os
import time

import pytest
from selenium import webdriver
from pages.usuario_page import UsuarioPage


@pytest.fixture
def usuario(request):
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')

    if os.path.isfile(_chromedriver):
        driver_ = webdriver.Chrome(_chromedriver)
    else:
        driver_ = webdriver.Chrome()
    usuarioPage = UsuarioPage(driver_)
    
    driver_.maximize_window()
    driver_.implicitly_wait(30)

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return usuarioPage


def test_usuario_usuario(usuario, logo_re='Jogatina.com', buraco_re='Buraco', domino_re="Dominó", bingo_re='Bingo',
                          tranca_re='Tranca', truco_re='Truco', paciencia_re='Paciência', poker_re='Poker',
                          email_re='viniciustester04@tester', senha_re='123123'):
    assert usuario.localiza_logo() == logo_re
    usuario.rolar_abaixo()
    time.sleep(3)
    assert usuario.localiza_buraco() == buraco_re
    assert usuario.localiza_domino() == domino_re
    assert usuario.localiza_bingo() == bingo_re
    assert usuario.localiza_tranca() == tranca_re
    assert usuario.localiza_truco() == truco_re
    assert usuario.localiza_paciencia() == paciencia_re
    assert usuario.localiza_poker() == poker_re
    usuario.rolar_acima()
    usuario.clicar_botao_cadastrar()
    time.sleep(3)
    usuario.preencher_email_senha(email_re, senha_re)
    time.sleep(3)
    usuario.clicar_botao_criacao_de_conta()

    assert usuario.validar_email_perfil() == email_re
    usuario.deslogar_da_conta()

def test_dados_perfil_usuario(usuario, perfil_re='Perfil', gerenciamento_re='Gerenciar Conta',
                               cidade= 'Cariacica', estado='Espirito Santo', email_re='viniciustester04@tester',
                              senha_re='123123'):
    usuario.clicar_botao_entrar(email_re, senha_re)
    usuario.validar_email_perfil()
    usuario.clicar_em_ver_perfil()
    assert usuario.valida_perfil() == perfil_re
    assert usuario.validar_gerenciamento_de_conta() == gerenciamento_re
    usuario.clicar_editar_no_perfil()
    usuario.muda_tela()
    usuario.localiza_formulario_e_preenche(cidade, estado)
    ###...
