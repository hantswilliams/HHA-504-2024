# Assignments for HHA504 GCP and Azure
## General Instructions
- Each assignment will require the creation of a github repo with the specified name.
- You will then submit to me the github link into Brightspace for me to open and review your work.
- These assignments may be difficult and you are likely to run into error messages. Do not let errors discourage you or prevent you from completing the assignment. Document your errors if you cannot resolve them and how you attempted to resolve them. 
- I encourage you to collaborate with your colleages if your run into difficulties, and use all utilities at your disposal to resolve the issues you encounter. Please use Microsoft Teams chat channel for the class to ask questions and collaborate with your classmates.


# Assignment: Exploring Cost Management and Billing on Azure and GCP

## Objective
The objective of this assignment is to introduce you to the cost management and billing interfaces of Azure and Google Cloud Platform (GCP). By the end of this assignment, you will be able to navigate these platforms to understand how cloud costs are tracked and managed.

## Instructions

### 1. Explore the Cost Management Dashboards
- **Azure:**
  - Navigate to the Azure Cost Management and Billing service.
  - Take a tour of the dashboard to familiarize yourself with the available tools and reports.
  - Identify where you would monitor costs and set budgets or alerts.
- **GCP:**
  - Access the Google Cloud Console and go to the Billing section.
  - Explore the Billing Overview and Reports sections to understand how GCP presents cost data.

### 2. Set Up a Hypothetical Budget
- **Azure:**
  - Create a budget for a hypothetical monthly spend (e.g., $8).
  - Set up a notification to alert you when your hypothetical spending reaches 80% of the budget.
- **GCP:**
  - Create a budget in GCP for the same hypothetical amount ($8).
  - Set up a notification to alert you when your costs approach the budget limit.

### 3. Investigate Cost Management Features
- **Azure:**
  - Review the available options for forecasting future costs based on your budget.
  - Explore the cost-saving recommendations provided by Azure Advisor (even if no data is present, you can see where these recommendations would appear).
- **GCP:**
  - Explore the "Cost Breakdown" and "Budgets & alerts" features to see how GCP allows you to track and manage your costs.
  - Investigate the "Recommendations" section under GCP Billing to understand potential cost-saving suggestions (if any are provided based on the budget).

### 4. Submit Your Work
- Create a Markdown document summarizing your exploration of the cost management features in both Azure and GCP.
- Include the following in your document:
  - Screenshots of the dashboards you explored.
  - Screenshots showing the setup of your hypothetical budgets and alerts.
  - A brief explanation of the cost management features you found most interesting or useful.
- Commit and push this Markdown document, along with the screenshots, to your GitHub repository.

## Deliverables
- September 8 2024: 11:59pm EST
- A Markdown document in a GitHub repository called `HHA504_assignment_cloudcosts` that includes:
  - Screenshots of the cost management and billing dashboards.
  - Screenshots of the budget and alert setups in both Azure and GCP.
  - Descriptions of interesting features and your reflections on them.


# Assignment: Working with Virtual Machines in Azure and GCP

## Objective
The objective of this assignment is to provide hands-on experience with managing Virtual Machines (VMs) in both Azure and Google Cloud Platform (GCP). You will learn how to start, stop, and monitor the costs associated with running VMs on these cloud platforms.

## IMPORTANT NOTE FOR AZURE: 
You MAY not have permissions to start a VM within Azure because of a change either by Microsoft or Stony Brook. If you do not have permissions, or our unable to, that is fine. Please then just continue with the assignment with GCP. 

## Instructions

### 1. Start and Stop a Virtual Machine
- **GCP:**
  - Access the Google Cloud Console and create a new VM instance using Compute Engine.
  - Select a basic configuration (e.g., Debian GNU/Linux, e2-micro instance type).
  - Start the VM and let it run for a few minutes.
  - Stop the VM and document the steps you followed.
- **Azure:**
  - Navigate to the Azure portal and create a new Virtual Machine.
  - Choose a basic configuration (e.g., Ubuntu Server, Standard B1s size).
  - Start the VM and allow it to run for a few minutes.
  - Stop the VM and take note of the actions you took.

IMPORTANT Notes:
- **Remember to stop the VMs after a few minutes to avoid incurring unnecessary costs.**


### 2. Monitor VM Costs
- **Azure:**
  - After starting and stopping the VM, navigate to the Cost Management and Billing section.
  - Find the cost associated with running your VM for the time it was active.
- **GCP:**
  - In the GCP Console, go to the Billing section and identify the cost incurred by your VM during its runtime.

### 3. Compare and Reflect
- Compare the costs of running a VM in Azure versus GCP. Consider factors such as the configuration used, the duration for which the VM was active, and any differences in cost visibility between the platforms.
- Reflect on the ease of starting, stopping, and monitoring VMs on each platform. Which platform did you find more intuitive or user-friendly? Why?

### 4. Submit Your Work
- Create a Markdown document that includes:
  - Screenshots of the VM creation and cost monitoring processes in both Azure and GCP.
  - A comparison of the costs between the two platforms.
  - Your reflections on the experience of using Azure and GCP for VM management.
- Commit and push this Markdown document, along with the screenshots, to your GitHub repository.

## Deliverables
- September 15 2024: 11:59pm EST
- A Markdown document in a GitHub repository called `HHA504_assignment_vms` that includes:
  - Screenshots of VM creation and cost monitoring.
  - A cost comparison between Azure and GCP.
  - Reflections on your experience with both platforms.


# Assignment: Networking in Azure and GCP - IPs and Domain Management

## NEW VERSION OF ASSIGNMENT

### Objective
The objective of this assignment is to explore the networking features in Azure and Google Cloud Platform (GCP), focusing on Virtual Private Cloud (VPC), IP addresses, domain management, and mapping a Flask web application to a custom domain. You will gain practical experience in reserving either static or dynamic IPs, mapping them to domains, and configuring firewall settings for public access.

### Instructions

#### 1. Create a Virtual Private Cloud (VPC)
- **Azure:**
  - Navigate to the Azure portal and create a new Virtual Network (VNet).
  - Choose a simple IP address range and subnet configuration.
- **GCP:**
  - Access the Google Cloud Console and create a new VPC network.
  - Configure the IP address range and subnets similarly to your Azure setup.

#### 2. Assign a Dedicated or Dynamic IP
- **Azure:**
  - You may either reserve a static public IP address for a resource (e.g., a virtual machine) within your VNet or use the dynamic public IP assigned by Azure.
- **GCP:**
  - Reserve a static external IP address for a Compute Engine instance within your VPC or use the dynamically assigned public IP.

#### 3. Map IP to a Domain Acquired via GitHub Student Pack
- Use your GitHub Student Developer Pack to acquire a domain through Namecheap (or another supported registrar).
- Set up an **A record** for your main domain (e.g., `yourdomain.com`) and a **subdomain** (e.g., `app.yourdomain.com`).

#### 4. Deploy Flask Application
- Deploy the provided Flask application located at [HHA 504 Flask Networking](https://github.com/hantswilliams/hha-504-flask-networking) to your virtual machine on Azure or GCP.
- Ensure that the Flask application is running on a specific port (e.g., port 5007).

#### 5. Configure Firewall Settings
- Make sure that the port on which your Flask application is running is accessible to the general public.
  - **Azure:** Configure Network Security Group (NSG) rules to allow inbound traffic on the specified port.
  - **GCP:** Configure Firewall rules to allow traffic on the specified port.

#### 6. Access Your Application via Domain
- Visit your deployed Flask application using the custom domain or subdomain you mapped, including the port number in the URL (e.g., `http://app.yourdomain.com:5000`).
  
#### 7. Submit Your Work
- Create a Markdown document that includes:
  - Screenshots of the VPC/VNet creation and IP reservation process in both Azure and GCP.
  - Screenshots and documentation of the steps taken to map the IP address to the domain (including the creation of A records and subdomains).
  - Screenshots of the running Flask application accessible via your domain or subdomain.
  - Documentation on how you configured the firewall rules to allow access to the Flask app.
- Errors 
  - As usual, if you run into errors, document them and how you attempted to resolve them.
  - It is ok if you are unable to resolve the errors, document what you tried and what you think the error might be.

- Commit and push this Markdown document, along with the screenshots, to your GitHub repository.

### Deliverables
- A Markdown document in a GitHub repository called `HHA504_assignment_networking` that includes:
  - Screenshots of VPC/VNet creation and IP reservation.
  - Steps and screenshots for mapping IPs to domains and configuring subdomains.
  - Screenshots of the Flask app running and accessible via the mapped domain or subdomain.
  - Firewall rule configurations that allow public access to the Flask application.

## OLDER VERSION OF ASSIGNMENT (you can use this one if you prefer, ok if you have already submitted)
### Objective
The objective of this assignment is to explore the networking features in Azure and Google Cloud Platform (GCP), focusing on Virtual Private Cloud (VPC), Virtual Private Network (VPN), IP addresses, and domain management. You will gain practical experience in assigning dedicated IPs and mapping them to domains.

### Instructions

#### 1. Create a Virtual Private Cloud (VPC)
- **Azure:**
  - Navigate to the Azure portal and create a new Virtual Network (VNet).
  - Choose a simple IP address range and subnet configuration.
- **GCP:**
  - Access the Google Cloud Console and create a new VPC network.
  - Configure the IP address range and subnets similarly to your Azure setup.

#### 2. Assign a Dedicated IP
- **Azure:**
  - Reserve a static public IP address for a resource (e.g., a virtual machine) within your VNet.
- **GCP:**
  - Reserve a static external IP address for a Compute Engine instance within your VPC.

#### 3. Map IP to a Domain
- **Azure:**
  - Use Azure DNS or an external domain registrar to map the reserved IP address to a domain name.
- **GCP:**
  - Use Google Cloud DNS or an external domain registrar to map the reserved IP address to a domain name.

#### 4. Explore VPN and Tunnels (Optional)
- **Azure:**
  - Explore the VPN Gateway service and document the steps you would take to set up a site-to-site VPN.
- **GCP:**
  - Explore the Cloud VPN service and outline the process to create a tunnel between two VPCs.

#### 5. Submit Your Work
- Create a Markdown document that includes:
  - Screenshots of the VPC/VNet creation and IP reservation process in both Azure and GCP.
  - Documentation of the steps taken to map the IP address to a domain in both platforms.
  - (Optional) Brief notes on VPN setup in Azure and GCP.
- Commit and push this Markdown document, along with the screenshots, to your GitHub repository.

### Deliverables
- A Markdown document in a GitHub repository called `HHA504_assignment_networking` that includes:
  - Screenshots of VPC/VNet creation and IP reservation.
  - Steps and screenshots for mapping IPs to domains.
  - (Optional) Notes on VPN setup in Azure and GCP.


# Assignment: Exploring Serverless Computing and Cron Jobs in Azure, GCP, and GitHub

## Objective
The objective of this assignment is to introduce you to serverless computing and the use of cron jobs in cloud environments. You will deploy serverless functions on both Azure and Google Cloud Platform (GCP), and create a scheduled task using GitHub Actions.

## Instructions

### 1. Deploy a Serverless Function
- **Azure:**
  - Navigate to the Azure portal and create an Azure Function.
  - Choose a simple trigger (e.g., HTTP trigger) and deploy a basic function (e.g., "Hello, World").
- **GCP:**
  - Access the Google Cloud Console and create a Google Cloud Function.
  - Deploy a similar function with an HTTP trigger in GCP.

### 2. Create a Cron Job
- **GitHub Actions:**
  - Create a new GitHub repository (or use an existing one).
  - Set up a GitHub Action workflow that runs a script on a schedule (e.g., daily at midnight). You can use a simple script that logs "Scheduled task executed" to the console.

### 3. Explore Functions as a Service (FaaS)
- Reflect on the use cases for serverless functions in cloud environments. Consider the benefits and limitations of using Functions as a Service (FaaS) in both Azure and GCP.

### 4. Submit Your Work
- Create a Markdown document that includes:
  - Screenshots of the serverless function deployment process in both Azure and GCP.
  - The code and configuration of your GitHub Action workflow.
  - Screenshots or documentation of the GCP Cloud Scheduler setup.
  - A brief reflection on the use cases, benefits, and limitations of serverless functions.
- Commit and push this Markdown document, along with the screenshots and code, to your GitHub repository.

## Deliverables
- A Markdown document in a GitHub repository called `HHA504_assignment_functions` that includes:
  - Screenshots of the serverless function deployments.
  - Code and configuration for the GitHub cron job.
  - Documentation of the GCP Cloud Scheduler setup.
  - Reflection on serverless computing.


# Assignment: Working with Cloud Storage in Azure and GCP

## Objective
The objective of this assignment is to familiarize you with cloud storage services in Azure and Google Cloud Platform (GCP). You will learn how to upload files to Azure Blob Storage and GCP Cloud Storage using both Python and the platform's GUI.

## Instructions

### 1. Upload Files Using the GUI
- **Azure Blob Storage:**
  - Navigate to the Azure portal and create a new Storage Account.
  - Create a Blob container within the Storage Account.
  - Upload a sample file (e.g., a text file or image) to the Blob container using the Azure portal.
- **GCP Cloud Storage:**
  - Access the Google Cloud Console and create a new Cloud Storage bucket.
  - Upload a similar sample file to the bucket using the GCP Console.
  - Example repo of what we did during class: ['Class Repo'](https://github.com/hantswilliams/gcp-cloud-storage-demo)

### 2. Upload Files Using Python
- For this section, if you want to make it more realistic, I recommend finding some open source open source x-ray images and uploading them to the cloud storage. This though is not a requirement, just a suggestion. Potential sites where you can find medical images: 
  - [Stanford - Center for Ai and Machine Learning](https://aimi.stanford.edu/shared-datasets)
  - [Kaggle - Xray COVID images](https://www.kaggle.com/datasets/andyczhao/covidx-cxr2)
  - [NLM - Open Access Biomedical images search engine](https://openi.nlm.nih.gov/)
  - [Cancer - Imaging Archive](https://www.cancerimagingarchive.net/browse-collections/)
- **Azure Blob Storage:**
  - Write a Python script that uploads a file to the Blob container you created. Use the `azure-storage-blob` library to handle the upload.
- **GCP Cloud Storage:**
  - Write a Python script that uploads a file to the GCP Cloud Storage bucket you created. Use the `google-cloud-storage` library to handle the upload.

### 3. Explore Storage Features
- **Azure:**
  - Explore and document the options for managing and securing data in Azure Blob Storage (e.g., access policies, tiers).
- **GCP:**
  - Explore and document the options for managing and securing data in GCP Cloud Storage (e.g., IAM permissions, lifecycle rules).

### 4. Submit Your Work
- Create a Markdown document that includes:
  - Screenshots of the file upload process in both Azure Blob Storage and GCP Cloud Storage using the GUI.
  - The Python code used to upload files to both Azure and GCP.
  - Documentation of the storage management and security features you explored.
- Commit and push this Markdown document, along with the screenshots and code, to your GitHub repository.

## Deliverables
- A Markdown document in a GitHub repository called `HHA504_assignment_storage` that includes:
  - Screenshots of file uploads via GUI in Azure and GCP.
  - Python code for uploading files to Azure Blob Storage and GCP Cloud Storage.
  - Notes on storage management and security features in Azure and GCP.


# Assignment: Working with Managed Databases in Azure and GCP

## Objective
The objective of this assignment is to introduce you to managed database services in Azure and Google Cloud Platform (GCP). You will learn how to start, stop, and monitor database-related services, including BigQuery and MySQL.

## Instructions

### 1. Start and Configure a Managed Database
- **Azure MySQL:**
  - Navigate to the Azure portal and create an Azure Database for MySQL.
  - Configure the database with basic settings (e.g., compute and storage options).
  - Start the database service and note the connection details.
- **GCP MySQL:**
  - Access the Google Cloud Console and create a Cloud SQL instance with MySQL.
  - Configure the database instance similarly, noting any differences in setup between Azure and GCP.
  - Start the database service and document the connection details.

### 2. Explore BigQuery (GCP)
- **BigQuery:**
  - In GCP, navigate to BigQuery and create a dataset.
  - Load a small sample data file into a table within the dataset (e.g., a CSV file).
  - Run a simple query against the dataset to retrieve specific data.
  - Monitor the usage and cost associated with running the query.

### 3. Monitor Database Services
- **Azure:**
  - Use the Azure portal to monitor the performance and cost of the MySQL database. Explore metrics like CPU usage, memory, and query performance.
- **GCP:**
  - Use the GCP Console to monitor the Cloud SQL instance and the BigQuery dataset. Pay attention to similar metrics and note any differences in monitoring tools between the two platforms.

### 4. Submit Your Work
- Create a Markdown document that includes:
  - Screenshots of the database creation and configuration process in both Azure and GCP.
  - The SQL query run in BigQuery and the results.
  - Documentation of the monitoring process for both Azure MySQL and GCP MySQL/BigQuery.
  - Reflections on the differences between managing databases on Azure and GCP.
- Commit and push this Markdown document, along with the screenshots and query results, to your GitHub repository.

## Deliverables
- A Markdown document in a GitHub repository called `HHA504_assignment_dbs` that includes:
  - Screenshots of managed database creation and monitoring in Azure and GCP.
  - BigQuery dataset creation and query results.
  - Reflections on database management across Azure and GCP.


# Assignment: Connecting to SQL Databases with SQLAlchemy in Python

## Objective
The objective of this assignment is to help you gain hands-on experience in connecting to SQL databases using SQLAlchemy in Python. You will deploy your own MySQL instance, connect to it using SQLAlchemy, and interact with the database.

## Instructions

### 1. Deploy a MySQL Database
- **Self-Deploy MySQL:**
  - Choose one of the following options to deploy a MySQL database:
    - Deploy a MySQL instance on a local machine or virtual machine.
    - Use a cloud provider to create a MySQL database without using managed services.
  - Document the deployment process, including any configurations made (e.g., user creation, database setup).

### 2. Install SQLAlchemy and Connect to MySQL
- **Install SQLAlchemy:**
  - Install SQLAlchemy and the necessary MySQL connector (`mysqlclient` or `pymysql`) in your Python environment.
- **Connect to MySQL:**
  - Write a Python script that uses SQLAlchemy to connect to your deployed MySQL database.
  - Ensure that the connection string includes the correct credentials and database information.
  
### 3. Interact with the Database
- **Create and Query Tables:**
  - Use SQLAlchemy to create a simple table within your MySQL database (e.g., a table to store user information).
  - Insert some sample data into the table using SQLAlchemy.
  - Write a query using SQLAlchemy to retrieve the data you inserted, and print the results to the console.

### 4. Submit Your Work
- Create a Markdown document that includes:
  - Documentation of your MySQL deployment process.
  - The Python code used to connect to the MySQL database and interact with it using SQLAlchemy.
  - Screenshots of the Python script execution and the query results.
  - Any challenges you faced during the process and how you resolved them.
- Commit and push this Markdown document, along with the Python code and screenshots, to your GitHub repository.

## Deliverables
- A Markdown document in a GitHub repository called `HHA504_assignment_sqlalchemy` that includes:
  - Documentation of MySQL deployment.
  - Python code for connecting and interacting with the MySQL database using SQLAlchemy.
  - Screenshots of the script execution and query results.
  - Reflections on challenges and solutions.


# Assignment: Exploring AI and Analytics with Pre-trained Models in Azure and GCP

## Objective
The objective of this assignment is to introduce you to the use of pre-trained machine learning models in Azure and Google Cloud Platform (GCP). You will use cloud-based notebooks to interact with these models, focusing on speech and vision capabilities.

## Instructions

### 1. Work with Pre-trained Speech Models
- **GCP Speech-to-Text:**
  - Navigate to GCP and access the Vertex AI Notebooks.
  - Use a pre-configured notebook to interact with the GCP Speech-to-Text API.
  - Upload a sample audio file and transcribe it using the pre-trained speech model.
  - Document the results and the steps you took to achieve them.

### 2. Work with Pre-trained Vision Models
- **GCP Vision API:**
  - In the same or a new notebook, interact with the GCP Vision API.
  - Upload an image and use the Vision API to detect objects or text within the image.
  - Document the results and provide a brief analysis of the model's accuracy.
  
- **Azure AI Vision:**
  - Switch to Azure and access Azure Machine Learning (AML) Notebooks.
  - Use a pre-trained vision model in AML to perform a similar task as with GCP, such as object detection or text recognition.
  - Compare the results with those from GCP and document your findings.

### 3. Submit Your Work
- Create a Markdown document that includes:
  - Screenshots or outputs from the GCP Speech-to-Text and Vision API interactions.
  - Screenshots or outputs from the Azure AI Vision model interactions.
  - A comparison of the results from GCP and Azure, including reflections on model accuracy and ease of use.
  - Any challenges faced and how you resolved them.
- Commit and push this Markdown document, along with any relevant notebooks or code, to your GitHub repository.

## Deliverables
- A Markdown document in a GitHub repository called `HHA504_assignment_ai` that includes:
  - Screenshots/outputs from pre-trained model interactions (speech and vision) in GCP and Azure.
  - A comparison and reflection on the results from both platforms.
  - Documentation of any challenges and resolutions.


# Assignment: Deploying and Managing Containers with GCP Cloud Run and Azure Container Apps

## Objective
The objective of this assignment is to provide you with hands-on experience in deploying and managing containers using GCP Cloud Run and Azure Container Apps. You will learn how to containerize an application with Docker and deploy it on both platforms.

## Instructions

### 1. Containerize a Simple Application
- **Create a Docker Image:**
  - Choose a simple application (e.g., a Python Flask app) and create a Dockerfile to containerize the application.
  - Build the Docker image locally and test it to ensure that it runs as expected.

### 2. Deploy to GCP Cloud Run
- **GCP Cloud Run:**
  - Push your Docker image to Google Container Registry (GCR).
  - Deploy the containerized application to GCP Cloud Run.
  - Configure the deployment, including setting environment variables and scaling options.
  - Test the deployed application to ensure it is running correctly.

### 3. Deploy to Azure Container Apps
- **Azure Container Apps:**
  - Push your Docker image to Azure Container Registry (ACR).
  - Deploy the containerized application to Azure Container Apps.
  - Configure the deployment similarly to the GCP deployment, including environment variables and scaling options.
  - Test the deployed application to ensure it is running as expected.

### 4. Submit Your Work
- Create a Markdown document that includes:
  - The Dockerfile used to containerize your application.
  - Screenshots of the deployment process in both GCP Cloud Run and Azure Container Apps.
  - Links to the running applications on both platforms.
  - A reflection on the deployment experience, including any challenges and how you resolved them.
- Commit and push this Markdown document, along with your Dockerfile and any other relevant code, to your GitHub repository.

## Deliverables
- A Markdown document in a GitHub repository called `HHA504_assignment_containers` that includes:
  - The Dockerfile for your containerized application.
  - Screenshots of the deployments on GCP Cloud Run and Azure Container Apps.
  - Links to the deployed applications.
  - Reflections on the deployment process and any challenges faced.


