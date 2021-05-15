# Address Book Flask application

Flask application with MongoDB, each record contains :  

`Name`, `Address`, `City`, `State`, `Country`, `Pincode`, `PhoneNumber`, `EmailAddress`.

REST API support for 
- Adding new record
- Updating existing record
- View/search records based on `Name`, `City` and `Pincode`
- Remove records

## Requirements:
- Python
- venv
- MongoDB
- Flask
- PyMongo
- MongoEngine 


## Usage Directions
1. Clone the directory with 
`git clone https://github.com/maxflow7/AddressBook.git`
2. Activate the virutal environment (venv here)
`.\Scripts\activate`
3. Start flask application with
`python app.py`  


## Rest API's documentation


- ### _SHOW_
    Shows all the records stored in the database.

    #### URL
    `localhost:5000/show`
    #### Method
    `GET`
    #### URL Params
    ```python
    {
        'database':'user_database',
        'collection':'user_info'
    }

    ```

    #### Success Response
    `200`

    

    #### Error Response
    `400`

    #### Sample Call
    ```python
        import requests

        show_url = "http://127.0.0.1:5000/show"
        data={
            'database':'user_database',
            'collection':'user_info'
        }
        r = requests.get(url = show_url, json = json.dumps(data))
        resp = r.json()

        print(resp)
    ```


- ### _INSERT_
    Inserts new record in the database.
    #### URL
    `localhost:5000/insert`
    #### Method
    `POST`
    #### URL Params
    ```python

    {
        'database'   : 'address_book',
        'collection' : 'data' ,
        'Document'   : {
            "Name"         : "KomalTiwari",
            "Address"      : "11/11Kanpur",
            "City"         : "Kanpur",
            "State"        : "UttarPradesh",
            "Country"      : "India",
            "Pincode"      : '0',
            "PhoneNumber"  : '1111111111',
            "EmailAddress" : "abcd@gmail.com",
    }

    ```
    #### Success Response
    `200`
    

    #### Error Response
    `400`

    #### Sample Call
    ```python
    import requests

    insert_url = "http://127.0.0.1:5000/insert"
    data = {
        'database'   : 'address_book',
        'collection' : 'data' ,
        'Document'   : {
            "Name"         : "KomalTiwari",
            "Address"      : "11/11Kanpur",
            "City"         : "Kanpur",
            "State"        : "UttarPradesh",
            "Country"      : "India",
            "Pincode"      :  '0',
            "PhoneNumber"  : '1111111111',
            "EmailAddress" : "abcd@gmail.com"
        } 
    }   
    r = requests.post(url = insert_url, json = json.dumps(data))
    resp = r.json()
    print(resp) 

    ```
- ### _UPDATE_
    Updates records in the database.
    #### URL
    `localhost:5000/update`
    #### Method
    `PUT`
    #### URL Params
    ```python
    {
        'database'        : 'address_book',
        'collection'      : 'data' ,
        'Filter'          : {'address' : '11/11Kanpur'},
        'DataToBeUpdated' : {'Address' : '11/11Kanpur'}
    }

    ```

    #### Success Response
    `200`
    

    #### Error Response
    `400`
    
    #### Sample Call
    ```python
        import requests

        update_url = "http://127.0.0.1:5000/update"
        data = {
            'database'        : 'address_book',
            'collection'      : 'data' ,
            'Filter'          : {'address' : '11/11Kanpur'},
            'DataToBeUpdated' : {'Address' : '11/11Kanpur'}
        }
        r = requests.put(url = update_url, json = json.dumps(data))
        resp = r.json()
        print(resp)
    ```
- ### _DELETE_
    Deletes the given record.
    
    #### URL
    `localhost:5000/delete`
    #### Method
    `DELETE`
    #### URL Params
    ```python
    {
        'database'   : 'address_book',
        'collection' : 'data' ,
        'Filter'     : {'address' : '11/11Kanpur'}
    }
    
    ```
    
    
    #### Success Response
    `200`
    
    
    #### Error Response
    `400`
    
    #### Sample Call
    ```python
        import requests
        delete_url = "http://127.0.0.1:5000/delete"
        data = {
        'database'   : 'address_book',
        'collection' : 'data' ,
        'Filter'     : {'address' : '11/11Kanpur'}
        }
        r = requests.delete(url = delete_url, json = json.dumps(data))
        resp = r.json()
        print(resp) 
    
    ```



- ### _QUERY_
    Search records based on Name/City/Pin/etc.
    #### URL
    `localhost:5000/query`
    #### Method
    `GET`
    #### URL Params
    ```python
    {
        'database'   : 'address_book',
        'collection' : 'data',
        'Filter'     : {'Name' : 'KomalTiwari'}
    }

    ```


    #### Success Response
    `200`
    

    #### Error Response
    `400`

    #### Sample Call
    ```python
        import requests

        search_url = "http://127.0.0.1:5000/query"
        data = {
        'database'   : 'address_book',
        'collection' : 'data',
        'Filter'     : {'Name' : 'KomalTiwari'}
        }
        r = requests.get(url = search_url, json = json.dumps(data))
        resp = r.json()
        print(resp)
    ```

## References

- https://flask.palletsprojects.com/en/1.1.x/tutorial/
- https://www.youtube.com/watch?v=GMppyAPbLYk&ab_channel=TechWithTim
- https://www.youtube.com/watch?v=9OPP_1eAENg&list=PL4cUxeGkcC9jpvoYriLI0bY8DOgWZfi6u&ab_channel=TheNetNinja
- https://www.youtube.com/watch?v=mtiyVsRQTA8&ab_channel=JulianNash
- https://www.youtube.com/watch?v=9N6a-VLBa2I&ab_channel=CoreySchafer

## TODOs
- Integrate with MongoDB cloud server, application is currently running on localhost
- Implement logging
- Validation checks on input data eg. If a character is passed in `PhoneNumber` , Incorrect email format
- Deployment of the application on web server.