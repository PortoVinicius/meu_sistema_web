### Testes de Segurança Realizados

Este documento descreve os testes de segurança aplicados ao sistema com o objetivo de identificar e mitigar vulnerabilidades comuns.
Inclui tanto testes manuais quanto teste automatizado de brute force simulado.

### 1. Teste de Autenticação

Verificação do processo de login.

Validação de credenciais inválidas.

Bloqueio ou tratamento adequado de tentativas incorretas.

Observação: Atualmente, o sistema aceita tentativas ilimitadas sem bloqueio; o teste automatizado registra cada tentativa para fins de visibilidade.

### 2. Teste de Autorização entre Usuários

Verificação de acesso indevido a recursos restritos.

Garantia de que usuários só acessam dados permitidos.

Testes de escalonamento de privilégios.

### 3. Verificação de Hash de Senha

Confirmação de que senhas não são armazenadas em texto puro.

Uso de algoritmos de hash seguros (pbkdf2:sha256).

Validação de comparação correta de hashes.

### 4. Teste contra SQL Injection

Tentativas de injeção em campos de entrada.

Verificação do uso de consultas parametrizadas.

Avaliação da proteção contra manipulação de queries.

### 5. Teste contra XSS (Cross-Site Scripting)

Inserção de scripts maliciosos em campos de formulário.

Verificação de sanitização e escape de dados.

Validação da renderização segura no frontend.

### 6. Teste de Encerramento de Sessão

Verificação do logout correto do usuário.

Invalidação de sessão no servidor.

Teste de reutilização de sessão após logout.

### 7. Teste Automatizado de Brute Force Simulado

Um script Python foi criado para simular múltiplas tentativas consecutivas de login com senha incorreta.

O teste foi executado em ambiente controlado, com o Flask rodando em desenvolvimento.

Nenhum bloqueio ocorreu, mas cada tentativa foi registrada no banco de dados LoginAttempt, incluindo:

endereço IP da tentativa

nome de usuário

resultado (success=False)

timestamp

O objetivo do teste é visibilidade e auditoria, permitindo análise de comportamento do sistema frente a tentativas repetidas de login.

## Observações Gerais

Os testes descritos foram realizados em ambiente de desenvolvimento e têm como objetivo melhorar a segurança geral do sistema.

Todos os testes automatizados são de simulação controlada, sem impacto externo.

Novos testes podem ser adicionados conforme a evolução do projeto.

A implementação de limites de tentativa ou bloqueio por IP é uma etapa futura sugerida.
