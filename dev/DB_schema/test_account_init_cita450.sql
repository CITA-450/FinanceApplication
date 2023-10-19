INSERT INTO users (email,passwd,bk_email)
VALUES ('test@cita450.com','password','backuptest@cita450.com');
INSERT INTO ledger (user_id, name, port_dts)
VALUES ((SELECT id FROM db_cita450.users where users.email ='test@cita450.com'), 'testledger', 'test_ledger_detatil');
INSERT INTO line (ledger_id,amount,deb_cred,freq,date_begin,line_dts)
VALUES ((SELECT id FROM db_cita450.ledger where ledger.name ='testledger'),1234.56, 1,0,'2023-12-12','testline');