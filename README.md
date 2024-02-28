# LP3 IFSP

Repositório para organizar os códigos da disciplina Linguagem de Programação 3.

## Instruções Lab de Informática

Ao chegar no laboratório:

Configurar o usuário do git

'''bash
git config --global user.name "seu nome"
git config -- global user.email "seu email@email.com"

Fazer o clone do seu repositório no GitHub

'''bash
git clone https://github.com/SEU_USUARIO/lp3-ifsp.git

Abrir o repo no VSCode
''' bash
code lp3-ifsp
'''

Criar um token para realizar os pushs
Settings -> Developer settings -> personal access tokens -> Tokens (classic)
Generate new token, selecionar a opção Generate new token classic, marcar a opção scope repo

## Antes de sair do laboratório
1- Remover configurações de usuário do git local
'''bash
git config  --global --unset user.name
git config  --global --unset user.email
'''

2- Deletar o token do GitHub

3