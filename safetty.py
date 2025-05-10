import os
import streamlit as st
from crewai import Agent, Task, Crew, LLM

# Set your Gemini API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyDiHecufG4caaZpc8fJr_iZ6hTGmm1gPuw"  # Replace 'key' with your actual API key

# Initialize LLM with Gemini
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7,
    api_key=os.environ["GOOGLE_API_KEY"]
)

# Setup the Agent
safety_professional = Agent(
    role="Senior safety expert",
    goal="Give the best safety advice and analysis",
    backstory="You work at a top firm with global insights.",
    verbose=True,
    llm=llm
)

# Streamlit App Interface
st.set_page_config(page_title="CrewAI Safety Advisor", layout="centered")
st.title("🛡️ Safety Advisor")
st.write("Your safety is important to me.")

# Input box for question
user_input = st.text_input("Enter your safety-related question:")

# Button to run CrewAI
if st.button("Get Advice") and user_input:
    with st.spinner("Thinking..."):
        # Create a new task for each input
        task = Task(
            description=user_input,
            expected_output="Clear, expert safety advice or analysis.",
            agent=safety_professional
        )

        # Create crew and run
        crew = Crew(agents=[safety_professional], tasks=[task], verbose=False)
        result = crew.kickoff()

        # Display result
        st.success("✅ Advice Received")
        st.markdown(f"**Response:**\n\n{result}")
