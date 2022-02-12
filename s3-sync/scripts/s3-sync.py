from concurrent import futures
import os
import boto3
import time

def download_dir(bucket, prefix, localpathpath):

    client = boto3.client('s3')

    def create_folder_and_download_file(k):
        dest_pathname = os.path.join(localpathpath, k)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
        print(f'downloading {k} to {dest_pathname}')
        client.download_file(bucket, k, dest_pathname)

    keys = []
    dirs = []
    next_token = ''
    base_kwargs = {
        'Bucket': bucket,
        'Prefix': prefix,
    }
    while next_token is not None:
        kwargs = base_kwargs.copy()
        if next_token != '':
            kwargs.update({'ContinuationToken': next_token})
        results = client.list_objects_v2(**kwargs)
        contents = results.get('Contents')
        for i in contents:
            k = i.get('Key')
            if k[-1] != '/':
                keys.append(k)
            else:
                dirs.append(k)
        next_token = results.get('NextContinuationToken')
    for d in dirs:
        dest_pathname = os.path.join(localpath, d)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
    with futures.ThreadPoolExecutor() as executor:
        futures.wait(
            [executor.submit(create_folder_and_download_file, k) for k in keys],
            return_when=futures.FIRST_EXCEPTION,
        )

def s3_sync(bucket, prefix, destpath):
    while True:
        download_dir('bucket' , 'prefix', 'localpath')
        time.sleep(360)

if __name__ == '__main__':
    bucket = 'aistemos-mark-day'
    prefix = 'airflow/dags'
    localpath = '/tmp/dags'
    s3_sync(bucket, prefix, localpath)
