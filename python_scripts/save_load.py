"""
Arquivo para scripts referentes a salvar/carregar dados
"""

import boto3
import pandas as pd

BUCKET_BRUTOS = 'projetointerdisciplinardadosbrutos'
BUCKET_PROCESSADOS = 'projetointerdisciplinardadosprocessados'
BUCKET_MODEL = 'projetointerdisciplinartreinoteste'

def __get_bucket(tipo='bruto'):
    if tipo=='processado':
        return BUCKET_PROCESSADOS
    elif tipo == 'bruto':
        return BUCKET_BRUTOS
    elif tipo == 'model':
        return BUCKET_MODEL
    
def load_df_from_bucket(file_name, tipo='bruto'):
    """
    Função auxiliar para ler csv de buckets do projeto.
    Se processado for True, lê o bucket de dados processados; 
    caso contrário, lê bucket de dados brutos.
    """
    bucket = __get_bucket(tipo)
    return pd.read_csv(f's3://{bucket}/{file_name}')


def save_to_s3_bucket(file_name, tipo='bruto'):
    """
    Função auxiliar para fazer upload de um arquivo para bucket no S3.
    Se processado for True, salva no bucket de dados processados; 
    caso contrário, salva no bucket de dados brutos.
    """
    bucket = __get_bucket(tipo)
    s3 = boto3.resource('s3')
    with open(file_name, 'rb') as f:
        s3.Bucket(bucket).put_object(Key=file_name, Body=f)
        

def save_df_to_s3_bucket(df, file_name, tipo='bruto'):
    bucket = __get_bucket(tipo)
    df.to_csv(f's3://{bucket}/{file_name}', encoding='utf-8', index=False)