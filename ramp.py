import requests
import json

# API Ű�� �⺻ URL ����
api_key = 'dce42638afaf57784a701d4b5371cdef'
base_url_jobs = 'https://www.career.go.kr/cnet/front/openapi/jobs.json'
base_url_major = 'https://www.career.go.kr/cnet/openapi/getOpenApi.json'

# ������� ������ ��������
def fetch_jobs_data(api_key, page_index=1):
    params = {
        'apiKey': api_key,
        'pageIndex': page_index,
    }
    response = requests.get(base_url_jobs, params=params)
    if response.status_code == 200:
        return response.json().get('jobs', [])
    else:
        print(f"Error fetching jobs data: {response.status_code}")
        return []

# �а����� ������ ��������
def fetch_major_data(api_key, page=1, per_page=50):
    params = {
        'apiKey': api_key,
        'svcType': 'api',
        'svcCode': 'MAJOR',
        'contentType': 'json',
        'gubun': 'univ_list',
        'thisPage': page,
        'perPage': per_page
    }
    response = requests.get(base_url_major, params=params)
    if response.status_code == 200:
        return response.json().get('dataSearch', {}).get('content', [])
    else:
        print(f"Error fetching major data: {response.status_code}")
        return []

# ������ ��ó�� �Լ�
def preprocess_data(data, data_type='job'):
    processed_data = []
    
    if data_type == 'job':
        for item in data:
            processed_item = {
                'job_name': item.get('job_nm'),
                'work': item.get('work'),
                'aptitude': item.get('aptitudeList', []),
                'related_certificates': item.get('certiList', []),
                'related_departments': item.get('departList', [])
            }
            processed_data.append(processed_item)
    
    elif data_type == 'major':
        for item in data:
            processed_item = {
                'major_name': item.get('title'),
                'major_code': item.get('majorSeq'),
                'university': item.get('univ_name'),
                'department': item.get('department')
            }
            processed_data.append(processed_item)
    
    return processed_data

# ���� ���� �Լ�
if __name__ == "__main__":
    # ������� ������ �������� �� ��ó��
    jobs_data = fetch_jobs_data(api_key)
    processed_jobs_data = preprocess_data(jobs_data, data_type='job')
    
    # �а����� ������ �������� �� ��ó��
    major_data = fetch_major_data(api_key)
    processed_major_data = preprocess_data(major_data, data_type='major')
    
    # ��� ��� �Ǵ� ���Ϸ� ����
    with open('processed_jobs_data.json', 'w', encoding='utf-8') as f:
        json.dump(processed_jobs_data, f, ensure_ascii=False, indent=4)
    
    with open('processed_major_data.json', 'w', encoding='utf-8') as f:
        json.dump(processed_major_data, f, ensure_ascii=False, indent=4)
    
    print("Data processing completed and saved to JSON files.")