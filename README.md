# 📝 Sistema de Inscrições em Minicursos — Flask

Sistema web modular para gerenciamento de inscrições em minicursos de eventos acadêmicos, desenvolvido como projeto prático para a disciplina de Desenvolvimento Web na **UESB (Universidade Estadual do Sudoeste da Bahia)**.

## 🏛️ Arquitetura e Tecnologias

- **Linguagem:** Python 3.8+
- **Framework:** Flask
- **Banco de Dados:** SQLite (Embarcado)
- **Padrão de Arquitetura:** MVC (Model-View-Controller) integrado ao padrão **DAO (Data Access Object)** para isolamento da camada de persistência.
- **Renderização:** Jinja2 Templates com herança estrutural.

## 🔒 Diferenciais Técnicos e Segurança

- **Inicialização Automatizada:** O arquivo `database.py` gera o banco e popula tabelas padrões na primeira execução.
- **Proteção contra SQL Injection:** Uso de consultas parametrizadas com placeholders (`?`).
- **Prevenção contra XSS:** Auto-escaping nativo do motor Jinja2.

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale as dependências: `pip install Flask`.
3. Inicie a aplicação: `python app.py`.
4. Acesse: `http://127.0.0.1:5000/`.

---

**Desenvolvedor:** Camilla Novaes Mendes
