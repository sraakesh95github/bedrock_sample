# T-Mobile-Broadband-AI

## Important links
- [Architecture Review](https://ibm.box.com/s/eaes97yllx79h4ia8o83ujsts64kyc7j)
- [Bedrock Knowledge Handling](https://medium.com/cloud-devops-security-ai-career-talk/)
- [Bedrock AI Agents](https://medium.com/develop-a-fully-automated-chat-based-assistant-by-using-amazon-bedrock-agents-and-knowledge-bases-a8fb336c9a38)
- [Bedrock RAG](https://medium.com/@kapil-raina/aws-bedrock-exploring-agents-knowledge-base-rag-bd2856c80d2f)
- [AWS CDK](https://medium.com/tysonworks/introduction-to-aws-cdk-with-ec2-example-2355505c70b3)
- [SigV4 Signing](https://medium.com/towards-aws/aws-sigv4-in-3-mins-c324d20f19cf)
- [Frontend](https://docs.streamlit.io/)
- [YT Demo](https://www.youtube.com/watch?v=MKKGhiMTmJ4)

Resources to deploy are available in the `cdk` folder.

## Replace the following variables and secrets:
1. In `start.sh`, replace the environment variables with your AWS credentials (`aws key` and `aws secret key id` for the service role).
2. In `Dockerfile`, replace the environment variables.
3. In the `InvokeAgent` file, replace the AWS profile and region with your AWS configuration on the local compute.
4. In the `InvokeAgent` file, replace `AGENT_ID` and `AGENT_ALIAS_ID` with the ones created using Bedrock.

## To deploy AWS resources, using the terminal:
1. Navigate to the `cdk` directory:
    ```sh
    cd cdk
    ```
2. Ensure you have CDK installed:
    ```sh
    npm install -g aws-cdk
    ```
3. Create a virtual environment:
    ```sh
    python -m venv .env
    source .env/bin/activate  # On Windows, use `.env\Scripts\activate`
    ```
4. To run Python-based files:
    ```sh
    pip install aws-cdk.core
    cdk init app --language python
    ```
5. To bootstrap with the AWS profile:
    ```sh
    cdk bootstrap
    ```
6. To finally deploy:
    ```sh
    cdk deploy
    ```

## Important files:
- `model_prep/AgentPrompt`: Contains the prompt for the deployed model.
- `model_prep/WorkingSchemaUserStory.json`: Contains the OpenAPI schema to configure with the Lambda function triggers.

## UI Deployment
In the `Streamlit_App` folder:
Ensure you have Streamlit installed and run:
```sh
streamlit run fb_interface_2.py
