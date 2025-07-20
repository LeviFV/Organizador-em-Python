# Organizador de Arquivos Automático 📂✨

Um script Python simples, mas poderoso, para organizar automaticamente os arquivos de uma pasta (como a sua pasta de Downloads) em subpastas categorizadas por tipo de arquivo. Chega de bagunça digital!

# 📌 Sobre o Projeto

Sua pasta de Downloads vive lotada e desorganizada? Este projeto foi criado para resolver exatamente esse problema. Ele é um excelente exemplo de como a automação com Python pode simplificar tarefas do dia a dia. O script verifica cada arquivo em um diretório específico e o move para uma pasta correspondente à sua categoria (Imagens, Documentos, Vídeos, etc.), deixando tudo limpo e fácil de encontrar.



# ✨ Funcionalidades:

📂 Organização por Tipo: Move arquivos para pastas pré-definidas com base em sua extensão.

🤖 Automação: Executa uma tarefa repetitiva de forma rápida e sem intervenção manual.

🔧 Fácil de Personalizar: Adicione novas pastas e extensões de arquivo editando apenas um dicionário no código.

♻️ Lógica de "Outros": Arquivos com extensões não mapeadas são movidos para uma pasta "Outros", garantindo que nada seja deixado para trás.



# 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando apenas Python 3 e suas bibliotecas padrões:

- Python 3

- Biblioteca os: Para interagir com o sistema operacional (criar pastas, listar arquivos).

- Biblioteca shutil: Para realizar operações de alto nível em arquivos, como movê-los.



# 🚀 Como Executar
Para executar este projeto localmente, siga os passos abaixo:

- Clone o repositório

- git clone https://github.com/LeviFV/Organizador-em-Python.git

- Configure o caminho

- Abra o arquivo organizador.py.

- Na linha 8, altere a variável caminho_para_organizar para o caminho da pasta que você deseja organizar.

## Exemplo para Windows

caminho_para_organizar = "C:/Users/SeuUsuario/Downloads"

## Exemplo para macOS ou Linux

caminho_para_organizar = "/home/SeuUsuario/Downloads"

- Execute o script

Abra o seu terminal, navegue até a pasta do projeto e execute o seguinte comando:

python organizador.py

Pronto! Seus arquivos serão organizados.


### Feito por Levi Vieira.
