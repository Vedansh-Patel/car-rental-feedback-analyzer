# Car Rental Customer Feedback Analyzer

This project analyzes customer reviews of car rental services to identify sentiment, extract key issues, and generate an automated performance summary.

## Objective
- Classify customer sentiments (Positive, Negative, Neutral)
- Extract recurring service issues (e.g., late delivery, dirty car)
- Visualize trends to help service teams improve performance

## Tools & Technologies
- Python 3.x
- IBM watsonx.ai (Prompt Lab)
- IBM Cloud Object Storage
- Pandas, Matplotlib, Seaborn
- Boto3 for IBM COS access
- VSCode/Any IDE

## Project Structure
project/
├── car2.csv              # Sample dataset
├── feedback_analysis.py  # Main analysis script
├── .env.example          # Template for environment variables



COS_ENDPOINT=https://s3.us-south.cloud-object-storage.appdomain.cloud
COS_API_KEY=your_ibm_api_key
BUCKET_NAME=sentiment-8gbw7k1z4jnwop1
OBJECT_NAME=car2.csv

## How to Run
python project/feedback_analysis.py

Outputs:
- Pie chart of sentiment breakdown
- Bar chart of top customer issues
- Printed performance summary

## Prompt Lab Usage

- Sentiment Prompt:
  Classify the sentiment of this customer review as Positive, Negative, or Neutral. Give answer in one word.

- Issue Extraction Prompt:
  Extract any service-related issues mentioned. If there are no issues, return an empty string.

## Sample Output
- Pie chart showing distribution of customer sentiment
- Bar chart of top 10 issues (e.g., dirty car, late delivery)
- Summary:
  - Total Reviews
  - Sentiment Counts
  - Top Issues

## Author
Vedansh Patel  
IBM GenAI Project | IBM watsonx.ai + Python


