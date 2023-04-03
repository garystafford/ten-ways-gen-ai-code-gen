terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# write a terrform file to create a dynamodb table with the name of "users", a primary key of "name", a sort key of "age", with a read capacity of 5 and a write capacity of 5
