Dashboard de Reclamações em Python com Streamlit, Panda e Plotly
Este projeto desenvolve um dashboard interativo de reclamações, utilizando o Streamlit como framework de implantação e integrando as bibliotecas Pandas e Plotly para a manipulação e visualização dos dados. O objetivo é oferecer uma análise interativa das reclamações, possibilitando filtragens, agrupamentos e gráficos dinâmicos, o que facilita a compreensão das tendências e categorias das reclamações.

Introdução
O dashboard proporciona uma visualização interativa das reclamações, permitindo que os usuários explorem os dados de maneira intuitiva. Com gráficos de distribuição e séries temporais, ele também oferece opções de filtragem por categorias, datas e níveis de severidade das reclamações. A interface é intuitiva e foi projetada para facilitar a análise dos dados por qualquer usuário, independentemente de seu nível de experiência.


Requisitos
Python 3.12
Pandas
Plotly
Streamlit

Instalação
Para rodar este projeto localmente, siga os seguintes passos:

Clone o repositório:

git clone (https://github.com/thiagopintopereira/ReclameAquiEstudo)
Navegue até o diretório do projeto:

cd ReclameAquiEstudo
Crie um ambiente virtual e ative-o:

python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
Instale as dependências:

pip install -r requirements.txt
Como Executar o Projeto
Para executar o dashboard localmente, basta rodar o comando abaixo:

streamlit run streamlit_app.py
