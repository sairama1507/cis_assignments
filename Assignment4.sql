
create table customer(c_id int, dates date);

insert into customer values
(1111,'2022-12-01'),
(1111,'2022-10-01'),
(1111,'2022-09-01'),
(1111,'2023-01-01'),
(2222,'2022-01-01'),
(2222,'2022-05-01'),
(2222,'2022-04-01');

select * from customer;


SELECT c_id, Round(DATEDIFF(dates, MIN(dates) OVER (PARTITION BY c_id)) / 30) AS month_difference
FROM customer;