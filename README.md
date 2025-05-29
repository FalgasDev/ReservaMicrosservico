# 📚 API de Reserva de Salas

Este repositório contém a **API de Reserva de Salas**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Reserva de Salas é um **microsserviço** que faz parte de um sistema maior de [School System](https://github.com/caio-ireno/School-System-Api)
, sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ **Esta API depende de outra API de Gerenciamento Escolar (School System)**, que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se a **Turma** existe (`GET /turmas/<id>`)
- (Opcional) Se o **Aluno** existe (`GET /alunos/<id>`) – pode ser desativado se não usado.

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (como banco de dados local)
- Requests (para consumo da API externa)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/FalgasDev/ReservaMicrosservico.git
cd ReservaMicrosservico
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:5001`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

- `GET /reservas` – Lista todas as reservas
- `POST /reservas` – Cria uma nova reserva



### Exemplo de corpo JSON para criação:

```json
{
  "turma_id": 1,
  "sala": "101",
  "data": "2025-05-06",
  "hora_inicio": "14:00",
  "hora_fim": "16:00"
}
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando em:

```
http://localhost:5000
```

E que os endpoints de `GET /turmas/<id>` (e opcionalmente `GET /alunos/<id>`) estejam funcionando corretamente para que a validação seja feita com sucesso.

---

## 📦 Estrutura do Projeto

```
Reserva_salas/
├── instance/
├── app.py
├── config.py
├── database.py
├── dockerfile
├── readme.md
├── requirements.txt
├── models/reserva_models.py
└── controllers/reserva_route.py
```

---

## 🛠️ Futuras Melhorias

- Validação de conflito de horário na sala
- Integração via fila (RabbitMQ) com outros microsserviços
- Autenticação de usuários

---

# Contatos
- caso tenha duvidas ou sugestões, entre em contato com:
**NOMES**
# Kaio Nogueira Mungo
# Diego da Silva Criscuolo
# Bruna Bispo Andreata
# Luiz Henrique Barros Calazans
# Fábio Luiz Garrote Ramaldes

**EMAIL**
# kaio.mungo@aluno.faculdadeimpacta.com.br
# diego.criscuolo@aluno.faculdadeimpacta.com.br
# bruna.andreata@aluno.faculdadeimpacta.com.br
# luiz.calazans@aluno.faculdadeimpacta.com.br
# fabio.ramaldes@aluno.faculdadeimpacta.com.br

**GITHUB**
# https://github.com/KaioMungo
# https://github.com/Diego09cr
# https://github.com/BrunaAndreata
# https://github.com/LuizCalazans
# https://github.com/FalgasDev

📜 Licença
**Este projeto está licenciado sob os contatos acima.**
