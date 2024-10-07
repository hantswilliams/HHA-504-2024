# Step 1: Set Up Your Azure Account and Storage Account
1. Log in to Azure Portal
- Go to the Azure Portal and log in with your credentials.
2. Create a Storage Account
- Navigate to Storage accounts by searching in the top search bar.
- Click + Create to make a new Storage Account.
- Select a Resource Group or create a new one.
- Provide a Storage account name (it must be unique).
- Select a Region and a Performance/Replication type based on your requirements.
- Click Review + create and then Create.

# Step 2: Set Up Access Credentials
1. Create a Shared Access Signature (SAS) Token
- In the Azure Portal, go to your Storage Account.
- Navigate to Settings > Shared access signature.
- Set the permissions you need (in this case, Read, Write, Create).
- Set the Start and Expiry Date/Time as needed.
- Click Generate SAS and connection string.
- Copy the SAS Token and Connection String—you will need this in your script.

2. Install Azure Storage Client Library
- To interact with Azure Storage from Python, you need the azure-storage-blob library.
- Run the following command in your terminal:
```bash
pip install azure-storage-blob Pillow
```

# Step 3: Write Python Code to Upload Fake Images
- Below is a Python script that uses the Azure Storage Blob client library to upload a fake image to Azure Blob Storage. The image will be generated using the Pillow library.
- Python Script:
```python
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
import io

# Step 1: Set up your Azure Storage connection string
# Replace the below with your connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName=your_account_name;AccountKey=your_account_key;EndpointSuffix=core.windows.net"

# Step 2: Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Step 3: Create a container or use an existing one
container_name = "your-container-name"  # Change this to your container name
try:
    container_client = blob_service_client.create_container(container_name)
except Exception as e:
    print(f"Container already exists or an error occurred: {e}")

# Step 4: Create a fake image using Pillow
image = Image.new('RGB', (100, 100), color = (150, 100, 200))
image_byte_array = io.BytesIO()
image.save(image_byte_array, format='PNG')
image_bytes = image_byte_array.getvalue()

# Step 5: Upload the fake image to Azure Blob Storage
blob_client = blob_service_client.get_blob_client(container=container_name, blob="fake_image.png")
blob_client.upload_blob(image_bytes, blob_type="BlockBlob", overwrite=True)

print("Image uploaded successfully to Azure Blob Storage!")
```
- Parts of the code you will need to update:
    - `connection_string = "DefaultEndpointsProtocol=https;AccountName=your_account_name;AccountKey=your_account_key;EndpointSuffix=core.windows.net"`: Replace `your_account_name` and `your_account_key` with your Azure Storage account name and account key.
    - `container_name = "your-container-name"`: Update this to the name of your Azure Blob Storage container.
    - `blob_client = blob_service_client.get_blob_client(container=container_name, blob="fake_image.png")`: Update the name of the image file you want to upload.

# Step 4: Run the Python Script
- Save the Python script to a file (e.g., `upload_images.py`) and run it using a Python interpreter.
- The script will generate a fake image and upload it to your Azure Blob Storage account.