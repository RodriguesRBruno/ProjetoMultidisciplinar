"""
Arquivo para scripts referentes a salvar/carregar dados
"""

import boto3
import pandas as pd

BUCKET_BRUTOS = 'projetointerdisciplinardadosbrutos'
BUCKET_PROCESSADOS = 'projetointerdisciplinardadosprocessados'

def __get_bucket(processado=False):
    if processado:
        return BUCKET_PROCESSADOS
    else:
        return BUCKET_BRUTOS

    
def load_df_from_bucket(file_name, processado=False):
    """
    Função auxiliar para ler csv de buckets do projeto.
    Se processado for True, lê o bucket de dados processados; 
    caso contrário, lê bucket de dados brutos.
    """
    bucket = __get_bucket(processado)
    return pd.read_csv(f's3://{bucket}/{file_name}')


def save_to_s3_bucket(file_name, processado=False):
    """
    Função auxiliar para fazer upload de um arquivo para bucket no S3.
    Se processado for True, salva no bucket de dados processados; 
    caso contrário, salva no bucket de dados brutos.
    """
    bucket = __get_bucket(processado)
    s3 = boto3.resource('s3')
    with open(file_name, 'rb') as f:
        s3.Bucket(bucket).put_object(Key=file_name, Body=f)
        

def save_df_to_s3_bucket(df, file_name, processado=False):
    bucket = __get_bucket(processado)
    df.to_csv(f's3://{bucket}/{file_name}', encoding='utf-8', index=False)