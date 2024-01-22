from langchain.prompts import PromptTemplate

"""
    This python file acts as a prompt database, although not effective, but is effective when it comes to rapid prototyping.
"""

prompt_template_general = PromptTemplate.from_template(
    """Your task is to generate a pursuasive cover letter given two things:
            1) Resume
            2) Job Description
      
        Resume(Assume that the first few lines are personal details such as name and contact information):
        {resume}
        ------------
        Job Listing
        {job_listing}

        To help you, here is a general structure of a good cover letter:

            - ALWAYS LIMIT the response to less than 300 words. This is VERY IMPORTANT.
            - Opening Remark: Always start the cover letter with a salutation to {hiring_manager_recruiter_name}. Do not forget this!"
            - Introductory Paragraph:
                - It should introduce yourself, the purpose of why you are writing this cover letter. 
                - If you were referred to the job, be sure to mention it, here is the name: {referrer_name}
            - Body Paragraphs:
                - In this section, list your highly relevant, overlapping skills and experience to the job description.
                - Also, do not forget to mention the impact you made with you previous employers.
                - Mention any Awards or Publications if within the word limit.
            - Closing Paragraphs: Here, you should re-emphasize how the company will benefit from your experience, and how you would make a good fit. 
            - Call to Action Paragraph: Thank the employer, and call to action by inviting them to follow up "Let's find a common time to discuss further, thanks!".
        
        Important dos and don'ts while generating the cover letter:
            A. Do's
                - Clearly provide only the relevant information from your resume that overlaps and syncs with the job description.
                - Use a professional, buisness oriented, engaging, optimistic tone.
            B. Don'ts
                - Do not make any grammatical errors, or typographic errors.
                - Do not make up any skills, technologies, or experiences that are not present in the resume text.
                - Do not include any contact information (to or from) received from the resume text.
                - Do not put a introduce a lot of technical jargon.
                - Do not include all technologies or skills mentioned in the resume. 
        
"""
)

template_for_parsing_job_posting_url = PromptTemplate.from_template(
    """
        You are given a job description, your task is to extract the relevant sections which contain information about the following: 
            - Information about the company, namely: Company Name, Company Location, Company Mission and Values
            - Job responsibilities and requirements
            - Required Candidate Qualifications
            - Skills and Technologies required. 
        
        You should not extract any information related to compensation, salary, or employment benfits.:\n{job_description_text}"""
)
