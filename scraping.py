import requests
import pandas as pd

# Base URL tanpa offset agar dapat digunakan dalam loop
base_url = 'https://api-sscasn.bkn.go.id/2024/portal/spf?kode_ref_pend=5109751&offset='

# Headers, termasuk User-Agent yang diisi dengan informasi yang sesuai
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Referer': 'https://sscasn.bkn.go.id/',
    'Origin': 'https://sscasn.bkn.go.id'
}

# List untuk menyimpan semua data
all_data = []

# Initial offset value
offset = 0

# Items per page, tergantung pada jumlah yang ditampilkan per halaman
items_per_page = 10

# Maksimal data yang diketahui (bisa disesuaikan)
max_data = 2552

while offset < max_data:
    url = f'{base_url}{offset}'
    print(f"Requesting data from URL: {url}")
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        break
    
    try:
        response_json = response.json()  # Parse JSON response
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        print(f"Response content: {response.text}")
        break
    
    if 'data' in response_json and 'data' in response_json['data']:
        data = response_json['data']['data']
        all_data.extend(data)  # Add data to the all_data list
        offset += items_per_page  # Increase offset by the number of items per page
    else:
        print("No more data available.")
        break

# Convert list of data to DataFrame
df = pd.DataFrame(all_data)

# Save DataFrame to CSV file
df.to_csv('data_formasi_s1-arsitektur.csv', index=False)

print("Data has been successfully saved to 'data_formasi_s1-arsitektur.csv")