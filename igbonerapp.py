import streamlit as st
import spacy
from spacy import displacy

# Define a function to read entities from files
def read_entities_from_file(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        entities = [line.strip() for line in file if line.strip()]
    return entities

# Read entities from the files
locs = read_entities_from_file('IgboNER_loc.txt')
orgs = read_entities_from_file('IgboNER_org.txt')
pers = read_entities_from_file('IgboNER_per.txt')
dates = read_entities_from_file('IgboNER_date.txt')

# Load the English model and disable NER and parser
nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"]) # we will change the English model later...

# add spacy's EntityRuler
ruler = nlp.add_pipe('entity_ruler', before='ner')

# Define entity patterns based on LOC, DATE, ORG, and PER tokens
patterns  = [{'label':'LOC', 'pattern':loc} for loc in set(locs)]
patterns += [{'label':'DATE', 'pattern':date} for date in set(dates)]
patterns += [{'label':'ORG', 'pattern':orgs} for orgs in set(orgs)]
patterns += [{'label':'PER', 'pattern':pers} for pers in set(pers)]

# Add the patterns to the entity ruler
ruler.add_patterns(patterns)

st.markdown("## Igbo NER Demo")
st.markdown("##### This is the demo app for Igbo Named Entity Recognition")

input_text = st.text_area( "Text to analyze",
  "O mere Steeti Abịa nwee gọvanọ dịkarịsịrị njọ na republik nke anọ ya bụ Theodore Orji."
  "Ihe nyere ọṅụ banyere okwu a bụ na Orji Uzor Kalu kwuru na facebook bụ na ọ banyere APC n'ihi nkwa nke Buhari kwere ya na ndị ọrụ ngo nke Ndịdaọwụwa Anyanwụ South-East agaalaghị nihu ọrụ tupu ọnwa Nọvemba."
  "Abanyere m APC nihi na Buhari emezuola nkwa nke o kwere m ma nwekwaa olileanya na ọ gaeme karịa."
  "Dịka ihe nrite ịbanye APC president Buhari nyere ọtụtụ ọrụ okporoụzọ naka ndị ọrụ ngo Slok Holding."
  "Nakwa Niger Delta Development Commission nyere ndị Slok Holding ego ịrụ okporoụzọ si Ụmụahịa jee Uzuakoli nakwa nke si Uzuakoli jee Ozuitem."
  "Na chi ọjọọ nke Sinetọ Orji Uzor Kalụ okwu ụlọikpe ya na ndị Economic and Financial Crimes Commission nwere apụghị dịka o lere anya."
  "Ugbua Kalu na-eje mkpọrọ ndị dịka Tinubu, Patience Jonathan, Olisa Metu, Femi Fanikayode, ga-enye mkpesa etu ha siri jeere ọhanaeze ozi."
  "Ka anyị na-achịkọba ihe nkpata ndị a niile, anyị na-atụ anya ife na mmalite afọ 2020 ma nyefee n'afọ 2021."
  "Satọde abalị iri abụọ na otu nke ọnwa Mee afọ 2016, 'The Great Hall, nke Kensington dị na mba London, chịkọbara emume inye onyinye nke bukarịsịrị n'ibu nye ụmụ nwaanyị nke mba Europe na ndị Commonwealth."
, height=150,
)

doc = nlp(input_text)

# Take the text from the input field and render the entity html.
# Note that style="ent" indicates entities.
ent_html = displacy.render(doc, style="ent", jupyter=False)

# Display the entity visualization in the browser:
st.markdown(ent_html, unsafe_allow_html=True)

# st.write(f"You wrote {len(input_text)} characters.")
