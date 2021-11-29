// Loads in the AWS SDK
const AWS = require('aws-sdk'); 

// Creates the document client specifing the region 
// The tutorial's table is 'in us-east-1'
const ddb = new AWS.DynamoDB.DocumentClient({region: 'us-east-1'}); 

exports.handler = async (event, context, callback) => {
    // Handle promise fulfilled/rejected states
    const params = {
        TableName: 'testOne',
        Limit: 10,
        Key:{
            'OrderId':'10',
            'CreationDate':'2021'
        }
    }

return ddb.get(params, function(err, data) {
    if (err) {
        console.error("Unable to read item. Error JSON:", JSON.stringify(err, null, 2));
    } 
}).promise();

};