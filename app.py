import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="James D. Mora | AI Portfolio Hub",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Architecting Clarity from Complexity")
st.subheader("James D. Mora | Technical Program Leader")

st.markdown(
    """
    I bridge the gap between high-level business strategy and deep technical operations. 
    Below are Next-Gen AI tools built to unlock actionable intelligence, establish clear guardrails, and eliminate administrative drag.

    *Every engine below is fully containerized and hosted live on **Google Cloud Run**.*
    """
)

st.write("---")

#  App Prototype Grid Layout
st.header("Project Prototypes")

# --- APP 1: Stakeholder Alignment Dashboard ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("1. Schedule Risk Dashboard")
        st.markdown(
            """
            **The Bottleneck:** Schedule risk signals are scattered across plans, updates, issue logs, and meeting notes, making slippage hard to detect before milestones are missed.

            **The Pipeline:** A schedule-risk engine that connects tasks, dependencies, issues, updates, and meeting evidence into early warnings, prioritized findings, and actionable responses.
            """
        )
    with col2:
        st.write("##")  # Visual spacing
        st.link_button(
            "Launch Prototype",
            "https://schedule-risk-783573342516.us-east1.run.app/",
            type="primary",
            use_container_width=True
        )

st.write("---")

# --- APP 2: Stakeholder Alignment Dashboard ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("2. Stakeholder Alignment Dashboard")
        st.markdown(
            """
            **The Bottleneck:** Fragmented records and inconsistent engagement cadences create governance blind spots that stall project momentum.

            **The Pipeline:** A risk-weighted engine that synthesizes raw stakeholder feedback into a prioritized, executive-ready roadmap for decisive action.
            """
        )
    with col2:
        st.write("##")  # Visual spacing
        st.link_button("Launch Prototype", " https://stakeholder-management-255439027529.us-east1.run.app/", type="primary",
                       use_container_width=True)

st.write("---")

# --- APP 2: Automated Risk Audit ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("3. Risk Audit Dashboard")
        st.markdown(
            """
            **The Bottleneck:** The greatest project threats are the ones completely missing from your active registers.

            **The Pipeline:** Uses an intelligent audit engine that cross-references registered risks against localized vector store embeddings to surface hidden operational threats.
            """
        )
    with col2:
        st.write("##")
        st.link_button("Launch Prototype", "https://risk-engine-git-255439027529.us-east1.run.app/", type="primary",
                       use_container_width=True)

st.write("---")


# --- APP 3: Automated Risk Report ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("4. Risk Report Dashboard")
        st.markdown(
            """
            **The Bottleneck:** Data-dense, insight-poor static spreadsheets stall alignment.

            **The Pipeline:** A three-stage pipeline normalizing risk data, applying LLM contextual synthesis, and generating structured executive-ready narratives.
            """
        )
    with col2:
        st.write("##")  # Visual spacing
        st.link_button("Launch Prototype", "https://risk-report-git-226264856502.us-east1.run.app/", type="primary",
                       use_container_width=True)

st.write("---")

# --- APP 4: Automated Project Charter ---
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("5. Project Charter Dashboard")
        st.markdown(
            """
            **The Bottleneck:** Aligning early-stage scoping charters with corporate strategy is slow and manually fragmented.

            **The Pipeline:** Contextual synthesis engine that ingests stakeholder raw parameters and compiles a unified charter mathematically mapped to strategic enterprise outcomes.
            """
        )
    with col2:
        st.write("##")
        st.link_button("Launch Prototype", "https://charter-creation-git-255439027529.us-east1.run.app/", type="primary",
                       use_container_width=True)

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