from langchain.document_loaders import AsyncChromiumLoader
from PyPDF2 import PdfReader
from langchain.document_transformers import Html2TextTransformer
from llm_agent.initialize_llm import setup_agent
from prompts import prompt_database


def resume_parser(path):
    """
    Use PyPDF2 as a PDF Parser
    There are various PDF Parser's available in open source.

    This function takes in the PDF, and parses the first page of the resume, and returns the extracted text.

    """
    loader = PdfReader(path)
    text = loader.pages[0].extract_text()
    return text


def job_url_listing_parser(url):
    """
        This function loads the URL, and uses HTML parsing to extract the text from relevant HTML tags.

    """
    loader = AsyncChromiumLoader([url])
    html = loader.load()

    html2text_function = Html2TextTransformer()
    job_description_text = html2text_function.transform_documents(html)[0].page_content

    # call the LLM to extract important sections from the job description
    agent = setup_agent(temperature=1.0)
    prompt_template = prompt_database.template_for_parsing_job_posting_url.format(job_description_text=job_description_text)

    resp = agent.invoke(prompt_template.format(job_description_text=job_description_text))
    text = resp.content

    return text


def cover_letter_generation_invoke(resume_text, job_listing_text, prompt_template, hiring_manager_recruiter_name, referrer_name):

    """
        This function invokes the LLM agent, and performs prompt templating with the arguments.
    """
    agent = setup_agent()
    resp = agent.invoke(prompt_template.format(resume=resume_text, job_listing=job_listing_text, hiring_manager_recruiter_name = hiring_manager_recruiter_name, referrer_name = referrer_name))
    text = resp.content
    return text