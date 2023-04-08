# chatAi
+ Open ended conversation with an AI assistant.
+ It can be used as AI assistant which can perform tasks like Correct sentences into standard English,Explain a complicated piece of code,Turn meeting notes into a summary,Create interview questions and many more tasks be creative and try it for yourself for more such interesting,useful tasks
+ This code uses the OpenAI API to generate responses to questions input by the user. It prompts the user to input a question, sends the question to the API, and then prints out the generated response. It does this using the text-davinci-003 model, which is a high-performing language model developed by OpenAI. The generated response is controlled using various parameters such as temperature, max_tokens, and top_p, which allow for more or less randomness in the generated response. The program is designed to be run in a loop, allowing the user to input multiple questions and receive multiple responses.


 # keywords
+ model: specifies the model to use for generating the response (in this case, text-davinci-003).
+ prompt: specifies the question to use as the prompt for generating the response.
+ temperature: sets the randomness of the generated response. A value of 0 will always generate the most likely response, while higher values will generate more diverse responses.
+ max_tokens: sets the maximum length of the generated response.
+ top_p: controls the diversity of the generated response.
+ frequency_penalty: adjusts the likelihood of repeating the same answer.
+ presence_penalty: adjusts the likelihood of generating an answer that doesn't match the input question.

# prerequisites:
> Run the following commands in command prompt
1. python
2. openai library
`pip install openai`
3. openai api key
