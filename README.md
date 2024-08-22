# FastAPI Template

Template for FastAPI project

## Requirements
- Python 3.8
- fastapi 0.112.1
- hypercorn 0.17.3
- python-dotenv 1.0.1

## Installation
1. Clone repository using the following URL: `https://github.com/matt-novoselov/FastAPI-Template.git`
2. Create Environment File:
   - Create a file named `.env` in the root directory of the source folder.
   - Use the provided `.env.example` file as a template.
3. Replace the placeholder values with your specific configuration:
   - API_ROOT_PATH: Root path is `/` my default. Change it if you are using a proxy.
4. Build and run `main.py` using hypercorn. Example: `hypercorn app.main:app --bind 0.0.0.0:8080`

<br>

Distributed under the MIT license. See **LICENSE** for more information.

Developed with ❤️ by Matt Novoselov
