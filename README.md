Abstract
- Introduction: The European Union Deforestation Regulation (EUDR) mandates that companies demonstrate their products do not contribute to deforestation or forest degradation. This
regulatory requirement has intensified the need for precise tracking and verification of environmental impacts, particularly within sectors where deforestation risks are significant. However,
the lack of detailed, asset-level data presents a major challenge for accurate environmental impact assessments. Current databases primarily focus on broad financial and operational metrics,
lacking the granularity needed to assess the specific contributions of physical assets to deforestation and existing methods of physical asset database creation require extensive manual labour.
This data and automation gap hinders regulatory compliance and limits the ability to develop
accurate models for predicting environmental impacts.
- Objectives: This research aims to develop an automated LLM-based end-to-end systematic data extraction pipeline for structured database creation, cleaning and validation, creating
high-quality datasets essential for environmental impact analysis, including asset-based deforestation, specifically targeting sectors with high deforestation risks.
- Methods: The proposed pipeline employs advanced Natural Language Processing (NLP)
techniques, integrating a novel, domain-specific prompting method—Instructional, Role-Based,
Zero-Shot Chain-of-Thought (IRZ-CoT) prompting—to enhance data extraction accuracy. Additionally, the Retrieval-Augmented Validation (RAV) process is introduced to incorporate realtime web searches into the validation phase, further ensuring data reliability.
- Results: The pipeline was applied to SEC EDGAR filings across the Mining, Oil & Gas, and
Utilities sectors. The results demonstrate a substantial improvement in data extraction accuracy,
with the IRZ-CoT prompting technique achieving a notable increase in the F1 score by 11.9%
over zero-shot prompting. The RAV process further enhanced data validation, leading to an
average absolute increase in overall validation coverage by 12.5%. The final datasets were visualised through company-specific dashboards, providing detailed insights into the database of
each company. These results underscore our pipeline’s effectiveness in bridging data gaps and
enhancing the quality of asset-level databases.
- Conclusion: The research introduces a novel, automated pipeline that addresses the significant data gaps in asset-level environmental impact assessments. Key contributions include the
development of the IRZ-CoT prompting technique, a three-step database cleaning process, and
the implementation of the novel RAV approach, all integrated into a cohesive pipeline. It offers
a practical tool for companies to meet regulatory requirements, fulfill their Corporate Social Responsibility (CSR) and align with Environmental, Social and Governance (ESG) standards. The
methodologies developed can be adapted and extended to other sectors, supporting broader
sustainability and regulatory efforts.
