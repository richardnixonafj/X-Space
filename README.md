# Desafio_Zapay

Aplicação disponível em: https://desafiozapay.herokuapp.com/

Repositório criado para resolver o desafio proposto pela empresa Zapay para vaga de python Dev.

[![GitHub issues](https://img.shields.io/github/issues/richardnixonafj/Desafio_Zapay.svg)](https://github.com/richardnixonafj/Desafio_Zapay/issues)
[![codecov](https://codecov.io/gh/richardnixonafj/Desafio_Zapay/branch/master/graph/badge.svg)](https://codecov.io/gh/richardnixonafj/Desafio_Zapay)
[![GitHub license](https://img.shields.io/github/license/richardnixonafj/Desafio_Zapay.svg)](https://github.com/richardnixonafj/Desafio_Zapay)
[![Build Status](https://travis-ci.org/richardnixonafj/Desafio_Zapay.svg?branch=master)](https://travis-ci.org/richardnixonafj/Desafio_Zapay)
[![Updates](https://pyup.io/repos/github/richardnixonafj/Desafio_Zapay/shield.svg)](https://pyup.io/repos/github/richardnixonafj/Desafio_Zapay/)
[![Python 3](https://pyup.io/repos/github/richardnixonafj/Desafio_Zapay/python-3-shield.svg)](https://pyup.io/repos/github/richardnixonafj/Desafio_Zapay/)


Segui os principios de "Twelve-Factor App" https://12factor.net/ para o desenvolvimento do desafio.

* Utilizando o git como controlador de versao, implementado um deploy automatico com entrega continua integrando o github, e o Heroku.
* A Aplicação foi construida com o Framework Django, o proprio framework ja segue um padrao 
de MVC.

* Seguindo a convenção da PEP 257, adicionamos varios Docstrings para documentar a semantica da aplicação.

* Travis CI foi utilizado para configurar a integração continua. 
* Utilizamos a ferramenta **PIPENV** e foram declaradas e isoladas as dependências do sistema, utilizando os arquivos 
  Pipfile e Pipfile.lock para garantir a consistência das fontes de onde estamos buscando as libs.
* Foi separado o processo de Linter com Frake8 (https://pypi.org/project/flake8/).
* Teste Unitário com Pytest(https://docs.pytest.org/en/latest/).
* Cobertura de Testes com o CODECOV.
* A aplicação não armazena estado, nenhum elementos depedende de armazenamento, é possivel restartar a aplicação a qualquer momento.
* Foi realizada a integração de Deploy automatico no Heroku.
* Gerenciamento do update das libs com Pyup, pro garantir que nossas libs da aplicação se mantenham sempre atualizadas.
* Nao existe nenhuma tarefa pesada no processo de inicialização/desligamento do servidor da aplicação o que dentro do
 do conceito de 12 factor é chamado de Descartabilidade.
* Foi criada uma cobertura de testes para as rotinas de consulta pedidas no desafio.`Desafio_Zapay/spacex/base/tests/`



### Rodando o projeto localmente

1. Clone o repositório digitando `$ git clone https://github.com/richardnixonafj/Desafio_Zapay.git` no Gitbash.
2. Vá até a pasta onde você clonou o repositório em seu computador.
3. instale o pipenv `$ pip install pipenv` e depois execute `$ pipenv install` no Terminal.
4. instale as dependencias do Pyramid, digite: `$ pip install -d .`
5. Digite: `$ pipenv shell` para ativar o ambiente virtual.
6. Com o ambiente virtual ativo digite: `python manage.py runserver`
3. Abra o seu navegador e digite `http://127.0.0.1:8000/`. Se tudo der certo você conseguirá ver a aplicação rodando.


##### Comentários do candidato:


