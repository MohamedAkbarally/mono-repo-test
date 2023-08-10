FROM public.ecr.aws/lambda/python:3.10 AS production

ARG RISK_TOOLING_PERSONAL_TOKEN

ADD src src
ADD module.toml module.toml
ADD main.py main.py
ADD lambda_helper lambda_helper

RUN yum install -y gcc git postgresql-devel

ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
RUN python -m pip install --upgrade pip 
RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD [ "main.main_handler" ]
