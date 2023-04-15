package main

import (
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"

	"fmt"
	"log"
)

func main() {
	// create a new session
	sess, err := session.NewSession(&aws.Config{
		Region: aws.String("us-east-1")},
	)

	// create a new dynamodb client
	svc := dynamodb.New(sess)
	
	// create a new dynamodb table, with a primary key of "Artist", and a sort key of "SongTitle", with a read capacity of 5 and a write capacity of 5
	input := &dynamodb.CreateTableInput{
		AttributeDefinitions: []*dynamodb.AttributeDefinition{
			{
				AttributeName: aws.String("Artist"),
				AttributeType: aws.String("S"),
			},
			{
				