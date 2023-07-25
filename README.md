# Text-to-Image Generation

### Este projeto é uma implementação em Python de um modelo de geração de imagens baseado em texto usando um modelo pré-treinado. A estrutura do projeto segue o padrão Domain-Driven Design (DDD).

## Estrutura do Projeto

```
Aqui está a estrutura de alto nível do projeto:
├── application
├── domain
├── infrastructure
└── interface
```

1. **Camada de Aplicação (application)**: Aqui estão os comandos e handlers que lidam com as operações de alto nível, como treinar o modelo e gerar uma imagem.

2. **Camada de Domínio (domain)**: Aqui estão os modelos de domínio e os serviços que lidam com a lógica de negócios, como a lógica de treinamento do modelo e a lógica de geração de imagens.

3. **Camada de Infraestrutura (infrastructure)**: Aqui estão os repositórios e outros serviços de infraestrutura que lidam com a persistência de dados e outras operações de infraestrutura.

4. **Camada de Interface (interface)**: Aqui estão os controladores que lidam com a interação com o usuário, seja através de uma interface de linha de comando (CLI) ou de uma interface web.

## Instalação

1. Clone o repositório
2. Instale as dependências usando pip: `pip install -r requirements.txt`

## Como usar

### Treinar o modelo

Para treinar o modelo, execute o seguinte comando:

`python main.py train`

#### Isso iniciará o processo de treinamento do modelo. O progresso do treinamento será exibido na linha de comando.

### Gerar uma imagem

# Para gerar uma imagem a partir de um texto, execute o seguinte comando:

`python main.py generate "seu texto aqui`

### Isso iniciará o processo de geração de imagem e a imagem gerada será salva em seu diretório local.
