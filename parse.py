import openai
import configparser

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Read the API key from the configuration file
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['openai']['api_key']

# Set the OpenAI API key
openai.api_key = api_key

# Reading the contents of the files
my_information = read_file('HoneyMath/My_information.txt')
gpt_prompt = read_file('HoneyMath/GPT_prompt.txt')

# Combined prompt
combined_prompt = f"{my_information}\n{gpt_prompt}"

# Call the API with the combined prompt
response = openai.Completion.create(
    engine="davinci-codex",
    prompt=combined_prompt,
    max_tokens=150
)

# Output the response
print(response.choices[0].text.strip()) 
# response에 저장된 내용의 첫번째 선택지를 출력하고, 응답 텍스트 앞뒤 공백을 text.strip으로 제거 함