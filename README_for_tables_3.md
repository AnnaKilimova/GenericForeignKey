### After creating new models and adding migrations

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
 public | blog_comment               | table | kilimovaann
 public | blog_post                  | table | kilimovaann
 public | core_actionlog             | table | kilimovaann
 public | django_admin_log           | table | kilimovaann
 public | django_content_type        | table | kilimovaann
 public | django_migrations          | table | kilimovaann
 public | django_session             | table | kilimovaann
 public | users_profile              | table | kilimovaann
(14 rows)
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
 25 | Can add profile         |               7 | add_profile
 26 | Can change profile      |               7 | change_profile
 27 | Can delete profile      |               7 | delete_profile
 28 | Can view profile        |               7 | view_profile
 29 | Can add post            |               8 | add_post
 30 | Can change post         |               8 | change_post
 31 | Can delete post         |               8 | delete_post
 32 | Can view post           |               8 | view_post
 33 | Can add comment         |               9 | add_comment
 34 | Can change comment      |               9 | change_comment
 35 | Can delete comment      |               9 | delete_comment
 36 | Can view comment        |               9 | view_comment
 37 | Can add action log      |              10 | add_actionlog
 38 | Can change action log   |              10 | change_actionlog
 39 | Can delete action log   |              10 | delete_actionlog
 40 | Can view action log     |              10 | view_actionlog
(40 rows)
```
### blog_comment
```bash
 id | content | created_at | author_id | post_id 
----+---------+------------+-----------+---------
(0 rows)
```
### blog_post 
```bash
 id | title | content | created_at | updated_at | author_id 
----+-------+---------+------------+------------+-----------
(0 rows)
```
### core_actionlog
```bash
 id | action_type | timestamp | object_id | content_type_id | user_id 
----+-------------+-----------+-----------+-----------------+---------
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
  7 | users        | profile
  8 | blog         | post
  9 | blog         | comment
 10 | core         | actionlog
(10 rows)
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
 10 | auth         | 0005_alter_user_last_login_null          | 2025-11-01 20:06:04.852757+00
 11 | auth         | 0006_require_contenttypes_0002           | 2025-11-01 20:06:04.854229+00
 12 | auth         | 0007_alter_validators_add_error_messages | 2025-11-01 20:06:04.857661+00
 13 | auth         | 0008_alter_user_username_max_length      | 2025-11-01 20:06:04.870244+00
 14 | auth         | 0009_alter_user_last_name_max_length     | 2025-11-01 20:06:04.878539+00
 15 | auth         | 0010_alter_group_name_max_length         | 2025-11-01 20:06:04.885362+00
 16 | auth         | 0011_update_proxy_permissions            | 2025-11-01 20:06:04.888733+00
 17 | auth         | 0012_alter_user_first_name_max_length    | 2025-11-01 20:06:04.893333+00
 18 | sessions     | 0001_initial                             | 2025-11-01 20:06:04.903307+00
 19 | blog         | 0001_initial                             | 2025-11-03 16:37:53.700994+00
 20 | core         | 0001_initial                             | 2025-11-03 16:37:53.720103+00
 21 | users        | 0001_initial                             | 2025-11-03 16:37:53.737152+00
(21 rows)
```
### users_profile
```bash
 id | biography | city | birth_date | user_id 
----+-----------+------+------------+---------
(0 rows)
```

