
#text= "Hello! World" [::-1]
#print(text)

# var1= "<<>>"
# var2= "hello"
# print(var1[:2] +var2 +var1[2:])


# var1="aabb"
# var2="hello"
# print(var1[:2] +var2 +var1[2:])

print("here we are creating our own ARN for AWS")

partition=str(input ("Please provide a partition: "))

service=str(input ("please provide service: "))

region=str(input("please provide region: "))

account_id=int(input("please provide account id: "))

resource_id=int(input ("please provide resource id: "))

print("arn",partition,service,region,account_id,resource_id, sep=":")

