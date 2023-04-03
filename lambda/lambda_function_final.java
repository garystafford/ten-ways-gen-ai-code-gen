import java.io.*;
import java.util.*;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.lambda.runtime.events.S3Event;
import com.amazonaws.services.s3.*;
import com.amazonaws.services.s3.model.*;
import com.amazonaws.services.dynamodbv2.*;
import com.amazonaws.services.dynamodbv2.model.*;

public class S3ToDynamoDB implements RequestHandler<S3Event, String> {
    public String handleRequest(S3Event input, Context context) {
        LambdaLogger logger = context.getLogger();
        logger.log("S3ToDynamoDB");

        AmazonS3 s3 = AmazonS3ClientBuilder.defaultClient();
        AmazonDynamoDB dynamodb = AmazonDynamoDBClientBuilder.defaultClient();
        String bucketName = System.getenv("BUCKET_NAME");
        String tableName = System.getenv("TABLE_NAME");

        ListObjectsV2Result result = s3.listObjectsV2(bucketName);
        List<S3ObjectSummary> objects = result.getObjectSummaries();
        while (result.isTruncated()) {
            result = s3.listNextBatchOfObjects(result);
            objects.addAll(result.getObjectSummaries());
        }

        for (S3ObjectSummary os : objects) {
            logger.log(os.getKey());
            S3Object obj = s3.getObject(bucketName, os.getKey());
            BufferedReader reader = new BufferedReader(new InputStreamReader(obj.getObjectContent()));
            String line;
            while ((line = reader.readLine()) != null) {
                logger.log(line);
                try {
                    dynamodb.putItem(new PutItemRequest().withTableName(tableName).withItem(parseLine(line)));
                } catch (AmazonDynamoDBException e) {
                    logger.log(e.getMessage());
                    System.exit(1);
                }
            }
        }

        return "Hello from Lambda!";
    }

    private static Map<String, AttributeValue> parseLine(String line) {
        String[] tokens = line.split(",");
        Map<String, AttributeValue> item = new HashMap<>();
        item.put("ID", new AttributeValue().withN(tokens[0]));
        item.put("Name", new AttributeValue().withS(tokens[1]));
        item.put("School", new AttributeValue().withS(tokens[2]));
        item.put("Grade", new AttributeValue().withN(tokens[3]));
        return item;
    }
}