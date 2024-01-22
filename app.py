from prompts import prompt_database
import pyperclip
import streamlit as st
from parser_functions.utils_functions import *
from dotenv import load_dotenv
load_dotenv()


def main():
    if 'cover_letter' not in st.session_state:
        st.session_state.cover_letter = None

    st.title(":open_book: Generator AI: Cover Letter :open_book:")

    # openai_api_key = st.sidebar.text_input('OpenAI API Key')

    # Upload Resume
    st.header("1. Resume Upload (PDF)")
    resume = st.file_uploader("Choose a file or drag & drop", type=["pdf"])
    extracted_text_from_resume = None
    if resume is not None:
        extracted_text_from_resume = resume_parser(resume)

    # Job Description
    st.header("2. Input Job Listing")

    job_type = st.radio("Select job input type", ("URL", "Text"))

    job_description_text = st.session_state.job_type if "job_description_text" in st.session_state else None
    
    if job_type == "URL":
        job_link_url = st.text_input("Enter the job listing URL/Link", "")
        if st.button("Retrieve Job Listing"):
            job_description_text = job_url_listing_parser(job_link_url)
            st.session_state.job_description_text = job_description_text
    elif job_type == "Text":
        job_description_text = st.text_area("Copy, and paste the entire description", "")

    # Hiring Manager or Recruiter
    st.header("3. Hiring Manager or Recruiter's Name")
    hiring_manager_recruiter_name = st.text_area('Enter the name of hiring manager or recruiter.. else keep empty')

    # Referral
    st.header("4. Did someone refer you?")
    referrer_name = st.text_area('Enter the name of person who referred you..')

    # Trigger the Cover Letter Generator
    st.header(":rocket: :rocket: Generate the Cover Letter")
    if st.button("Generate the Cover Letter"):
        
        if extracted_text_from_resume is not None and job_description_text is not None and hiring_manager_recruiter_name is not None and referrer_name is not None:
            prompt_template = prompt_database.prompt_template_general
            cover_letter = cover_letter_generation_invoke(extracted_text_from_resume, job_description_text, prompt_template, hiring_manager_recruiter_name, referrer_name)
            st.subheader("Cover Letter:")
            st.markdown(cover_letter)
            st.session_state.cover_letter = cover_letter
        else:
            st.warning("Please upload a resume and provide a job listing.")

    # Show the cover letter as an output or response
    if st.session_state.cover_letter is not None:
        if st.button("You may copy it to clipboard here"):
            pyperclip.copy(st.session_state.cover_letter)
            st.success("Copied!")

if __name__ == "__main__":
    main()
