import os
import time
import pandas as pd
import openai
from dotenv import load_dotenv
import taipy as tp
from taipy import Gui, Config
from functions import get_primer,format_question,run_request,format_response_plt,format_response



load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

figure = "my_plot1"
code = "generated_script.py"
plot_area = None
path = ""
question = " Type a question about the data. " 
primer1,primer2 = "",""
answer=""


stylekit = {
  
  "font_family": "Times new roman",
  "color_primary": "#049db8",
  "color_secondary": "#049db8",

}


# Graphy_app
Graphy_app = """

<|navbar|>

<|card card-bg|

  <center>
  **Taphy**
  </center>
  
|>

<|{path}|file_selector|label=Upload File|on_action=load_csv|extensions=.csv|drop_message=Drop Message|>

<|
<|{question}|input|class_name=fullwidth|>

<|Generate|button|on_action=plot_graph|>
|>

<|Table|expandable|
<|{df}|table|page_size=10|>
|>
<br/>

<|
<|{figure}|file_download|label=Download Graph|> <|{code}|file_download|label=Download Code|>
|>

<br/>

<center>
<|{figure}|image|width="700px"|>
</center>



"""

page2_md = """
<|navbar|>

<|card card-bg|

  <center>
  **Taphy**
  </center>
  
|>
<|part|class_name=m3|
**Mission**       

Our mission is to provide a user-friendly platform for data enthusiasts to explore and understand their datasets using advanced data visualization techniques.
<br/>
<br/>
**What Sets Us Apart?**
<br/>
*Innovative Data Visualization*
<br/>
 Our platform transforms raw data from .csv files into visually compelling charts, graphs, and dashboards that are both informative and user-friendly.
<br/>
<br/>
*Seamless Integration with ChatGPT APIs*
<br/>
To enhance your data exploration experience, we've seamlessly integrated ChatGPT APIs into our platform. This integration allows you to interact with your data through natural language queries, receiving instant responses to help you gain deeper insights and ask complex questions.
<br/>
<br/>
*User-Friendly Interface*
<br/>
Whether you're a seasoned data analyst or new to the world of data, our platform is designed for you. The user-friendly interface ensures that you can navigate the application effortlessly, making data visualisation a simple process!
|>


"""



df = pd.DataFrame()



def load_csv(state, var_name, payload):
    global df,primer1,primer2
    temp =  pd.read_csv(state.path)
    state.df = temp.copy()
    df = temp.copy()
    print(df)
    df.to_csv('data.csv')
    primer1,primer2 = get_primer(df,"df")


# def load_question(state: str) -> str:
#     global question
#     question = state.question
#     print(question)





def plot_graph(state) -> None:

    try:
        if os.path.exists('my_plot1.png'):
            os.remove('my_plot1.png')

        # Format the question 
        question_to_ask = format_question(primer1, primer2, state.question)   
        print(question_to_ask)
        print("Running OpenAI API...")
        # Run the question
        answer=""
        answer = run_request(question_to_ask, "gpt-3.5-turbo", key=openai.api_key)
        answer = format_response(answer)
        # the answer is the completed Python script so add to the beginning of the script to it.
        answer = primer2 + answer
        answer = format_response_plt(answer)
        answer = answer + "\nmy_plot = plt.gcf()\n" + "my_plot.savefig('my_plot1.png')\n"
        
        print(answer,"\n end")
        
        state.answer = answer
        # plot_area = 
        # plot_area = exec(answer)

        # Write the generated script to a new file
        with open('generated_script.py', 'w') as f:
            f.write(answer)

        # Now execute the generated script from the new file
        os.system('python generated_script.py')

        # exec(answer)  
        #sleep the program for 1 second to allow the file to be created
        time.sleep(5)
        state.figure = "my_plot1.png"       
        state.code = "generated_script.py"
        
        state.df = df
    except Exception as e:
        state.question = "Error occurred. Please try again...!"
        if type(e) == openai.error.APIError:
            print("OpenAI API Error. Please try again a short time later. (" + str(e) + ")")
        elif type(e) == openai.error.Timeout:
            print("OpenAI API Error. Your request timed out. Please try again a short time later. (" + str(e) + ")")
        elif type(e) == openai.error.RateLimitError:
            print("OpenAI API Error. You have exceeded your assigned rate limit. (" + str(e) + ")")
        elif type(e) == openai.error.APIConnectionError:
            print("OpenAI API Error. Error connecting to services. Please check your network/proxy/firewall settings. (" + str(e) + ")")
        elif type(e) == openai.error.InvalidRequestError:
            print("OpenAI API Error. Your request was malformed or missing required parameters. (" + str(e) + ")")
        elif type(e) == openai.error.AuthenticationError:
            print("Please enter a valid OpenAI API Key. (" + str(e) + ")")
        elif type(e) == openai.error.ServiceUnavailableError:
            print("OpenAI Service is currently unavailable. Please try again a short time later. (" + str(e) + ")")               
        else:
            print("Unfortunately the code generated from the model contained errors and was unable to execute.")

        





logo = "logo.jpg"
pages = {
    "Home": Graphy_app,
    "About": page2_md
}

Gui(pages=pages).run(stylekit=stylekit)

# run the app
#Gui(page=Graphy_app).run(title="Graph Generator")
