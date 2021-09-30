-- auto-generated definition
create table opportunity
(
    id    serial      not null
        constraint sites_pkey
            primary key,
    label varchar(50) not null
);

alter table opportunity
    owner to xxx;

create unique index opportunity_id_uindex
    on opportunity (id);


