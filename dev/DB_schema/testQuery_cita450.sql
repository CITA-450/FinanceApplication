-- test query

select * from users as u 
join ledger as l on l.user_id = u.id
join line as n on n.ledger_id = l.id
order by l.id;