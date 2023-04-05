// create a new dynamodb table, with a primary key of "name", and a sort key of "age",
// with a read capacity of 1 and a write capacity of 1
package main

import (
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"

	"fmt"
	"log"
)

func main() {
	
	