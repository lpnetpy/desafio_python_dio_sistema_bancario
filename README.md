# Primeiro Desafio Python sistema bancário simples
# Sistema Bancário em Python

Projeto desenvolvido como desafio de aprendizado (DIO), simulando as operações básicas de um sistema bancário via terminal: depósito, saque, extrato e consulta de saldo.

---

## Funcionalidades

| Opção | Ação |
|:---:|---|
| `d` | Depositar — adiciona valores ao saldo da conta |
| `s` | Sacar — retira valores do saldo, respeitando limites de segurança |
| `e` | Extrato — exibe o histórico de movimentações e o saldo atual |
| `c` | Saldo — consulta rápida do saldo disponível |
| `q` | Sair — encerra o programa |

---

## Regras de negócio

- O valor de depósito deve ser **maior que zero**
- O valor de saque deve ser **maior que zero**
- Cada saque está limitado a **R$ 500,00**
- São permitidos no máximo **3 saques** por execução
- Não é possível sacar um valor **maior que o saldo disponível**

---

## Como executar

Pré-requisito: ter o [Python 3](https://www.python.org/downloads/) instalado.

```bash
python desafio.py
```

Ao rodar, um menu interativo será exibido no terminal:

```
[d] Depositar
[s] Sacar
[e] Extrato
[c] Saldo
[q] Sair
```

Basta digitar a letra correspondente à opção desejada e seguir as instruções.

---

## Estrutura do código

O projeto é organizado em funções, cada uma responsável por uma operação:

| Função | Responsabilidade |
|---|---|
| `deposito(valor)` | Realiza o depósito e atualiza o extrato |
| `saque(valor)` | Valida e realiza o saque, respeitando os limites |
| `mostrar_extrato()` | Exibe o histórico de movimentações e o saldo |

---

## Melhorias futuras

- Refatorar as funções para não depender de variáveis globais (`global`), utilizando parâmetros e retorno (`return`) para deixar o código mais testável e reutilizável
- Adicionar suporte a múltiplas contas e usuários
- Persistir os dados em arquivo ou banco de dados, para manter o histórico entre execuções
- Criar testes automatizados para validar as regras de negócio

---

## Tecnologias

- Python 3

---

## Licença

Projeto livre para fins de estudo.
