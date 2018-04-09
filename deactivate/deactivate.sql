select * from res_users;
UPDATE ir_mail_server SET active = False, smtp_user = 'user', smtp_pass = '123456';
UPDATE ir_config_parameter SET value = '123456' WHERE key = 'web.base.url';
