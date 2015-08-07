This project allows to search for lessons by titles on [Stepic](http://stepic.org).

Requirements
===

Python >=3.4 required.

[Elasticsearch](https://www.elastic.co/downloads/elasticsearch) == 1.7.1 must be installed. 

Let's Start
===
0. Install [Elasticsearch](https://www.elastic.co/downloads/elasticsearch)
 * For macos simple install:
  ```
  brew install elasticsearch
  ```
2. Install other requirements:

  ```
  pip install -r requirements.txt
  ```
3. Prepare your db:

  ```
  python manage.py migrate
  ```
4. Load lessons in local models:
  * From [Stepic] (http://stepic.org) by running command in project root directory:
  
    ```
    python manage.py loadlessons
    ```
    This command will load all available lessons, or you can bound loading pages count with:
    ```
    python manage.py loadlessons -p {pages_count}
    ```
  * From file:
  
    ```
    python manage.py loadlessons -f {path_to_file}
    ```
    File should be with JSON content like:
    
    ```
    {
      "lessons": [
        { "id": 1, "title": "A Journey of a Thousand Miles. . ." },
        { "id": 2, "title": "Hidden Messages in the Replication Origin" },
        { "id": 3, "title": "Some Hidden Messages are More Surprising than Others" }
      ]
    }
    ```
5. Run [elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html)

  ```
  $ bin/elasticsearch
  ```
4. Index lessons with command:

  ```
  python manage.py createindex
  ```
6. Run server:

  ```
  python manage.py runserver
  ```
7. Go to [your site](http://localhost:8000/search/) and try to search! Or if you need to see all lessons, try [this link](http://localhost:8000/lessons/).

If you need to delete lessons from your db, you can use command:

```
python manage.py clearlessons
```
