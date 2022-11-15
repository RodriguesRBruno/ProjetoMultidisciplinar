from sklearn.model_selection import train_test_split
import sagemaker
import s3fs
import boto3
from python_scripts.save_load import BUCKET_MODEL

def create_train_validation_test_sets(model_df, stratify_col, test_size=0.2, random_state=None, validation_size=0.5):
    """
    Função auxiliar para gerar sets de treinamento, validação e teste.
    Inicialmente separa os dados de treinamento e teste+validação conforme proporção dada em test_size.
    Em seguida, o set de teste+validação é separado na metade para definir sets de teste e validação individualmente.
    """      
    train, test_validate = train_test_split(model_df, test_size=test_size, random_state=random_state,
                                           stratify=model_df[stratify_col])
    test, validate = train_test_split(test_validate, test_size=validation_size, random_state=random_state,
                                      stratify=test_validate[stratify_col])
    
    return train, test, validate


def setup_model(model_name, base_image='xgboost', instance_count=1, instance_type='ml.m4.xlarge',
                hyperparams=None):
    container = sagemaker.image_uris.retrieve('xgboost',boto3.Session().region_name,'1.5-1')
    
    if hyperparams is None:
        # Valores padrão de um lab
        hyperparams={"num_round":"42",
                     "eval_metric": "auc",
                     "objective": "binary:logistic"}

    s3_output_location=f"s3://{BUCKET_MODEL}/output/{model_name}"

    xgb_model=sagemaker.estimator.Estimator(container,
                                            sagemaker.get_execution_role(),
                                            instance_count=instance_count,
                                            instance_type=instance_type,
                                            output_path=s3_output_location,
                                            hyperparameters=hyperparams,
                                            sagemaker_session=sagemaker.Session())

    train_channel = sagemaker.inputs.TrainingInput(
        "s3://{}/{}/{}".format(BUCKET_MODEL,'train',f'{model_name}.libsvm'), content_type='libsvm')

    validate_channel = sagemaker.inputs.TrainingInput(
        "s3://{}/{}/{}".format(BUCKET_MODEL,'validate',f'{model_name}.libsvm'), content_type='libsvm')

    data_channels = {'train': train_channel, 'validation': validate_channel}
    
    return xgb_model, data_channels


def make_prediction(predictor, model_name, threshold=0.5):
    fs = s3fs.S3FileSystem()
    s3_path = f's3://projetointerdisciplinartreinoteste/test/{model_name}.libsvm'
    
    with fs.open(s3_path) as libsvm_file:
        y_pred = predictor.predict(libsvm_file)
        
    y_pred_list = [1 if float(x) >= threshold else 0 for x in y_pred.decode('utf-8').split('\n') if x != '']
    return y_pred_list