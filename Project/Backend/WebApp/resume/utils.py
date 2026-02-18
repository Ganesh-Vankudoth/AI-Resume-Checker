import PyPDF2
import re
def extract_text_from_pdf(file_path):
    text=""

    try:
        with open(file_path,'rb') as file:
            reader=PyPDF2.PdfReader(file)

            for page in reader.pages:
                extracted=page.extract_text()
                if extracted:
                    text+=extracted
    except Exception as e:
        print("Error extracting text:",e)
    return text

ROLE_KEYWORDS={
    "python_dev":["python","django","api","mysql","git"],
    "frontend_dev":["react","javascript","html","css","redux"],
    "data_analyst":["python","pandas","sql","excel","powerbi"]
}
def analyze_resume(text,job_role):
    

    text=text.lower()
    keywords = ROLE_KEYWORDS.get(job_role,[])
    matched=[]
    for keyword in keywords:
        pattern = r"\b" + re.escape(keyword) + r"\b"
        if re.search(pattern,text):
            matched.append(keyword)
    missing = list(set(keywords) - set(matched))    
    if len(keyword)>0:
        score=int((len(matched)/len(keywords))*100)
    else:
        score=0
    return score,matched,missing