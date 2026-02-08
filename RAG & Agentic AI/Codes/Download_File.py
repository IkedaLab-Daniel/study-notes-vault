import wget

filename = 'companyPolicies.txt'
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/6JDbUb_L3egv_eOkouY71A.txt'

try:
    with open(filename, 'r') as file:
        print("File already exists, cancelling download file...")
    
except:     
    # Use wget to download the file
    wget.download(url, out=filename)
    print('file downloaded')

# > Read content

with open(filename, 'r') as file:
    # Read the contents of the file
    contents = file.read()
    print(contents)