use schema blog_site;

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

-- auto-generated definition
create table if not exists comment
(
    id              bigint unsigned auto_increment,
    user_comment_id bigint unsigned not null,
    post_id         bigint unsigned not null,
    content         text            not null,
    primary key (id, user_comment_id, post_id),
    constraint comment_blog_id_fk
        foreign key (post_id) references blog (id),
    constraint comment_user_id_fk
        foreign key (post_id) references user (id)
);

DELIMITER //
CREATE PROCEDURE addNewComment(IN userId BIGINT UNSIGNED, IN postId BIGINT UNSIGNED, IN comment TEXT)
    BEGIN
        INSERT INTO comment(user_comment_id, post_id, content) VALUES (userId, postId, comment);
    end //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE deleteComment(IN commentId BIGINT UNSIGNED)
    BEGIN
        DELETE FROM comment WHERE id = commentId;
    end //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE getPostFromContent(IN commentId BIGINT UNSIGNED)
    BEGIN
       SELECT blog.id, blog.date_posted, blog.user_id, blog.content
           FROM blog JOIN comment on blog.id = comment.post_id
        WHERE comment.id = commentId;
    END //
DELIMITER ;