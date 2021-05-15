import requests   
import json
from pprint import pprint

def test_show():
    show_url = "http://localhost:5000/show"
    data = {
        'database'   : 'address_book',
        'collection' : 'data'
    }
    r = requests.get(url = show_url, json = json.dumps(data))
    resp = r.json()
    pprint(resp)

  

def test_insert():
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
             "Pincode"      : '0',
             "PhoneNumber"  : '1111111111',
             "EmailAddress" : "abcd@gmail.com"
         } 
    }   
    r = requests.post(url = insert_url, json = json.dumps(data))
    resp = r.json()
    pprint(resp) 



def test_update():
    update_url = "http://127.0.0.1:5000/update"
    data = {
              'database'        : 'address_book',
              'collection'      : 'data' ,
              'Filter'          : {'address' : '11/11Kanpur'},
              'DataToBeUpdated' : {'Address' : '11/11Kanpur'}
      }
    r = requests.put(url = update_url, json = json.dumps(data))
    resp = r.json()
    pprint(resp)



def test_delete():

    delete_url = "http://127.0.0.1:5000/delete"
    data = {
         'database'   : 'address_book',
         'collection' : 'data' ,
         'Filter'     : {'address' : '11/11Kanpur'}
     }
    r = requests.delete(url = delete_url, json = json.dumps(data))
    resp = r.json()
    pprint(resp) 



def test_query():
    search_url = "http://127.0.0.1:5000/query"
    data = {
         'database'   : 'address_book',
         'collection' : 'data',
         'Filter'     : {'Name' : 'KomalTiwari'}
     }
    r = requests.get(url = search_url, json = json.dumps(data))
    resp = r.json()
    pprint(resp)




def main():
    # Remove comments to test the functions

    # test_show()
    # test_insert()
    # test_update()
    # test_query()
    # test_delete()

if __name__ == "__main__":
    main()