import requests
import uuid
import json

myuuid = uuid.uuid4().hex
url = "https://credapi.credify.tech/api/brportorch/v2/login"
myheaders = {
    "x-cf-source-id": "coding-challenge",
    "x-cf-corr-id": myuuid,
    "Content-Type": "application/json"
}
payload = {
    "username": "coding.challenge.login@upgrade.com",
    "password": "On$3XcgsW#9q"
}

#Step1::
def post():
    response = requests.post(url, json=payload, headers=myheaders)
    print(response.status_code)
    print(response.text)

post()


#Step2::
def producttype():
    response = {
        "firstName": "Ian",
        "userId": 9114917,
        "userUuid": "34c16f53-38c4-461a-bd14-11fa748d2663",
        "loanApplications": [],
        "loansInReview": [{
            "id": 9545966,
            "uuid": "230ea84a-7199-41c9-bf38-fff27e35970d",
            "status": "PENDING",
            "productType": "PERSONAL_LOAN",
            "sourceSystem": "BORROWER_FUNNEL_V2",
            "hasOpenBackendCounter": False,
            "purpose": "CREDIT_CARD",
            "createDate": "2019-08-21T18:18:59.959Z",
            "postIssuanceStatus": None
        }]

}
    finalproducttype = response['loansInReview'][0]["productType"]
    assert finalproducttype == "PERSONAL_LOAN"
    print("Yes the product type in the response is PERSONAL_LOAN ")
# value1 = response['loansInReview']
# value2 = value1[0]
# print(value2)
# value3 = value2["productType"]
# print(value3)

producttype()

#Step3::
def unauthorised():
    invalidpayload = {
        "username": "mbmnb",
        "password": "kkiu"
    }
    newresponse = requests.post(url, json=invalidpayload, headers=myheaders)
    print(newresponse.status_code)


unauthorised()

