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
