"""
Arquivo para scripts referentes a salvar/carregar dados
"""
import io
import boto3
import pandas as pd
from sagemaker.amazon.common import write_spmatrix_to_sparse_tensor
from sklearn.datasets import dump_svmlight_file

BUCKET_BRUTOS = 'projetointerdisciplinardadosbrutos'
BUCKET_PROCESSADOS = 'projetointerdisciplinardadosprocessados'
BUCKET_MODEL = 'projetointerdisciplinartreinoteste'

def __get_bucket(tipo='bruto'):
    if tipo=='processado':
        return BUCKET_PROCESSADOS
    elif tipo == 'bruto':
        return BUCKET_BRUTOS
    elif tipo == 'modelo':
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
        

def save_df_to_s3_bucket(df, file_name, prefix=None, tipo='bruto'):
    bucket = __get_bucket(tipo)
    if prefix is not None:
        df.to_csv(f's3://{bucket}/{file_name}', encoding='utf-8', index=False)
    
    
def save_sparse_vector_to_s3_bucket_as_recordio(spvec, filename, tipo='bruto'):

    bucket = __get_bucket(tipo)
    prefix = filename.split('.')[0]
    data_location = f"{prefix}/{filename}"
    buf = io.BytesIO()
    write_spmatrix_to_sparse_tensor(buf,spvec)
    buf.seek(0)
    boto3.resource('s3').Bucket(bucket).Object(data_location).upload_fileobj(buf)

    
def save_to_s3_bucket_as_libsvm(x_values, y_values, prefix, filename, tipo='bruto'):

    bucket = __get_bucket(tipo)
    data_location = f"{prefix}/{filename}"
    buf = io.BytesIO()
    dump_svmlight_file(x_values, y_values, buf)
    buf.seek(0)
    boto3.resource('s3').Bucket(bucket).Object(data_location).upload_fileobj(buf)