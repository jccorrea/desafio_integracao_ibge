# desafio_integracao_ibge
Desafio de integração de dados  do IBGE


**Ferramentas utilizadas/tools used**

* Basecamp: para organizar as tarefas e os objetivos
* Github: code versioning
* Count.co: para criar a POC com mais facilidade no canvas com SQL e Python.
* Anaconda suite, conda,Python, Spark, Delta
* Whimsical: Usado para criar documentações 
* Navicat Data Modeler Essentials: Modelagem
* dbdiagram.io 

**Python/Spark - local**

> python -m pip show pyspark
Name: pyspark
Version: 3.3.1
Summary: Apache Spark Python API
Home-page: https://github.com/apache/spark/tree/master/python
Author: Spark Developers
Author-email: dev@spark.apache.org
License: http://www.apache.org/licenses/LICENSE-2.0
Location: /Users/dal/anaconda3/envs/delta_env/lib/python3.10/site-packages
Requires: py4j
Required-by: 

**APIs utilizadas**

1. https://servicodados.ibge.gov.br/api/docs

**Fonte de dados utilizadas**
Decidi usar apenas dados dos municípios de SP. Então todas as URLs da API foram preparadas para trazer dados nesse nível.

1. Localidades: município, microrregiao, mesorregião, região e estado
2. PIB dos municípios dos 3 anos
3. Dados de IDH/IDHM dos municípios de SP


