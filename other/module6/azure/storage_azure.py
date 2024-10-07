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