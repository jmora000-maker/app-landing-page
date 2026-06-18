import streamlit as st

# 1. Page Configuration (using correct standard straight quotes)
st.set_page_config(
    page_title="James D. Mora | AI Portfolio Hub",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Hero Section / Brand Positioning
st.title("Architecting Clarity from Complexity")
st.subheader("Technical Program Leader")

st.markdown(
    """
    I bridge the gap between high-level business strategy and deep technical operations. 
    Below are next-gen AI tools built to eliminate administrative drag, 
    establish clear guardrails, and unlock actionable intelligence.

    *Every engine below is fully containerized and hosted live on **Google Cloud Run**.*
    """
)

st.write("---")

# 3. App Prototype Grid Layout
st.header("Project Prototypes")

# --- APP 1: Automated Risk Report ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("1. Risk Report Dashboard")
        st.markdown(
            """
            **The Bottleneck:** Data-dense, insight-poor static spreadsheet logs stall alignment.

            **The Pipeline:** A three-stage pipeline parsing raw data, applying LLM contextual synthesis, and generating structured executive-ready narratives.
            """
        )
    with col2:
        st.write("##")  # Visual spacing spacing
        st.link_button("Launch Prototype", "https://risk-report-git-226264856502.us-east1.run.app/", type="primary",
                       use_container_width=True)

st.write("---")

# --- APP 2: Automated Risk Audit ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("2. Risk Audit Dashboard")
        st.markdown(
            """
            **The Bottleneck:** The greatest project threats are the ones completely missing from your active registers.

            **The Pipeline:** Uses an intelligent audit engine that cross-references sprint logs against localized vector store embeddings to surface hidden operational threats.
            """
        )
    with col2:
        st.write("##")
        st.link_button("Launch Prototype", "https://risk-engine-git-255439027529.us-east1.run.app/", type="primary",
                       use_container_width=True)

st.write("---")

# --- APP 3: Automated Project Charter ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("3. Project Charter Dashboard")
        st.markdown(
            """
            **The Bottleneck:** Aligning early-stage scoping charters with corporate capital strategy is slow and manually fragmented.

            **The Pipeline:** Contextual synthesis engine that ingests stakeholder raw parameters and compiles a unified charter mathematically mapped to strategic enterprise outcomes.
            """
        )
    with col2:
        st.write("##")
        st.link_button("Launch Prototype", "https://charter-creation-git-255439027529.us-east1.run.app/", type="primary",
                       use_container_width=True)

st.write("---")

# --- APP 4: Stakeholder Gap Detector (IN PROGRESS) ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("4. Stakeholder Audit Dashboard")
        st.markdown(
            """
            **The Bottleneck:** Aligning emerging stakeholder signals with intended stakeholder engagement and actual engagement activity.

            **The Architecture:** A comparative, evidence-grounded multi-document RAG system that analyzes stakeholder artifacts to detect execution gaps, coverage gaps, and emerging engagement risks.
            """
        )
    with col2:
        st.write("##")
        st.button("In Progress", disabled=True, use_container_width=True)


st.write("---")

# 4. Footer & Fiduciary Proof
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.85em;'>
        James D. Mora, PMP | Next-Gen Delivery | Villanova AI Certified <br>
        <a href='https://www.linkedin.com/in/jamesdmora' target='_blank'>Connect on LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)