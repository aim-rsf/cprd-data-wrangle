# Software installation

Step 1 of the workflow uses **Python** and **PostgreSQL**. To create this workflow, we used a [Data Science Virtual Machine (DSVM)](https://azure.microsoft.com/en-gb/products/virtual-machines/data-science-virtual-machines)(Ubuntu 20.04) which already had Python and PostgreSQL installed.

- **Python**: the installation of Python will depend on your operating system, reference [the main Python docs](https://www.python.org) for more details. The python files (`.py` below) were created with Python 3.8, using the Python extension within [Visual Studio Code](https://code.visualstudio.com).

- **PostgreSQL**: On the DSVM, it was likely installed by `sudo apt install postgresql postgresql-contrib`. Reference [the main PostgreSQL docs](https://www.postgresql.org/download) for more details on how to install on your operating system. 

It is likely that your research institution will already have their existing infrastructure and compulsory/recommended software set-ups. If not, we include some extra information in the next section, to cover:
- how we configured PostgreSQL for our set-up and created users with different permissions
- how we executed sql commands via the psql terminal, a sql script, and a shell script
- how we used Visual Studio Code to provide a graphical user interface to execute sql commands, as well as our favoured way to connect to the VM via the ssh connection
- how we integrate PostgreSQL with Jupyter Notebook

# PostgreSQL on Ubuntu DSVM

## Configure & create users
Resources: [1-Azure Quick Start](https://learn.microsoft.com/en-us/samples/azure/azure-quickstart-templates/postgresql-standalone-server-ubuntu/) and [2-PostgreSQL on DSVM](https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/linux-dsvm-walkthrough?view=azureml-api-2#postgresql-and-squirrel-sql)

1. Check configuration files for postgresql (resource 2)
> They talk about `/var/lib/pgsql/data/pg_hba.conf` but ours was here: `/etc/postgresql/12/main/pg_hba.conf`
> They say to *'Change the IPv4 local connections line to use md5 instead of ident, so we can log in by using a username and password.'* This was already done for our files, so did not need to change anything. 
2. Launch psql, the interactive terminal for PostgreSQL, as the built-in postgres user:

`sudo su - postgres psql`

3. As postgres user, check you can create a database, create table, and insert into this table (resource 1)
   
5. Create a user account (resource 2), and assign the appropriate [roles](https://www.postgresql.org/docs/current/predefined-roles.html) and [privileges](https://www.postgresql.org/docs/current/ddl-priv.html). 

7. Quit the interactive terminal with `\q`
> It said could not save history to file `"/var/lib/postgresql/.psql_history": No such file or directory`. It's trying to save the history of what we've done so far in psql as user the 'postgres'. Fortunately this does not seem like it really needs immediate solving because when we go on to use psql with our user accounts, it saves the history here `/home/your-username/.psql_history`.

6. Write `su your_username` to get back to user profile

7. Log back into the the interactive psql terminal by writing `psql` in the terminal and checking that your desired default username is being used

## Exploring PostgreSQL file layout on the DSVM

Using [this documentation](https://www.postgresql.org/docs/current/storage-file-layout.html) and cross referencing with our set-up on the DSVM:

Cluster configuration files are here:
> etc/postgresql/12/main/

The docs talk of a PGDATA directory where data files used by the database cluster are stored. We don't have anything called that but it seems to be here:
> ls /var/lib/postgresql/12/main/

We also have postgresql files in these locations:
> /usr/share/postgresql/12/
> /usr/share/postgresql-common/

And, as expected, there are executables in `/bin` which start with `pg_`

## Test psql commands 

:bulb: A cheat sheet of helpful commands: https://tomcam.github.io/postgres/#using-psql

### Interactive psql terminal 

When logged in to psql terminal with your username, try these commands:

  - `CREATE DATABASE your_database;`
  - `\c your_database`
  - `CREATE TABLE products (product integer, name text, price numeric);`
  - `INSERT INTO products VALUES (1, 'Cheese',4.99);`
  - `SELECT * FROM products;`
  - Make a csv file with multiple rows, with these columns `n, name, price`
  - `COPY products (n, name, price) FROM 'test_files/products.csv' WITH (FORMAT 'csv', HEADER, DELIMITER ',');`
  - `SELECT * FROM products;`

### Execute from sql script
- Create a new file on the shell terminal `touch test.sql`
- Paste the above commands that you ran on the psql terminal into the test.sql file
- Log into psql `psql`
- Run the sql script, with outputs displayed: `\i test.sql`
- Run the sql script, with outputs pasted into a text file: `\o output.txt` `\i test.sql`

### Execute from shell script
- Create a new file on the shell terminal `touch test_sql.sh`
- Inside this test_sql.sh file write:

> #!/bin/sh
> 
> dbname="database-name-that-exists"
> 
> username="your-username"
> 
> psql $dbname $username << EOF
> 
> SELECT * FROM table-that-exists;
> 
> EOF

All the postgreSQL commands are provided inside the EOF block. You can also use shell variables inside the sql command e.g. 

`wherecond="something"`

`SELECT * FROM table-that-exists WHERE col_name = '$wherecond';`

## ssh to the DSVM with VSCode (ignore if no VM being used)

On our local MacOS we installed *Remote Explorer* and *Remote - ssh* by Microsoft. Instead of using an ssh connection via the terminal app, we can ssh connect to the VM via our local [Visual Studio (VS) Code](https://code.visualstudio.com/) app, with these extensions. 

**After installing extensions:**
-    Note a small green box in bottom left of VSCode, with the '**><**' icon
-    Click on **><** to open a remote window
-    In the dialog box, select Connect to Host (Remote SSH) > Add new SSH host
-    Enter ssh connection details - it needed username, server IP and private key. We located and selected the SSH configuration file previously created. This added the host to our configuration file.
-    Select **><** , Connect to Host, and select the server IP address from the drop down. This prompt us to enter a password
-    Once done, a new remote window will open. You can confirm this is connected to the host as the >< icon will change in the bottom left 

## Visual Studio Code to interact with PostgreSQL

As an alternative to using PostgreSQL on terminal only, we can use an extension to VS Code to give us a graphical user interface (GUI). There are other GUIs available!

We installed the *PostgreSQL Management Tool* extension by *Chris Kolkman* in two locations: on VSCode on the VM (access via remote desktop) and on VSCode on our local MacOS. 

When in the postgreSQL explorer on VS Code, press the + button to add a database connection. 
- Hostname was 'localhost'
- Put in postgreSQL credentials (created earlier)
- Kept the default port
- Chose a secure connection

## PostgreSQL Integration with Jupyter Notebook

These python libraries must be installed: ipython-sql, sqlalchemy, Psycopg2

Then run this in a Python cell:

`` 
%load_ext sql
from sqlalchemy import create_engine
``

Connecting to a PostgreSQL database run:

`` 
%sql dialect+driver://username:password@host:port/database
`` 

For example:

`` 
%sql postgresql://postgres:password123@localhost/mydatabase
``


