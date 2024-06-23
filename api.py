import pickle
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
import  sklearn
import  pandas as pd
import json

app = FastAPI()

# CORS middleware to allow requests from specified origins
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:83",
    "http://localhost:433",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Load the saved model during startup
MODEL = None
with open('./models/model_.pkl', 'rb') as f:
    MODEL = pickle.load(f)


# Define a function to prepare input data for prediction
def prepare_input_data(input_data):
    # Example: Convert JSON data to numpy array or other suitable format
    # This function needs to be customized based on your model's input requirements
    try:
        # Example: Convert JSON input to a numpy array
        input_array = np.array(list(float(x) for x in input_data.values()))
        return input_array
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/ping")
async def ping():
    return "Hello, I am alive"


@app.post("/predict")
async def predict(json_data: dict):
    try:
        # Prepare input data for prediction
        input_data = prepare_input_data(json_data)


        print(input_data)
        print([1,2,3,4,5])
        print(type(MODEL))

        # # Make predictions using the loaded model
        user_input = pd.DataFrame({
            "Programming_Languages_Proficiency": [input_data[0]],
            "Web_Development_Proficiency": [input_data[1]],
            "Mobile_Development_Proficiency": [input_data[2]],
            "Data_Science_Proficiency": [input_data[3]],
            "DevOps_Proficiency": [input_data[4]],
            "Cybersecurity_Proficiency": [input_data[5]],
            "AI_ML_Proficiency": [input_data[6]],
            "Game_Development_Proficiency": [input_data[7]],
            "Database_Proficiency": [input_data[8]],
            "API_Proficiency": [input_data[9]],
            "Full_Stack_Proficiency": [input_data[10]],
            "Problem_Solving_Skills": [input_data[11]],
            "Collaboration_Skills": [input_data[12]],
            "Graphic_Design_Proficiency": [input_data[13]],
            "Web_Security_Knowledge": [input_data[14]],
            "Performance_Optimization_Skills": [input_data[15]],
            "SEO_Knowledge": [input_data[16]],
            "Testing_Debugging_Skills": [input_data[17]],
            "Preferred_technology_stack": [input_data[18]]

        })
        predictions = MODEL.predict(user_input)
        print(predictions)
        #
        #
        # # Example: Extract predicted class or value
        predicted_class = predictions[0]  # Adjust based on your model's output

        myDict={
            0: "AI / ML",
            1: "Cybersecurity",
            2: "Data Science",
            3: "DevOps",
            4: "Game Development",
            5: "IT Support",
            6: "Mobile Development",
            7: "Network Administration",
            8: "Technical Writing" ,
            9:" Web Development"
        }


        # Return the predicted result as JSON
        return {
            'predicted_class': myDict[predicted_class],
            'message': 'Prediction successful'
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)

