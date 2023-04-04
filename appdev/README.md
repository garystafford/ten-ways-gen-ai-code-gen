# AppDev Examples

## Golang App

```shell
GOPATH=/Users/garystafford/go
go install github.com/aws/aws-sdk-go

go mod init github.com/garystafford/dynamodemo
go mod tidy
go build
go run main.go

aws dynamodb list-tables
aws dynamodb delete-table --table-name test
aws dynamodb describe-table --table-name test
```

## Node App

```shell
cd appdev/node
yarn init
yarn add aws-sdk @aws-sdk/client-dynamodb
yarn add chai mocha --dev
yarn
yarn test
```
