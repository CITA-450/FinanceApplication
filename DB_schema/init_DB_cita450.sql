#For DB Named DB_cita450 
#init DB
CREATE DATABASE if not exists db_cita450;
#create users table
CREATE TABLE if not exists users (
##<<<_KEYS>>>
  #primary _key
  id int AUTO_INCREMENT NOT NULL,
##<<<USER_DEETS>>>
  email varchar(38) NOT NULL,
  #Password Should be stored and validated as a hash (sha or md5) T.B.D.
  passwd varchar(255) NOT NULL,
  #user email
  bk_email varchar(30),
##<<<VALIDATION>>> 
  UNIQUE (id),
  UNIQUE (email),
  PRIMARY KEY (id)
  );

# create ledger table
CREATE TABLE if not exists ledger (
##<<<_KEYS>>>
  #primary key
  id int AUTO_INCREMENT NOT NULL,
  user_id int NOT NULL,
  #<<<USER_DEETS>>>
  #Name of the ledger volume
  name varchar(20) NOT NULL,
  ##Details on ledger ledger volume
  port_dts varchar(255),
##<<<VALIDATION>>> 
  UNIQUE (id),
  UNIQUE (name),
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
  );

  #create ledger line in ledger volume
CREATE TABLE if not exists line ( 
#<<<KEYS>>>
  #primary key
  id int AUTO_INCREMENT NOT NULL,
  #foreign key
  ledger_id int NOT NULL,
  #date entered
  #line_date- born on date that can be used for referencing changes to the ledger volume 
  #the format for 'TIMESTAMP' is{ - format: YYYY-MM-DD HH:MI:SS }
  line_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#<<<DOLLARS>>>
  #Dollar amount 
      #DECIMAL!(THIS MEANS 'FLOAT')
      #MUST: be positive value validation should be done in python because this is an unsigned decimal.
      #SEE: 'deb_cred' boolean for the associate attribution
      # I think that there is going to be an error if the number entered has more than 2 decimal digits or exceeding 10 whole digits
      #DO THIS: 9,999,999,999.99 or 0.01 If you are warren buffet this may not be the DB for you.
      #NOT THIS: 99,999,999.99 or 0.01999999999
  amount DECIMAL(10,2) NOT NULL,
#<<<VALIDATION>>> 
  #'CHECK'just to double triple check to make sure nobody fucked up!
  CHECK (amount > 0),#'CHECK'just to double triple check to make sure nobody fucked up!
  #'CHECK'just to double triple check to make sure nobody fucked up!
  # 
  #dollar amount signature
  #debt or credit this is a boolean represent as 0 = false, 1 = true (in our case this mean positive or negative dollar value)
  #DO: 0 or 1, 
  #DANGER: true or false will work but don't do it MYSQL will kill a kitten on your behalf when you make it think. PLEASE be kind to kittens
  deb_cred TINYINT(1),
#<<<DATES>>>
  #frequency; in PYTHON send queries 0-8 integer to associate the appropriate formula when creating the automation
    #NO: negative entries!
    #single = 0 (make default in python)
    #daily = 1
    #weekly = 2
    #bi-monthly = 3
    #monthly = 4
    #quarterly = 5
    #bi-annually= 6
    #annually = 7
    #every other year = 8
    #*DO NOT USE 8 IN PYTHON SCRIPT* 
        #** 9 & 10 = no current association determined but may allow a complexity for occurrences**
    #DO: 0 or 1 or 2 ...or 8
    #DO NOT DO: 8 or 9 or -7 or anything other than 0-8
  freq TINYINT(10) NOT NULL, 
#<<<VALIDATION>>> 
  CHECK (freq >= 0),#SEE ABOVE; however, if this is really needed I imagine it is because you did not read the scripts
  #                              so me writing this is pointless :(
  #***The most difficult part when working with dates is to be sure that the format of the
  #   date you are trying to insert, matches the format of the date column in the database.
  #   As long as your data contains only the date portion, your queries will work as expected.***
  #
  #Date start
  #format: { - format YYYY-MM-DD }
  #validate entry with python
  #must have value
  date_begin DATE NOT NULL,
  #Date end
  #format: { - format YYYY-MM-DD }
  #validate entry with python
  date_end DATE DEFAULT NULL,
#<<<USER_DEETS>>>  
  #details should be self explanatory 
  line_dts varchar(255) NOT NULL,
#<<<VALIDATION>>>    
  UNIQUE (id),
  PRIMARY KEY (id),
  FOREIGN KEY (ledger_id) REFERENCES ledger(id)
  
  );

#the end


