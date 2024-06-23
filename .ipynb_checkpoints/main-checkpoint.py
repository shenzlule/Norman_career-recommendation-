import csv
import os
import pandas as pd
import numpy as np



def append_dict_to_csv(file_name, dict_data):
    """
    Appends a dictionary object to a CSV file.

    Args:
    - file_name (str): The name of the CSV file to append to.
    - dict_data (dict): The dictionary object to append. Keys will be column headers, values will be row values.

    Returns:
    - None
    """
    file_exists = os.path.isfile(file_name)

    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dict_data.keys())

        if not file_exists:
            writer.writeheader()  # Write a header if the file is being created for the first time

        writer.writerow(dict_data)


# Define possible values for categorical variables
education_levels = ["High School", "Associate Degree", "Bachelor's Degree", "Master's Degree", "Ph.D."]
work_environments = ["Startup", "Corporate", "Freelance", "Remote"]
tech_domains = ["Web Development", "Data Science", "DevOps", "AI/ML", "Cybersecurity", "Mobile Development",
                "Game Development", "IT Support", "Network Administration", "Technical Writing"]
career_goals = ["Technical Leadership", "Project Management", "Specialized Technical Expert", "Entrepreneur"]
technology_stacks = ["MERN", "MEAN", "LAMP", "JAMstack", "React Native", "Flutter", "Unity", "Unreal Engine", "Django",
                     "Ruby on Rails"]


technology_stacks_needed = {
    "Web Development": ["MERN", "MEAN", "LAMP", "JAMstack", "React Native", "Flutter", "Django", "Ruby on Rails"],
    "Data Science": ["Python (NumPy, Pandas, SciPy)", "R", "SQL", "TensorFlow", "PyTorch", "Scikit-learn"],
    "DevOps": ["AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "Jenkins", "Ansible"],
    "AI/ML": ["Python", "TensorFlow", "PyTorch", "Scikit-learn", "Keras"],
    "Cybersecurity": ["Wireshark", "Metasploit", "Nmap", "Snort", "Kali Linux", "Security Onion"],
    "Mobile Development": ["React Native", "Flutter", "Swift", "Kotlin", "Java (Android)"],
    "Game Development": ["Unity", "Unreal Engine", "Godot Engine", "CryEngine", "Lumberyard"],
    "IT Support": ["Windows Server", "Active Directory", "Linux", "Networking Basics", "Troubleshooting"],
    "Network Administration": ["Cisco", "Juniper", "CCNA", "CCNP", "Network Security"],
    "Technical Writing": ["Markdown", "Adobe FrameMaker", "MadCap Flare", "MS Word", "XML"]
}


# Function to generate random samples
def generate_sample():
    age = np.random.randint(22, 36)
    education_level = np.random.choice(education_levels)
    years_of_experience = np.random.randint(2, 11)
    programming_languages_proficiency = np.random.randint(5, 11)

    # Assign proficiencies based on chosen career domain
    tech_domain = np.random.choice(tech_domains)
    if tech_domain in ["Web Development", "Mobile Development"]:
        web_dev_proficiency = np.random.randint(7, 11)
        mobile_dev_proficiency = np.random.randint(7, 11)
        data_science_proficiency = np.random.randint(1, 6)
        devops_proficiency = np.random.randint(1, 6)
        cybersecurity_proficiency = np.random.randint(1, 6)
        ai_ml_proficiency = np.random.randint(1, 6)
        game_dev_proficiency = np.random.randint(1, 6)
        database_proficiency = np.random.randint(5, 10)
        api_proficiency = np.random.randint(5, 10)
        full_stack_proficiency = np.random.randint(7, 11)
        preferred_technology_stack = np.random.choice(technology_stacks_needed[tech_domain])
    elif tech_domain == "Data Science":
        preferred_technology_stack = np.random.choice(technology_stacks_needed[tech_domain])
        web_dev_proficiency = np.random.randint(1, 6)
        mobile_dev_proficiency = np.random.randint(1, 6)
        data_science_proficiency = np.random.randint(7, 11)
        devops_proficiency = np.random.randint(1, 6)
        cybersecurity_proficiency = np.random.randint(1, 6)
        ai_ml_proficiency = np.random.randint(7, 11)
        game_dev_proficiency = np.random.randint(1, 6)
        database_proficiency = np.random.randint(5, 10)
        api_proficiency = np.random.randint(5, 10)
        full_stack_proficiency = np.random.randint(1, 6)
    elif tech_domain == "DevOps":
        preferred_technology_stack = np.random.choice(technology_stacks_needed[tech_domain])
        web_dev_proficiency = np.random.randint(1, 6)
        mobile_dev_proficiency = np.random.randint(1, 6)
        data_science_proficiency = np.random.randint(1, 6)
        devops_proficiency = np.random.randint(7, 11)
        cybersecurity_proficiency = np.random.randint(1, 6)
        ai_ml_proficiency = np.random.randint(1, 6)
        game_dev_proficiency = np.random.randint(1, 6)
        database_proficiency = np.random.randint(5, 10)
        api_proficiency = np.random.randint(5, 10)
        full_stack_proficiency = np.random.randint(1, 6)
    elif tech_domain == "AI/ML":
        preferred_technology_stack = np.random.choice(technology_stacks_needed[tech_domain])
        web_dev_proficiency = np.random.randint(1, 6)
        mobile_dev_proficiency = np.random.randint(1, 6)
        data_science_proficiency = np.random.randint(7, 11)
        devops_proficiency = np.random.randint(1, 6)
        cybersecurity_proficiency = np.random.randint(1, 6)
        ai_ml_proficiency = np.random.randint(7, 11)
        game_dev_proficiency = np.random.randint(1, 6)
        database_proficiency = np.random.randint(1, 6)
        api_proficiency = np.random.randint(1, 6)
        full_stack_proficiency = np.random.randint(1, 6)
    elif tech_domain == "Cybersecurity":
        preferred_technology_stack = np.random.choice(technology_stacks_needed[tech_domain])
        web_dev_proficiency = np.random.randint(1, 6)
        mobile_dev_proficiency = np.random.randint(1, 6)
        data_science_proficiency = np.random.randint(1, 6)
        devops_proficiency = np.random.randint(1, 6)
        cybersecurity_proficiency = np.random.randint(7, 11)
        ai_ml_proficiency = np.random.randint(1, 6)
        game_dev_proficiency = np.random.randint(1, 6)
        database_proficiency = np.random.randint(1, 6)
        api_proficiency = np.random.randint(1, 6)
        full_stack_proficiency = np.random.randint(1, 6)
    elif tech_domain == "Game Development":
        preferred_technology_stack = np.random.choice(technology_stacks_needed[tech_domain])
        web_dev_proficiency = np.random.randint(1, 6)
        mobile_dev_proficiency = np.random.randint(1, 6)
        data_science_proficiency = np.random.randint(1, 6)
        devops_proficiency = np.random.randint(1, 6)
        cybersecurity_proficiency = np.random.randint(1, 6)
        ai_ml_proficiency = np.random.randint(1, 6)
        game_dev_proficiency = np.random.randint(7, 11)
        database_proficiency = np.random.randint(1, 6)
        api_proficiency = np.random.randint(1, 6)
        full_stack_proficiency = np.random.randint(1, 6)
    elif tech_domain == "IT Support":
        preferred_technology_stack = np.random.choice(technology_stacks_needed[tech_domain])
        web_dev_proficiency = np.random.randint(1, 6)
        mobile_dev_proficiency = np.random.randint(1, 6)
        data_science_proficiency = np.random.randint(1, 6)
        devops_proficiency = np.random.randint(1, 6)
        cybersecurity_proficiency = np.random.randint(7, 11)
        ai_ml_proficiency = np.random.randint(1, 6)
        game_dev_proficiency = np.random.randint(1, 6)
        database_proficiency = np.random.randint(1, 6)
        api_proficiency = np.random.randint(1, 6)
        full_stack_proficiency = np.random.randint(1, 6)
    elif tech_domain == "Network Administration":
        preferred_technology_stack = np.random.choice(technology_stacks_needed[tech_domain])
        web_dev_proficiency = np.random.randint(1, 6)
        mobile_dev_proficiency = np.random.randint(1, 6)
        data_science_proficiency = np.random.randint(1, 6)
        devops_proficiency = np.random.randint(7, 11)
        cybersecurity_proficiency = np.random.randint(7, 11)
        ai_ml_proficiency = np.random.randint(1, 6)
        game_dev_proficiency = np.random.randint(1, 6)
        database_proficiency = np.random.randint(1, 6)
        api_proficiency = np.random.randint(1, 6)
        full_stack_proficiency = np.random.randint(1, 6)
    elif tech_domain == "Technical Writing":
        preferred_technology_stack = np.random.choice(technology_stacks_needed[tech_domain])
        web_dev_proficiency = np.random.randint(1, 6)
        mobile_dev_proficiency = np.random.randint(1, 6)
        data_science_proficiency = np.random.randint(1, 6)
        devops_proficiency = np.random.randint(1, 6)
        cybersecurity_proficiency = np.random.randint(1, 6)
        ai_ml_proficiency = np.random.randint(1, 6)
        game_dev_proficiency = np.random.randint(1, 6)
        database_proficiency = np.random.randint(1, 6)
        api_proficiency = np.random.randint(1, 6)
        full_stack_proficiency = np.random.randint(1, 6)
    else:
        # Fallback for other domains
        web_dev_proficiency = np.random.randint(1, 6)
        mobile_dev_proficiency = np.random.randint(1, 6)
        data_science_proficiency = np.random.randint(1, 6)
        devops_proficiency = np.random.randint(1, 6)
        cybersecurity_proficiency = np.random.randint(1, 6)
        ai_ml_proficiency = np.random.randint(1, 6)
        game_dev_proficiency = np.random.randint(1, 6)
        database_proficiency = np.random.randint(1, 6)
        api_proficiency = np.random.randint(1, 6)
        full_stack_proficiency = np.random.randint(1, 6)

    problem_solving_skills = np.random.randint(1, 11)
    communication_skills = np.random.randint(1, 11)
    time_management_skills = np.random.randint(1, 11)
    collaboration_skills = np.random.randint(1, 11)
    ui_ux_proficiency = np.random.randint(1, 11)
    graphic_design_proficiency = np.random.randint(1, 11)
    prototyping_wireframing_skills = np.random.randint(1, 11)
    web_security_knowledge = np.random.randint(1, 11)
    performance_optimization_skills = np.random.randint(1, 11)
    seo_knowledge = np.random.randint(1, 11)
    testing_debugging_skills = np.random.randint(1, 11)
    staying_updated_skills = np.random.randint(1, 11)
    flexibility = np.random.randint(1, 11)
    preferred_work_environment = np.random.choice(work_environments)
    career_goal = np.random.choice(career_goals)
    # preferred_technology_stack = np.random.choice(technology_stacks)
    predicted_career_path = tech_domain

    return {
        "Age": age,
        "Education_Level": education_level,
        "Years_of_Experience": years_of_experience,
        "Programming_Languages_Proficiency": programming_languages_proficiency,
        "Web_Development_Proficiency": web_dev_proficiency,
        "Mobile_Development_Proficiency": mobile_dev_proficiency,
        "Data_Science_Proficiency": data_science_proficiency,
        "DevOps_Proficiency": devops_proficiency,
        "Cybersecurity_Proficiency": cybersecurity_proficiency,
        "AI_ML_Proficiency": ai_ml_proficiency,
        "Game_Development_Proficiency": game_dev_proficiency,
        "Database_Proficiency": database_proficiency,
        "API_Proficiency": api_proficiency,
        "Full_Stack_Proficiency": full_stack_proficiency,
        "Problem_Solving_Skills": problem_solving_skills,
        "Communication_Skills": communication_skills,
        "Time_Management_Skills": time_management_skills,
        "Collaboration_Skills": collaboration_skills,
        "UI_UX_Proficiency": ui_ux_proficiency,
        "Graphic_Design_Proficiency": graphic_design_proficiency,
        "Prototyping_Wireframing_Skills": prototyping_wireframing_skills,
        "Web_Security_Knowledge": web_security_knowledge,
        "Performance_Optimization_Skills": performance_optimization_skills,
        "SEO_Knowledge": seo_knowledge,
        "Testing_Debugging_Skills": testing_debugging_skills,
        "Staying_Updated_Skills": staying_updated_skills,
        "Flexibility": flexibility,
        "Preferred_work_environment":preferred_work_environment,
        "Career_goal":career_goal,
        "Preferred_technology_stack":preferred_technology_stack,
        "Predicted_career_path":predicted_career_path

    }


if __name__ == "__main__":
    for i in range(5000):
        append_dict_to_csv("./data_set_norman_gen-5000.csv",generate_sample())





