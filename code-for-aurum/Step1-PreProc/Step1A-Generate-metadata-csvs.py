# CPRD Aurum Data Specification, Version 2.9, Date: 27 April 2023
# The metadata was copied manually from CPRD's PDF data specifications and pasted below
# This code takes this copied metadata and creates a csv file for each table
# All csv files are saved within 'metadata_csv' directory and used for Step1C

import csv

dataspec_version = 'v2p9'

## Create quick function to avoid copy & pasting for every file
def write_medata_csv(file_name, row_list):
    csv_name = 'metadata_csv/' + file_name + '-' + dataspec_version + '.csv'
    with open(csv_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list) 

## 1. Patient
file_name = 'Patient'
row_list = [
    ["Column name","Field name","Type","Format","Mapping","Description"], 
    ["Patient identifier","patid","TEXT","6-19 numeric characters","None","Encrypted unique identifier given to a patient in CPRD Aurum. The patient identifier is unique to CPRD Aurum and may represent a different patient in the CPRD GOLD database. This is the primary key for this table. The last 5 characters will be same as the CPRD practice identifier"],
    ["CPRD practice identifier","pracid","INTEGER","5","Link Practice table","Encrypted unique identifier given to a practice in CPRD Aurum"],
    ["Usual GP","usualgpstaffid","TEXT","Up to 10 numeric characters","Link Staff table","The GP that the patient is nominally registered with. To be used with the Staff table for reference"],
    ["Gender","gender","INTEGER","3","Lookup: Gender.txt","Patient's gender"],
    ["Year of birth","yob","INTEGER","4","None","Patient's year of birth. This is actual year of birth e.g. 1984."],
    ["Month of birth","mob","INTEGER","2","None","Patient's month of birth (for those aged under 16)."],
    ["Date of death","emis_ddate","DATE","DD/MM/YYYY","None","Date of death as recorded in the EMIS® software. Researchers are advised to treat the emis_ddate with caution and consider using the cprd_ddate variable below."],
    ["Registration start date","regstartdate","DATE","DD/MM/YYYY","None","The date that the patient registered with the CPRD contributing practice. Most recent date the patient is recorded as having registered at the practice. If a patient deregistered for a period of time and returned, the return date would be recorded."],
    ["Patient type","patienttypeid","INTEGER","5","Lookup: PatientType.txt","The category that the patient has been assigned to e.g. private, regular, temporary."],
    ["Registration end date","regenddate","DATE","DD/MM/YYYY","None","Date the patient's registration at the practice ended. This may represent a transfer-out date or death date."],
    ["Acceptable flag","acceptable","INTEGER","1","None","Flag to indicate whether the patient has met certain quality standards: 1 =acceptable, 0 = unacceptable"],
    ["CPRD death date","cprd_ddate","DATE","DD/MM/YYYY","None","Estimated date of death of patient - derived using a CPRD algorithm"]
    ]
write_medata_csv(file_name,row_list)

## 2. Practice
file_name = 'Practice'
row_list = [
    ["Column name","Field name","Type","Format","Mapping","Description"],
    ["Practice identifier","pracid","INTEGER","5","None","Encrypted unique identifier given to a practice in CPRD Aurum. This is the primary key for this table."],
    ["Last Collection Date","lcd","DATE","DD/MM/YYYY","None","Date of the most recent CPRD data collection for the practice."],
    ["Up-to-standard date","uts","DATE","DD/MM/YYYY","None","The date at which the practice data is deemed to be of research quality, based on CPRD algorithm. [Not currently populated]"],
    ["Region","region","INTEGER","5","Lookup: Region.txt","Value to indicate where in the UK the practice is based. The region denotes the ONS Region for English practices."]
    ]
write_medata_csv(file_name,row_list)

## 3. Staff
file_name = 'Staff'
row_list = [
    ["Column name","Field name","Type","Format","Mapping","Description"],
    ["Staff identifier","staffid","TEXT","Up to 10 numeric characters","None","Encrypted unique identifier given to the practice staff member in CPRD Aurum. This is the primary key for this table."],
    ["Practice identifier","pracid","INTEGER","5","Link Practice table","Encrypted unique identifier given to a practice in CPRD Aurum"],
    ["Job category","jobcatid","INTEGER","5","Lookup JobCat.txt","Job category of the staff member who created the event"]
]
write_medata_csv(file_name,row_list)

## 4. Consultation
file_name = 'Consultation'
row_list = [
    ["Column name","Field name","Type","Format","Mapping","Description"],
    ["Patient identifier","patid","TEXT","6-19 numeric characters","Link Patient table","Encrypted unique identifier given to a patient in CPRD Aurum. The patient identifier is unique to CPRD Aurum and may represent a different patient in the CPRD GOLD database."],
    ["Consultation identifier","consid","TEXT","Up to 19 numeric characters","None","Unique identifier given to the consultation. This is the primary key for this table."],
    ["Practice identifier","pracid","INTEGER","5","Link Practice table","Encrypted unique identifier given to a practice in CPRD Aurum"],
    ["Event date","consdate","DATE","DD/MM/YYYY","None","Date associated with the event"],
    ["Entered date","enterdate","DATE","DD/MM/YYYY","None","Date the event was entered into the practice system"],
    ["Staff identifier","staffid","TEXT","Up to 10 numeric characters","Link Staff table","Encrypted unique identifier given to the practice staff member who took the consultation in CPRD Aurum"],
    ["EMIS® consultation source identifier","conssourceid","TEXT","Up to 10 numeric characters","Lookup: ConsSource.txt","Identifier that allows retrieval of anonymised information on the source or location of the consultation as recorded in the EMIS® software. Only the most frequently occurring strings have been anonymised and are included in the lookup. All others have been withheld by CPRD, pending anonymisation where feasible."],
    ["CPRD consultation source identifier","cprdconstype","INTEGER","3","Lookup: cprdconstype.txt [not included in initial release]","Type of consultation: this will be generated by CPRD based on information recorded in the consmedcodeid and conssourceid variables. [Not currently populated]"],
    ["Consultation source code identifier","consmedcodeid","TEXT","6-18 numeric characters","Medical dictionary. Maps to medcodeid","Source of the consultation from EMIS® software. This is a medical code that can be used with the medical dictionary. It may contain information similar to the consultation source identifiers but is available for use now. Some of the codes may not be interpretable e.g. Awaiting clinical code migration to EMIS Web®."]
    ]
write_medata_csv(file_name,row_list)

## 5. Observation
file_name = 'Observation'
row_list = [
    ["Column name","Field name","Type","Format","Mapping","Description"],
    ["Patient identifier","patid","TEXT","6-19 numeric characters","Link Patient table","Encrypted unique identifier given to a patient in CPRD Aurum. The patient identifier is unique to CPRD Aurum and may represent a different patient in the CPRD GOLD database."],
    ["Consultation identifier","consid","TEXT","Up to 19 numeric characters","Link Consultation table","Linked consultation identifier. In EMIS Web® it is not necessary to enter observations within a consultation, so this identifier may be missing."],
    ["Practice identifier","pracid","INTEGER","5","Link Practice table","Encrypted unique identifier given to a practice in CPRD Aurum"],
    ["Observation identifier","obsid","TEXT","Up to 19 numeric characters","None","Unique identifier given to the observation. This is the primary key for this table."],
    ["Event date","obsdate","DATE","DD/MM/YYYY","None","Date associated with the event"],
    ["Entered date","enterdate","DATE","DD/MM/YYYY","None","Date the event was entered into EMIS Web®"],
    ["Staff identifier","staffid","TEXT","Up to 10 numeric characters","Link Staff table","Encrypted unique identifier given to the practice staff member who took the consultation in CPRD Aurum"],
    ["Parent observation identifier","parentobsid","TEXT","Up to 19 numeric characters","Link Observation table","Observation identifier (obsid) that is the parent to the observation. This enables grouping of multiple observations, such as systolic and diastolic blood pressure, or blood test results."],
    ["Medical code","medcodeid","TEXT","6-18 numeric characters","Lookup: Medical dictionary","CPRD unique code for the medical term selected by the GP"],
    ["Value","value","NUMERIC","19.3","None","Measurement or test value"],
    ["Numeric unit identifier","numunitid","INTEGER","10","Lookup: NumUnit.txt","Unit of measurement"],
    ["Observation type identifier","obstypeid","INTEGER","5","Lookup: ObsType.txt","Type of observation (allergy, family history, observation)"],
    ["Numeric range low","numrangelow","NUMERIC","19.3","None","Value representing the low boundary of the normal range for this measurement"],
    ["Numeric range high","numrangehigh","NUMERIC","19.3","None","Value representing the high boundary of the normal range for this measurement"],
    ["Problem observation identifier","probobsid","TEXT","Up to 19 numeric characters","Link Observation table","Observation identifier (obsid) of any problem that an observation is associated with. An example of this might be an overarching condition that the current observation is associated with such as 'wheezing' with the problem observation identifier that links to an observation of 'asthma', that in turn contains information in the problem table."]
    ]
write_medata_csv(file_name,row_list)

## 5a. Referral
file_name = 'Referral'
row_list = [
    ["Column name","Field name","Type","Format","Mapping","Description"],
    ["Patient identifier","patid","TEXT","6-19 numeric characters","Link Patient table","Encrypted unique identifier given to a patient in CPRD Aurum. The patient identifier is unique to CPRD Aurum and may represent a different patient in the CPRD GOLD database."],
    ["Observation identifier","obsid","TEXT","Up to 19 numeric characters","Link Observation table","Unique identifier given to the observation. This is the primary key for this table."],
    ["Practice identifier","pracid","INTEGER","5","Link Practice table","Encrypted unique identifier given to a practice in CPRD Aurum"],
    ["Referral source organisation identifier","refsourceorgid","INTEGER","10","Lookups: Organisation.txt [not included in initial release] and OrgType.txt","Source organisation of the referral. Organisations are identified by an ID number and each organisation has a type (e.g. hospital inpatient department, community clinic). Both the organisation table and the OrgType lookup are required. The lookups are undergoing anonymisation work. [Not currently populated]"],
    ["Referral target organisation identifier","reftargetorgid","INTEGER","10","Lookups: Organisation.txt [not included in initial release] and OrgType.txt","Source organisation of the referral. Organisations are identified by an ID number and each organisation has a type (e.g. hospital inpatient department, community clinic). Both the organisation table and the OrgType lookup are required. The lookups are undergoing anonymisation work. [Not currently populated]"],
    ["Referral urgency identifier","refurgencyid","INTEGER","1","Lookup: RefUrgency.txt","Urgency of the referral e.g. routine, urgent, dated"],
    ["Referral service type identifier","refservicetypeid","INTEGER","2","Lookup: RefServiceType.txt","Type of service the referral relates to e.g. assessment, management, investigation"],
    ["Referral mode identifier","refmodeid","INTEGER","1","Lookup: RefMode.txt","Mode by which the referral was made e.g. telephone, written"]
    ]
write_medata_csv(file_name,row_list)

## 5b. Problem
file_name = 'Problem'
row_list = [
    ["Column name","Field name","Type","Format","Mapping","Description"],
    ["Patient identifier","patid","TEXT","6-19 numeric characters","Link Patient table","Encrypted unique identifier given to a patient in CPRD Aurum. The patient identifier is unique to CPRD Aurum and may represent a different patient in the CPRD GOLD database."],
    ["Observation identifier","obsid","TEXT","Up to 19 numeric characters","Link Observation table","Unique identifier given to the observation. This is the primary key for this table."],
    ["Practice identifier","pracid","INTEGER","5","Link Practice table","Encrypted unique identifier given to a practice in CPRD Aurum"],
    ["Parent problem observation identifier","parentprobobsid","TEXT","Up to 19 numeric characters","Link Observation table","Observation identifier for the parent observation of the problem. This can be used to group problems via the Observation table."],
    ["Problem end date","probenddate","DATE","DD/MM/YYYY","None","Date the problem ended"],
    ["Expected duration","expduration","INTEGER","5","None","Expected duration of the problem in days"],
    ["Last review date","lastrevdate","DATE","DD/MM/YYYY","None","Date the problem was last reviewed"],
    ["Last review staff identifier","lastrevstaffid","TEXT","Up to 10 numeric characters","Link Staff table","Staff member who last reviewed the problem"],
    ["Parent problem relationship identifier","parentprobrelid","INTEGER","5","Lookup ParentProbRel.txt","Description of the relationship of the problem to another problem e.g. the problem may have evolved or been merged with another problem as the problem, or the GP’s understanding of the problem, changes"],
    ["Problem status identifier","probstatusid","INTEGER","5","Lookup: ProbStatus.txt","Status of the problem (active, past)"],
    ["Significance","signid","INTEGER","5","Lookup: Sign.txt","Significance of the problem (minor, significant)"],
    ]
write_medata_csv(file_name,row_list)

## 6. Drug Issue
file_name = 'DrugIssue'
row_list = [
    ["Column name","Field name","Type","Format","Mapping","Description"],
    ["Patient identifier","patid","TEXT","6-19 numeric characters","Link Patient table","Encrypted unique identifier given to a patient in CPRD Aurum. The patient identifier is unique to CPRD Aurum and may represent a different patient in the CPRD GOLD database."],
    ["Issue record identifier","issueid","TEXT","Up to 19 numeric characters","None","Unique identifier given to the issue record. This is the primary key for this table."],
    ["Practice identifier","pracid","INTEGER","5","Link Practice table","Encrypted unique identifier given to a practice in CPRD Aurum"],
    ["Problem observation identifier","probobsid","TEXT","Up to 19 numeric characters","Link Observation and Problem tables","Unique identifier for the observation that links to a problem under which this prescription was issued. This refers to an 'obsid' in the Observation table which, in turn, can be linked to a record in the Problem table using 'obsid'."],
    ["Drug record identifier","drugrecid","TEXT","Up to 19 numeric characters","None","Unique identifier to a drug template record, which is not currently for release. At present this may be used to group repeat prescriptions from the same template."],
    ["Event date","issuedate","DATE","DD/MM/YYYY","None","Date associated with the event"],
    ["Entered date","enterdate","DATE","DD/MM/YYYY","None","Date the event was entered into EMIS Web®"],
    ["Staff identifier","staffid","TEXT","Up to 10 numeric characters","Link Staff table","Encrypted unique identifier given to the practice staff member issued the treatment in CPRD Aurum"],
    ["Drug code identifier","prodcodeid","TEXT","6-18 numeric characters","Lookup: Product dictionary","Unique CPRD code for the treatment selected by the GP"],
    ["Dosage identifier","dosageid","TEXT","64 characters","Lookup: common_ dosages.txt","Identifier that allows dosage information on the event to be retrieved. Not included in first release"],
    ["Quantity","quantity","DECIMAL","9.3 (The number before the decimal point gives the precision i.e. the total number of digits. The number after the decimal point denotes the scale number of decimal places)"," ","Total quantity entered by the GP for the prescribed treatment"],
    ["Quantity unit identifier","quantunitid","INTEGER","2","Lookup: QuantUnit.txt","Unit of the treatment (capsule, tablet)"],
    ["Course duration in days","duration","INTEGER","10","None","Duration of the treatment in days"],
    ["Estimated NHS cost","estnhscost","DECIMAL","10.4 (The number before the decimal point gives the precision i.e. the total number of digits. The number after the decimal point denotes the scale number of decimal places)","None","Estimated cost of the treatment to the NHS"]
    ]
write_medata_csv(file_name,row_list)

## I. Medical dictionary
file_name = 'MedicalDictionary'
row_list = [
    ["Column name","Type","Format","Mapping","Description"],
    ["medcodeid","TEXT","6-18 numeric characters","None","CPRD code to describe the observation. Links to the observation table. This is the primary key for this table."],
    ["term","TEXT","255 characters","None","Description of the observation associated with the codeid"],
    ["originalreadcode","TEXT","100 characters","None","The original Read code text as provided in the EMIS® dictionary (contains codes which are not valid Read codes)"],
    ["cleansedreadcode","TEXT","7 characters","None","CPRD-cleaned and validated version of the originalreadcode"],
    ["snomedctconceptid","TEXT","Up to 19 numeric characters","None","The SNOMED CT concept identifier associated with the observation"],
    ["snomedctdescriptionid","TEXT","Up to 19 numeric characters","None","The SNOMED CT description identifier associated with the observation"],
    ["release","TEXT","100 characters","None","Reference data version. [Not currently populated]"],
    ["emiscodecategoryid","INTEGER","2","Lookup: EMISCodeCat.txt","Category identifier in EMIS® that describes the observation"]
    ]
write_medata_csv(file_name,row_list)

# ## II. Product dictionary
file_name = 'ProductDictionary'
row_list = [
    ["Column name","Type","Format","Mapping","Description"],
    ["prodcodeid","TEXT","6-18 numeric characters","None","CPRD code to describe the treatment. Links to the Drug Issue table. This is the primary key for this table."],
    ["dmdid","TEXT","Up to 19 numeric characters","None","The DM+D code associated with the treatment"],
    ["termfromemis","TEXT","255 characters","None","Description of the treatment provided by EMIS® associated with the prodcodeid"],
    ["productname","TEXT","Up to 999 characters","None","Name of the product"],
    ["formulation","TEXT","Up to 999 characters","None","Formulation of the product"],
    ["routeofadministration","TEXT","Up to 999 characters","None","Route of administration for the product"],
    ["drugsubstancename","TEXT","Up to 999 characters","None","Active ingredient(s) included in the product. For combination therapies, each component is listed, separated by /"],
    ["substancestrength","TEXT","Up to 999 characters","None","Strength of each active ingredient listed in the drugsubstancename column, including units. Separated by / if more than 1"],
    ["bnfchapter","TEXT","Up to 999 characters","None","BNF chapter to which the product belongs"],
    ["release","TEXT","100 characters","None","Reference data version. [Not currently populated]"]
    ]
write_medata_csv(file_name,row_list)

## LOOK UP TABLES

### Gender
file_name = 'Gender'
row_list = [
    ["Field name","Type"],
    ["genderid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### PatientType
file_name = 'PatientType'
row_list = [
    ["Field name","Type"],
    ["patienttypeid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### Region
file_name = 'Region'
row_list = [
    ["Field name","Type"],
    ["regionid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### JobCat
file_name = 'JobCat'
row_list = [
    ["Field name","Type"],
    ["jobcatid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### ConsSource
file_name = 'ConsSource'
row_list = [
    ["Field name","Type"],
    ["conssourceid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### ObsType
file_name = 'ObsType'
row_list = [
    ["Field name","Type"],
    ["obstypeid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### NumUnit
file_name = 'NumUnit'
row_list = [
    ["Field name","Type"],
    ["numunitid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### RefServiceType
file_name = 'RefServiceType'
row_list = [
    ["Field name","Type"],
    ["refservicetypeid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### RefUrgency
file_name = 'RefUrgency'
row_list = [
    ["Field name","Type"],
    ["refurgencyid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### OrgType
file_name = 'OrgType'
row_list = [
    ["Field name","Type"],
    ["orgtypeid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### RefMode
file_name = 'RefMode'
row_list = [
    ["Field name","Type"],
    ["refmodeid","INTEGER"],
    ["Description","TEXT" ]
    ]
write_medata_csv(file_name,row_list)

### ParentProbRel
file_name = 'ParentProbRel'
row_list = [
    ["Field name","Type"],
    ["parentprobrelid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### ProbStatus
file_name = 'ProbStatus'
row_list = [
    ["Field name","Type"],
    ["probstatusid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### Sign
file_name = 'Sign'
row_list = [
    ["Field name","Type"],
    ["signid","INTEGER"],
    ["Description","TEXT"],
    ]
write_medata_csv(file_name,row_list)

### Common_dosages
# Reading all in as TEXT, but return to later: FLOAT, INT or DECIMAL may be more appropriate
file_name = 'Common_dosages'
row_list = [ 
    ["Field name","Type"],
    ["dosageid","TEXT"],
    ["dosage_text","TEXT"],
    ["daily_dose","TEXT"],
    ["does_number","TEXT"],
    ["dose_unit","TEXT"],
    ["dose_frequency","TEXT"],
    ["dose_interval","TEXT"],
    ["choice_of_dose","TEXT"],
    ["dose_max_average","TEXT"],
    ["change_dose","TEXT"],
    ["dose_duration","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### QuantUnit
file_name = 'QuantUnit'
row_list = [
    ["Field name","Type"],
    ["quantunitid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)

### EMISCodeCat
file_name = 'EMISCodeCat'
row_list = [
    ["Field name","Type"],
    ["emiscodecatid","INTEGER"],
    ["Description","TEXT"]
    ]
write_medata_csv(file_name,row_list)
