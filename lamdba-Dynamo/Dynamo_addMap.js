// Loads in the AWS SDK
const AWS = require('aws-sdk'); 

// Creates the document client specifing the region 
// The tutorial's table is 'in us-east-1'
const ddb = new AWS.DynamoDB.DocumentClient({region: 'us-east-1'}); 

exports.handler = async (event, context, callback) => {
    // Handle promise fulfilled/rejected states
    const params = {
    TableName:"commentsT1",
    Key:{
        "ID": "2"
        },
    UpdateExpression: 'set responses = list_append(responses, :responses_obj)',
    ExpressionAttributeValues :{
            ":responses_obj": [
                 {'myObject':
                    {
                        'Body': "22@othing.com",
                        'Name': '323',
                        'ID': '4',
                    }
                }
            ]
        }

};

return ddb.update(params, function(err, data) {
    if (err) {
        console.error("Unable to read item. Error JSON:", JSON.stringify(err, null, 2));
    } 
}).promise();

};