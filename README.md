# OpenAI API: Fine-Tuning
This is the repository for the LinkedIn Learning course `OpenAI API: Fine-Tuning`. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

Fine-tuning GPT models allows you to submit examples of the types of responses the AI system should provide based on user input. This is a great way of ensuring the system speaks in a voice and tone of your choosing, and eliminates the need for providing a description of the agent before each prompt.

OpenAI’s API enables you to submit your own fine-tuning training data. In this course, Senior Staff Instructor and AI whisperer Morten Rand-Hendriksen shows you how to fine-tune OpenAI’s GPT models by uploading your own data to create a unique custom model.

This course takes you through the process of preparing your data, submitting the data for fine-tuning through the OpenAI API, and using the fine-tuned model for regular interactions with the AI API. 

Fine-tuning GPT provides better performance, enables you to shorten your prompts, and keeps the AI system on track and on target with your business content and context.

_See the readme file in the main branch for updated instructions and information._

## Instructions
This repository holds example data and two Jupyter Notebooks:
- `create-training-data/create-training-data.ipynb` demonstrates how to prepare data for fine-tuning
- `fine-tune-flow.ipynb` demonstrates how to perform fine-tuning through the OpenAI API.

The first time you run a block in a Jupyter Notebook, the environment will ask you to pick an environment. Follow the instructions and pick the first available Python environment. 

NOTE: The first code block will take a while to load because the environment has to load first.

## Installing
It is recommended you run these exercise files in GitHub Codespaces. This gives you a pre-configured Python environment for the Jupyter Notebooks to run.
To use the exercise files, follow these steps:
1. In the root folder, rename the file `env-template` to `.env`.
2. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).
3. Generate a new key and copy the key to your clipboard.
4. In `.env` add the key without quotes or parentheses.

### Instructor

Morten Rand-Hendriksen

Senior Staff Instructor, Speaker, Web Designer, and Software Developer

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/morten-rand-hendriksen?u=104).

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/openai-api-fine-tuning-21058733
[lil-thumbnail-url]: https://media.licdn.com/dms/image/D4D0DAQFE_LhqtfTWIw/learning-public-crop_675_1200/0/1713563299935?e=2147483647&v=beta&t=VFZaYAvNo0s7fvslE_g9JlEjZnX5TwmXyw9x8N4Fhq8

