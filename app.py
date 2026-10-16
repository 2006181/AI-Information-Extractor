from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional
import json


# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="AI Information Extractor",
    page_icon="🎬",
    layout="wide"
)


# -------------------- PYDANTIC SCHEMA --------------------

class MovieInfo(BaseModel):
    main_subject: str = Field(description="Main subject of the paragraph")
    title_name: str = Field(description="Title or name")
    category_type: str = Field(description="Category or type")
    release_year_date: Optional[int] = Field(
        default=None,
        description="Release year"
    )
    people_cast: List[str] = Field(description="People or cast members")
    director_creator_author: List[str] = Field(
        description="Director, creator, or author"
    )
    organizations_companies: List[str] = Field(
        description="Organizations or companies"
    )
    genre_category: str = Field(description="Genre or category")
    subgenres: List[str] = Field(description="Subgenres")
    themes_topics: List[str] = Field(description="Themes or topics")


# -------------------- MODEL & PARSER --------------------

@st.cache_resource
def load_chain():
    model = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0
    )

    parser = PydanticOutputParser(
        pydantic_object=MovieInfo
    )

    prompt = PromptTemplate(
        template="""
You are an Information Extraction Assistant.

Extract information only from the given paragraph.

PARAGRAPH:
{paragraph}

Rules:
- Do not invent information.
- If a string field is missing, return "Not mentioned".
- If a list field has no information, return an empty list.
- If the release year is unavailable, return null.
- Return data according to the given schema.
- Return only JSON. Do not include explanations or markdown.

{format_instructions}
""",
        input_variables=["paragraph"],
        partial_variables={
            "format_instructions": parser.get_format_instructions()
        }
    )

    chain = prompt | model | parser

    return chain


# -------------------- HEADER --------------------

st.title("🎬 AI Information Extractor")

st.write(
    "Extract structured information from any paragraph "
    "using Google Gemini, LangChain, and Pydantic."
)

st.divider()


# -------------------- INPUT SECTION --------------------

st.subheader("📝 Enter Your Paragraph")

paragraph = st.text_area(
    "Paste your text below",
    placeholder=(
        "Example: Inception is a science fiction movie "
        "released in 2010. It was directed by Christopher "
        "Nolan and stars Leonardo DiCaprio."
    ),
    height=180
)

extract_button = st.button(
    "🚀 Extract Information",
    type="primary",
    use_container_width=True
)


# -------------------- EXTRACTION --------------------

if extract_button:

    if not paragraph.strip():
        st.warning("Please enter a paragraph first.")

    else:
        try:
            with st.spinner("🤖 Analyzing your paragraph..."):

                chain = load_chain()
                result = chain.invoke({
                    "paragraph": paragraph
                })

                json_output = result.model_dump_json(indent=4)
                data = json.loads(json_output)

            st.success("Information extracted successfully!")

            st.divider()

            # -------------------- RESULTS --------------------

            st.subheader("📊 Extracted Information")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Main Subject",
                    data["main_subject"]
                )

            with col2:
                st.metric(
                    "Category",
                    data["category_type"]
                )

            with col3:
                st.metric(
                    "Release Year",
                    (
                        data["release_year_date"]
                        if data["release_year_date"] is not None
                        else "Not mentioned"
                    )
                )

            # -------------------- DETAILS --------------------

            st.subheader("📌 Detailed Information")

            with st.expander("🎥 Basic Information", expanded=True):
                st.write("**Title / Name:**", data["title_name"])
                st.write("**Main Subject:**", data["main_subject"])
                st.write("**Category / Type:**", data["category_type"])
                st.write(
                    "**Release Year:**",
                    data["release_year_date"]
                    if data["release_year_date"] is not None
                    else "Not mentioned"
                )

            with st.expander("👥 People & Organizations"):
                st.write("**People / Cast:**")
                st.write(data["people_cast"] or ["Not mentioned"])

                st.write("**Director / Creator / Author:**")
                st.write(
                    data["director_creator_author"] or ["Not mentioned"]
                )

                st.write("**Organizations / Companies:**")
                st.write(
                    data["organizations_companies"] or ["Not mentioned"]
                )

            with st.expander("🏷️ Classification"):
                st.write("**Genre / Category:**", data["genre_category"])

                st.write("**Subgenres:**")
                st.write(data["subgenres"] or ["Not mentioned"])

                st.write("**Themes / Topics:**")
                st.write(data["themes_topics"] or ["Not mentioned"])

            # -------------------- JSON OUTPUT --------------------

            st.divider()

            st.subheader("💻 JSON Output")

            st.caption(
                "Validated structured output generated using Pydantic."
            )

            st.code(json_output, language="json")

            # -------------------- DOWNLOAD --------------------

            st.download_button(
                label="⬇️ Download JSON",
                data=json_output,
                file_name="extracted_information.json",
                mime="application/json",
                use_container_width=True
            )

        except Exception as e:
            st.error(
                "Something went wrong while extracting information."
            )
            st.exception(e)


# -------------------- FOOTER --------------------

st.divider()

st.caption(
    "Built with Streamlit • LangChain • Google Gemini • Pydantic"
)