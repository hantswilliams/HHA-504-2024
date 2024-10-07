# Step 1: Set Up Your Google Cloud Project
1. Create or Select a Google Cloud Project
- Go to the Google Cloud Console.
- Click on Select a Project (top left) and either select an existing project or create a new one.
2. Enable the Google Cloud Storage API
- Go to the APIs & Services Dashboard.
- Click + Enable APIs and Services.
- Search for Cloud Storage API and click Enable.

# Step 2: Set Up Authentication and Download Access Keys
1. Create a Service Account
- Go to the IAM & Admin Dashboard.
- Click + Create Service Account.
- Fill in the details and click Create and Continue.
2. Grant Permissions to the Service Account
- Click on the newly created service account.
- Assign the role Storage Admin to give permissions to manage Google Cloud Storage.
- Click on Add Key and create a new key in JSON format.
3. Download the Key File
- Download the JSON key file and save it securely on your local machine.
- This key file will be used to authenticate your application to Google Cloud Storage.
- Do not share this key file with others. You can rename it to something simple like `gcp-storage-key.json`. 
- Make sure to add this file to your `.gitignore` file 

# Step 3: Install the Google Cloud SDK
- You need to install the `google-cloud-storage` library to interact with Google Cloud Storage from Python.
- ```bash
    pip install google-cloud-storage
    ```

# Step 4: Write Python Code to Upload Fake Images
- We will use `PIL` library to generate fake images and upload them to Google Cloud Storage.
- Install the `Pillow` library using `pip install Pillow`.
- Create a Python script `upload_images.py` and write the following code:
```python

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
```
- Parts of the code you will need to update: 
    - `os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/service_account_key.json'`: Update the path to your service account key file.
    - `bucket_name = 'your-bucket-name'`: Update this to the name of your Google Cloud Storage bucket.
    - `blob = bucket.blob('fake_image.png')`: Update the name of the image file you want to upload.

# Step 5: Run the Python Script
- Run the Python script using `python upload_images.py`.
- Check your Google Cloud Storage bucket to see if the fake image was uploaded successfully.
