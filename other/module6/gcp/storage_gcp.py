from google.cloud import storage
from PIL import Image
import io
import os

# Step 1: Set up your Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/service_account_key.json'

# Step 2: Create a Google Cloud Storage client
client = storage.Client()

# Step 3: Create a bucket or use an existing one
bucket_name = 'your-bucket-name'  # Change this to your bucket name
bucket = client.bucket(bucket_name)

# Step 4: Create a fake image using Pillow
image = Image.new('RGB', (100, 100), color = (73, 109, 137))
image_byte_array = io.BytesIO()
image.save(image_byte_array, format='PNG')

# Step 5: Upload the fake image to Google Cloud Storage
blob = bucket.blob('fake_image.png')
blob.upload_from_string(image_byte_array.getvalue(), content_type='image/png')

print("Image uploaded successfully to Google Cloud Storage!")