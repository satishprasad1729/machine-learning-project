# machine-learning-project
this is the first machine learning project

# Software and account requirement
1. [Github account](https://github.com/)
2. [Heroku account](https://dashboard.heroku.com/)
3. [Vs Code IDE](https://code.visualstudio.com/download)
4. [Git CLI](https://git-scm.com/downloads)
5. [Git Documentation](https://git-scm.com/docs/git)

Creating conda environment
'''
conda create -p venv python==3.7 -y
'''

'''
conda activate venv/
'''
OR
'''
conda activate venv
'''

'''
pip install -r requirements.txt
'''

to add files to git
'''
git add file
'''

to check version
'''
git log
'''

> Note: to ignore file or folder from git we can write .gitignore file

To check git status
'''
git status
'''

to check all v ersion maintained by git
'''
git log
'''

to create version/commit all changes
'''
git commit -m "message"
'''

to send version/changes to github
'''
git push origin main
'''

to check remote url
'''
git remote -v
'''

to check branch name
'''
git branch
'''

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL =satishprasad1729@gmail.com
2. HEROKU_API_KEY = 7b69b82e-f4e6-4b9e-bc18-e853bc5e8b8b
3. HEROKU_APP_NAME = 

BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname> .
'''
> Note:image name for docker must be lowercase

to list docker images
'''
docker images
'''

to run docker image
'''
docker run -p 5000:5000 -e PORT=5000 d45a13fc8e10
'''

To check running container in docker
'''
docker ps
'''

to stop docker container
'''
docker stop <container_id>
'''

