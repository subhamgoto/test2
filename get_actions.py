import re
import spacy
nlp = spacy.load("en_core_web_sm")

def isAction(text):
    words = ['are', 'arent', 'can', 'could', 'did', 'do', 'does', 'dont', 'had', 'has', 'have', 'how', 'is', 'may', 'might', 'shall', 'should', 'to', 'was', 'were', 'what', 'when', 'where', 'which', 'who', 'whom', 'whose', 'why', 'will', 'wont', 'would']
    if (text.lower().strip().split(" ")[0].strip() in words or "?" in text):
        return True
    else:
        return False
    
def isAction2(text):
    text=text.strip()
    doc = nlp(text)
    pos = [token.pos_ for token in doc]
    if len(pos)>2 and pos[1]=="VERB":
        return True
    else:
        return False
    
def processText(text):
    sentences = re.split('\?|\.|!|\n',text)
    out = [s for s in sentences if (isAction(s) or isAction2(s))]
    return out
    
text = """
Hello Team,

Can you please reset my password? I am not able to open it for long time. Also can you please unlock my account?
"""
processText(text)
