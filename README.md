# gutenberg_api

Guternberg API retrieves the Book Information in JSON format
Guternberg API retrieves only 25 books at a time

### Gutenberg API response
```text

{
    "status_code": 200,
    "response": {
        "total_no_of_books_available": 2,
        "retrieved_book_count": 2,
        "books": [
            {
                "title": "John F. Kennedy's Inaugural Address",
                "author_info": [
                    {
                        "name": "Kennedy, John F. (John Fitzgerald)",
                        "birth_year": 1917,
                        "death_year": 1963
                    }
                ],
                "subject": [
                    "Presidents -- United States -- Inaugural addresses",
                    "United States -- Foreign relations -- 1961-1963"
                ],
                "language": [
                    "en"
                ],
                "bookself": [],
                "download_link": [
                    {
                        "mime_type": "application/epub+zip",
                        "url": "http://www.gutenberg.org/ebooks/3.epub.noimages"
                    }
                ]
            },
            {
                "title": "Lincoln's Gettysburg Address: Given November 19, 1863 on the battlefield near Gettysburg, Pennsylvania, USA",
                "author_info": [
                    {
                        "name": "Lincoln, Abraham",
                        "birth_year": 1809,
                        "death_year": 1865
                    }
                ],
                "subject": [
                    "Consecration of cemeteries -- Pennsylvania -- Gettysburg",
                    "Lincoln, Abraham, 1809-1865. Gettysburg address",
                    "Soldiers' National Cemetery (Gettysburg, Pa.)"
                ],
                "language": [
                    "en"
                ],
                "bookself": [
                    "US Civil War"
                ],
                "download_link": [
                    {
                        "mime_type": "application/epub+zip",
                        "url": "http://www.gutenberg.org/ebooks/4.epub.images"
                    }
                ]
            }
        ]
    },
    "message": "Books extracted Successfully"
}
```

### This library provides following APIs

###### 1. /guternberg_api/get_books_by_g_id?g_id=3,4
```text
- This API retrieve the Book info filtered by provided gutenberg_id
- This API allows multiple filter values eg.. g_id=3,4
```

###### 2. /guternberg_api/get_books_by_lang?lang=eng,la
```text
- This API retrieve the Book info filtered by provided language
- This API allows multiple filter values eg.. lang=eng,la
- This API provides case sensitive full match
- This API does not allow case insensitive partial match
```

###### 3. /guternberg_api/get_books_by_mime_type?mime_type=text/plain,application/prs.tex
```text
- This API retrieve the Book info filtered by provided mime_type
- This API allows multiple filter values eg.. mime_type=text/plain,application/prs.tex
- This API provides case sensitive full match
- It does not allow case insensitive partial match
```

###### 4. /guternberg_api/get_books_by_topic?topic=child,infant
```text
- This API retrieve the Book info filtered by provided topic
- This API allows multiple filter values eg.. topic=child,infant
- Topic is filter on either ‘subject’ or ‘bookshelf’ or both. 
- Case insensitive partial matches are supported.
```

###### 5. /guternberg_api/get_books_by_author?author=Jefferson,Henry
```text
- This API retrieve the Book info filtered by provided author
- This API allows multiple filter values eg.. author=Jefferson,Henry
- Case insensitive partial matches are supported.
```

###### 6. /guternberg_api/get_books_by_title?title=slavery,history
```text
- This API retrieve the Book info filtered by provided title
- This API allows multiple filter values eg.. title=slavery,history
- Case insensitive partial matches are supported.
```

###### 7. /guternberg_api/get_books?lang=eng,la&topic=child,infant
```text
- This API retrieve the Book info filtered by all provided criteria
- This API allows multiple filter values for each criteria
- This API can be called with one or more than one criteria mentioned below
  a) g_id=3,4
  b) lang=eng,la
  c) mime_type=text/plain,application/prs.tex
  d) topic=child,infant
  e) author=Jefferson,Henry
  d) title=slavery,history
- Here only Author, Title and topic supports case insensitive partial match 

```


