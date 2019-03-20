CREATE OR REPLACE VIEW log_article_auths AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;

CREATE OR REPLACE VIEW log_article_vws AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;

CREATE OR REPLACE VIEW l_o_g_s AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as Log_Count
FROM log
GROUP BY Date;

CREATE OR REPLACE VIEW err_logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as Error_Count
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;