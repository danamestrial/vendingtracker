# API Documentation

## Table of Content
- [Http Verbs](#http-verbs)
- [Resources](#resources)
  - [Responses](#responses)
    - [Example Responses](#example-responses)
  - [**Machine Methods**](#machine-methods)
    - [**GET** /machine/list-all](#get-machinelist-all)
    - [**POST** /machine/add](#post-machineadd)
    - [**DELETE** /machine/delete](#delete-machinedelete)
    - [**PATCH** /machine/update](#patch-machineupdate)
  - [**Item Methods**](#item-methods)
    - [**GET** /item/list-all](#get-itemlist-all)
    - [**POST** /item/add](#post-itemadd)
    - [**DELETE** /item/delete](#delete-itemdelete)
    - [**PATCH** /item/update](#patch-itemupdate)
  - [**Stock Methods**](#stock-methods)
    - [**GET** /stock/list](#get-stocklist)
    - [**POST** /stock/add](#post-stockadd)
    - [**DELETE** /stock/delete](#delete-stockdelete)
    - [**PATCH** /stock/update](#patch-stockupdate)


# Http Verbs
| Verb | Description |
| --- | ----------- |
| GET | Retrieve a resource |
| POST | To create a new resource |
| PATCH | To update an existing resource |
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

## **Machine Methods**
### ***GET*** /machine/list-all
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

### ***POST*** /machine/add
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| handle<br> *required* | varchar  | Assign a name to the vending machine       |
| location <br> *required* | varchar | Assign a location to the vending        |
| status <br> *optional*  | bool (0,1) | Whether or not the machine is online or offline, default is offline (0)

<br></br>

### ***DELETE*** /machine/delete
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| machine_id<br> *required* | int  | Delete the machine using it's unique id |

<br></br>

### ***PATCH*** /machine/update
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| machine_id <br> *required* | int | Update a machine's information given the machine's unique id
| handle<br> *optional* | varchar  | Assign a name to the vending machine       |
| location <br> *optional* | varchar | Assign a location to the vending        |
| status <br> *optional*  | bool (0,1) | Whether or not the machine is online or offline, default is offline (0)

<br></br>

--------------

## **Item Methods**
### ***GET*** /item/list-all
*no arguments required*
### Example Response
```json
{
    "message": [
        {
            "id": 1,
            "name": "Lays"
        },
        {
            "id": 3,
            "name": "LEO"
        }
    ],
    "status": true
}
```
<br></br>

### ***POST*** /item/add
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| handle<br> *required* | varchar  | Assign a name to the item       |

<br></br>

### ***DELETE*** /item/delete
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| item_id<br> *required* | int  | Delete the item using it's unique id |

<br></br>

### ***PATCH*** /item/update
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| item_id <br> *required* | int | Update a item's information given the item's unique id
| item_name <br> *optional* | varchar  | Update item name       |

<br></br>

--------------

## **Stock Methods**

### ***GET*** /stock/list
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| machine_id<br> *required* | int  | Use machine_id to retrieve machine's stock

### Example Response
```json
{
    "message": [
        {
            "item_id": 1,
            "item_name": "Lays",
            "quantity": 9
        },
        {
            "item_id": 3,
            "item_name": "LEO",
            "quantity": 5
        }
    ],
    "status": true
}
```
<br></br>

### ***POST*** /stock/add
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| machine_id<br> *required* | int | Machine's id to add stock to |
| item_id<br> *required* | int | Item's id to add items to the machine |
| quantity<br> *required* | int | Amount of items to be added in the machine |

<br></br>

### ***DELETE*** /stock/delete
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| machine_id<br> *required* | int | The machine's unique id |
| item_id<br> *required* | int  | The item's unique id |

<br></br>

### ***PATCH*** /stock/update
| Arguments   |  Type  | Description |
| ----------- | --------- | ----------- |
| machine_id<br> *required* | int | The machine's unique id |
| item_id<br> *required* | int  | The item's unique id |
| quantity<br> *optional* | int  | Amount of item's to change |

<br></br>
