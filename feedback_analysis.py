import ibm_boto3
from ibm_botocore.client import Config
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import io
import os
from dotenv import load_dotenv

load_dotenv()

cos_endpoint = os.getenv("COS_ENDPOINT")
cos_api_key_id = os.getenv("COS_API_KEY")
bucket_name = os.getenv("BUCKET_NAME")
item_name = os.getenv("OBJECT_NAME")

cos = ibm_boto3.client(
    service_name='s3',
    ibm_api_key_id=cos_api_key_id,
    config=Config(signature_version='oauth'),
    endpoint_url=cos_endpoint
)

csv_obj = cos.get_object(Bucket=bucket_name, Key=item_name)
body = csv_obj['Body'].read()
df = pd.read_csv(io.BytesIO(body))

# Sentiment distribution
sentiment_counts = df['Sentiment'].value_counts()
plt.figure(figsize=(6, 6))
sentiment_counts.plot.pie(autopct='%1.1f%%', title="Sentiment Distribution", ylabel="")
plt.show()

# Key issues analysis
all_issues = df['KeyIssues'].dropna().astype(str).str.split(',').sum()
issue_cleaned = [issue.strip().lower() for issue in all_issues]
issue_counts = Counter(issue_cleaned)
issue_df = pd.DataFrame(issue_counts.items(), columns=['Issue', 'Frequency']).sort_values(by='Frequency', ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(data=issue_df.head(10), x='Frequency', y='Issue', palette='coolwarm')
plt.title("Top 10 Customer Issues")
plt.xlabel("Count")
plt.ylabel("Issue")
plt.tight_layout()
plt.show()

# Summary
print("Performance Summary")
print("-" * 40)
print(f"Total Reviews: {len(df)}")
print("\nSentiment Breakdown:")
print(sentiment_counts.to_string())
print("\nTop 5 Issues:")
print(issue_df.head().to_string(index=False))
