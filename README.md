🚀 Funcionalidades da API

✅ Cadastro e gerenciamento de usuários (Admin, Auditor, Líder de Setor)  
✅ Registro e gestão de setores da empresa  
✅ Cadastro de Itens Padrão separados por cada "S" (Seiri, Seiton, Seiso, Seiketsu, Shitsuke)  
✅ Auditorias completas com checklist por item  
✅ Acompanhamento de Rankings e performance dos setores  
✅ Histórico de pendências e ações corretivas aplicadas  

⚡ Instalação e Execução Local
# Clone o repositório
git clone https://github.com/Jorgelzz/Kaizen-backend.git
cd organiza-ai-backend
# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
# Instale as dependências
pip install -r requirements.txt
# Configure as variáveis de ambiente (.env)
cp .env.example .env
# Execute as migrações
python manage.py migrate

# Crie um superusuário para acessar o admin
python manage.py createsuperuser

# Inicie o servidor de desenvolvimento
python manage.py runserver
Acesse o painel administrativo: http://localhost:8000/admin


✔️ Monitoramento estruturado das práticas de organização e disciplina
✔️ Facilidade na aplicação de checklists separados por cada "S"
✔️ Comparativo entre setores e rankings automáticos
✔️ Histórico de ações corretivas para promover melhoria contínua
✔️ Interface web segura e intuitiva para todos os envolvidos

🛠️ Requisitos para Desenvolvimento
Python 3.10+
Virtualenv
SQLite (ou outro banco relacional)
