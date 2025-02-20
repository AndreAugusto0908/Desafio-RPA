# Desafio-RPA
Criação de código em Python para checagem de estatísticas de empresas no Reclame Aqui

# Como realizei a solução

Para desenvolver o projeto, comecei analisando a documentação do Selenium, a principal biblioteca utilizada. Após visualizar parte da documentação, decidi iniciar o desenvolvimento.

No começo, consegui coletar as notas das empresas sem dificuldades. No entanto para conseguir informações detalhadas das melhores e piores empresas, ao tentar acessar mais que uma url do Reclame Aqui dentro do mesmo navegador, comecei a ser barrado pela verificação de robô. Depois de várias tentativas frustradas de contornar essa verificação, tive a ideia de abrir um novo navegador para cada empresa pesquisada. Dessa forma, evitei o bloqueio e consegui continuar a coleta de dados.

Após implementar essa lógica para coletar informações detalhadas de todas as empresas desejadas e testar se tudo estava funcionando corretamente, percebi que precisava classificar as empresas com nota 0. Como há muitas empresas com essa nota, defini que a pior empresa seria aquela com o maior número de solicitações no Reclame Aqui.

Assim, o código percorre todas as empresas com nota 0, analisando uma por uma, o que torna a execução um pouco demorada. O objetivo é encontrar as três empresas com mais solicitações e nota 0.

Por fim, depois de coletar os dados das três melhores e três piores empresas, salvo essas informações em uma planilha, incluindo a data e hora da extração.

# Organização de Codigo

Organizei meu código em um padrão semelhante ao MVC simplificado, separando as responsabilidades em diferentes diretórios. O diretório Models contém as classes que representam os dados do sistema, Services armazena os serviços responsáveis por operações sobre esses dados, e Utils reúne funções auxiliares e reutilizáveis em todo o sistema.

Além disso, documentei todas as funções para facilitar futuras manutenções e ajudar outros desenvolvedores na compreensão do código.

# Como rodar

Primeiramente será necessaria a intalação do ChromeDriver, após intalação do ChromeDriver adicione o aquivo que vem no zip junto ao arquivo .exe do Python

Entre no Diretório do Projeto utilizando

-  cd BuscaReclameAqui

Crie um ambiente virtual

- py -m venv .venv

Instale as dependencias

- pip install pandas selenium webdriver-manager

Execute o arquivo principal

- py main.py
d
