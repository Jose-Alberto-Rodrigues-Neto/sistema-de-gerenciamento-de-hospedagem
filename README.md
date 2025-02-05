# Visão Geral do Projeto

Este projeto tem como objetivo o desenvolvimento de um Sistema de Gerenciamento de Hospedagem em Hotéis, utilizando a linguagem Python e uma interface textual. A atividade proporcionará aos alunos uma experiência prática no uso da lógica de programação.

A turma será dividida em quatro equipes, cada uma responsável por um módulo essencial do sistema. A entrega final consistirá no código-fonte funcional, e os times deverão garantir a comunicação adequada entre os módulos para o bom funcionamento do sistema.

## Estrutura do Sistema e Equipes

O sistema será dividido em quatro módulos principais, cada um atribuído a uma equipe específica:

### Equipe 1: Interface e Dashboard

Responsável por desenvolver a interface textual, garantindo uma navegação intuitiva pelo sistema.

- Criará `menus`, receberá `entradas do usuário` e exibirá as informações de maneira clara.
- Também será responsável pelo `Dashboard`, que mostrará `relatórios e estatísticas` do hotel, como `número de hóspedes ativos`, `quartos disponíveis` e `histórico de check-ins` e `check-outs`.
- Deve garantir que os dados sejam apresentados de maneira organizada e compreensível.

Interface/Dashboard

-    Johnny Ferreira
-    Ana Karoline
-    Ingrid Stephanye
-    Pablo Miguel
-    Thaynara Alice
-    Jorge Henrique
-    Rayana Lima
-    Maria Larissa
-    Luan Nascimento
-    Radmilly Brito
-    Marianna Onofre
-    Francisco Diemes
-    Francisco Willame
-    Maurício Gonçalves
-    Rafael Viana
-    Keven Gonçalves

### Equipe 2: Integração

Será responsável pela comunicação entre os módulos do sistema.

- Garantirá que os dados fluam corretamente entre os diferentes componentes, permitindo que a Interface, Entrada e Saída de Hóspedes funcionem sem falhas.
- Definirá `estruturas de dados padronizadas` para que todos os módulos utilizem o mesmo formato de informações.
- Implementará `funções para armazenar e recuperar informações`, garantindo a persistência temporária dos dados.

#### Equipe

Integração

-    Juliana Morais
-    Pedro Sávio
-    Bruno Henrique
-    Ingrid Oliveira
-    Raul Maia
-    Pedro Leandro
-    José Alberto
-    Paulo Henrique

### Equipe 3: Entrada de Hóspedes

Criará as funcionalidades de check-in

- `Registrar novos hóspedes` no sistema.
- Cada hóspede deve ser `cadastrado` com informações básicas como `nome`, `número do quarto`, `data de entrada` e `status da hospedagem`.
- Deve se comunicar corretamente com a Integração, garantindo que os dados sejam armazenados corretamente e possam ser acessados pelos outros módulos.
- Possíveis validações, como `verificar se um quarto está disponível` antes de registrar um novo hóspede.

#### Equipe

Entrada de Hóspedes (Check-in)

-    Pedro Lucas
-    Thiago Torres
-    Geovanna Angelino
-    José Alberto
-    Caio Jordan
-    José Pedro
-    Lucas Duarte

### Equipe 4: Saída de Hóspedes

Desenvolverá o sistema de check-out 

- Atualizando o `status do hóspede` quando ele deixar o hotel.
- Implementará o `cálculo do valor da estadia` com base no `tempo de permanência` (se aplicável).
- Deve garantir que a Integração receba corretamente os dados atualizados, `removendo o hóspede` da lista de ativos e `armazenando-o no histórico de hóspedes`.

#### Equipe

Saída de Hóspedes (Check-out)

-    Marcos Emanuel
-    Kainan Crescelino

# Como rodar o projeto?

Instale as dependências usando o poetry

```python
    poetry install
```
Rode o porjeto usando o poetry

```python
    poetry run python src/main.py
```

ou, caso não tenha o poetry baixado

```python
    python src/main.py
```