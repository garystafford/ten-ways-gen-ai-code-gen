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
resource "aws_dynamodb_table" "users" {
  name           = "users"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "name"
  range_key      = "age"

  attribute {
    name = "name"
    type = "S"
  }

  attribute {
    name = "age"
    type = "N"
  }
}
