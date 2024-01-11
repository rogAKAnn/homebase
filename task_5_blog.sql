create schema blog_site;
use blog_site;

create table if not exists blog_site.user
(
    full_name varchar(255) null,
    id        bigint unsigned auto_increment
        primary key,
    user_name varchar(255) null
);

create table if not exists blog_site.blog
(
    id          bigint unsigned auto_increment,
    date_posted timestamp default CURRENT_TIMESTAMP not null,
    user_id     bigint unsigned                     not null,
    content     longtext                            null,
    primary key (id, user_id),
    constraint blog_user_id_fk
        foreign key (user_id) references blog_site.user (id)
);

DELIMITER //
CREATE PROCEDURE addNewBlog ( IN userId bigint unsigned, IN date timestamp, IN blogContent mediumText)
    BEGIN
     INSERT INTO blog(date_posted, user_id, content) VALUES (date, userId, blogContent);
    END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE getBlog (IN userId bigint unsigned, IN begin_date timestamp, IN end_date timestamp)
    BEGIN
        SELECT user_id, date_posted, content
        FROM blog
        WHERE user_id = userId AND date_posted >= begin_date AND date_posted <= end_date;
    END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE updateBlog(IN userId bigint unsigned, IN blogId bigint unsigned, IN updateContent MEDIUMTEXT)
    BEGIN
        UPDATE blog
            SET content = updateContent
        WHERE user_id = userId and id = blogId;
    END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE deleteBlog(IN blogId bigint unsigned)
    BEGIN
        DELETE FROM blog WHERE id = blogId;
    END //
DELIMITER ;


