# GraphQl Documentation


GraphQL endpoint can be accessed at:

```
http://localhost/
```

## General Queries

The following query will return news information availabe in the local databse.

```
query{
  allNews{
    id
    title
    body

  }
}
```

```
query{
  newsById(id: "1"){
    id
    title
    body

  }
}
```

`addNews` mutation to add new news.

Example:

```
mutation{
  addNews(title: "This is a great short news!", body: "body here"){
    news{
      id
      title
      body
    }
  }
}

```

## Error handling

Error in GQL gives 200 HTTP status code so we have to always to look for `errors` key in the response to check if the request succeed or failed.

Example Error:

```
{
  "errors": [
    {
      "message": "You are not logged in",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "user"
      ]
    }
  ],
  "data": {
    "user": null
  }
}


```
