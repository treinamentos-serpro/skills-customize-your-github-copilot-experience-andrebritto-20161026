# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI e modelos Pydantic. Você praticará métodos HTTP, rotas, validação de dados e respostas de erro.

## 📝 Tarefas

### 🛠️ Criar a aplicação e as primeiras rotas

#### Descrição
Configure o FastAPI e crie as rotas iniciais para verificar o estado da API e consultar a coleção de tarefas. Use um modelo Pydantic para representar uma tarefa.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI com um título descritivo.
- Definir um modelo de tarefa com `id`, `title` e `completed`.
- Implementar `GET /health`, retornando `{"status": "ok"}`.
- Implementar `GET /tasks`, retornando uma lista vazia quando ainda não houver tarefas.
- Iniciar a API localmente e conferir as rotas em `/docs`.

Para executar, instale `fastapi` e `uvicorn`, renomeie `starter-code.py` para `main.py` e use `uvicorn main:app --reload`.

### 🛠️ Implementar operações CRUD

#### Descrição
Armazene tarefas em memória e complete as rotas para criar, consultar, atualizar e remover uma tarefa. Cada tarefa deve ter um identificador único, um título e um estado de conclusão.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa e retornar o recurso criado.
- Implementar `GET /tasks/{task_id}` para consultar uma tarefa pelo identificador.
- Implementar `PUT /tasks/{task_id}` para atualizar o título e o estado de conclusão.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa.
- Retornar os códigos HTTP apropriados para criação, consulta, atualização e remoção.

Exemplo de corpo para criar uma tarefa:

```json
{
  "title": "Estudar FastAPI",
  "completed": false
}
```

### 🛠️ Validar entradas e tratar erros

#### Descrição
Adicione validação ao modelo de entrada e respostas claras para solicitações inválidas ou tarefas inexistentes.

#### Requisitos
O programa concluído deve:

- Rejeitar títulos vazios usando validação do Pydantic.
- Retornar HTTP `404 Not Found` quando uma rota receber um `task_id` que não existe.
- Retornar HTTP `201 Created` ao criar uma tarefa e HTTP `204 No Content` ao removê-la.
- Testar os fluxos de sucesso e erro usando a interface `/docs`.