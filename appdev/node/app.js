import { DynamoDBClient, CreateTableCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient({ region: "us-east-1" });

// create a new DynamoDB table name "Music", with a partion key of "Artist" and a sort key of "SongTitle", and a read capacity of 5 and write capacity of 5 
function createTable() {
    const params = {
        "AttributeDefinitions": [
            {
                "AttributeName": "Artist",
                "AttributeType": "S"
            },
            {
                "AttributeName": "SongTitle",
                "AttributeType": "S"
            }
        ],
        "KeySchema": [
            {
                "AttributeName": "Artist",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "SongTitle",
                "KeyType": "RANGE"
            }
        ],
        "ProvisionedThroughput": {
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
        "TableName": "Music"
    };

    const command = new CreateTableCommand(params);
    client.send(command).then((data) => console.log(data)).catch((err) => console.log(err));
}

createTable();