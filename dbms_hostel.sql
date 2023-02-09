CREATE TABLE hstudent1 (
    stud_id varchar(15) NOT NULL,
    stud_name varchar(20) NOT NULL,
    stud_dept varchar(15) NOT NULL,
    stud_year number NOT NULL,
    stud_room_no varchar(20) NOT NULL,
    stud_addr varchar(20) NOT NULL,
    stud_dob date,  
    stud_phone number NOT NULL,    
    PRIMARY KEY (stud_id)
);

desc hstudent1;

INSERT INTO hstudent1 values ('BH1-12','Ananya Trinach','UIET CSE' ,2, '2A/54','Chamba', DATE '2002-06-11', 8965485926);
INSERT INTO hstudent1 values ('BH1-16','Anesh Sayal','UIET CSE' ,2, '2A/56','Gurgaon', DATE '2003-09-11', 9965485926);
INSERT INTO hstudent1 values ('BH1-17','Akshat Verma','UIET CSE' ,2, '2B/56','Delhi', DATE '2004-06-11', 9999485926);
INSERT INTO hstudent1 values ('BH1-22','Aaryan Singh','UIET CSE' ,2, '3B/54','Lucknow', DATE '2002-06-11', 8865485926);
INSERT INTO hstudent1 values ('BH1-99','Bibhuti Singha','UIET CSE' ,2, '2B/54','Siliguri', DATE '2002-04-11', 9932964859);


CREATE TABLE hemployee1 (
    emp_id varchar(15) NOT NULL,
    emp_name varchar(20) NOT NULL,
    emp_designation varchar(30),
    emp_dept varchar(15) NOT NULL,
    emp_addr varchar(20) NOT NULL,  
    emp_phone number NOT NULL,  
    emp_salary number,  
    emp_date_of_join date,
    PRIMARY KEY (emp_id)
);

desc hemployee1;

INSERT INTO hemployee1 values ('E01', 'Dr.Gajendra Purohit','warden','admin','Chandigarh',1256485963,200000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E02', 'Ramesh','Cashier','Finance','Chandigarh',9965485963,120000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E03', 'Jatin','Incharge','admin','Chandigarh',8656485963,180000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E14', 'Ram','Cook','Mess','Chandigarh',5532485963,25000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E15', 'XYZ','Cook','Mess','Chandigarh',7782485963,25000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E16', 'ABC','Cook','Mess','Chandigarh',6632885963,16000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E17', 'ERD','waiter','Mess','Chandigarh',821485963,9000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E18', 'LMN','waiter','Mess','Chandigarh',9648592636,9000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E19', 'YUI','waiter','Mess','Chandigarh',8219658665,9000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E20', 'CVB','waiter','Mess','Chandigarh',8989626162,9000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E21', 'WSC','Security gaurd','Security','Chandigarh',111185963,11000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E22', 'ASD','Security Incharge','Security','Chandigarh',223685963,60000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E23', 'WSC1','Security gaurd','Security','Chandigarh',963285963,11000, DATE '2021-01-10');
INSERT INTO hemployee1 values ('E24', 'WSC2','Security gaurd','Security','Chandigarh',777685963,11000, DATE '2021-01-10');

CREATE TABLE hvisitors1 (
    visitor_id varchar(15) NOT NULL,
    visitor_name varchar(20) NOT NULL,
    visit_purpose varchar(30),
    visit_to varchar(15) ,
    visitor_addr varchar(20) NOT NULL,  
    visitor_phone number NOT NULL,    
    visit_date date,
    PRIMARY KEY (visitor_id)
);

desc hvisitors1;

INSERT INTO hvisitors1 values ('V101','Rachit Sharma','meet','BH1-12','Chandigarh',9623562358, DATE '2022-12-12');
INSERT INTO hvisitors1 values ('V102','Ram','mess','null','Chandigarh',9965962358, DATE '2022-23-12');


CREATE TABLE hroom1 (
    room_no varchar(20) NOT NULL,
    allocated_to varchar(25),
    Roommate varchar(25),
    no_of_chairs_available varchar(30),
    no_of_tables_available varchar(30),
    no_of_beds_available varchar(30),
    cooler_available varchar(20) 
);

desc hroom1;

INSERT INTO hroom1 values ('2/54','Bibhuti Singha','Ananya Trinach','3','2','2','yes');
INSERT INTO hroom1 values ('2/56','Aneesh Sayal','Akshat Verma','1','1','2','No');
INSERT INTO hroom1 values ('1/60','NULL','NULL','1','2','2','NO');

CREATE TABLE fees_bill1 (
    stud_id varchar(15) NOT NULL,
    room_no varchar(20),
    paid_sem_fees varchar(15),
    mess_bill number,
    canteen_bill number,
    fine number,   
    PRIMARY KEY (stud_id) 
);

desc fees_bill1;

INSERT INTO fees_bill1 values ('BH1-12','2A/54','yes' ,1500, 2500, 390);
INSERT INTO fees_bill1 values ('BH1-16','2A/56','yes' ,1800, 300, 390);
INSERT INTO fees_bill1 values ('BH1-17','2B/56','yes' ,900,'null', 'null');
INSERT INTO fees_bill1 values ('BH1-22','3B/54','yes' ,2215, 2500, 390);
INSERT INTO fees_bill1 values ('BH1-99','2B/54','yes' ,650, 'null', 'null');

CREATE TABLE mess_canteen1 (
    item_no number NOT NULL,
    menu varchar(20),
    price varchar(15),
    availibility varchar(20),
    timings varchar(20)
);

desc mess_canteen1;

INSERT INTO mess_canteen1 values('01','Aloo paratha','18','everyday', 'Morning');
INSERT INTO mess_canteen1 values('02','Paneer paratha','18','everyday', 'Morning');
INSERT INTO mess_canteen1 values('03','Maggi','25','everyday', 'Morning,Evening');
INSERT INTO mess_canteen1 values('04','Macaroni','25','everyday', 'Morning,Evening');
INSERT INTO mess_canteen1 values('05','Sandwich','20','everyday', 'working hours');
INSERT INTO mess_canteen1 values('06','Bread Pakode','20','Weekends', 'Evening');
INSERT INTO mess_canteen1 values('07','Drinks','25','everyday', 'working hours');
INSERT INTO mess_canteen1 values('08','Chole Puri','45','Sunday', 'Lunch');
INSERT INTO mess_canteen1 values('09','Egg Curry','25','Wednesday,Friday', 'Dinner');
INSERT INTO mess_canteen1 values('10','Regular menu','45','everyday', 'working hours');

