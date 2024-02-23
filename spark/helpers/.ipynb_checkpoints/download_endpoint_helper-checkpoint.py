#Julio Cesar Correa

import os
import pandas as pd, numpy as np

import pyspark
from pyspark.sql import SparkSession

# Import all functions and types
from pyspark.sql.types import *
from pyspark.sql.functions import *

# A simple Dict with all URLs to download data
url_endpoints = {'url_pop_mun_sp' : "https://servicodados.ibge.gov.br/api/v3/agregados/9520/periodos/-6/variaveis/93?localidades=N6[N3[35]]",
                  'url_localidade_mun_sp' : "https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/municipios"}

# Root Delta table directory
delta_root_dir = "/Users/dal/Documents/desafio_ibge/data/delta_dir"
transient_dir = "transient"
raw_dir = "raw"
trusted_dir = "trusted"

"""
delta_directories = {'delta_root_dir':"/Users/dal/Documents/desafio_ibge/data/delta_dir",
               'transient_dir':"transient",
               'raw_dir':"raw",
               'trusted_dir':"trusted"}
"""

#schema examples
#Municipios Schema
schema = StructType([
  StructField("maxRecords", IntegerType(), True),
  StructField("results", ArrayType(
    StructType([
      StructField("Make_ID", IntegerType()),
      StructField("Make_Name", StringType())
    ])
  ))
])
