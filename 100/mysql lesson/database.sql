screate table account_trans(
trans_sn varchar(32) not null,
trans_date datetime not null,
acct_no varchar(32) not null,
trans_type int null,
amt decimal(10,2) not null,
unique(trans_sn),
index(trans_date)
)
default charset = utf8;

create table account_new
select * from account
where 1=0;

select a.customer_id, customer_name,account_id,customer_tel 
from customer c left join account a
on c.customer_id=a.customer_id;