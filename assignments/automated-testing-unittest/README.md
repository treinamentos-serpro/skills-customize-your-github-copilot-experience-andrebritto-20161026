# 📘 Assignment: Automated Testing with unittest

## 🎯 Objetivo

Aprenda a verificar o comportamento de funções Python com testes automatizados usando o módulo `unittest`, que faz parte da biblioteca padrão. Você praticará testes de resultados comuns, valores-limite e exceções esperadas.

## 📝 Tarefas

### 🛠️ Testar uma condição simples

#### Descrição
Complete os testes de `is_passing(score)` para verificar se uma nota atinge a pontuação mínima de aprovação.

#### Requisitos
O programa concluído deve:

- Usar `unittest.TestCase` para organizar os testes.
- Verificar que a nota `60` é aprovada e que a nota `59` não é aprovada.
- Executar os testes com `python3 -m unittest -v test_calculations.py`.

### 🛠️ Testar cálculos e valores-limite

#### Descrição
Adicione testes para `calculate_average(values)`, verificando uma lista com vários números e uma lista com apenas um número.

#### Requisitos
O programa concluído deve:

- Verificar que a média de `[70, 80, 90]` é `80`.
- Verificar que a média de `[42]` é `42`.
- Usar asserções do `unittest` para comparar os resultados esperados com os resultados obtidos.

### 🛠️ Testar uma exceção esperada

#### Descrição
Verifique que `calculate_average(values)` informa um erro quando recebe uma lista vazia.

#### Requisitos
O programa concluído deve:

- Confirmar que uma lista vazia causa `ValueError` usando `assertRaises`.
- Substituir todos os `self.fail(...)` do starter code por asserções que verificam o comportamento esperado.
- Executar novamente a suíte e confirmar que todos os testes passam.

Renomeie `starter-code.py` para `test_calculations.py` antes de executar o comando. Não é necessário instalar pacotes.