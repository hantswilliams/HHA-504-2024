import requests
import pandas as pd

# Function to search for articles using a specific MeSH term
def search_pubmed(term, retmax=10):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": f"{term}[MeSH Terms]",
        "retmode": "json",
        "retmax": retmax
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    else:
        print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
        return []

# Function to fetch article details using esummary
def fetch_article_details(pmid_list):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmid_list),
        "retmode": "json"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = []
        for pmid, details in data.get("result", {}).items():
            if pmid != "uids":  # Skip the "uids" key
                articles.append({
                    "PMID": pmid,
                    "Title": details.get("title", "N/A"),
                    "Journal": details.get("source", "N/A"),
                    "Publication Date": details.get("pubdate", "N/A"),
                })
        return articles
    else:
        print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
        return []

# Main function to search and create the DataFrame
def pubmed_to_dataframe(mesh_term, retmax=10):
    pmid_list = search_pubmed(mesh_term, retmax)
    if pmid_list:
        article_details = fetch_article_details(pmid_list)
        df = pd.DataFrame(article_details)
        df['link'] = 'https://pubmed.ncbi.nlm.nih.gov/' + df['PMID']
        return df
    else:
        print("No articles found.")
        return pd.DataFrame()


mesh_term = "digital health"  # MeSH term to search
df_pubmed = pubmed_to_dataframe(mesh_term, retmax=10)

# Display the DataFrame
print(df_pubmed)