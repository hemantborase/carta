# Nginx log parser

Extract the code from the zip on your local and setup the paython3 env as per the requirements.txt file.

Build the docker image and tag it. Command to use for build and tagging 
```docker build -t hbcarta:v0.1```

Run ```dokcer images``` on local to see image is buid correctly. Image name will be  ```hbcarta:v0.1```

Run the docker image by ```docker run -it -p 8080:8080 hbcarta:v0.1```

Logs with show up the IP addresss and occurrences of each source IP in the logs file. Also it will show how many distinct IP addresses belong to each of the following subnets ```108.162.0.0/16, 173.245.56.0/23 and 212.129.32.128/25```

```
Address 173.245.54.251 was encountered 4 time(s)
Address 173.245.50.230 was encountered 1 time(s)
Address 173.245.56.221 was encountered 6 time(s)
Address 173.245.54.223 was encountered 1 time(s)
Address 108.162.218.17 was encountered 1 time(s)
Address 108.162.219.38 was encountered 2 time(s)
Address 108.162.219.32 was encountered 1 time(s)
------------------------------------------------
The bucket 108.162.0.0/16 contains 8 addresses
The bucket 212.129.32.128/25 contains 1 addresses
The bucket 173.245.56.0/23 contains 3 addresses
```

Open browser and type url as http://localhost:8080 to get the buckets of CIDRs and number of ips occured in the CIDR

```{
  "bucketes": {
    "108.162.0.0/16": 8, 
    "173.245.56.0/23": 3, 
    "212.129.32.128/25": 1
  }
}
```
