# CPRD Aurum Synthetic Data Workflow

We are assuming some familiarity with coding in order to follow this workflow. Step 1 of the workflow uses Python and PostgreSQL. To understand more about our environmental set-up and software configurations, see the [installation-setup.md](installation-setup.md) file.  If you already have your CPRD Aurum data loaded into a database, you might want to skip to Step 2.


## [Step 1](Step1-PreProc): From text files to SQL tables

Step 1 starts with the raw text files provided by CPRD, and formats them into relational tables in a SQL database. 

### Step 1A: Meta-data, from PDF to csv

In order to create the tables in a SQL database, we require a machine readable metadata file which provides the *name of each data table* and the *field names* and *data types* within each table. This python code below creates a csv file for each table:

`` python Step1A-Generate-metadata-csvs.py``

> ❗ Step1A is a manual process and is not best practice. For more details on our ideal workflow, read here [^1]. As metadata sources become more available, complete and accurate, some of these pre-processing steps will no longer be relevant and/or can be automated. This was the best solution we found at the time of analysis. 

### Step 1B: Data, from text to csv

The files are provided by CPRD as flat files in text format. In this section, a Python script is used to convert the format from text to csv format. This gives more flexibility when using PostgreSQL's COPY command later in the workflow, to import the csv file to a relational table. More specifically, the script alters the field delimiter, wrapped quotes and datetime field formatting. 

To run this file conversion:

``python Step1B-Generate-data-csvs.py``

### Step 1C: From csv to SQL table

This section assumes that steps 1A and 1B have been completed, and a database has been created in PostgreSQL (in which you have permissions to write). A Python script is used to create a .sql file, based on the data and metadata csv files:

``python Step1C-Generate-SQL-queries.py``

This will output a .sql file called `Step1C-create-tables.sql`

Running this sql file, when connected to your specified database, will create the relational tables.

## [Step 2](Step2-Notebooks): Workbooks (Notebook tutorials) 

### Step2A: Introduction to CPRD Aurum Sample (Synthetic) Dataset

The aim of this notebook is provide familiarity with the tables that make up the CPRD Aurum Sample (Synthetic) Dataset.

### Step2B: Summary statistics for CPRD Aurum Sample (Synthetic) Dataset

The summary statistics created in this notebook follow the structure of those within the ['Release Notes: CPRD Aurum Sample Dataset October 2021'](https://www.cprd.com/sites/default/files/2022-02/CPRD%20Aurum%20Sample%20Dataset%20Release%20Notes.pdf) PDF. This notebook aims to replicate the numbers that CPRD provides using SQL commands, as an introduction to interacting with this dataset and the tables with SQL.

### Step2C: CPRD Cohort Criteria Examples

This notebook was created to replicate the example criteria given in CPRD Aurum FAQs v2.4 (see their [website](https://www.cprd.com/primary-care-data-public-health-research)).
This notebook uses these examples to increase understanding of the tables and explain how to write queries for example criteria. These types of queries would allow a research team to filter the CPRD data, to create a sample cohort that matches their research questions e.g. select patients within a certain age range and on a specific medication.

### How to interact with the notebooks

These Jupyter notebooks are intended to be interactive, because they contains markdown cells with explanatory text alongside cells with processing code, each which is rendered differently. They were written using Visual Studio Code using the Python and Jupyter extensions. To run a notebook, you need to be connected to a Python kernel. To be able to run PostgreSQL commands within a notebook you need to follow the steps explained in [installation-setup.md](installation-setup.md) under 'PostgreSQL Integration with Jupyter Notebook'.

Alternatively, you can simply read the notebook as a guide and copy and paste the SQL commands into whatever interface you are using to interact with your database!
 

[^1]: This is a bit long-winded and hard-coded in places due to limitations of file inputs. Our ideal workflow looks something like [this](https://github.com/aim-rsf/cprd-data-wrangle/blob/main/code-for-aurum/workflow_idea.png). This python code Step 1A was written because the CPRD Aurum Data Specification is only provided in PDF format. It was created by copy and pasting manually from the PDF data spec (Version 2.9, Date: 27 April 2023). There is a chance of errors! This is temporary code that acts as a proof of principle - showing what the workflow can be with a machine readable metadata file. The look-up tables did not have table descriptions with the PDF so we made some sensible choices, choosing 'TEXT' or 'INTEGER' for data types. The ideal scenario would be to have regularly updated machine readable data specs (metadata). The format of the metadata must match the format of the data files. The *[Metadata Catalogue](https://modelcatalogue.cs.ox.ac.uk/hdruk_live/#/catalogue/dataModel/all)* allows you to easily download CPRD metadata in a machine-readable format (XML, JSON, XLSX). However, the metadata provides 'Column name' only, but the columns in CPRD data files are actually named after 'Field name'. This (and some other differences noted between these metadata files and the data files) meant we could not use the metadata catalogue files in an automated workflow. 
