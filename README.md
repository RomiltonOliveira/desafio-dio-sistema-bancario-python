# desafio-dio-sistema-bancario-python

## Objetivo Geral 
Criar um sistema bancário com as operações:
*  Sacar
*  Depositar
*  Vizualizar Extrato

## Contextualização do Desafio
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar
suas operações e para isso escolheu a linguagem python. Para a primeira versão do sistema devemos implementar
apenas 3 operações: depósito, saque e extrato.

## Descrição da função "depósito"
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

## Descrição da função "saque"
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## Descrição da função "extrato"
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx
Exemplo:
1500.45 = R$ 1500.45

## Descrição da função "criar_usuario"
O programa deve armazenar usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro -bairro - cidade/sigla estado.
Deve ser armazenado somente os números do cpf. Não podemos cadastrar dois usuários com o mesmo cpf.

## Descrição da função "criar_conta"
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". o usuário pode
ter mais de uma conta, mas uma conta pertence a somente um usuário.
