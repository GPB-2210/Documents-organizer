# Documents Organizer

Um organizador simples de arquivos feito em Python. Ele ajuda a separar os arquivos de uma pasta por tipo ou pela data da última modificação.

## Funcionalidades

- Organiza arquivos por categoria: imagens, vídeos, documentos, músicas, código, arquivos compactados e outros.
- Organiza arquivos em pastas com a data da última modificação, no formato AAAA-MM-DD.
- Mostra uma prévia antes de mover qualquer arquivo.
- Evita sobrescrever arquivos: quando já existe um arquivo com o mesmo nome, acrescenta um número ao novo nome.
- Ignora arquivos de configuração INI e processa somente os demais arquivos diretamente na pasta escolhida; não percorre subpastas.

## Requisitos

- Python 3
- Tkinter disponível na instalação do Python

## Como usar

1. Baixe ou clone este repositório.
2. Abra um terminal na pasta do projeto.
3. Execute:

   ~~~bash
   python main.py
   ~~~

4. Selecione a pasta que deseja organizar.
5. Escolha organizar por tipo ou por data de modificação.
6. Confira a prévia. Digite s para confirmar; qualquer outra resposta cancela a operação.

No Windows, se o comando python não funcionar, tente py main.py.

## Dica de segurança

Na primeira utilização, teste com uma pasta contendo cópias de alguns arquivos. O programa move arquivos depois da confirmação e não tem uma função automática para desfazer a operação.

## Próximas melhorias possíveis

- Permitir que o usuário escolha ou edite as categorias e extensões.
- Adicionar uma opção para organizar por data de criação, quando o sistema operacional oferecer essa informação de forma adequada.
