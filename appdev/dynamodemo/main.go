// Purpose: Create a new table in DynamoDB and insert an item
// Author: Gary A. Stafford
// Date: 2023-04-04

package main

import (
	"log"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/awserr"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"
)

func main() {
	// create a new session
	sess, err := session.NewSession(&aws.Config{
		Region: aws.String("us-east-1")},
	)

	// create a new dynamodb client
	svc := dynamodb.New(sess)

	createTable(sess, err, svc)

	item := map[string]string{
		"Artist":     "No One You Know",
		"SongTitle":  "Call Me Today",
		"AlbumTitle": "Somewhat Famous",
		"Awards":     "1",
	}
	insertItem(sess, err, svc, item)
}

func createTable(sess *session.Session, err error, svc *dynamodb.DynamoDB) {
	// create a new dynamodb table
	input := &dynamodb.CreateTableInput{
		AttributeDefinitions: []*dynamodb.AttributeDefinition{
			{
				AttributeName: aws.String("Artist"),
				AttributeType: aws.String("S"),
			},
			{
				AttributeName: aws.String("SongTitle"),
				AttributeType: aws.String("S"),
			},
		},
		KeySchema: []*dynamodb.KeySchemaElement{
			{
				AttributeName: aws.String("Artist"),
				KeyType:       aws.String("HASH"),
			},
			{
				AttributeName: aws.String("SongTitle"),
				KeyType:       aws.String("RANGE"),
			},
		},
		ProvisionedThroughput: &dynamodb.ProvisionedThroughput{
			ReadCapacityUnits:  aws.Int64(5),
			WriteCapacityUnits: aws.Int64(5),
		},
		TableName: aws.String("Music"),
	}

	_, err = svc.CreateTable(input)
	err = svc.WaitUntilTableExists(&dynamodb.DescribeTableInput{
		TableName: aws.String("Music"),
	})
	if err != nil {
		if aerr, ok := err.(awserr.Error); ok {
			switch aerr.Code() {
			case dynamodb.ErrCodeResourceInUseException:
				log.Println(dynamodb.ErrCodeResourceInUseException, aerr.Error())
			case dynamodb.ErrCodeLimitExceededException:
				log.Println(dynamodb.ErrCodeLimitExceededException, aerr.Error())
			case dynamodb.ErrCodeInternalServerError:
				log.Println(dynamodb.ErrCodeInternalServerError, aerr.Error())
			default:
				log.Println(aerr.Error())
			}
		} else {
			// Print the error, cast err to awserr.Error to get the Code and
			// Message from an error.
			log.Println(err.Error())
		}
		return
	}

	log.Println("Created the table")
}

// insert an item into the table
func insertItem(sess *session.Session, err error, svc *dynamodb.DynamoDB, item map[string]string) {
	// insert an item into the table
	input := &dynamodb.PutItemInput{
		Item: map[string]*dynamodb.AttributeValue{
			"Artist": {
				S: aws.String(item["Artist"]),
			},
			"SongTitle": {
				S: aws.String(item["SongTitle"]),
			},
			"AlbumTitle": {
				S: aws.String(item["AlbumTitle"]),
			},
			"Awards": {
				S: aws.String(item["Awards"]),
			},
		},
		TableName: aws.String("Music"),
	}

	_, err = svc.PutItem(input)
	if err != nil {
		if aerr, ok := err.(awserr.Error); ok {
			switch aerr.Code() {
			case dynamodb.ErrCodeConditionalCheckFailedException:
				log.Println(dynamodb.ErrCodeConditionalCheckFailedException, aerr.Error())
			case dynamodb.ErrCodeProvisionedThroughputExceededException:
				log.Println(dynamodb.ErrCodeProvisionedThroughputExceededException, aerr.Error())
			case dynamodb.ErrCodeResourceNotFoundException:
				log.Println(dynamodb.ErrCodeResourceNotFoundException, aerr.Error())
			case dynamodb.ErrCodeItemCollectionSizeLimitExceededException:
				log.Println(dynamodb.ErrCodeItemCollectionSizeLimitExceededException, aerr.Error())
			case dynamodb.ErrCodeInternalServerError:
				log.Println(dynamodb.ErrCodeInternalServerError, aerr.Error())
			default:
				log.Println(aerr.Error())
			}
		} else {
			// Print the error, cast err to awserr.Error to get the Code and
			// Message from an error.
			log.Println(err.Error())
		}
		return
	}

	log.Println("Inserted the item")
}
