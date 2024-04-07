import boto3
import time
import json

# Substitua 'your-pdf-file-path.pdf' pelo caminho do seu arquivo PDF
pdf_file_path = 'pdf/index.pdf'
# Substitua 'your-bucket-name' pelo nome do seu bucket no S3 onde o arquivo PDF será armazenado
s3_bucket_name = 'gusmao-dados'
# Substitua 'pdf-file-name-in-s3.pdf' pelo nome do arquivo no S3
s3_object_name = 'pdf/index.pdf'

# Inicialize o cliente S3 e Textract
s3_client = boto3.client('s3', 'us-east-1')
textract_client = boto3.client('textract', 'us-east-1')

# Carrega o arquivo PDF no S3
s3_client.upload_file(pdf_file_path, s3_bucket_name, s3_object_name)

# Inicia a detecção de texto no documento
response = textract_client.start_document_text_detection(
    DocumentLocation={
        'S3Object': {
            'Bucket': s3_bucket_name,
            'Name': s3_object_name
        }
    }
)

# Pega o ID do trabalho
jobId = response['JobId']
print(f"Started job with id: {jobId}")

# Aguarda a conclusão do trabalho
while True:
    response = textract_client.get_document_text_detection(JobId=jobId)
    status = response['JobStatus']
    if status == 'IN_PROGRESS':
        time.sleep(5)
        continue
    break

if status == 'SUCCEEDED':
    # Processa os resultados
    pages = []
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            pages.append(item['Text'])
    print("\n".join(pages))
else:
    print(f"Text detection failed with status: {status}")
    
# Formato JSON
# if status == 'SUCCEEDED':
#     # Extrai somente os blocos de texto
#     text_blocks = [item for item in response['Blocks'] if item['BlockType'] == 'LINE']
    
#     # Salva os resultados em um arquivo JSON
#     with open('extracted_text.json', 'w') as json_file:
#         json.dump(text_blocks, json_file, indent=4, ensure_ascii=False)
    
#     print("Text extracted and saved to extracted_text.json")
# else:
#     print(f"Text detection failed with status: {status}")


# Limpeza: Remover o arquivo PDF do S3 se desejado
# s3_client.delete_object(Bucket=s3_bucket_name, Key=s3_object_name)
