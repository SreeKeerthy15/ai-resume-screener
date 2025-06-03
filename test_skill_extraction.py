import spacy
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

nlp = spacy.load("en_core_web_sm")
phrase_matcher = PhraseMatcher(nlp.vocab)
skill_extractor = SkillExtractor(nlp, SKILL_DB, phrase_matcher)

SKILL_CATEGORIES = {
    "Technical": ["python", "java", "c++", "sql", "html", "css"],
    "Tools": ["git", "docker", "kubernetes", "aws"]
    ,
    "Soft Skills": ["communication", "leadership", "teamwork"],
    "Certifications": ["aws certified", "pmp", "azure fundamentals"],
}

def extract_skills(text):
    extracted_skills = skill_extractor.extract_skills(text)
    skills = [skill[0].lower() for skill in extracted_skills]
    return list(set(skills))

sample_text = """
I am experienced in Python, Java, Docker, AWS Certified Solutions Architect, and great communication skills.
"""

print(extract_skills(sample_text))
