# Ten Ways to Leverage Generative AI for Development on AWS

Code examples from the post, [Ten Ways to Leverage Generative AI for Development on AWS](https://garystafford.medium.com/ten-ways-to-leverage-generative-ai-for-development-on-aws-c0a11145aa4d): Explore ten ways you can use Generative AI coding tools to accelerate development and increase your productivity on AWS. In the post, we look at the ten ways you can use Generative AI coding tools, like GitHub Copilot, to improve your development productivity on AWS. This post is also available on [LinkedIn](https://www.linkedin.com/pulse/ten-ways-leverage-generative-ai-development-onaws-gary-stafford/).

The synthetic data sample applications are detailed in the post, [Unlocking the Potential of Generative AI for Synthetic Data Generation](https://medium.com/@garystafford/unlocking-the-potential-of-generative-ai-for-synthetic-data-generation-f42907cf0879): Explore the capabilities and applications of generative AI to create realistic synthetic data for software development, analytics, and machine learning.

## Resources

This project includes all the code samples shown in the two posts listed above. Files with the suffix `_partial` are the partial code samples used to demonstrate code generation with GitHub Copilot or similar AI coding assistants. Files with the suffix `_final` are the final, complete code samples. __All code should be thoroughly tested and reviewed before being used in production.__

All samples were created in [Visual Studio Code](https://code.visualstudio.com/) using the latest [GitHub Copilot Nightly extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-nightly). For an in-depth analysis of multiple generative AI-powered coding assistants, see the post, [Accelerate Software Development with Six Popular Generative AI-Powered Coding Tools](https://medium.com/@garystafford/accelerating-development-with-generative-ai-powered-coding-tools-f1480664b6ab): Explore six popular generative AI-powered tools, including ChatGPT, Copilot, CodeWhisperer (Preview), Tabnine, Bing, and ChatSonic. This post is also available on [LinkedIn](https://www.linkedin.com/pulse/accelerating-development-generative-ai-powered-gary-stafford/).

```text
.
├── LICENSE
├── README.md
├── airflow
│   ├── airflow_dag_final.py
│   └── airflow_dag_partial.py
├── appdev
│   ├── README.md
│   ├── dynamodemo
│   │   ├── dynamodemo
│   │   ├── go.mod
│   │   ├── go.sum
│   │   └── main.go
│   ├── main_partial.go
│   └── node
│       ├── app.js
│       ├── package.json
│       └── yarn.lock
├── cloudformation
│   ├── cloudformation_final.json
│   ├── cloudformation_final.yaml
│   └── cloudformation_partial.yaml
├── data
│   ├── README.md
│   ├── chatgpt_coffee_shop_data_gen.py
│   ├── coffee_shop_data_gen_final.py
│   ├── coffee_shop_data_gen_initial.py
│   ├── coffee_shop_data_gen_tests.py
│   ├── demographic_data_gen.py
│   ├── output
│   │   ├── address_data.csv
│   │   ├── coffee_shop_sales_data.csv
│   │   ├── coffee_shop_sales_data_chatgpt.csv
│   │   ├── coffee_shop_sales_data_test.csv
│   │   └── demographic_data.csv
│   └── residential_address_data_gen.py
├── iam
│   ├── s3_policy_final.json
│   └── s3_policy_partial.json
├── k8s
│   ├── k8s_deployment_final.yaml
│   └── k8s_deployment_partial.yaml
├── kafka
│   ├── source_connector_final.json
│   └── source_connector_partial.json
├── lambda
│   ├── lambda_function_final.java
│   ├── lambda_function_final.py
│   └── lambda_function_partial.py
├── postgresql
│   ├── postgresql_final.sql
│   └── postgresql_partial.sql
├── pyspark
│   ├── spark_final.py
│   └── spark_partial.py
├── terraform
│   ├── main_final.tf
│   └── main_partial.tf
└── utilities
    ├── utility_final.py
    └── utility_partial.py
```

---

_The contents of this repository represent my viewpoints and not of my past or current employers, including Amazon Web Services (AWS). All third-party libraries, modules, plugins, and SDKs are the property of their respective owners._