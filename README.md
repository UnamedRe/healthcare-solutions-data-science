# 🏥 HealthCare Solutions - Melhoria do Atendimento ao Paciente com Data Science

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![Autor](https://img.shields.io/badge/Autor-Daniel%20Sanjines%20Lozano-orange)

## 📘 Descrição do Projeto

Este projeto foi desenvolvido como parte da disciplina **Data Science Fundamentals**, com o objetivo de aplicar técnicas de **Ciência de Dados** no contexto hospitalar da empresa fictícia **HealthCare Solutions**.

O foco é demonstrar como o uso de dados provenientes de **registros eletrônicos de saúde (EHRs)**, **dispositivos de monitoramento**, **pesquisas de satisfação** e **dados administrativos** pode melhorar a **qualidade do atendimento ao paciente** e reduzir **readmissões hospitalares**.

---

## 🎯 Objetivos

- Unificar e tratar dados dispersos de múltiplas fontes hospitalares.  
- Aplicar métodos de análise exploratória e preditiva para identificar padrões.  
- Desenvolver um modelo de Machine Learning para prever o risco de readmissão em 30 dias.  
- Criar visualizações que auxiliem a tomada de decisão clínica e operacional.  

---

## 🧠 Metodologia Aplicada

O projeto segue o **ciclo completo de Ciência de Dados**:

1. **Coleta e Simulação de Dados:**  
   Geração de dataset realista com 2.000 registros de pacientes anonimizados.  

2. **Limpeza e Pré-processamento:**  
   - Tratamento de valores ausentes.  
   - Criação de variáveis derivadas (ex: tempo de internação).  
   - Codificação de variáveis categóricas.  

3. **Análise Exploratória (EDA):**  
   - Distribuição de idade e satisfação.  
   - Correlação entre tempo de internação e satisfação.  

4. **Modelagem Preditiva:**  
   - Algoritmo: `RandomForestClassifier`.  
   - Variável alvo: `readmission_30d`.  
   - Métricas: *Accuracy*, *AUC*, *Classification Report*.  

5. **Visualizações e Resultados:**  
   Gráficos salvos em `outputs/` (gerados automaticamente pelo script).  

---

## ⚙️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+  
- **Bibliotecas Principais:**
  - pandas  
  - numpy  
  - scikit-learn  
  - matplotlib  
  - joblib  
  - reportlab  

---

## 📂 Estrutura do Projeto

```
📦 healthcare_project
 ┣ 📜 dataset_healthcare_simulated.csv
 ┣ 📜 main.py
 ┣ 📜 report_Daniel_Sanjines_Lozano.pdf
 ┣ 📜 requirements.txt
 ┣ 📜 LICENSE
 ┣ 📜 README.md
 ┗ 📂 outputs/ (gerado após execução)
```

---

## 🚀 Execução do Projeto

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/healthcare_project.git
   cd healthcare_project
   ```

2. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar o pipeline:**
   ```bash
   python main.py
   ```

4. **Ver resultados:**
   - Figuras e relatório gerados em `/outputs`
   - Modelo salvo: `random_forest_readmission.joblib`

---

## 📊 Exemplos de Resultados

| Métrica | Valor aproximado |
|----------|------------------|
| **Acurácia** | 0.78 |
| **AUC** | 0.83 |
| **Feature mais importante** | Número de condições crônicas |

*Os resultados podem variar levemente a cada execução.*

---


## 📋 Levantamento de Requisitos - Entrevista Simulada com a Gestão da HealthCare Solutions

Durante a etapa de planejamento do projeto, foram realizadas entrevistas simuladas com gestores e profissionais da área de saúde.  
Abaixo estão **10 perguntas e respostas** que orientaram o desenvolvimento do projeto de Ciência de Dados:

| Nº | Pergunta | Resposta Simulada |
|----|-----------|------------------|
| 1 | Quais são os principais indicadores de desempenho hospitalar atualmente monitorados? | Taxa de readmissão em 30 dias, tempo médio de permanência e nível de satisfação dos pacientes. |
| 2 | Há integração entre os sistemas administrativos e clínicos? | Não totalmente. Os sistemas funcionam em silos, exigindo consolidação manual de dados. |
| 3 | Que tipo de dados os dispositivos de monitoramento coletam? | Frequência cardíaca média, pressão arterial e passos diários registrados por wearables. |
| 4 | O hospital possui histórico de pesquisas de satisfação? | Sim, as pesquisas são aplicadas digitalmente e armazenadas em formato CSV desde 2022. |
| 5 | Qual é o principal problema relatado pelos pacientes? | Tempo de espera elevado e falta de acompanhamento pós-alta. |
| 6 | Como é feita a anonimização dos dados sensíveis? | Identificadores pessoais são removidos e substituídos por IDs internos antes da análise. |
| 7 | Qual o objetivo principal da análise de dados neste projeto? | Reduzir a taxa de readmissão hospitalar e aumentar o índice de satisfação. |
| 8 | Existe alguma restrição legal quanto ao uso dos dados? | Sim, é necessário seguir integralmente a LGPD e manter auditoria sobre o uso dos dados. |
| 9 | Quais setores devem ter acesso aos dashboards e relatórios? | Diretoria médica, setor administrativo e equipe de qualidade. |
| 10 | Há planos de expansão do sistema de análise? | Sim, a intenção é integrar modelos preditivos ao sistema hospitalar interno até 2026. |

Essas informações permitiram compreender as necessidades da instituição e alinhar as soluções de Data Science às metas estratégicas da empresa.


## 🔐 Aspectos Éticos e Legais

O projeto respeita os princípios da **Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018)**, garantindo anonimização dos dados e uso apenas para fins acadêmicos.

---

## 🧾 Licença

Este projeto está licenciado sob os termos da licença **MIT**.  
Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---

## ✨ Autor

**Daniel Sanjines Lozano**  
Estudante de Ciência de Dados  
📧 Contato: *(adicione seu e-mail acadêmico ou profissional)*  
🌐 GitHub: [github.com/SEU_USUARIO](https://github.com/SEU_USUARIO)

---

## 📹 Observação

A entrega original do trabalho incluía também um vídeo explicativo (*não obrigatório neste repositório*).  
Este projeto contém apenas a parte teórica e prática completa.

---
