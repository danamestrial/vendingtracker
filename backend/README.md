# API Documentation
## Http Verbs
| Verb | Description |
| --- | ----------- |
| GET | Retrieve a resource |
| POST | To create a new resource |
| PUT | To update an existing resource |
| DELETE | To delete an existing resource |

# Resources

## Responses

All api will **always** return with two things 'status' : bool AND 'message' : {payload | error}. For methods that is **not** GET, 'message' will always return "" on 'status' : true.

### Example Responses
```json
{
    "status": false,
    "message": "(2003, \"Can't connect to MySQL server on '127.0.0.1:3306' (61)\")"
}
```
```json
{
    "status": true,
    "message": ""
}
```

-------

## Machine Methods
### **GET** /list-all-machines
*no arguments required*
### Example Response
```json
{
    {
    "message": [
        {
            "handle": "numerouno",
            "id": 2,
            "location": "outside muic building",
            "status": 1
        },
        {
            "handle": "numerolots",
            "id": 3,
            "location": "inside muic building",
            "status": 0
        },
        {
            "handle": "numero3",
            "id": 4,
            "location": "outside muic new building",
            "status": 1
        }
    ],
    "status": true
}
}
```
<br></br>

### **POST** /add-machine
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| handle<br> *required* | varchar  | Assign a name to the vending machine       |
| location <br> *required* | varchar | Assign a location to the vending        |
| status <br> *optional*  | bool (0,1) | Whether or not the machine is online or offline, default is offline (0)

### Example Response
```json
{
    "status": {true | false},
    "message": {"" | error}
}
```
<br></br>

### **DELETE** /delete-machine
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| machine_id<br> *required* | int  | Delete the machine using it's unique id |

### Example Response
```json
{
    "status": {true | false},
    "message": {"" | error}
}
```
<br></br>
### **PUT** /update-machine
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| machine_id <br> *required* | int | Update a machine's information given the machine's unique id
| handle<br> *optional* | varchar  | Assign a name to the vending machine       |
| location <br> *optional* | varchar | Assign a location to the vending        |
| status <br> *optional*  | bool (0,1) | Whether or not the machine is online or offline, default is offline (0)

### Example Response
```json
{
    "status": {true | false},
    "message": {"" | error}
}
```
<br></br>