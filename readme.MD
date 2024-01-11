## REPORT
This report is about displaying the result of my take-home test for the Software Engineer position

The file `requirements.txt` contains the dependencies needed to run through all the sections (except Task 5). I use Python 3.11.5 version for all Python tasks.

# Task 1

In this task, I calculate the average age of the individuals mentioned on the file `data/data.csv`. In addition to computing alone, I also handle some common errors which may occurred:
- Missing value in either columns: I drop all rows contains missing value
- Wrong type of object in the column `age` (float numbers, string, ...): I also drop these columns and then cast the type of this column to integer
- Illogical value for value in the column `age` (negative): In this part, I choose to omit those having a negative value.

To run this part, use this command:
```
    python3 task_1.py 
```

The result will appear on the console:
```
    The average age of all individuals are 26.25
```

# Task 2
In this task, I design the database schema for the E-commerce Inventory. The final diagrams can be accessed at `task_2.png`, which describes the physical design for the tables. Some abbreviations: PK (Primary Key), FK (Foreign key). The relationship between entities are followed: 
- Product - Inventory: One to Many
- Product - Order: One to Many. 
- Customer - Order: One to Many

# Task 3
In this task, I crawl various information for the real estate from **Batdongsan.com**. In this part, I crawl these information: 
- price
- area
- num_of_bedroom
- num_of_wc
- location
from 2 sections: `nha-dat-ban` and `nha-dat-cho-thue`

To run this program, use this command:
```
    python3 task_3.py
```

the result will appear in `csv` format at the folder `task_3.result`

# Task 4
In this task, I simulate a nested set model for storing hierarchical data. In particular, I create a pandas dataframe which contains two columns: The left and right index of each nodes. 

To query for the children of the parent, we just need to query those having the left and right values within this parent left and right values.

To get a representation of the nested set model by pandas, use this command:
```
    python3 task_4.py --get-nested-set
```
The result will be seen on the console 

To query for the child of the parents, use this command:
```
    python3 task_4.py --get_parent_name `PARENT_NAME`
```

To get the time performance when creating the nested set, use this command
```
    python3 task_4.py --get_time_performance 
```

# Task 5
In this task, I create various store procedures for manipulating contents and blogs. They can be accessed through two files `task_5_blog.sql` and `task_5_comment.sql` for blog and comment procedures, respectively. 

I run these scripts on MySQL 8.3.0 so it will be necessary to install them first.

After running these scripts, to use the command procedures, you can use this SQL command:

```
CALL addNewBlog(1, current_timestamp(), "Hi, My name is Nguyen");
```

There are 6 procedures you can use: `addNewBlog`, `getBlog`, `updateBlog`, `deleteBlog`, `addNewComment`, `deleteComment`, `getPostFromComment`. These must be called with appropriate parameters which are indicated in the prototype of these procedures

