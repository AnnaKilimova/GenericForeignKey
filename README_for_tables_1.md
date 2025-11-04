```bash
                    List of relations
 Schema |            Name            | Type  |    Owner    
--------+----------------------------+-------+-------------
 public | auth_group                 | table | kilimovaann
 public | auth_group_permissions     | table | kilimovaann
 public | auth_permission            | table | kilimovaann
 public | auth_user                  | table | kilimovaann
 public | auth_user_groups           | table | kilimovaann
 public | auth_user_user_permissions | table | kilimovaann
 public | django_admin_log           | table | kilimovaann
 public | django_content_type        | table | kilimovaann
 public | django_migrations          | table | kilimovaann
 public | django_session             | table | kilimovaann
(10 rows)
```
### auth_group
```bash
 id | name 
----+------
(0 rows)
```
### auth_group_permissions
```bash
 id | group_id | permission_id 
----+----------+---------------
(0 rows)
```
### auth_permission
```bash
id |          name           | content_type_id |      codename      
----+-------------------------+-----------------+--------------------
  1 | Can add log entry       |               1 | add_logentry
  2 | Can change log entry    |               1 | change_logentry
  3 | Can delete log entry    |               1 | delete_logentry
  4 | Can view log entry      |               1 | view_logentry
  5 | Can add permission      |               2 | add_permission
  6 | Can change permission   |               2 | change_permission
  7 | Can delete permission   |               2 | delete_permission
  8 | Can view permission     |               2 | view_permission
  9 | Can add group           |               3 | add_group
 10 | Can change group        |               3 | change_group
 11 | Can delete group        |               3 | delete_group
 12 | Can view group          |               3 | view_group
 13 | Can add user            |               4 | add_user
 14 | Can change user         |               4 | change_user
 15 | Can delete user         |               4 | delete_user
 16 | Can view user           |               4 | view_user
 17 | Can add content type    |               5 | add_contenttype
 18 | Can change content type |               5 | change_contenttype
 19 | Can delete content type |               5 | delete_contenttype
 20 | Can view content type   |               5 | view_contenttype
 21 | Can add session         |               6 | add_session
 22 | Can change session      |               6 | change_session
 23 | Can delete session      |               6 | delete_session
 24 | Can view session        |               6 | view_session
(24 rows)
```
### auth_user
```bash
 id | password | last_login | is_superuser | username | first_name | last_name | email | is_staff | is_active | date_joined 
----+----------+------------+--------------+----------+------------+-----------+-------+----------+-----------+-------------
(0 rows)
```
### auth_user_groups
```bash
 id | user_id | group_id 
----+---------+----------
(0 rows)
```
### auth_user_user_permissions
```bash
 id | user_id | permission_id 
----+---------+---------------
(0 rows)
```
### django_admin_log
```bash
 id | action_time | object_id | object_repr | action_flag | change_message | content_type_id | user_id 
----+-------------+-----------+-------------+-------------+----------------+-----------------+---------
(0 rows)
```
### django_content_type
```bash
 id |  app_label   |    model    
----+--------------+-------------
  1 | admin        | logentry
  2 | auth         | permission
  3 | auth         | group
  4 | auth         | user
  5 | contenttypes | contenttype
  6 | sessions     | session
(6 rows)
```
### django_migrations
```bash
id |     app      |                   name                   |            applied            
----+--------------+------------------------------------------+-------------------------------
  1 | contenttypes | 0001_initial                             | 2025-11-01 20:06:04.69298+00
  2 | auth         | 0001_initial                             | 2025-11-01 20:06:04.769856+00
  3 | admin        | 0001_initial                             | 2025-11-01 20:06:04.806777+00
  4 | admin        | 0002_logentry_remove_auto_add            | 2025-11-01 20:06:04.812547+00
  5 | admin        | 0003_logentry_add_action_flag_choices    | 2025-11-01 20:06:04.818877+00
  6 | contenttypes | 0002_remove_content_type_name            | 2025-11-01 20:06:04.833052+00
  7 | auth         | 0002_alter_permission_name_max_length    | 2025-11-01 20:06:04.837813+00
  8 | auth         | 0003_alter_user_email_max_length         | 2025-11-01 20:06:04.842948+00
  9 | auth         | 0004_alter_user_username_opts            | 2025-11-01 20:06:04.846837+00
 10 | auth         | 0005_alter_user_last_login_null          | 2025-11-01 20:
06:04.852757+00
 11 | auth         | 0006_require_contenttypes_0002           | 2025-11-01 20:
06:04.854229+00
 12 | auth         | 0007_alter_validators_add_error_messages | 2025-11-01 20:
06:04.857661+00
 13 | auth         | 0008_alter_user_username_max_length      | 2025-11-01 20:
06:04.870244+00
 14 | auth         | 0009_alter_user_last_name_max_length     | 2025-11-01 20:
06:04.878539+00
 15 | auth         | 0010_alter_group_name_max_length         | 2025-11-01 20:
06:04.885362+00
 16 | auth         | 0011_update_proxy_permissions            | 2025-11-01 20:
06:04.888733+00
 17 | auth         | 0012_alter_user_first_name_max_length    | 2025-11-01 20:
06:04.893333+00
 18 | sessions     | 0001_initial                             | 2025-11-01 20:
06:04.903307+00
(18 rows)
```
### django_session
```bash
 session_key | session_data | expire_date 
-------------+--------------+-------------
(0 rows)
```
